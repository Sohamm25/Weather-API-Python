# import requests
# import pandas as pd
# api_key = '870618cb1a53f314adbfceded4e4747e'
# weather_df = pd.DataFrame(columns=["City", "Country", "Temp1", "Temp2", "Pressure", "Humidity"])
# while True:
#     city = input("Enter City name (type 'exit' to quit): ")
#     if city.lower() == 'exit':
#         break
#     try:
#         response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         data = response.json()
#         weather_data = {
#             "City": data['name'],
#             "Country": data['sys']['country'],
#             "Temp1": data['main']['temp_min'],
#             "Temp2": data['main']['temp_max'],
#             "Pressure": data['main']['pressure'],
#             "Humidity": data['main']['humidity'],
#         }
#         weather_df = pd.concat([weather_df, pd.DataFrame([weather_data])], ignore_index=True)
#     except requests.RequestException as e:
#         print("Error fetching data:", e)
#     except KeyError as e:
#         print("Error processing data:", e)
#     else:
#         print(weather_data)
# print("Weather data for all cities:")
# weather_df.index += 1
# print(weather_df)
# weather_df.to_csv('abc.csv', index=False)
# #2ND CODE - WITH SELECTION OF WHAT YOU WANT TO BE INCLUDED IN DATAFRAME 
import requests
import pandas as pd
api_key = '870618cb1a53f314adbfceded4e4747e'
weather_df = pd.DataFrame(columns=["City", "Country", "Temp_Min", "Temp_Max", "Pressure", "Humidity"])
while True:
    city = input("Enter City name (type 'exit' to quit): ")
    if city.lower() == 'exit':
        break
    try:
        ab = input("From - city, country, temp_min, temp_max, pressure, humidity, all. Choose one or multiple separated by comma: ").lower()
        ab = [i.strip() for i in ab.split(',')]
        if "all" in ab:
            ab = ["country", "temp_min", "temp_max", "pressure", "humidity"]
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        weather_data = {}
        for contents in ab:
            if contents == "country":
                weather_data["Country"] = data['sys']['country']
            elif contents == "temp_min":
                weather_data["Temp_Min"] = data['main']['temp_min']
            elif contents == "temp_max":
                weather_data["Temp_Max"] = data['main']['temp_max']
            elif contents == "pressure":
                weather_data["Pressure"] = data['main']['pressure']
            elif contents == "humidity":
                weather_data["Humidity"] = data['main']['humidity']
        weather_data["City"] = data['name']
        weather_df = pd.concat([weather_df, pd.DataFrame([weather_data])], ignore_index=True)
    except requests.RequestException as e:
        print("Error fetching data:", e)
    except KeyError as e:
        print("Error processing data:", e)
    else:
        print(weather_data)
print("Weather data for all cities:")
print(weather_df)