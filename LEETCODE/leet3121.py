def numberOfSpecialChars(word):
        count = 0
        checked = set()
        for i in range(len(word) - 1, -1, -1):
            letter = word[i]
            if 97 <= ord(letter) <= 122 and letter not in checked:
                checked.add(letter)
                upper = chr(ord(letter) - 32)                           #ai as it failed for "cCceDC" without this
                if upper in word[i:] and upper not in word[:i]:         #it checks if theres a upper befor i as we check for upper after i ourself
                    count += 1
        return count

word = "aaAbcBC"
print(numberOfSpecialChars(word))


# class Solution(object):                                       MY CODE 
#     def numberOfSpecialChars(self, word):
#         count = 0
#         checked = set()
#         for i in range(len(word)-1, -1, -1):
#             letter = word[i]
#             if 97 <= ord(letter) <= 122 and letter not in checked:
#                 checked.add(letter)
#                 if (chr(ord(letter) - 32) in word[i:]):
#                     count += 1
#         return count