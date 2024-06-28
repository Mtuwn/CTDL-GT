class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        step = -1
        rows = [""] * numRows
        column = 0
        for char in s:
            rows[column] += char
            if column == 0 or column == numRows - 1:
                step = -step
            column += step
        
        return "".join(rows)
        

String = str(input('Nhập chuỗi: '))
number = int(input("Number: "))

test = Solution()
test.convert(String, number)
