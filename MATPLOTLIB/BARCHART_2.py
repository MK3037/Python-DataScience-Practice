from matplotlib import pyplot as plt
from collections import Counter
import csv
import os
os.chdir('C:\\Users\\purve\\OneDrive\\Desktop\\python\\EXTRA')
language_counter = Counter()

with open('data.csv') as f:
    f = csv.DictReader(f)          # reads header automatically, skips it
    for line in f:
        # print(line)                {'Responder_id': '88249', 'LanguagesWorkedWith': 'Python;Ruby;Swift'}
        languages = line['LanguagesWorkedWith']
        language_counter.update(languages.split(';'))

top_n = 15
languages = []
counts = []
for lang, count in language_counter.most_common(top_n):
    languages.append(lang)
    counts.append(count)

plt.bar(languages, counts)          #TRY .BARH and change axes labels
plt.xticks(rotation=75)
plt.xlabel("Languages")
plt.ylabel("Number of People Who Use")
plt.title("Most Popular Languages")
plt.tight_layout()
plt.show()