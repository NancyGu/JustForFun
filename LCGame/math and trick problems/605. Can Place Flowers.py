# https://leetcode.com/problems/can-place-flowers/
# Step1: Solved 2019-1-8
# Step2: 在速度上做提升

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # 3空插1个，开头和结尾是2空
        i,count = 0, 0
        # 算最大插入量，如果n<最大，则return true
        while i < len(flowerbed):
            if (flowerbed[i] == 0 and ( i==0 or flowerbed[i-1] == 0) and ( i==len(flowerbed)-1 or flowerbed[i+1] == 0)):
                flowerbed[i] = 1;
                count = count + 1
            i = i + 1
        return count>=n