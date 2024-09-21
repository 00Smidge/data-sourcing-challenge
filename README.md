# Data Sourcing Challenge

Prediction system to aid [NOOA](https://www.swpc.noaa.gov/about-space-weather) in the tracking of Geomagnetic Storms (GSTs)

## Development Environment

[Python 3.12.4](https://www.python.org/downloads/release/python-3124/)

## "Production" Environment (personal version on some functions)

 [Python 3.12.4](https://www.python.org/downloads/release/python-3124/)
 Service function differences: [services](notebooks/services/services.py)
 cme_data differences: [services](notebooks/cme_data.ipynb)
 gst_data differences: [services](notebooks/gst_data.ipynb)
 merge_data differences: [services](notebooks/merge_data.ipynb)

## Workflow Brake Down

 All custom functions including those used for making request.get() class are housed in
 the [services](notebooks/services/services.py). 

### Part 1: [Request CME data from the NASA API](notebooks/cme_data.ipynb)

	1. ```query_url``` 
 1. ```get``` 
 1. ```cme_response``` 
 1. ```cme_json``` 
 1. ```activityId```, ```startTime```,```linkedEvents```
 1. ```json.dumps(data, indent=4)``` 
 1. ```extract_activityID_from_dict``` 
 1. ```GST_ActivityID``` 

### Part 2: [Request GST data from the NASA API](notebooks/gst_data.ipynb)

### Part 3: [Merge and Clean the Data for Export](notebooks/merge_data.ipynb)

### Part D: [**Automation**](main.py)

 convert the ipynb(s) into py script files
 jupyter nbconvert --to script --output-dir=./scripts notebooks/*.ipynb

### Part E(Jupyter Notebook): [**Automation**](main.ipynb)

## Sources

- [NASA](https://api.nasa.gov/): National Aeronautics and Space Administration
