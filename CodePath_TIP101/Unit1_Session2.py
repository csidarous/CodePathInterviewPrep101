# def print_list(lst):
#   for i in lst:
#     print(i)

# lst = ["squirtle", "gengar", "charizard", "pikachu"]

# print_list(lst)


# ## Problem 2

# def doubled(lst):
#   for i in lst:
#     print(i * 2)


# lst = [1,2,3]
# doubled(lst)



## Peoblem 3
# def doubled(lst):
#   new_list = []
#   for i in lst:
#     new_list.append(i*2)
#   return new_list 

# lst = [1,2,3]
# print(doubled(lst))


##Problem 4
# def flip_sign(lst):
#     new_list = []
#     for i in lst:
#       new_list.append(i * -1)
#     return new_list

# lst = [1,-2,-3,4]
# flipped_lst = flip_sign(lst)
# print(flipped_lst)


##problem 5
# def max_difference(lst):
#   lst.sort()
#   min = lst[0]
#   max = lst[len(lst)-1]
#   diff = max - min
#   print(diff)


# lst1 = [5,22,8,10,2]
# max_diff = max_difference(lst1)


##Problem 6
# def count_less_than(numbers, threshold):
#   count = 0
#   for num in numbers:
#     if num < threshold:
#       count +=1
#   return count


# numbers = [12,8,2,4,4,10]
# counter = count_less_than(numbers,5)
# print(counter)

##Problem 7 
# def get_evens(lst):
#     evns = []
#     for num in lst:
#       if num %2 == 0:
#         evns.append(num)
#     return evns

# lst = [1,2,3,4]
# evens_lst = get_evens(lst)
# print(evens_lst)


##Problem 8
# def multiples_of_five():
#   for i in range(5, 101, 5):
#     print(i)

# multiples_of_five()

##Probelm 9
# def find_divisors(n):
#   lst = []
#   for i in range(n, 0, 1):
#     if n % i == 0:
#       lst.append(i)
#     return lst

# lst = find_divisors(6)
# print(lst)


##Problem 10
# def fizzbuzz(n):
#   for i in range(1,n):
#     if i % 3 == 0:
#       print("Fizz!")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#       print(i)
# fizzbuzz(13) 



##Problem 11
# def print_indices(lst):
#   for i in range(len(lst)):
#     print(i)

# lst = [5,1,3,8,2]
# print_indices(lst)


##Probelm 12

# def linear_search(lst, target):
#   for index, x in enumerate(lst):



# lst = [1,4,5,2,8]
# position = linear_search(lst,5)
# print(position)



def average(scores):
  total = 0
  for scor in scores:
    total += scor
  return total / len(scores)

scores = [84,73,92,95,88]
avg_score = average(scores)
print(avg_score)

