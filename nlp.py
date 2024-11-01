import nltk

papers = {}

def read_files(filename):
    strings = []
    for file in filename:
        with open(file) as f:
            strings.append(f.read())

    return ('\n'.join(strings))

federalist_by_author = {}

for author, files in papers.item():
    federalist_by_author[author] = read_files(files)

authors = ('Hamilton','Madison','jay')
author_token = {}
length_distribution = {}

for a in authors:
    tokens = nltk.word_tokenize(federalist_by_author[a])

    author_token[a] = ([token for token in tokens if any(c.isaplha() for c in token)])
    token_lengths = [len(token) for token in author_token[a]]
    length_distribution[a] = nltk.FreqDist(token_lengths)
    length_distribution[a].plot(15, title=author)