import flet as ft
import random


def main(page: ft.Page):
    #List Quotes, colors 
    quotes = [
        {
            "content": "Without freedom of thought, there can be no such thing as wisdom - and no such thing as public liberty without freedom of speech.",
            "author": "Benjamin Franklin",
        },
        {
            "content": "We cannot do everything at once, but we can do something at once.",
            "author": "Calvin Coolidge",
        },
        {
            "content": "Your big opportunity may be right where you are now.",
            "author": "Napoleon Hill",
        },
        {
            "content": "There is more wisdom in your body than in your deepest philosophy.",
            "author": "Friedrich Nietzsche",
        },
        {
            "content": "If you smile when no one else is around, you really mean it.",
            "author": "Andy Rooney",
        },
        {
            "content": "Well done is better than well said.",
            "author": "Benjamin Franklin",
        },
        {
            "content": "Every artist dips his brush in his own soul, and paints his own nature into his pictures.",
            "author": "Henry Ward Beecher",
        },
        {
            "content": "A good head and a good heart are always a formidable combination.",
            "author": "Nelson Mandela",
        },
        {
            "content": "The supreme art of war is to subdue the enemy without fighting.",
            "author": "Sun Tzu",
        },
        {
            "content": "Friendship always benefits; love sometimes injures.",
            "author": "Seneca the Younger",
        },
        {
            "content": "Inspiration exists, but it has to find us working.",
            "author": "Pablo Picasso",
        },
        {
            "content": "If you are out to describe the truth, leave elegance to the tailor.",
            "author": "Albert Einstein",
        },
        {
            "content": "There is no friendship, no love, like that of the parent for the child.",
            "author": "Henry Ward Beecher",
        },
        {
            "content": "Every great dream begins with a dreamer. Always remember, you have within you the strength, the patience, and the passion to reach for the stars to change the world.",
            "author": "Harriet Tubman",
        },
        {
            "content": "If the shoe doesn't fit, must we change the foot?",
            "author": "Gloria Steinem",
        },
    ]
    colors = [
        "#FFD81B60",
        "#FFE53935",
        "#FFFB8C00",
        "#FFFFA000",
        "#FF7CB342",
        "#FF43A047",
        "#FF00897B",
        "#FF00ACC1",
        "#FF039BE5",
        "#FF1E88E5",
        "#FF3949AB",
        "#FF8E24AA",
    ]

    #Inicial values
    page.title = "Random Quote Machine"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor="#FFD81B60"
    txt_content = ft.Text(
        value="❝ There is no friendship, no love, like that of the parent for the child.",
        text_align=ft.TextAlign.RIGHT,
        width=600,
        size=25,
        color="#FFD81B60"
    )
    txt_author = ft.Text(
        value="- Henry Ward Beecher",
        text_align=ft.TextAlign.RIGHT,
        width=200,
        size=20,
        color="#FFD81B60"
    )
  
    #Function generate new Quote
    def new_quote(e):
        randomColor = random.randrange(0, len(colors))
        randomIndex = random.randrange(0, len(quotes))
        txt_content.value = "❝ " + str(quotes[randomIndex]["content"])
        txt_author.value = "- " + str(quotes[randomIndex]["author"])
        page.bgcolor=colors[randomColor]
        txt_content.color=colors[randomColor]
        txt_author.color=colors[randomColor]
        page.update()
    #Create Container
    container = ft.Container(
        bgcolor=ft.colors.WHITE,
        height=350,
        width=700,
        padding=30,
        border_radius=15,
        content=ft.Column(
            [
                txt_content,
                ft.Container(height=30),
                txt_author,
                ft.Container(height=10),
                ft.ElevatedButton(
                    "new Quote",
                    on_click=new_quote,
                    height=50,
                    style=ft.ButtonStyle(
                        color={
                            ft.MaterialState.HOVERED: ft.colors.AMBER,
                            ft.MaterialState.DEFAULT: ft.colors.WHITE,
                        },
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.END,
        ),
    )

    page.add(container)
    page.update()


ft.app(target=main,view="web_browser")
