import snscrape.modules.twitter as snt
import pandas as pd
from pymongo import MongoClient
import streamlit as st
import datetime as dt
import json
import urllib.parse

def Scrapetweets():
    Tweets=[]
    for i, tweet in enumerate(snt.TwitterSearchScraper(scrapekeys).get_items()):
                              if i ==Tweet_limit:
                                  break
                              Tweets.append([tweet.date,tweet.id,tweet.url,
                                             tweet.content,
                                             tweet.user.username,
                                             tweet.replyCount,
                                             tweet.retweetCount,tweet.lang,
                                             tweet.source,tweet.likeCount])
    global Tweets_df
    Tweets_df=pd.DataFrame(Tweets,columns=['Datetime','Tweet Id','Tweet URL',
                                           'Tweet Content','User Name',
                                           'Reply Count','Retweet Count',
                                           'Tweet Language','Source',
                                           'Like Count'])
    return Tweets_df
    print(Tweets_df)

def Streamlit_interface():
    st.title('**Twitter Scraping**')
    global Twitterhandle
    Twitterhandle=st.text_input('''Enter :blue[**Twitter handle**] name 
                                without :red[**@**]''',"",
                                placeholder='Eg: @elonmusk → elonmusk')
    if Twitterhandle!="":
        pass
    else:
        st.write(':red[*Field cannot be empty*]')
        
    global Startdate
    Startdate=st.date_input('Enter Starting date',dt.date.today(),
                            min_value=dt.date(2023,1,1),
                            max_value=dt.date.today())
    global Enddate
    Enddate=st.date_input('Enter Ending date',dt.date.today(),
                          min_value=Startdate,
                          max_value=dt.date.today())
    st.write('Note: Ending date is not inclusive. So, select 1 day further'
             ' to have the previous date included.')
    global Tweet_limit
    Tweet_limit=int(st.number_input('Enter a number :red[between 1 and 1,000]'
                                    ,min_value=1,max_value=1000))
    if Tweet_limit!="":
        pass
    else:
        st.write(':red[*Field cannot be empty*]')
        
#def init_connection():
   # username=urllib.parse.quote_plus(st.secrets.mongo_username)
    #password=urllib.parse.quote_plus(st.secrets.mongo_password)
    #return MongoClient("mongodb+srv://"+username+":"+password+"@st.secrets.cluster_name.gw5r3mj.mongodb.net/?retryWrites=true&w=majority")

def init_connection():
    username=st.secrets.mongo_username
    password=st.secrets.mongo_password
    return MongoClient("mongodb+srv://"+username+":"+password+"@st.secrets.cluster_name.gw5r3mj.mongodb.net/?retryWrites=true&w=majority")

#def init_connection():
    #username=urllib.parse.quote_plus('nighil_unnikrishnan')
    #password=urllib.parse.quote_plus('Rasenmongoatlas@94')
    #return MongoClient("mongodb+srv://"+username+":"+password+"@cluster0.gw5r3mj.mongodb.net/?retryWrites=true&w=majority")

def Store_to_mongodb():
    client = init_connection()
    db = client['Test_database']
    mycol=db['Tweet_Collection']
    mydoc={"Scraped_Name":Twitterhandle,
           "Scraped_Date":str(Startdate)+" to "+str(Enddate),
           "Scraped_Data":Tweets_df.to_dict("records")}
    mycol.insert_one(mydoc)
    st.write('Upload Succesful!')
        
Streamlit_interface()

State = st.selectbox('''Choose the action to be performed: 
                     (Keep :red['None'] to avoid unwanted execution)''',
                      ('None','Display data','Display and upload to Mongodb'),0)
if State=='None':
    pass
elif State=="Display data":
    if Twitterhandle=="":
        st.write('*:red[Please enter Twitterhandle name]*')
    else:
        scrapekeys='from:'+Twitterhandle+" since:"+str(Startdate)+" until:"+str(Enddate)
        Scrapetweets()
        st.dataframe(Tweets_df)
        st.cache_data
        st.download_button('Download as .json file',
                Tweets_df.to_json(),Twitterhandle+'\'s Tweets.json',
                mime='json'
                )
        st.download_button('Download as .csv',
                Tweets_df.to_csv(),Twitterhandle+'\'s Tweets.csv',
                mime='csv'
                )
else:
    if Twitterhandle=="":
        st.write('*:red[Please enter Twitterhandle name]*')
    else:
        scrapekeys='from:'+Twitterhandle+" since:"+str(Startdate)+" until:"+str(Enddate)
        Scrapetweets()
        st.dataframe(Tweets_df)
        st.cache_data
        Store_to_mongodb()
        st.download_button('Download as .json file',
                Tweets_df.to_json(),Twitterhandle+'\'s Tweets.json',
                mime='json'
                )
        st.download_button('Download as .csv',
                Tweets_df.to_csv(),Twitterhandle+'\'s Tweets.csv',
                mime='csv'
                )





    

    
    
    
    
    
    
