from typing import List, Optional


class WordSearch:
    def __init__(self):
        self.cols: Optional[int] = None
        self.rows: Optional[int] = None
        self.board: Optional[List[List[str]]] = None
        self.dirs: List[List[int]] = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    def valid_cell(self, r: int, c: int, visited: List[List[int]]) -> bool:
        return (
            0 <= r < len(self.board)
            and 0 <= c < len(self.board[0])
            and visited[r][c] == 0
        )

    def search_string(
        self, match_str: str, r: int, c: int, visited: List[List[int]]
    ) -> bool:
        if len(match_str) == 0:
            return True

        if not self.valid_cell(r, c, visited):
            return False

        if self.board[r][c] != match_str[0]:
            return False

        visited[r][c] = 1
        for d in self.dirs:
            new_r, new_c = r + d[0], c + d[1]
            if self.search_string(match_str[1:], new_r, new_c, visited):
                return True

        visited[r][c] = 0

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.rows = len(self.board)
        self.cols = len(self.board[0])

        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == word[0]:
                    visited = [
                        [0 for c_i in range(self.cols)] for r_i in range(self.rows)
                    ]
                    if self.search_string(word, r, c, visited):
                        return True

        return False


search = WordSearch()
print(
    search.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEED"
    )
)
