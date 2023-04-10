# Twitter_Scraping using snscrape and webapp deployment using streamlit:

**Module Description:**

**snscrape -** It is a scraper for social networking services (SNS). It scrapes things like user profiles, hashtags, or searches and returns the discovered items, e.g. the relevant posts. It can scrape data from popular social media sites like Twitter, Facebook, Instagram, etc..,.

Read more about snscrape here https://github.com/JustAnotherArchivist/snscrape.git

**streamlit -** It turns data scripts into shareable web apps using pythong without having the need to learn front-end development.

Read more about streamlit here https://docs.streamlit.io/


**Requirements**
snscrape module (requires pythong 3.8 or higher)
pandas library
pymongo module
streamlit module
datetime module
urllib.parse module


**Project Description:**

In this project, we will be scraping data from twitter based on twitter handle name or hashtag name. We will scrape the following data.

_['Datetime','Tweet Id','Tweet URL','Tweet Content','User Name','Reply Count','Retweet Count','Tweet Language','Source', 'Like Count']_

The entire code has been written using python and the input is taken directly from the deployed streamlit app, where the user will provide the necessary input data. After execution of the code, the output (scraped data) is displayed as a pandas dataframe and the user has the option to upload the data to a Mongodb cloud server or download in .json and .csv formats.


**Code Description:**

The python code has 5 functional blocks viz, (_'Scrapetweets()','Streamlit_interface()','init_connection(),'Store_to_mongodb()' and 'Execution()'_) as explained below.

  1. Function 'Scrapetweets()': This function block contains the code for scraping the tweets. The function execution requires the **user inputs**,
**'Twitterhandle' or 'hashtag'** name for keyword search, **'Starting and Ending Dates'**(taken as separate inputs) for date range to search, and **'Tweet limit'** to limit the number of tweets to be scraped (between 1 and 1,000). The function is **called under the 'Execution()' block.**

  2. Function 'Streamlit_interface()': The code for the Streamlit GUI or webapp is written in this functional block. This function **takes multiple inputs** **from** the **streamlit app** as variables **and passes it onto the 'Scrapetweets()' function** as a single variable. This is the **first function called in the code** and is not part of any functional blocks.

  3. Function 'init_connection()': The code block contains the code to connect to Mongodb cloud servers. The connection to the cloud server is established by passing the login credentials as variables, from the **Web App's Secrets** folder to the code block. This function is **called under the 'Store_to_mongodb()' block.**

  4. Function 'Store_to_mongodb()': This block contains the code for storing the displayed dataframe data to mongodb database. The scraped data is stored as **documents** having the **keys ('Scrapped_Name', 'Scrapped_Date', 'Scraped_Data')** under a designated collection in a designated database. The function is **called in the 'Execution()' block** by user action in the streamlit web app. 
  
  5. Function 'Execution()': This function block contains the entire code for **initiating the scraping**, **displaying** the data in a **dataframe**, **uploading or downloading** the scraped data. This function is called outside other function blocks.


**Execution Flow**
  1. The **'Streamlit_interface()'** function is **called when the app is deployed**, followed by the 'Execution()' function. 
  2. The **user provides** the necessary **input** directly in the **streamlit app**.
  3. The user **input data** is converted and **stored** as the **'scrapekeys' global variable**.
  4. The 'scrapekeys' **variable is passed** to the **'Scrapetweets()'** function which is called by the 'Execution()' block.
  5. **Based on the user's input**, the 'Execution()' function runs the code to **either display the data** alone or to **display and upload to mongodb**. Running **either options** will provide the **option to download the data** in the required format.


**To note:**
Streamlit doesn't allow looping of 'st.button()' to execute one command after another based on consecutive inputs. This created an issue where the data couldn't be displayed first and then uploaded, as the 'st.button('upload')' for uploading couldn't be embedded inside the 'st.button('display')' for displaying data. To overcome this, 'st.selectbog()' is used. Using this input widget, three different session states are generated and the user is given the option to either display the data alone or display and upload. But, after each execution, it is advised to keep the widget in 'None' state to avoid unwanted execution.
        ![image](https://user-images.githubusercontent.com/130289201/231006884-ca7b23f0-e6a8-4459-87d0-793e5a897d44.png)


