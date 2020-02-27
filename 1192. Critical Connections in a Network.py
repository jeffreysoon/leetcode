"""
[[0,1],[1,2],[2,0],[1,3]]
"""


class Solution:
    def criticalConnections(self, n: int, connections: [[int]]) -> [[int]]:
        from collections import defaultdict
        result = []
        print(connections)

        for index in range(len(connections)):
            tmp = connections[:index] + connections[index + 1:]
            con_map = defaultdict(set)
            for x, y in tmp:
                con_map[x].add(y)
                con_map[y].add(x)

            print(con_map)
            found = True
            for x, y in con_map.items():
                for m in y:
                    if m in con_map:
                        con_map[x] = con_map[x].union(con_map[m])
            print(con_map)

            for x, y in con_map.items():
                if len(y) == n:
                    found = False
                    break
            if found:
                result.append(connections[index])
        print(result)

    def criticalConnections2(self, n: int, connections: [[int]]) -> [[int]]:
        # use tarjan algorithm
        from collections import defaultdict
        steps = {}
        for i in range(n):
            steps[i] = -1
        nodes = defaultdict(set)
        for first, second in connections:
            nodes[first].add(second)
            nodes[second].add(first)
        result = []
        self.dfs(nodes, 0, -1, 0, steps, result)
        print(nodes)
        print(steps)
        print(result)
        return result

    def dfs(self, nodes, node, parent, step, steps, result):
        """
        return min step on node.
        """
        steps[node] = step + 1
        for next_node in nodes[node]:
            if next_node == parent:
                continue
            elif steps[next_node] == -1:
                steps[node] = min(steps[node], self.dfs(nodes, next_node, node, step + 1, steps, result))
            else:
                steps[node] = min(steps[node], steps[next_node])

        if steps[node] == step + 1 and parent != -1:
            result.append([node, parent])

        return steps[node]


if __name__ == '__main__':
    data = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
    test = Solution()
    test.criticalConnections2(6, data)
