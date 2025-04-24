text
# Weather Checker

A simple and lightweight command-line tool to check real-time weather for any city worldwide using the OpenWeatherMap API.

## Features

- Query current weather for any city
- Display temperature, humidity, wind speed, and weather description
- Easy to use and minimal dependencies

## Installation

1. **Clone the repository**
git clone https://github.com/Xw1314520/weather-checker.git
cd weather-checker

text

2. **Install dependencies**
pip install requests

text

3. **Get your OpenWeatherMap API Key**  
Register for a free API key at [OpenWeatherMap](https://openweathermap.org/api).

4. **Configure your API key**  
Open `weather.py` and set your API key:
API_KEY = "your_api_key_here"

text

## Usage

Run the script in your terminal:
python weather.py

text
Enter the city name when prompted, and the current weather details will be displayed.

## Example Output

Enter city name: London
Temperature: 20.1°C
Humidity: 56%
Wind Speed: 2.57 m/s
Description: Broken clouds

text

## License

MIT License
