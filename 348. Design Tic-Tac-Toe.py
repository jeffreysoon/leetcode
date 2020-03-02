class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.spaces = n * n
        self.grid = [[0] * n for _ in range(n)]
        self.cap = n
        self.row = [0 for _ in range(self.cap)]
        self.col = [0 for _ in range(self.cap)]
        self.diag1 = 0
        self.diag2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        paint = 999
        if player == 1:
            paint = 1

        if self.grid[row][col] != 0:
            print('Retry')
        else:
            self.grid[row][col] = paint
            self.spaces -= 1

        checksum = self.cap * paint
        self.row[row] = self.row[row] + paint
        self.col[col] = self.col[col] + paint
        if row == col:
            self.diag1 += paint
        if row+col == self.cap - 1:
            self.diag2 += paint

        if checksum in (self.row[row], self.col[col], self.diag1, self.diag2):
            print("{} wins".format(player))
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

if __name__ == '__main__':
    test = TicTacToe(3)
    test.move(0, 0, 1)
    test.move(0, 2, 2)
    test.move(2, 2, 1)
    test.move(1, 1, 2)
    test.move(2, 0, 1)
    test.move(1, 0, 2)
    test.move(2, 1, 1)
