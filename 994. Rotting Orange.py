"""
0 = empty slot
1 =  fresh orange
2 = rotted orange
"""


class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        from collections import deque
        if not grid:
            return -1
        row_len = len(grid)
        col_len = len(grid[0])
        queue = deque([])
        # put every rotted orange in queue
        level = []
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 2:
                    level.append((row, col))
        queue.append(level)

        directions = [1, 0], [-1, 0], [0, 1], [0, -1]
        minute = 0
        while queue:
            pos = queue.popleft()
            level = []
            for pos_x, pos_y in pos:
                for r, c in directions:
                    new_pos_x, new_pos_y = pos_x + r, pos_y + c
                    if 0 <= new_pos_x < row_len and 0 <= new_pos_y < col_len and grid[new_pos_x][new_pos_y] == 1:
                        grid[new_pos_x][new_pos_y] = 2
                        level.append((new_pos_x, new_pos_y))
            if level:
                minute += 1
                queue.append(level)
        print(minute)
        print(grid)
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1:
                    return -1
        return minute

if __name__ == '__main__':
    data = [[2], [1], [1], [1], [2], [1], [1]]
    test = Solution()
    result = test.orangesRotting(data)
    print(result)
