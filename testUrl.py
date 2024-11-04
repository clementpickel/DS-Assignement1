import requests

parameter_info = {
    1: "Air Temperature, Instantaneous value, once per hour, Celsius",
    2: "Air Temperature, Daily average, once daily at 00:00, Celsius",
    3: "Wind Direction, 10-minute average, once per hour, degrees",
    4: "Wind Speed, 10-minute average, once per hour, meters per second",
    5: "Precipitation Amount, Sum daily, once daily at 06:00, millimeters",
    6: "Relative Humidity, Instantaneous value, once per hour, percent",
    7: "Precipitation Amount, Sum hourly, once per hour, millimeters",
    8: "Snow Depth, Instantaneous value, once daily at 06:00, meters",
    9: "Air Pressure (Sea Level Adjusted), Sea level, instantaneous value, once per hour, hectopascal",
    10: "Sunshine Duration, Sum per hour, once per hour, seconds",
    11: "Global Irradiance (Swedish stations), Average per hour, every hour, watts per square meter",
    12: "Visibility, Instantaneous value, once per hour, meters",
    13: "Current Weather, Instantaneous value, once per hour or 8 times daily, code",
    14: "Precipitation Amount, Sum over 15 minutes, four times per hour, millimeters",
    15: "Precipitation Intensity, Max over 15 minutes, four times per hour, millimeters per second",
    16: "Total Cloud Cover, Instantaneous value, once per hour, percent",
    17: "Precipitation, Twice daily at 06:00 and 18:00, code",
    18: "Precipitation, Once daily at 18:00, code",
    19: "Air Temperature, Minimum, once daily, Celsius",
    20: "Air Temperature, Maximum, once daily, Celsius",
    21: "Wind Speed, Max, once per hour, meters per second",
    22: "Air Temperature, Average, once per month, Celsius",
    23: "Precipitation Amount, Sum, once per month, millimeters",
    24: "Longwave Irradiance, Average per hour, every hour, watts per square meter",
    25: "Max of Mean Wind Speed, Maximum of 10-minute average, over 3 hours, once per hour, meters per second",
    26: "Air Temperature, Minimum, twice daily at 06:00 and 18:00, Celsius",
    27: "Air Temperature, Maximum, twice daily at 06:00 and 18:00, Celsius",
    28: "Cloud Base, Lowest cloud layer, instantaneous value, once per hour, meters",
    29: "Cloud Coverage, Lowest cloud layer, instantaneous value, once per hour, code",
    30: "Cloud Base, Second cloud layer, instantaneous value, once per hour, meters",
    31: "Cloud Coverage, Second cloud layer, instantaneous value, once per hour, code",
    32: "Cloud Base, Third cloud layer, instantaneous value, once per hour, meters",
    33: "Cloud Coverage, Third cloud layer, instantaneous value, once per hour, code",
    34: "Cloud Base, Fourth cloud layer, instantaneous value, once per hour, meters",
    35: "Cloud Coverage, Fourth cloud layer, instantaneous value, once per hour, code",
    36: "Cloud Base, Lowest cloud base, instantaneous value, once per hour, meters",
    37: "Cloud Base, Lowest cloud base, minimum over 15 minutes, once per hour, meters",
    38: "Precipitation Intensity, Max of 15-minute average, four times per hour, millimeters per second",
    39: "Dew Point Temperature, Instantaneous value, once per hour, Celsius",
    40: "Ground Condition, Instantaneous value, once daily at 06:00, code"
}
# good stations: 98210(Stockholm), 71420(Goteborg), 74380(Wind good, Visby, Gotland), 62400 (Sundsvall, center of Sweden)
# for dam in north and center of sweden: 147570 (Gannarn), 148330(Lycksele), 137100 (Sollefteå), 135520 (Strömsund), 157870 (Buresjön), 157790 (     D)

base_url = "https://opendata-download-metobs.smhi.se/api/version/latest/parameter/{}/station/155960/period/corrected-archive/data.csv"

for param_id in range(1, 41):
    url = base_url.format(param_id)
    response = requests.get(url)
    
    if response.status_code == 200:
        param_description = parameter_info.get(param_id, "Unknown parameter")
        print(f"Parameter {param_id} returned status 200. {param_description}")
    else:
        print(f"Parameter {param_id} returned status {response.status_code}.")


{
  "query": [
    {
      "code": "Tid",
      "selection": {
        "filter": "item",
        "values": [
            "2021M01",
            "2021M02",
            "2021M03",
            "2021M04",
            "2021M05",
            "2021M06",
            "2021M07",
            "2021M08",
            "2021M09",
            "2021M10",
            "2021M11",
            "2021M12",
	        "2022M01",
	        "2022M02",
	        "2022M03",
	        "2022M04",
	        "2022M05",
	        "2022M06",
	        "2022M07",
	        "2022M08",
	        "2022M09",
	        "2022M10",
	        "2022M11",
	        "2022M12",
	        "2023M01",
	        "2023M02",
	        "2023M03",
	        "2023M04",
	        "2023M05",
	        "2023M06",
	        "2023M07",
	        "2023M08",
	        "2023M09",
	        "2023M10",
	        "2023M11",
	        "2023M12",
	        "2024M01",
	        "2024M02",
	        "2024M03",
	        "2024M04",
	        "2024M05",
	        "2024M06",
	        "2024M07",
	        "2024M08",

        ]
      }
    }
  ],
  "response": {
    "format": "json"
  }
}