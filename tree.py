#!/usr/bin/env python
# coding: utf-8

LIMITE_PADRAO = 5


class Node:
    def __init__(self, value):
        self.value = value

        self.left = None
        self.right = None

    def __str__(self):
        return u'{}'.format(self.value)


class Tree:
    def __init__(self):
        self.node = None

    def insert(self, value):
        if not self.node:
            self.node = Node(value)
        else:
            self._insert(value, self.node)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if not current_node.left:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if not current_node.right:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)

    def print_tree(self):
        if self.node:
            self._print_tree(self.node)

    def _print_tree(self, current_node):
        if current_node:
            self._print_tree(current_node.left)
            print('{} => [ left: {}, right: {}, parent: {}]'.format(
                  current_node.value, current_node.left, current_node.right))
            self._print_tree(current_node.right)

    def search(self, needle, limit=5):
        results = []
        if needle:
            needle = needle.lower()

            # Se a raiz satisfizer a busca
            if needle == self.node.value[:len(needle)]:
                results.append(self.node.value)
                if len(results) == limit and limit > 0:
                    return results
        else:
            results.append(self.node.value)

        # Pesquisa nas sub arvores a esquerda
        if self.node.left:
            self._search(self.node.left, needle, results, limit)

        # Pesquisa nas sub arvores a esquerda
        if self.node.right:
            self._search(self.node.right, needle, results, limit)

        results.sort()
        return results

    def _search(self, node, needle, results, limit):
        if len(results) == limit and limit > 0:
            return results

        if node:
            if needle:
                if needle == node.value[:len(needle)]:
                    results.append(node.value)
            else:
                results.append(node.value)

        if node.left:
            self._search(node.left, needle, results, limit)
        if node.right:
            self._search(node.right, needle, results, limit)

        return results


def log(texto):
    print("====================================")
    print(texto)
    print("====================================")


def loaddata():
    import csv
    log("Carregando dados...")

    T = Tree()
    with open('patients.csv', 'r+') as csvfile:
        content = csv.reader(csvfile, delimiter=';')
        for row in content:
            T.insert(row[0])
    return T


def search(T):
    search_for = str(input("Digite o ínicio do nome a ser buscado: ")).lower()
    limit_input = str(input("""Digite a quantidade de registros que deseja
                            [default: {}]: """.format(LIMITE_PADRAO)))
    limit = LIMITE_PADRAO
    if limit_input:
        limit = int(limit_input)

    log("Buscando por [{}]".format(search_for))
    results = T.search(search_for, limit)
    return (results)


def main():
    from datetime import datetime
    T = loaddata()

    inicio = datetime.now()
    results = search(T)
    termino = datetime.now()

    delta = termino - inicio
    log("{} resultados encontrados: ({})".format(len(results), delta))
    log(results)


if __name__ == '__main__':
    main()
