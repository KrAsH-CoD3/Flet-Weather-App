import flet as ft
from flet import *
import requests, datetime
from os import environ as env_variable

api_key: str = env_variable.get("OPENWEATHER_API_KEY")

_weather_response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat=6.4453&lon=3.2634&appid={api_key}"
)

_forcast_response = requests.get(
    f"https://api.openweathermap.org/data/2.5/forecast?lat=6.4453&lon=3.2634&appid={api_key}"
)

days: list = [
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
    "Sun",
]


def main(page: Page):
    page.horizontal_alignmen = "center"
    page.vertical_alignment = "center"

    # animation
    def _expand(e):
        if e.data == "true":
            _c.content.controls[1].height = 560
            _c.content.controls[1].update()
        else:
            _c.content.controls[1].height = 660 * 0.40
            _c.content.controls[1].update()

    # current temp
    def _temp():
        _temp: int = int(_forcast_response.json()["list"][0]["main"]["temp"])
        _weather: str = _forcast_response.json()["list"][0]["weather"][0][
            "main"
        ].lower()
        _description: str = _forcast_response.json()["list"][0]["weather"][0][
            "description"
        ].lower()
        _wind: int = int(_forcast_response.json()["list"][0]["wind"]["speed"])
        _humidity: int = int(_forcast_response.json()["list"][0]["main"]["humidity"])
        _feels: int = int(_forcast_response.json()["list"][0]["main"]["feels_like"])
        _todays_img_name: str = _forcast_response.json()["list"][0]["weather"][0][
            "description"
        ].lower()

        return [
            _temp,
            _weather,
            _description,
            _wind,
            _humidity,
            _feels,
            _todays_img_name,
        ]

    _today = _temp()

    def _extra():
        _extra_info: list = []

        _extra: list = [
            [
                int(_forcast_response.json()["list"][0]["visibility"] / 1000),
                "Km",
                "Visibility",
                "./assests/icons/visibility.png",
            ],
            [
                round(
                    _forcast_response.json()["list"][0]["main"]["pressure"] * 0.03, 2
                ),
                "inHg",
                "Pressure",
                "./assests/icons/barometer.png",
            ],
            [
                datetime.datetime.fromtimestamp(
                    _weather_response.json()["sys"]["sunrise"]
                ).strftime("%I:%M %p"),
                "",
                "Sunrise",
                "./assests/icons/sunrise.png",
            ],
            [
                datetime.datetime.fromtimestamp(
                    _weather_response.json()["sys"]["sunset"]
                ).strftime("%I:%M %p"),
                "",
                "Sunset",
                "./assests/icons/sunset.png",
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
                                content=Image(src=data[3], color="white"),
                                width=32,
                                height=32,
                            ),
                            Container(
                                content=Column(
                                    alignment="center",
                                    horizontal_alignment="center",
                                    spacing=0,
                                    controls=[
                                        Text(
                                            str(data[0]) + " " + data[1],
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
                            Text("Satellite Town, Lagos", size=16, weight="500"),
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
                                        image_src=f"./assests/clouds/{_today[6]}.png",
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
                                        "Overview - " + _today[6],
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
                                                src="./assests/icons/wind.png",
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
                                            "Wind",
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
                                                src="./assests/icons/humidity.png",
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
                                            "Humidity",
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
                                                src="./assests/icons/thermometer.png",
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
                                            "Feels Like",
                                            size=9,
                                            color="white54",
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    _today_extra,
                ],
            ),
        )

        return top

    def _bot_data():
        _bot_data: list = []

        for index in range(
            0, 33, 8
        ):  # Forcast are for only 5 days (5 * 8(hours in 24hrs))
            _bot_data.append(
                Row(
                    spacing=5,
                    alignment="spaceBetween",
                    controls=[
                        Row(
                            expand=1,
                            alignment="start",
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Text(
                                        days[
                                            datetime.datetime.weekday(
                                                datetime.datetime.fromtimestamp(
                                                    _forcast_response.json()["list"][
                                                        index
                                                    ]["dt"]
                                                )
                                            )
                                        ],
                                    ),
                                ),
                            ],
                        ),
                        Row(
                            expand=1,
                            controls=[
                                Container(
                                    content=Row(
                                        alignment="start",
                                        controls=[
                                            Container(
                                                width=20,
                                                height=20,
                                                alignment=alignment.center_left,
                                                content=Image(
                                                    src=f"/assests/clouds/{_today[6]}.png"
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
            ),
        return _bot_data

    def _bottom():
        _bot_column = Column(
            alignment="center",
            horizontal_alignment="center",
            spacing=25,
        )

        for data in _bot_data():
            _bot_column.controls.append(data)

        bottom = Container(
            padding=padding.only(top=280, right=20, bottom=20, left=20),
            content=_bot_column,
        )

        return bottom

    _c = Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor="black",
        padding=10,
        content=Stack(
            width=300,
            height=550,
            controls=[
                _bottom(),
                _top(),
            ],
        ),
    )

    page.title = "Weather App"
    page.window_height = 700
    page.window_width = 350
    page.add(_c)
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
