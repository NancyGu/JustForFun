# https://leetcode.com/problems/jewels-and-stones/submissions/
# 771. Jewels and Stones
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # count 统计出现次数的方法
        # map 将方法应用于第二个参数list
        return sum(map(J.count, S))
