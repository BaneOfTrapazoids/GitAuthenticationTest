from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.turn = "O"
        def callback(instance):
            if instance.text == "":
                instance.text = self.turn
                if self.turn == "O":
                    self.turn = "X"
                else:
                    self.turn = "O"
            button_list = self.buttons
            combinations = {
                "horizontal_1":[button_list[0], button_list[1], button_list[2]],
                "horizontal_2":[button_list[3], button_list[4], button_list[5]],
                "horizontal_3":[button_list[6], button_list[7], button_list[8]],
                "vertical_1":[button_list[0], button_list[3], button_list[6]],
                "vertical_2":[button_list[1], button_list[4], button_list[7]],
                "vertical_3":[button_list[2], button_list[5], button_list[8]],
                "diagonal_1":[button_list[0], button_list[4], button_list[8]],
                "diagonal_2":[button_list[2], button_list[4], button_list[6]],
            }

            for combination in combinations:
                current_buttons = combinations[combination]
                if current_buttons[0].text == "X" and current_buttons[1].text == "X" and current_buttons[2].text == "X":
                    print("X WINS")
                    button_list[4].font_size = 50
                    button_list[4].text = "X WINS"
                elif current_buttons[0].text == "O" and current_buttons[1].text == "O" and current_buttons[2].text == "O":
                    print("O WINS")
                    button_list[4].font_size = 50
                    button_list[4].text = "O WINS"
            if all([button_list[x].text for x in range(9)]):
                print("DRAW")
        self.rows = 3
        self.cols = 3
        self.buttons = [Button() for i in range(9)]
        for tile in self.buttons:
            tile.font_size = 100
            self.add_widget(tile)
            tile.bind(on_press=callback)

class TicTacToe(App):
    def build(self):
        return MainScreen()

TicTacToe().run()