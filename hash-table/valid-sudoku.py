class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def check_valid(idx_list):
            num_list = []
            for i,j in idx_list:
                if board[i][j] == ".":
                    continue
                if board[i][j] in num_list:
                    return False
                else:
                    num_list.append(board[i][j])
            return True
        # check rows
        for i in range(len(board)):
            idx_list = []
            for j in range(9):
                idx_list.append((i,j))
            if not check_valid(idx_list):
                return False
        # check cols
        for j in range(len(board[0])):
            idx_list = []
            for i in range(9):
                idx_list.append((i,j))
            if not check_valid(idx_list):
                return False
        # check sub-boxes
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                idx_list = []
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        idx_list.append((x, y))
                if not check_valid(idx_list):
                    return False
        return True

        