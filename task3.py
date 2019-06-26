def find_longest_word(inputstring_list):
    longest=0
    for words in inputstring.split():
        if len(words) > longest:
             longest = len(words)
             longest_word = words     
    return longest_word, len(longest_word)

print("Please input a list of words to evaluate: ")
inputstring=input()
print(find_longest_word(inputstring))
