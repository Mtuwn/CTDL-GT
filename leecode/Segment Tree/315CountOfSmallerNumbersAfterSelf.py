class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        self.count = [0] * n
        indexed_nums = list(enumerate(nums))
        self.merge_sort(indexed_nums)
        return self.count
    
    def merge_sort(self, indexed_nums):
        if len(indexed_nums) < 2:
            return indexed_nums
        
        mid = len(indexed_nums) // 2
        left_half = indexed_nums[:mid]
        right_half = indexed_nums[mid:]
        
        left_sorted = self.merge_sort(left_half)
        right_sorted = self.merge_sort(right_half)
          
        return self.merge(left_sorted, right_sorted)
    
    def merge(self, left, right):
        merged = []
        # print(left)
        # print(right)
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index][1] <= right[right_index][1]:
                merged.append(left[left_index])
                self.count[left[left_index][0]] += right_index
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        
        while left_index < len(left):
            merged.append(left[left_index])
            self.count[left[left_index][0]] += right_index
            left_index += 1
        
        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1
        
        return merged
    
array = [5,2,6,1,7,4]
a = Solution()
a.countSmaller(array)


# Trong hàm merge, chúng ta so sánh các phần tử từ hai mảng con left và right. Nếu phần tử từ left nhỏ hơn hoặc bằng phần tử từ right, điều này có nghĩa là:

# Phần tử này nhỏ hơn hoặc bằng tất cả các phần tử đã được thêm vào từ mảng right cho đến thời điểm đó.
# Do đó, số lượng phần tử từ right đã được thêm vào chính là số lượng phần tử nhỏ hơn mà chúng ta cần cộng vào self.count cho phần tử từ left.