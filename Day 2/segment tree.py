from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 1, 0, self.n - 1)

    def build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
            return

        mid = (start + end) // 2

        self.build(nums, 2 * node, start, mid)
        self.build(nums, 2 * node + 1, mid + 1, end)

        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2

        return (
            self.query(2 * node, start, mid, left, right) +
            self.query(2 * node + 1, mid + 1, end, left, right)
        )

    def sumRange(self, left: int, right: int) -> int:
        return self.query(1, 0, self.n - 1, left, right)