# frmo leeitcode 
# https://leetcode.ca/all/631.html#:~:text=int%20Get(int%20row%2C%20char,C(row%2C%20column)%20.

class Excel:
    def __init__(self, row, col):
        row, col = self.decodeCord(row, col)
        self.excel = [[0]*(col+1) for _ in range(row+1)]
        self.equations = {}
    
    def decodeCord(self, row, col):
        return int(row)-1, ord(col)-ord("A")
    
    def set(self, row, col, str):
        row, col = self.decodeCord(row, col)
        if not str.startswith('='):
            if (row, col) in self.equations:
                del self.equations[row][col]
            self.excel[row][col] = int(str)
            return self.excel[row][col]
        

    def compute(self, str):
        ans = 0
        for s in str:
            start_i, start_j, end_i, end_j = self.parseRange(s)
            for r in range(start_i, start_j+1):
                for c in range(end_i, end_j+1):
                    if (r,c) in self.equations:
                        ans += self.callable(self.equations[(r,c)])
                    else:
                        ans += self.excel[r][c]
            return ans

    def parseRange(self, s):
        start, end = s
        if ":" in s:
            start, end = s.split(":")
        start_i, start_j = start[0], start[1]
        end_i, end_j = end[0], end[1]
        return (start_i, start_j, end_i, end_j)
    
    def sum(self, row, col, str):
        row, col = self.decodeCord(row, col)
        self.formula[(row, col)] = str
        return self.compute(str)