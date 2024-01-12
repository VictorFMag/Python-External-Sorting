class BPlusNode:
    def __init__(self, leaf=True):
        self.keys = []  # Chaves de roteamento (nós internos e folhas)
        self.children = []  # Referências para os filhos (nós internos)
        self.next_leaf = None  # Próximo nó folha (nós folha)
        self.prev_leaf = None  # Nó folha anterior (nós folha)
        self.leaf = leaf

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusNode()
        self.t = t

    def search(self, key, node=None):
        if node is None:
            node = self.root

        if node.leaf:
            for k in node.keys:
                if key == k:
                    return "Chave encontrada"
                elif key < k:
                    return "Chave não encontrada"

            return "Chave não encontrada"

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        return self.search(key, node.children[i])

    def insert(self, key):
        root = self.root

        if len(root.keys) == (2 * self.t) - 1:
            new_root = BPlusNode(leaf=False)
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.root = new_root
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1

        if node.leaf:
            while i >= 0 and key < node.keys[i]:
                i -= 1

            node.keys.insert(i + 1, key)
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1

            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1

            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, index):
        t = self.t
        child = parent.children[index]
        new_child = BPlusNode(leaf=child.leaf)
        parent.keys.insert(index, child.keys[t - 1])
        parent.children.insert(index + 1, new_child)
        new_child.keys = child.keys[t: (2 * t) - 1]
        child.keys = child.keys[0: t - 1]
    
    def search(self, key, node=None):
        if node is None:
            node = self.root

        if node.leaf:
            for k in node.keys:
                if key == k:
                    return "Chave encontrada"
                elif key < k:
                    return "Chave não encontrada"

            return "Chave não encontrada"

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        return self.search(key, node.children[i])

    def remove(self, key):
        root = self.root
        if not root:
            return "A raiz não existe"
        if len(root.keys) == 1:
            if root.leaf:
                self.root = None
                return "Chave removida"
            if len(root.children[0].keys) == self.t - 1 and len(root.children[1].keys) == self.t - 1:
                self.merge_children(root, 0)
                root = self.root
        self._remove(root, key)
        return "Chave removida"

    def _remove(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if node.leaf:
            if key in node.keys:
                index = node.keys.index(key)
                del node.keys[index]
        elif not node.leaf:
            self.remove_from_subtree(node, key, i)
    
    def merge_children(self, node, index):
        child = node.children[index]
        next_child = node.children[index + 1]

        child.keys.extend(next_child.keys)
        del node.keys[index]
        del node.children[index + 1]

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

    def borrow_from_previous(self, node, index):
        child = node.children[index]
        sibling = node.children[index - 1]

        child.keys.insert(0, node.keys[index - 1])

        node.keys[index - 1] = sibling.keys.pop()

    def borrow_from_next(self, node, index):
        child = node.children[index]
        sibling = node.children[index + 1]

        child.keys.append(node.keys[index])

        node.keys[index] = sibling.keys.pop(0)