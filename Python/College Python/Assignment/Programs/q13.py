#find number of vovels in a string and reverse each word using while loop and print it in dictionary format.
string = input("Enter a string: ")
vowels = input("Enter the vowels to be counted: ")
vowel_count = 0
words = string.split()
reversed_words = []

i = 0
while i < len(string):
    if string[i] in vowels:
        vowel_count += 1
    i += 1

i = 0
while i < len(words):
    reversed_words.append(words[i][::-1])
    i += 1

result = {"vowel_count": vowel_count, "reversed_words": reversed_words}

print(result)