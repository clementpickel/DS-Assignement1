import requests

# Dictionary mapping parameter IDs to names and descriptions
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

# Base URL pattern
base_url = "https://opendata-download-metobs.smhi.se/api/version/latest/parameter/{}/station/71415/period/corrected-archive/data.csv"

# Loop through parameter IDs from 1 to 40
for param_id in range(1, 41):
    url = base_url.format(param_id)
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        param_description = parameter_info.get(param_id, "Unknown parameter")
        print(f"Parameter {param_id} returned status 200. {param_description}")
    else:
        print(f"Parameter {param_id} returned status {response.status_code}.")
