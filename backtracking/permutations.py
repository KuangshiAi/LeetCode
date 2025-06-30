class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False
        
        backtrack([], [False]*len(nums))
        return res
        
        # res = []  # 最终结果列表

        # def backtrack(path, used):
        #     if len(path) == len(nums):   # 如果 path 长度和 nums 一样，说明形成了一个完整排列
        #         res.append(path[:])      # 复制 path 添加到结果中
        #         return
        #     for i in range(len(nums)):   # 遍历 nums 中每个数字
        #         if used[i]:              # 如果这个数字已经用过，跳过
        #             continue
        #         used[i] = True           # 标记当前数字已使用
        #         path.append(nums[i])     # 选择这个数字，加入 path 中
        #         backtrack(path, used)    # 递归继续构造下一个位置
        #         path.pop()               # 回溯：撤销刚才的选择
        #         used[i] = False          # 回溯：标记这个数字未使用

        # backtrack([], [False] * len(nums))  # 初始调用
        # return res