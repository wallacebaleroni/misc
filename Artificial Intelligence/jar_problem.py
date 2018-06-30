def jar_DFS(max0, max1, objective):
    frontier = []
    explored = []

    root = Node([0, 0])
    frontier.append(root)

    while len(frontier) > 0:
        node = frontier[0]
        # print(node.value)
        if not(node.at(explored)):
            childs = node.do_actions(max0, max1)
            childs.reverse()
            for child in childs:
                if not(child.at(explored)):
                    if child.value == objective:
                        print_stack(child)
                        return
                    frontier.insert(0, child)

        explored.append(node)
        frontier.remove(node)


def jar_BFS(max0, max1, objective):
    frontier = []
    explored = []

    root = Node([0, 0])
    frontier.append(root)

    while len(frontier) > 0:
        node = frontier[0]
        # print(node.value)

        childs = node.do_actions(max0, max1)
        for child in childs:
            if not(child.at(frontier)) and not(child.at(explored)):
                if child.value == objective:
                    print_stack(child)
                    return
                frontier.append(child)

        explored.append(node)
        frontier.remove(node)


def print_stack(node):
    stack = []
    stack_parents(node, stack)
    stack.reverse()

    for each in stack:
        print(each)


def stack_parents(node, stack):
    stack.append(node.value)
    if node.parent is None:
        return
    stack_parents(node.parent, stack)


class Node:
    value = None
    parent = None

    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent

    def do_actions(self, max0, max1):
        actions = []
        # Fill jar 0
        if self.value[0] < max0:
            actions.append(Node([max0, self.value[1]], self))
        # Fill jar 1
        if self.value[1] < max1:
            actions.append(Node([self.value[0], max1], self))
        # Empty jar 0
        if self.value[0] != 0:
            actions.append(Node([0, self.value[1]], self))
        # Empty jar 1
        if self.value[1] != 0:
            actions.append(Node([self.value[0], 0], self))
        # Passes from jar 0 to 1
        if self.value[0] != 0 and self.value[1] != max1:
            jar0 = self.value[0]
            jar1 = self.value[1]

            jar1 += jar0
            if jar1 > max1:
                jar1 = max1
                jar0 -= max1 - self.value[1]
            else:
                jar0 = 0
            actions.append(Node([jar0, jar1], self))
        # Passes from jar 1 to 0
        if self.value[1] != 0 and self.value[0] != max0:
            jar0 = self.value[0]
            jar1 = self.value[1]

            jar0 += jar1
            if jar0 > max0:
                jar0 = max0
                jar1 -= max0 - self.value[0]
            else:
                jar1 = 0
            actions.append(Node([jar0, jar1], self))
        return actions

    def at(self, array):
        for node in array:
            if node.value == self.value:
                return True
        return False
