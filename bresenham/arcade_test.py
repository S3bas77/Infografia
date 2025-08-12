import arcade, bresenham

WIDTH = 1280
HEIGHT = 720
TITLE = "hola arcade"

class HelloView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.YELLOW


    def draw_vertical_line(self, x0, y0, x1, y1, color):
        assert x0 == x1
        for y in range(y0, y1 + 1):
            arcade.draw_point(x0, y, color, size=1)

    def on_draw(self):
        self.clear()
        arcade.draw_point(WIDTH // 2, HEIGHT // 2, arcade.color.BLUE,10)
        points = bresenham.get_line(600, 200, 100, 0)

        for x, y in points:
            arcade.draw_point(x, y, arcade.color.RED, 2)


def main():
    window = arcade.Window(WIDTH, HEIGHT, TITLE)
    game = HelloView()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()