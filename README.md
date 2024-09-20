# Data Sourcing Challenge

Prediction system to aid [NOOA](https://www.swpc.noaa.gov/about-space-weather) in the tracking of Geomagnetic Storms (GSTs)

## Sources

- [NOOA](https://www.swpc.noaa.gov/about-space-weather): Space Weather Prediction Center
- [NASA](https://api.nasa.gov/): National Aeronautics and Space Administration

notes:

	gst requests do not have parent activityID(s)

	convert the ipynb(s) into py script files
	jupyter nbconvert --to script --output-dir=./scripts notebooks/*.ipynb