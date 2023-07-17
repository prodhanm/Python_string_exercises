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