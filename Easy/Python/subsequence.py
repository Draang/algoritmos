"""
Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original 
string with some characters (can be none) deleted without changing the 
relative order of the remaining characters.
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        matriz=[ [0 for l2 in range(len(text2)+1)] for l in range(len(text1)+1)]

        for l1 in range(len(text1)):
            for l2 in range(len(text2)):
                if text1[l1]==text2[l2]:
                    num=matriz[l1][l2]+1
                    matriz[l1+1][l2+1]=num
                else:
                    matriz[l1+1][l2+1]=max(matriz[l1+1][l2],matriz[l1][l2+1])
        return matriz.pop().pop()
            