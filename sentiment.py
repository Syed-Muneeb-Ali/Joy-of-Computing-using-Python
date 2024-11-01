import nltk.downloader
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')

file = 'data.csv'
# If it's a CSV file, use:
# cs = pd.read_csv(file)
# If it's an Excel file, use:
xl = pd.read_excel(file)

# parsing excel sheet to data frame
dfs = xl.parse(xl.sheet_names[0])

# remove the blank rows
dfs = list(dfs['Timeline'])
print(dfs)

sid = SentimentIntensityAnalyzer()
for data in dfs:
    ss = sid.polarity_scores(data)
    print(data)
    for k in ss:
        print(k, ss[k])