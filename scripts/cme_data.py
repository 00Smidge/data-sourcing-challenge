#!/usr/bin/env python
# coding: utf-8

# ### Import Required Libraries and Set Up Environment Variables

# In[1]:


# Dependencies
import os
import sys
import pandas as pd
from dotenv import load_dotenv


# Add the parent directory (where the 'services' folder is located) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from notebooks.services import services

## Load the NASA_API_KEY from the env file
load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")


# 

# ### CME Data

# In[2]:


# Set the base URL to NASA's DONKI API:
base_url = "https://api.nasa.gov/DONKI/"

# Set the specifier for CMEs:
CME = "CME"

# Search for CMEs published between a begin and end date
startDate = "2013-05-01"
endDate = "2024-05-01"

# Build URL for CME
query_url = (
    f"{base_url}{CME}?startDate={startDate}&endDate={endDate}&api_key={NASA_API_KEY}"
)


# In[ ]:


# Convert the response variable to json and store it as a variable named cme_json
cme_json = services.fetch_data(query_url, {}, True)


# In[ ]:


# Convert cme_json to a Pandas DataFrame
df = pd.DataFrame(cme_json)

# Keep only the columns: activityID, startTime, linkedEvents
df = df[["activityID", "startTime", "linkedEvents"]]
df.info()


# In[ ]:


# Notice that the linkedEvents column allows us to identify the corresponding GST
# Remove rows with missing 'linkedEvents' since we won't be able to assign these to GSTs
df = df.dropna(how="any")
df.isna().sum()


# In[6]:


expanded_rows = services.expand_rows(df)


# In[ ]:


# Create a new DataFrame from the expanded rows
events_df = pd.DataFrame(expanded_rows)
events_df.sample(n=5)


# In[ ]:


# Apply this function to each row in the 'linkedEvents' column (you can use apply() and a lambda function)
# and create a new column called 'GST_ActivityID' using loc indexer:

df["CME_ActivityID"] = df.linkedEvents.apply(
    lambda x: services.extract_activityID_from_dict(x)
)

df.sample(n=5)


# In[ ]:


# Convert the 'GST_ActivityID' column to string format
# Convert the 'gstID' column to string format
# Convert startTime to datetime format
# Rename startTime to startTime_GST
# Drop linkedEvents
# Verify that all steps were executed correctly
clean_df = services.clean_up(df, "cme")
clean_df.info()


# In[ ]:


# We are only interested in CMEs related to GSTs so keep only rows where the CME_ActivityID column contains 'GST'
# use the method 'contains()' from the str library.

# save all strings that contain 'GST'
cme_to_gst_events = clean_df[clean_df.CME_ActivityID.str.contains("GST")]

cme_to_gst_events.to_csv("data/composed/cme_to_gst_events.csv", index=False)

# loop through the events and print each event
for event in cme_to_gst_events.CME_ActivityID:
    print(event)


# In[ ]:




