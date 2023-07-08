#solution15
#Write a Python program to find the length of the longest word in a sentence
def word_list(string):
    split_str = string.split(" ")
    return split_str
def len_words(words):
    all_lengths = []
    for i in words:
        length = len(str(i))
        all_lengths.append(length)
    return all_lengths
def max_length(all_lengths):
    result = max(all_lengths)
    return result
string = input("Enter a sentence: ")
words = word_list(string)
all_lengths = len_words(words)
result = max_length(all_lengths)
print(f"Length of the longest word is {result}")
