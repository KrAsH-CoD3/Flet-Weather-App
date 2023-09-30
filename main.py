import flet as ft
from flet import *
import requests, datetime
from os import environ as env_variable

api_key: str = env_variable.get("OPENWEATHER_API_KEY")

# _weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=6.4453&lon=3.2634&appid={api_key}")
_weather_response: dict = {
  "coord": {
    "lon": 3.2634,
    "lat": 6.4453
  },
  "weather": [
    {
      "id": 804,
      "main": "Clouds",
      "description": "overcast clouds",
      "icon": "04d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 301.01,
    "feels_like": 303.8,
    "temp_min": 301.01,
    "temp_max": 301.01,
    "pressure": 1011,
    "humidity": 72,
    "sea_level": 1011,
    "grnd_level": 1010
  },
  "visibility": 10000,
  "wind": {
    "speed": 2.83,
    "deg": 228,
    "gust": 3.02
  },
  "clouds": {
    "all": 100
  },
  "dt": 1696008270,
  "sys": {
    "country": "NG",
    "sunrise": 1695965703,
    "sunset": 1696009180
  },
  "timezone": 3600,
  "id": 2332459,
  "name": "Lagos",
  "cod": 200
}

days: list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun",] 


def main(page: Page):
    page.horizontal_alignmen = "center"
    page.vertical_alignment = "center"

    # animation
    def _expand(e):
        if e.data == "true":
            _c.content.controls[0].height = 560
            _c.content.controls[0].update()
        else:
            _c.content.controls[0].height = 660 * 0.40
            _c.content.controls[0].update()

    # current temp
    def _temp():
        # _temp: int = int(_weather_response.json()['main']['temp'])
        # _weather: str = _weather_response.json()['weather'][0]['main']
        # _description: str = _weather_response.json()['weather'][0]['description']
        # _wind: int = int(_weather_response.json()['wind']['speed'])
        # _humidity: int = int(_weather_response.json()['main']['humidity'])
        # _feels: int = int(_weather_response.json()['main']['feels_like'])

        _temp: int = int(_weather_response['main']['temp'])
        _weather: str = _weather_response['weather'][0]['main']
        _description: str = _weather_response['weather'][0]['description']
        _wind: int = int(_weather_response['wind']['speed'])
        _humidity: int = int(_weather_response['main']['humidity'])
        _feels: int = int(_weather_response['main']['feels_like'])

        return [_temp, _weather, _description, _wind, _humidity, _feels]

    def _extra():
        _extra_info: list = []

        _extra: list = [
            [
                int(_weather_response["visibility"] / 1000),
                "Km",
                "Visibility",
                "./assests/visibility.png",
            ],
            [
                round(_weather_response["main"]["pressure"] * 0.03, 2),
                "inHg",
                "Pressure",
                "./assests/barometer.png",
            ],
            [
                datetime.datetime.fromtimestamp(
                    _weather_response["sys"]["sunset"]
                ).strftime("%I:%M %p"),
                "",
                "Sunset",
                "./assests/sunset.png",
            ],
            [
                datetime.datetime.fromtimestamp(
                    _weather_response["sys"]["sunset"]
                ).strftime("%I:%M %p"),
                "",
                "Sunrise",
                "./assests/sunrise.png",
            ],
        ]

        for data in _extra:
            _extra_info.append(
                Container(
                    bgcolor="white10",
                    border_radius=12,
                    alignment=alignment.center,
                    content=Column(
                        alignment="center",
                        horizontal_alignment="center",
                        spacing=25,
                        controls=[
                            Container(
                                alignment=alignment.center,
                                content=Image(
                                    src=data[3],
                                    color="white"
                                ),
                                width=32,
                                height=32,
                            ),
                            Container(
                                content=Column(
                                    alignment="center",
                                    horizontal_alignment="center",
                                    spacing=0,
                                    controls=[
                                        Text(str(data[0]) + " " + data[1],
                                        size=14,
                                        ),
                                        Text(
                                            str(data[2]),
                                            size=11,
                                            color="white54",
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ),
            ),
        
        return _extra_info

    def _top():

        _today = _temp()

        _today_extra = GridView(
            max_extent=150,
            expand=1,
            run_spacing=5,
            spacing=5,
        )

        for info in _extra():
            _today_extra.controls.append(info)

        top = Container(
            width=310, 
            height=660 * 0.40, 
            gradient=LinearGradient(
                begin=alignment.bottom_left, 
                end=alignment.top_right, 
                colors=["lightblue600", "lightblue900"],
            ),
            border_radius=35,
            animate=animation.Animation(
                duration=350,
                curve="decelerate",
            ),
            on_hover=lambda e: _expand(e),
            padding=15,
            content=Column(
                alignment="start",
                spacing=10,
                controls=[
                    Row(
                        alignment="center",
                        controls=[
                            Text(
                                "Satellite Town, Lagos",
                                size=16,
                                weight="500"
                            ),
                        ],
                    ),
                    Container(padding=padding.only(bottom=5)),
                    Row(
                        alignment="center",
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        width=90,
                                        height=90,
                                        image_src=
                                        "assests/rain cloud.webp",
                                    ),
                                ],
                            ),
                            Column(
                                spacing=5,
                                horizontal_alignment="center",
                                controls=[
                                    Text(
                                        "Today",
                                        size=12,
                                        text_align="center",
                                    ),
                                    Row(
                                        vertical_alignment="start",
                                        spacing=0,
                                        controls=[
                                            Container(
                                                content=Text(
                                                    _today[0],
                                                    size=52,
                                                ),
                                            ),
                                            Container(
                                                content=Text(
                                                    "°",
                                                    size=28,
                                                    text_align="center",
                                                ),
                                            ),
                                        ],
                                    ),
                                    Text(
                                        _today[1] + " - Overcast",
                                        size=10,
                                        color="white54",
                                        text_align="center",
                                    ),
                                ],
                            ),
                        ],
                    ),
                    Divider(height=8, thickness=1, color="white10"),
                    Row(
                        alignment="spaceAround",
                        controls=[
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(
                                                src="./assests/wind.png",
                                                color="white",
                                            ),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(
                                            str(_today[3]) + " km/h",
                                            size=11,
                                        ),
                                        Text(
                                            'Wind',
                                            size=9,
                                            color="white54",
                                        ),
                                    ],
                                ),
                            ),
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(
                                                src="./assests/humidity.png",
                                                color="white",
                                            ),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(
                                            str(_today[4]) + "%",
                                            size=11,
                                        ),
                                        Text(
                                            'Humidity',
                                            size=9,
                                            color="white54",
                                        ),
                                    ],
                                ),
                            ),
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(
                                                src="./assests/thermometer.png",
                                                color="white",
                                            ),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(
                                            str(_today[5]) + "°",
                                            size=11,
                                        ),
                                        Text(
                                            'Feels Like',
                                            size=9,
                                            color="white54",
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )

        return top


    _c = Container(
        width=310, 
        height=660, 
        border_radius=35, 
        bgcolor="black", 
        padding=10, 
        content=Stack(
            width=300, 
            height=550, 
            controls=[_top(),],),)

    page.title= "Flet Weather App"
    page.window_height=700
    page.window_width=350
    page.add(_c)
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
