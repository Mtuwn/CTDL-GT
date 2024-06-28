class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ListLongest = [] # Sử dụng mảng này để lưu chuỗi các kí tự k bị trùng
        left = 0
        max_length = 0

        for right, char in enumerate(s):

            while char in ListLongest: # Kiểm tra đến khi nào chuỗi không còn chứa kí tự char nữa
                ListLongest.pop(0)
                left += 1  # Di chuyển con trỏ trái sang phải một vị trí

            # Thêm ký tự hiện tại vào danh sách
            ListLongest.append(char)
            # Cập nhật độ dài tối đa của chuỗi con không lặp
            max_length = max(max_length, right - left + 1)

        return max_length
