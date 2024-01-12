class Node:
    def __init__(self, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf
        self.start_position = None
        self.end_position = None


class BTreeV2:
    def __init__(self, t, file_path, page_size):
        self.root = Node()
        self.t = t
        self.file_path = file_path
        self.page_size = page_size

    # Procura por uma chave na árvore. Começa na raiz e se move para baixo na árvore conforme necessário para encontrar a chave
    def search(self, key):
        return self._search(self.root, key)

    # ==========================================================================================================================
    # Métodos auxiliares da busca

    def _search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return f"Chave {key} encontrada na página {node.start_position}-{node.end_position}"
        elif node.leaf:
            return f"Chave {key} não encontrada"
        else:
            return self._search(self.read_page(node.children[i].start_position, node.children[i].end_position), key)
        
    def read_page(self, start_position, end_position):
        with open(self.file_path, 'r') as file:
            file.seek(start_position)
            return file.read(end_position - start_position)

    # Insere uma chave na árvore. Se a raiz estiver cheia, a árvore é reorganizada para acomodar a nova chave
    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = Node(leaf=False)
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.root = new_root
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)

    # ==========================================================================================================================
    # Métodos auxiliares da inserção
            
    # Insere a chave em um nó que não está cheio
    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(0)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
            node.start_position = key
            node.end_position = key + self.page_size
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    # Divide o nó filho de um nó pai quando o filho está cheio
    def split_child(self, parent, index):
        t = self.t
        child = parent.children[index]
        new_child = Node(leaf=child.leaf)
        parent.keys.insert(index, child.keys[t - 1])
        parent.children.insert(index + 1, new_child)
        new_child.keys = child.keys[t: (2 * t) - 1]
        child.keys = child.keys[0: t - 1]
        if not child.leaf:
            new_child.children = child.children[t: 2 * t]
            child.children = child.children[0: t - 1]

    # ==========================================================================================================================
    
    # Remove uma chave da árvore e reorganiza a árvore se necessário após a remoção
    def remove(self, key):
        root = self.root
        if not root:
            return "A raiz não existe"
        if len(root.keys) == 1:
            if root.leaf:
                self.root = None
                return f"Valor {key} removido"
            if len(root.children[0].keys) == self.t - 1 and len(root.children[1].keys) == self.t - 1:
                self.merge_children(root, 0)
                root = self.root
        self._remove(root, key)
        return f"Valor {key} removido"

    # ==========================================================================================================================
    # Métodos auxiliares da remoção

    def _remove(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            if node.leaf:
                del node.keys[i]
                return
            return self.remove_internal_node(node, key, i)
        elif not node.leaf:
            return self.remove_from_subtree(node, key, i)

    # Remove uma chave de um nó interno
    def remove_internal_node(self, node, key, index):
        if node.leaf:
            if len(node.keys) > self.t - 1:
                del node.keys[index]
                return
        else:
            if len(node.children[index].keys) >= self.t:
                predecessor = self.get_predecessor(node, index)
                node.keys[index] = predecessor
                self._remove(node.children[index], predecessor)
                return
            elif len(node.children[index + 1].keys) >= self.t:
                successor = self.get_successor(node, index)
                node.keys[index] = successor
                self._remove(node.children[index + 1], successor)
                return
            else:
                self.merge_children(node, index)
                self._remove(node.children[index], key)

    # Obtém o predecessor de uma chave na árvore
    def get_predecessor(self, node, index):
        current = node.children[index]
        while not current.leaf:
            current = current.children[len(current.keys)]
        return current.keys[-1]

    # Obtém o sucessor de uma chave na árvore
    def get_successor(self, node, index):
        current = node.children[index + 1]
        while not current.leaf:
            current = current.children[0]
        return current.keys[0]

    # Mescla dois nós filhos de um nó pai quando um deles é removido
    def merge_children(self, node, index):
        child = node.children[index]
        next_child = node.children[index + 1]
        child.keys.append(node.keys[index])
        child.keys.extend(next_child.keys)
        if not child.leaf:
            child.children.extend(next_child.children)
        del node.keys[index]
        del node.children[index + 1]

    # Remove uma chave de um nó filho
    def remove_from_subtree(self, node, key, index):
        if len(node.children[index].keys) == self.t - 1:
            if index > 0 and len(node.children[index - 1].keys) >= self.t:
                self.borrow_from_previous(node, index)
            elif index < len(node.children) - 1 and len(node.children[index + 1].keys) >= self.t:
                self.borrow_from_next(node, index)
            else:
                if index < len(node.children):
                    self.merge_children(node, index)
                else:
                    self.merge_children(node, index - 1)
            self._remove(node.children[index], key)
        else:
            self._remove(node.children[index], key)

    # borrow_from_previous e borrow_from_next permitem a transferência de chaves entre nós vizinhos, garantindo o balanceamento da árvore
    def borrow_from_previous(self, node, index):
        child = node.children[index]
        sibling = node.children[index - 1]

        child.keys.insert(0, node.keys[index - 1])
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())

        node.keys[index - 1] = sibling.keys.pop()

    def borrow_from_next(self, node, index):
        child = node.children[index]
        sibling = node.children[index + 1]

        child.keys.append(node.keys[index])
        if not child.leaf:
            child.children.append(sibling.children.pop(0))

        node.keys[index] = sibling.keys.pop(0)