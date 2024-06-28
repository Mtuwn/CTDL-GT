## Chưa giải
# class SegmentTreeNode:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.sum = 0
#         self.left = None
#         self.right = None

# class SegmentTree:
#     def __init__(self, nums):
#         self.root = self._build_tree(nums, 0, len(nums) - 1)

#     def _build_tree(self, nums, start, end):
#         if start > end:
#             return None
#         root = SegmentTreeNode(start, end)
#         print(root.sum)
#         if start == end:
#             root.sum = nums[start]
#         else:
#             mid = (start + end) // 2
#             root.left = self._build_tree(nums, start, mid)
#             root.right = self._build_tree(nums, mid + 1, end)
#             root.sum = root.left.sum + root.right.sum
                   
#         return root

#     def update(self, root, index, val):
#         if root.start == root.end:
#             root.sum = val
#         else:
#             mid = (root.start + root.end) // 2
#             if index <= mid:
#                 self.update(root.left, index, val)
#             else:
#                 self.update(root.right, index, val)
#             root.sum = root.left.sum + root.right.sum

#     def query(self, root, start, end):
#         if root.start == start and root.end == end:
#             return root.sum
#         mid = (root.start + root.end) // 2
#         if end <= mid:
#             return self.query(root.left, start, end)
#         elif start > mid:
#             return self.query(root.right, start, end)
#         else:
#             return self.query(root.left, start, mid) + self.query(root.right, mid + 1, end)

# nums = [1, 3, 5, 7, 9, 11]
# seg_tree = SegmentTree(nums)
# # print(seg_tree.query(seg_tree.root, 1, 3))  # Output: 3+5+7=15
# # seg_tree.update(seg_tree.root, 2, 6)
# # print(seg_tree.query(seg_tree.root, 1, 4))  # Output: 3+6+7+9=25
