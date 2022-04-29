# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# a=input("Enter string 1:")

# b=input("Enter string 2:")

# count=0

# for i in a:

#     for j in b:

#         if i==j:

#             count=count+1

# if count==len(a):

#     print("Strings are anagram of each other.")


# from numpy import append

newlist = []
# def anagram(string):
#     count = 0
#     for i in string:
#         for j in string:
#             if i==j:
#                 count = count+1
#                 newlist.append(i)
#             else:
#                 newlist.append(i)
string = ["eat","tea","tan","ate","nat","bat"]
# for i in string:
    
#     if i == string:
#         newlist.append(i)
#     else:
#         newlist.append(i)
# print(newlist)
string = ["eat","tea","tan","ate","nat","bat"]
# class Solution:
#     def groupAnagrams(self, strs):
#         allResults=[]
#         results=[]
#         temp=''
#         for s in strs:  
#           temp=s[1:]+s[:1]
#           for i in range(0,len(strs)):
#               if temp==strs[i]:
#                 results.append(strs[i])
#           allResults.append(results)      
#           print(results)
#           return allResults  

# obj = Solution()
# print(obj.groupAnagrams(string))

class Solution(object):
    def groupAnagrams(self, strs):
        allResults = []
        added = set([])
        temp=''
        for i, s in enumerate(strs):
            results = []
            unique_s = "".join(sorted(s))
            if unique_s in added:
                continue
            else:
                added.add(unique_s)
            for x in strs[i:]:
              if unique_s=="".join(sorted(x)):
                results.append(strs[i])
            allResults.append(results)

        print(added)

        return allResults
obj = Solution()
print(obj.groupAnagrams(string))