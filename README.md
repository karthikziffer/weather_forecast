# :cloud: :snowflake: weather_forecast :open_umbrella: 



The pip package provides weather forecasting information based on location or address. Using address, the weather_forecast provides location specific forecast. Currently only one function is included i.e forecast. 


### Install
```
pip install weather_forecast
```


### Code snippet :v:


1. Default date and time. 
```
import weather_forecast as wf
wf.forecast(place = "Bangalore")
```


2. Custome date, time and location
```
import weather_forecast as wf
wf.forecast(place = "Bangalore" , time="23:15:00" , date="2019-09-12" , forecast= "daily")
```


### Command Line usage
```
python forecast.py -p Bangalore
```

```
python forecast.py -p Bangalore -d 2019-09-15
```


