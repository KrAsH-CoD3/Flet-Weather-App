import flet as ft
from flet import *
import requests #, datetime
from os import environ as env_variable

api_key: str = env_variable.get("OPENWEATHER_API_KEY")

_current = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=6.4453&lon=3.2634&appid={api_key}")

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
    def _current_temp():
        _current_temp = int(_current.json()['main']['temp'])
        return [_current_temp]

    def _top():

        _today = _current_temp()

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
                                "Satellite Town",
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
                                                )
                                            )
                                        ]
                                    )
                                ]
                            )
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

    page.add(_c)


if __name__ == "__main__":
    # print(_current.text)
    ft.app(target=main, assets_dir="assets")


# ft.app(target=main)