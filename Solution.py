#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Solution:
    """
    @param: A: an integer rotated sorted array
    @param: target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        index = 0
        if target in A:
            for i in A:
                if i == target:
                    return index  
                    # print(index)
                
                index += 1
        else:
            return -1  
            # print(-1)

            



def main():
    lst = [4, 5, 1, 2, 3]

    s = Solution()
    s.search(lst, 1)

if __name__ == '__main__':
    main()