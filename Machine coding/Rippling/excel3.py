# excel sheet with formula
# Ex: A2 = A1 + 1
class Excel:
    def __init__(self, size):
        row, col = self.decodeCord(size)
        self.excel = [[0]*(col+1) for _ in range(row+1)]
        self.equations = {}
    
    def decodeCord(self, str):
        col, row = (ord(str[0])-ord('@'), int(str[1:]))
        return (row, col)
    
    def set(self, position, value):
        row, col = self.decodeCord(position)
        if value.startswith('='):
            self.equations[(row, col)] = value
        else:
            if (row, col) in self.equations:
                del self.equations[(row, col)]
            self.excel[row][col] = int(value)
    
    def compute(self, str):
        str += '+'
        i = 1
        n = len(str)
        digit, sign, res = 0, 1, 0
        while i<n:
            if str[i].isdigit():
                digit = digit*10 + int(str[i])
                i+=1
            elif str[i].isalpha():
                cell = ""
                while str[i].isalnum():
                    cell += str[i]
                    i+=1
                row, col = self.decodeCord(cell)
                if (row, col) in self.equations:
                    res += self.compute(self.equations[(row, col)])
                else:
                    res += self.excel[row][col]
            elif str[i] in '+-':
                res += digit*sign
                digit = 0
                sign = 1 if str[i]=='-' else 1
                i+=1
        return res


    def get_value(self, position1, position2 = None):
        if not position2:
            position2 = position1
        row_i, col_i = self.decodeCord(position1)
        row_j, col_j = self.decodeCord(position2)
        ans = 0
        for row in range(row_i, row_j+1):
            for col in range(col_i, col_j+1):
                ans += self.get_value_helper(row, col)
        return ans
    
    def get_value_helper(self, row, col):
        if (row, col) in self.equations:
            return self.compute(self.equations[(row, col)])
        else:
            return self.excel[row][col]
        

        

excel = Excel("Z10")
excel.set("A1", "5")
excel.set("A2", "=A1+1")
excel.set("A3", "=A2+5")
excel.set("A4", "=A2+A3")
print(excel.equations)

print(excel.get_value("A1"))
print(excel.get_value("A2"))
print(excel.get_value("A3"))
print(excel.get_value("A1", "A4"))