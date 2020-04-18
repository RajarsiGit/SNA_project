import COVID19Py
covid19 = COVID19Py.COVID19(data_source="jhu")
latest = covid19.getLatest()
locations = covid19.getLocations()
print(latest)
print(locations)
