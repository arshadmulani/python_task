from collections import Counter
paragraph="apple banana apple orange banana banana"
words=paragraph.split()
word_count=Counter(words)
for word, count in word_count.items():
    print(f"{word}:{count}")
