from more_itertools import strip

# Testing a palindrome from a list of words
def palindr():
    words = ["kayak", "wow", "defied", "military", "poem", "racecar"]
    # words = "kayak"
    for word in words:
        for w in range(len(word)//2):
            if word[w] != word[len(word)-w-1]:
                palindrome = f"{word} is not a palidrome"
            else:
                palindrome = f"{word} is a palindrome."
        print(palindrome)

palindr()

# Testing a char to char ratio with three args in a range()
def w_ratio():
    words = "Anathema"
    for word in range(1,len(words)-1, 2):
        print(f"The index is at {word,word+1}:{words[word:word+2]}")
    # The result with the {word,word+1} is that the index is stored 
    # in a tuple.
w_ratio()

# concatenating strings in a list 
def str_case():
    words = ["I", "am", "going", "to", "the", "supermarket", "!"]
    quote = " "
    for word in range(0,len(words)):
        if len(words) > 0:
            quote = " ".join(words)
        else:
            quote = words[word]
    return quote.strip()
#Tech debt: figure out how to close out "!" into the last word."

print(str_case())

# if you want to reverse the srting
print(str_case()[::-1])

# parsing a char from a string
def parse_a():
    word = "Star Trek"
    for w in range(0, len(word), 2):
        print(word[w].capitalize())
    
parse_a()

# counting vowels
word_2 = "Pseudopseudohypoparathyroidism"

def vowel_ct(word_2):
    vowel = 'aeiou'
    vowels = 0
    for w in range(len(word_2)):
        if word_2[w] in vowel:
            vowels += 1
    return vowels

print(vowel_ct(word_2))

def vowel_li(word_2):
    vowel = 'aeiou'
    vowels = []
    for w in range(len(word_2)):
        if word_2[w] in vowel:
            vowels.append(word_2[w])
    return vowels

print(vowel_li(word_2))

        


                     
