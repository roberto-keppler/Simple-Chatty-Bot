word1 = input()
word2 = input()

# How many letters does the longest word contain?
len_word1 = len(word1)
len_word2 = len(word2)
maximum = len_word1
if maximum < len_word2:
    maximum = len_word2
print(maximum)
