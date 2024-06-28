# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         length = len(s)
#         maxlength = 1
#         start = 0
#         for i in range(length):
#             for j in range(i,length):
#                 flag = 1
#                 for k in range(0, (j-i)//2+1):
#                     if s[i+k] != s[j-k] :
#                         flag = 0
                
#                 if flag == 1 and j - i + 1 > maxlength:
#                     start = i
#                     maxlength = j - i +1

#         result = s[start:start + maxlength]
#         return result    

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        db = [[False] * n for _ in range(n)] # DB là một mảng 2 chiều được sử dụng để lưu trữ xem một chuỗi con có phải là palindrome hay không

        start = 0
        max_length = 1

        for i in range(n): # cho các chuỗi 1 kí tự luôn có giá trị là true 
            db[i][i] = True
        
        for i in range(n-1): # Kiểm tra xem chuỗi 2 kí tự có phải 2 kí tự trùng không
            if s[i] == s[i+1]:
                db[i][i+1] = True
                start = i
                max_length = 2
        
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1

                if db[i+1][j-1] and s[i] == s[j]:
                    db[i][j] = True
                    if length > max_length:
                        start = i
                        max_length = length
        print(max_length)
        print(s[start:start + max_length])

String = str(input('Nhập chuỗi: '))

test = Solution()
test.longestPalindrome(String)



