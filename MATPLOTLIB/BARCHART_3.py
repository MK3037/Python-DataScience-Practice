from matplotlib import pyplot as plt
from collections import Counter
import pandas as pd
import os
os.chdir('C:\\Users\\purve\\OneDrive\\Desktop\\python\\EXTRA')
language_counter = Counter()

data=pd.read_csv('data.csv')
ids=data['Responder_id']
lang_response=data['LanguagesWorkedWith']

for responses in lang_response:
    language_counter.update(responses.split(';'))

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