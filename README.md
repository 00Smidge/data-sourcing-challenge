# Data Sourcing Challenge

Prediction system to aid [NOOA](https://www.swpc.noaa.gov/about-space-weather) in the tracking of Geomagnetic Storms (GSTs)

### Part 1: [Request CME data from the NASA API](notebooks/cme_data.ipynb)

### Part 2: [Request GST data from the NASA API](notebooks/gst_data.ipynb)

### Part 3: [Merge and Clean the Data for Export](notebooks/merge_data.ipynb)

### Part D: [**Automation**](main.py)

notes:

 gst requests do not have parent activityID(s)

 convert the ipynb(s) into py script files
 jupyter nbconvert --to script --output-dir=./scripts notebooks/*.ipynb


## Sources

- [NASA](https://api.nasa.gov/): National Aeronautics and Space Administration
