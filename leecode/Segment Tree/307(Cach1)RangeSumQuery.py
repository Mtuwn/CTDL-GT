from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * self.n + nums
        for i in reversed(range(self.n)):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]
        print(self.tree)

    def update(self, i: int, val: int) -> None:
        i += self.n
        self.tree[i] = val
        while i > 0:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def sumRange(self, i: int, j: int) -> int:
        i += self.n
        j += self.n + 1
        result = 0
        while i < j:
            if i & 1:
                result += self.tree[i]
                i += 1
            if j & 1:
                j -= 1
                result += self.tree[j]
            i >>= 1
            j >>= 1
        return result



# Test code
if __name__ == "__main__":
    # Initialize NumArray with the list [1, 3, 5]
    numArray = NumArray([1, 3, 5])
    
    # Query sumRange(0, 2), should return 9 (1 + 3 + 5)
    print(numArray.sumRange(0, 4))  # Output: 9
    
    # Update index 1 to 2
    numArray.update(1, 2)
    
    # Query sumRange(0, 2) again, should return 8 (1 + 2 + 5)
    print(numArray.sumRange(0, 2))  # Output: 8
