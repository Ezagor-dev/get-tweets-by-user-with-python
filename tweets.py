import snscrape.modules.twitter as sntwitter
import pandas as pd
from fpdf import FPDF

query = "(gb AND deprem AND hediye) until:2023-02-14 since:2023-02-04"
tweets = []
limit = 1000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=['Date', 'User','Tweet'])
print(df)


pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", "B",16 )

pdf.write(4, df.to_csv('new_example3',index=True))

pdf.output("file.pdf")


