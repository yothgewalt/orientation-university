interest_word = input()

text = input()
text = str.replace(text, "\"", "")

word_counts: int = 0

for word in text.split():
    if word == interest_word:
        word_counts += 1

print(word_counts)
