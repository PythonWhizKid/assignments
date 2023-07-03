#my code
#sentence = input("Enter a sentence: ")
#punc = sentence.strip(".,?!")
#words = punc.split(" ")
#for w in words:
 #   print(w,":" , words.count(w))
#It works fine but it iterates a word which has more than one occurences as many times it occurs, to fix that we need to create a dictionary

sentence = input("Enter a sentence: ")

punc = sentence.strip(".,?!")
words = punc.split(" ")
word_count = {} #create a dictionary
for w in words:
    if w in word_count:
        word_count[w] += 1 #value corresponding to that word increases by 1
    else:
        word_count[w] = 1
for w, count in word_count.items():
    print(f"{w} : {count}")
