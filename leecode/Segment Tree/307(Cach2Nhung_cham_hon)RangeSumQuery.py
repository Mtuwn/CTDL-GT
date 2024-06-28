# Nếu có đọc tới bài này thì hãy nhớ cách 1 chạy hiệu quả hơn 
# 2 cách nộp đều đã success nhưng các 1 là 1147 ms còn cái náyf 2217ms

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        if self.n > 0:
            self.nums = nums[:]
            self.tree = [0] * (4 * self.n)
            self._build(1, 0, self.n - 1)

    def _build(self, v, tl, tr):
        if tl == tr:
            self.tree[v] = self.nums[tl]
        else:
            tm = (tl + tr) // 2
            self._build(v*2, tl, tm)
            self._build(v*2+1, tm+1, tr)
            self.tree[v] = self.tree[v*2] + self.tree[v*2+1]

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self._update(1, 0, self.n - 1, index, val)

    def _update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.tree[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self._update(v*2, tl, tm, pos, new_val)
            else:
                self._update(v*2+1, tm+1, tr, pos, new_val)
            self.tree[v] = self.tree[v*2] + self.tree[v*2+1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self._sumRange(1, 0, self.n - 1, left, right)

    def _sumRange(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        return self._sumRange(v*2, tl, tm, l, min(r, tm)) + \
               self._sumRange(v*2+1, tm+1, tr, max(l, tm+1), r)


# Your NumArray object will be instantiated and called as such:
nums = [3, 1, 4, 1, 5, 9, 2, 6]
obj = NumArray(nums)
print("Initial segment tree:", obj.tree)

# Update index 3 to value 10
obj.update(3, 10)
print("Segment tree after update:", obj.tree)

# Sum range from index 2 to 5
param_2 = obj.sumRange(2, 5)
print("Sum of range [2, 5]:", param_2)

# Sum range from index 0 to 7 (entire array)
param_2 = obj.sumRange(0, 7)
print("Sum of range [0, 7]:", param_2)
