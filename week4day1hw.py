# # #Question 1:
words = ['this' , 'is', 'a', 'sentence', '.']


# def reverse(words):
#     left = 0
#     right = len(words) -1
    
#     while left <= right:
#         words[left], words[right] = words[right], words[left]
#         left += 1
#         right -= 1
#     return (words)
# wordslist.reverse()

# print(wordslist)

def reverseElements(words):
    for i in range(len(words)):
        words[i] = words[i][::-1]
    words.reverse()
    print(words)


reverseElements(words)

# Question 2:
# Exercise #2
# Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...
def word_count(str):
    counts = dict()
    str = str.lower()
    words = str.split()
    

    for word in words:
        
        if word in counts:
            counts[word] += 1
            
        
        else:
            counts[word] = 1

    return counts

print(word_count('In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'))

#Question #3:
# Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.
# Hint: Linear Searching will require searching a list for a given number.

# nums_list = [10,23,45,70,11,15]
# target = 70

# # If number is not present return -1

#Answer:
def search(num_list, j):
    for i in range(len(num_list)):
        if num_list[i] == j:
            return i
    return -1

print(search([10,23,45,70,11,15], 70))