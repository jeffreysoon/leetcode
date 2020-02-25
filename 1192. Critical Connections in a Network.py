"""
[[0,1],[1,2],[2,0],[1,3]]
"""


class Solution:
    def criticalConnections(self, n: int, connections: [[int]]) -> [[int]]:
        result = []
        print(connections)
        for index in range(len(connections)):
            left = connections[:index]
            right = connections[index + 1:]
            left_path = set()
            right_path = set()
            for idx in range(len(left)):
                if len(left_path) == 0:
                    x, y = left[idx]
                    left_path.add(x)
                    left_path.add(y)
                else:
                    if any(x in left_path for x in left[idx]):
                        x, y = left[idx]
                        left_path.add(x)
                        left_path.add(y)
            for idx in range(len(right)):
                if len(right_path) == 0:
                    x, y = right[idx]
                    right_path.add(x)
                    right_path.add(y)
                else:
                    if any(x in right_path for x in right[idx]):
                        x, y = right[idx]
                        right_path.add(x)
                        right_path.add(y)
            if len(left_path) == n or len(right_path) == n:
                continue
            else:
                path = set()
                for x in right_path:
                    if x in left_path:
                        path = left_path.union(right_path)
                        break
                print("{} {} {}".format(left_path, right_path, path))
                if len(path) == n:
                    pass
                else:
                    result.append(connections[index])
        print(result)


if __name__ == '__main__':
    data = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
    test = Solution()
    test.criticalConnections(6, data)
