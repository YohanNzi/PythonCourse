from collections import Counter


text = "Two roads diverged in a yellow wood, \
And sorry I could not travel both \
And be one traveler, long I stood \
And looked down one as far as I could \
To where it bent in the undergrowth."
text = text.lower()

dict_letter = []

for c in text:
    if c != ' ' and c != '!' and c != '.' and c != ',':
        dict_letter.append(c)

counts = Counter(dict_letter)

print(counts)
