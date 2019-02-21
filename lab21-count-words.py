"""
Write a python module to analyze a given text file containing a
book for its vocabulary frequency and display the most frequent
words to the user in the terminal. Remember there isn't any "perfect"
way to identify a word in english (acronymns, mr/ms, contractions,
etc), try to find rules that work best.

Open the file.
Make everything lowercase, strip punctuation, split into a list of words.
"""
from string import punctuation

STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
             'you', "you're", "you've", "you'll", "you'd", 'your', 'yours',
             'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she',
             "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself',
             'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
             'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am',
             'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has',
             'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the',
             'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of',
             'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into',
             'through', 'during', 'before', 'after', 'above', 'below', 'to',
             'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under',
             'again', 'further', 'then', 'once', 'here', 'there', 'when',
             'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few',
             'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not',
             'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't',
             'can', 'will', 'just', 'don', "don't", 'should', "should've",
             'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren',
             "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn',
             "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven',
             "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',
             "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn',
             "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't",
             'wouldn', "wouldn't"
             ]

with open('siddhartha.txt') as s:
    book = s.read().split()


word_list = []
for word in book:
    translator = str.maketrans('', '', punctuation)
    string_without_punct = word.translate(translator)
    word_list.append(string_without_punct.lower())
    # print(word_list)

# if word not in STOPWORDS:
word_dict = {}
for i in range(len(word_list)-1):
    if word_list[i] not in STOPWORDS:
        if (word_list[i], word_list[i+1]) not in word_dict:
            word_dict[(word_list[i], word_list[i + 1])] = 1
        else:
            word_dict[(word_list[i], word_list[i + 1])] += 1

# word_dict: a dictionary where the key is the word and the value is the count
# .items() returns a list of tuples
words = list(word_dict.items())
# sort largest to smallest, based on count
words.sort(key=lambda tup: tup[1], reverse=True)
# print the top 10 words, or all of them, whichever is smaller
for i in range(min(10, len(words))):
    print(words[i])
