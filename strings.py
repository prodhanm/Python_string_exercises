from more_itertools import strip

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

def w_ratio():
    words = "Anathema"
    for word in range(1,len(words)-1, 2):
        print(f"The index is at {word,word+1}:{words[word:word+2]}")
    # The result with the {word,word+1} is that the index is stored 
    # in a tuple.
w_ratio()

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
print(str_case()[::-1])


                     
