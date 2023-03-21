
    
#Count the number of vowels,consontants,digit and special characters in a string using while loop and check for upper and lower case.

string = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
special_characters = 0
i = 0
while (i < len(string)):
    if (string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u' or string[i] == 'A' or string[i] == 'E' or string[i] == 'I' or string[i] == 'O' or string[i] == 'U'):
        vowels = vowels + 1
    elif (string[i] >= 'a' and string[i] <= 'z' or string[i] >= 'A' and string[i] <= 'Z'):
        consonants = consonants + 1
    elif (string[i] >= '0' and string[i] <= '9'):
        digits = digits + 1
    else:
        special_characters = special_characters + 1
    i = i + 1
count = vowels + consonants + digits + special_characters
print("Total number of characters in a string: ", count)
print("Total number of vowels in a string: ", vowels)
print("Total number of vovels in ")