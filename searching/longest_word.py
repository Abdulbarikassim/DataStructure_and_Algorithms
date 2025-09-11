"""
Find the longest word in the sentence and if there is a tier return the later word.
"""

def longest_word(sentence):
    longest = ""
    split_sent  = sentence.split()
    print(split_sent)
    for word in split_sent:
        if  len(word) >= len(longest):
            longest = word
    return longest


sentence = "Find the longest word in the sentence and if there is a tier return the later word"
print("Longest word: ", longest_word(sentence))


