#Problem 1
# def is_long_pressed(name, typed):
#   pointer_1=0
#   pointer_2=0
#   while pointer_2 < len(typed):
#     if name[pointer_1]==typed[pointer_2]:
#       pointer_1+=1
#     elif typed[pointer_2] != typed[pointer_2-1]:
#       return False
#     pointer_2+=1

#   return pointer_1==len(name)

# name = "alex"
# typed = "aaleex"
# print(is_long_pressed(name, typed))

# name2 = "saeed"
# typed2 = "ssaaedd"
# print(is_long_pressed(name2, typed2))

# name3 = "courtney"
# typed3 = "courtney"
# print(is_long_pressed(name3, typed3))

##Problem 2 
# def find_content_children(size, greed):
#   pointer = 0
#   count = 0
#   while pointer < len(size):
#     if len(greed) > pointer:
#       if size[pointer] >= greed[pointer]:
#         count += 1
#     pointer += 1
#   return count

# g = [1,2,1]
# s = [1,4,3]
# print(find_content_children(s, g))

##Problem 3
# def valid_palindrome(s):
#   # if s ==s[::-1]:
#   #   return True
#   # else:
#   #   s=s.split()
#   #   for i in range(len(s)):
#   #     del s[i]
#   #     if s==s[::-1]:
#   #       return True
#   #     else:
#   #       continue
#   # return False

#   p1 = 0 
#   p2 = len(s) - 1

#   while p1 < p2:
#     if s[p1] == s[p2]:
#       continue
#     else:
#       p1 += 1





# s = "aba"
# s2 = "abca"
# s3 = "abc"

# print(valid_palindrome(s))
# print(valid_palindrome(s2))
# print(valid_palindrome(s3))


