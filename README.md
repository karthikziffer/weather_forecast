# weather_forecast :open_umbrella: 



The pip package provides weather forecasting information based on location or address. Using address, the weather_forecast provides location specific forecast. Currently only one function is included i.e forecast. 



### Code snippet :v:


1. Default date and time. 
```
import weather_forecast
print(forecast(place = "Bangalore"))
```


2. Custome date, time and location
```
import weather_forecast
print(forecast(place = "Bangalore" , time="23:15:00" , date="12-09-2019" , forecast= "daily"))
```
