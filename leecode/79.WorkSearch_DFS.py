"""
Ý tưởng:
- Tìm kiếm vị trí các ô có kí tự trùng với kí tự đầu của word để làm điểm khởi đầu
- Sử dụng thuật toán DFS để tìm kiếm vị trí các ô trên dưới trái phải có kí tự trùng với kí tự tiếp theo của word
- Mỗi lần đến thăm các ô đánh dấu nó là -1 
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def searchWord(x, y, index):
            # Trả về True nếu kí tự cuối của word vẫn được tìm thấy
            if index == len(word) - 1: 
                return word[index] == board[x][y]
            
            if word[index] != board[x][y]:
                return False

            # Đánh dấu các ô đã được ghé thăm là -1
            temp = board[x][y]
            board[x][y] = "-1"

            
            directions = [(-1,0), (0,1), (1,0), (0,-1)]

            for dx, dy in directions:
                new_dx, new_dy = x + dx, y + dy # Tương ứng với các ô trên dưới trái phải
                
                # Kiểm tra ô còn nằm trong board không và đã được ghé thăm hay chưa -> gọi đệ quy DFS
                if 0 <= new_dx < rows  and 0 <= new_dy < columns and board[new_dx][new_dy] != "-1": 
                    if searchWord(new_dx, new_dy, index + 1):
                        return True
            
            board[x][y] = temp
            
            return False



        rows, columns = len(board), len(board[0])

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == word[0] and searchWord(i, j, 0):
                    return True
                
        return False