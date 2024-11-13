from collections import Counter

def countWords(text):
    words = text.split()
    return len(words)

def countCharacters(text):
    return len(text)

def findLongestWord(text):
    words = text.split()
    return max(words, key=len)

def wordFrequency(text):
    words = text.split()
    return Counter(words)

def main():
    text = input("Enter text: ")
    print("Word count:", countWords(text))
    print("Number of characters:", countCharacters(text))
    print("Longest word:", findLongestWord(text))
    print("Word frequency:", wordFrequency(text))

if __name__ == "__main__":
    main()
