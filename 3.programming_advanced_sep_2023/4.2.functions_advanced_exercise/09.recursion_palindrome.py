# Write a recursive function called palindrome() that will receive a word and an index (always 0). Implement the
# function, so it returns "{word} is a palindrome" if the word is a palindrome and "{word} is not a palindrome" if the
# word is not a palindrome using recursion.
#
# Input1:
# print(palindrome("abcba", 0))
#
# Output1:
# abcba is a palindrome
#
# Input2:
# print(palindrome("peter", 0))
#
# Output2:
# peter is not a palindrome

def palindrome(word, index):
    if index == len(word) //2: #we check to the middle, no need to check to the end because checking to the middle is enough
        return f"{word} is a palindrome"
    if word[index] != word[-1 - index]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
print()
print(palindrome("peter", 0))
