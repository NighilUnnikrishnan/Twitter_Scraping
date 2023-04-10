# Twitter_Scraping using snscrape and webapp deployment using streamlit:

**Module Description:**

**snscrape -** It is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items, e.g. the relevant posts. It can scrape data from popular social media sites like Twitter, Facebook, Instagram, etc..,.

Read more about snscrape here https://github.com/JustAnotherArchivist/snscrape.git

**streamlit -** It turns data scripts into shareable web apps using pythong without having the need to learn front-end development.

Read more about streamlit here https://docs.streamlit.io/

**Requirements**
snscrape.modules.twitter as snt
pandas
pymongo
streamlit
import datetime as dt
from datetime import timedelta as td
import json
import urllib.parse

**Project Description:**

In this project, we will be scraping data from twitter based on twitter handle name or hashtag name. We will scrape the following data.

_['Datetime','Tweet Id','Tweet URL','Tweet Content','User Name','Reply Count','Retweet Count','Tweet Language','Source', 'Like Count']_

The entire code has been written using python 
