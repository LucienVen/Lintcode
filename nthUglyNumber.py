#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Solution:
    """
    @param: n: An integer
    @return: the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        # write your code here
        if type(n) is not int:
            raise TypeError("n type error")

        temp = 0
        res = []

        while True:

            if len(res) == n:
                # print("loop break")
                print("第N位丑数为：{}".format(res[n - 1]))
                break

            temp += 1
            test = temp
            # print("test: {}".format(test))
            if temp == 1:
                res.append(temp)
                continue
            # 判断是否丑数
            # while test != 0:
            test = self.mold(test, 2)
            if test == 0:
                res.append(temp)
                continue
            else:
                test = self.mold(test, 3)

            if test == 0:
                res.append(temp)
                continue
            else:
                test = self.mold(test, 5)

            if test == 0:
                res.append(temp)
                # else:
                #     continue



            # 取模，递归
    def mold(self, n, m):
        # print("n={}, m={}".format(n, m))
        if type(m) is not int:
            raise TypeError("n type error")
        if type(n) is not int:
            raise TypeError("n type error")
        if m not in [2, 3, 5]:
            raise ValueError("in mold value")

        if n in [2, 3, 5]:
            return 0

        mold_value = n % m

        if mold_value == 0:
            return self.mold(n//m, m)
        else:
            return n



def main():
    test = Solution()
    test.nthUglyNumber(30)
    # test.mold(30, 2)


if __name__ == '__main__':
    main()