import requests

API_KEY = "6f49f0116574e035a3e36f9dfffccd65"
CITY = "New York"

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=zh_cn"
response = requests.get(url)
data = response.json()

if data.get("cod") != 200:
    print("查询失败，请检查城市名称或API密钥。")
else:
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    print(f"{CITY} 当前天气：{weather}")
    print(f"温度：{temp}°C")
    print(f"湿度：{humidity}%")
    print(f"风速：{wind} m/s")
