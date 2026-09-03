class Solution(object):
    def climbStairs(self, n):
        f1 = 0
        f2 = 1
        fn = 0
        for i in range(n):
            fn = f1 + f2
            f1 = f2
            f2 = fn
        return fn