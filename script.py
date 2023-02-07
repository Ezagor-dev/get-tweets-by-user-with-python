import snscrape.modules.twitter as sntwitter
import pandas as pd
from fpdf import FPDF

import webbrowser
import time

from jinja2 import Environment, FileSystemLoader



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

data = df
html_content = f'''
        <html> 
        <head> 
        <h1> {query} </h1> 
        </head>
        <body>
        {df}
           </body> 
           </html>
           '''

with open("index.html", "w") as html_file:
    html_file.write(html_content)
    print("HTML file created successfully !!")

    time.sleep(2)
    webbrowser.open_new_tab("index.html")



