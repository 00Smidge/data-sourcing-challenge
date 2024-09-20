#!/usr/bin/env python
# coding: utf-8

# ### Import Required Libraries and Set Up Environment Variables

# In[114]:


# Dependencies
import pandas as pd
from datetime import datetime


# 

# ### Merge both datatsets

# In[115]:


ctg_csv = pd.read_csv("data/composed/cme_to_gst_events.csv")
gtc_csv = pd.read_csv("data/composed/gst_to_cme_events.csv")
ctg_df = pd.DataFrame(ctg_csv)
gtc_df = pd.DataFrame(gtc_csv)


# In[ ]:


ctg_df.sample(n=5)


# In[ ]:


gtc_df.sample(n=5)


# In[118]:


# Now merge both datasets using 'gstID' and 'CME_ActivityID' for gst and 'GST_ActivityID' and 'cmeID' for cme. Use the 'left_on' and 'right_on' specifiers.

# gstID & CME_ActivityID: gst
# cmeID & GST_ActivityID: cme

ctg_df["cme"] = ctg_df["cmeID"] + "-" + ctg_df["CME_ActivityID"]
gtc_df["gst"] = gtc_df["gstID"] + "-" + gtc_df["GST_ActivityID"]


# In[ ]:


# Verify that the new DataFrame has the same number of rows as cme and gst
gtc_df.info()
gtc_df.isna().sum()


# In[ ]:


ctg_df.info()
ctg_df.isna().sum()


# In[ ]:


merge_result = pd.merge(
    gtc_df,
    ctg_df,
    left_on="gst",
    right_on="cme",
    how="outer",
)
merge_result = merge_result.fillna(method="ffill")


# In[ ]:


merge_result.sample(n=5)


# ### Computing the time it takes for a CME to cause a GST

# In[ ]:


merge_result.dropna(how="any")
merge_result.sample(n=5)


# In[124]:


# Compute the time diff between startTime_GST and startTime_CME by creating a new column called `timeDiff`.
merge_result.startTime_GST = pd.to_datetime(merge_result.startTime_GST)
merge_result.startTime_CME = pd.to_datetime(merge_result.startTime_CME)


# In[132]:


merge_result["timeDiff"] = merge_result["startTime_CME"] - merge_result["startTime_GST"]


# In[ ]:


merge_result.sample(n=5)


# In[ ]:


# Use describe() to compute the mean and median time
# that it takes for a CME to cause a GST.
merge_result.describe()


# ### Exporting data in csv format

# In[135]:


# Export data to CSV without the index
merge_result.to_csv("data/composed/gst_cme_merged.csv", index=False)


# In[ ]:




