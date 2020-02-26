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


if __name__ == '__main__':
    data = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
    test = Solution()
    test.criticalConnections(6, data)
