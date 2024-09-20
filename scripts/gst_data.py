#!/usr/bin/env python
# coding: utf-8

# ### Import Required Libraries and Set Up Environment Variables
#

# In[1]:


# Dependencies
import os
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

# project service file for housing python functions
from notebooks.services import services

## Load the NASA_API_KEY from the env file
load_dotenv()
NASA_API_KEY = os.getenv("NASA_API_KEY")


#

# ### GST Data
#

# In[2]:


# Set the base URL to NASA's DONKI API:
base_url = "https://api.nasa.gov/DONKI/"

# Set the specifier for Geomagnetic Storms (GST):
GST = "GST"

# Search for GSTs between a begin and end date
startDate = "2013-05-01"
endDate = "2024-05-01"

# Build URL for GST
query_url = (
    f"{base_url}{GST}?startDate={startDate}&endDate={endDate}&api_key={NASA_API_KEY}"
)


# In[ ]:


# Convert the response variable to json and store it as a variable named gst_json
# Preview the first result in JSON format
# Use json.dumps with argument indent=4 to format data
gst_json = services.fetch_data(query_url, {}, True)


# In[ ]:


print(gst_json)


# In[ ]:


# Convert gst_json to a Pandas DataFrame
df = pd.DataFrame(gst_json)

# Keep only the columns: activityID, startTime, linkedEvents
df = df[["gstID", "startTime", "linkedEvents"]]
df.info()


# In[ ]:


# Notice that the linkedEvents column allows us to identify the corresponding CME
# Remove rows with missing 'linkedEvents' since we won't be able to assign these to CME
df = df.dropna(how="any")
df.isna().sum()


# In[ ]:


# Notice that the linkedEvents sometimes contains multiple events per row
# Use the explode method to ensure that each row is one element. Ensure to reset the index and drop missing values.
# Initialize an empty list to store the expanded rows
expanded_rows = services.expand_rows(df)
print(expanded_rows)


# In[ ]:


# Apply the extract_activityID_from_dict function to each row in the 'linkedEvents' column (you can use apply() and a lambda function)
# and create a new column called 'CME_ActivityID' using loc indexer:
df["GST_ActivityID"] = df.linkedEvents.apply(
    lambda x: services.extract_activityID_from_dict(x)
)

# Remove rows with missing CME_ActivityID, since we can't assign them to CMEs:
df.sample(n=5)


# In[ ]:


# Convert the 'CME_ActivityID' column to string format
# Convert the 'cmeID' column to string format
# Convert startTime to datetime format
# Rename startTime to startTime_CME
# Drop linkedEvents
# Verify that all steps were executed correctly
clean_df = services.clean_up(df, "gst")
clean_df.info()


# In[ ]:


# We are only interested in GSTs related to CMEs so keep only rows where the CME_ActivityID column contains 'CME'
# use the method 'contains()' from the str library.

# save all strings that contain 'CME'
gst_to_cme_events = clean_df[clean_df.GST_ActivityID.str.contains("CME")]

gst_to_cme_events.to_csv("../data/gst_to_cme_events.csv", index=False)

for event in gst_to_cme_events.GST_ActivityID:
    print(event)


# In[ ]:
