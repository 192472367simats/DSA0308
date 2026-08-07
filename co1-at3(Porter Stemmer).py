class PorterStep2:
    def stem(self, word):
        n = len(word)
        if n >= 4:
            if word[n-4] == 'i' and word[n-3] == 'z' and word[n-2] == 'e' and word[n-1] == 'r':
                result = ""
                for i in range(n-4):
                    result = result + word[i]
                result = result + "ize"
                return result
        return word
obj = PorterStep2()
word = input("Enter a word: ")
print("Stemmed word:", obj.stem(word))
