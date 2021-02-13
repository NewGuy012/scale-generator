from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
# Builder.load_file('generator.kv')
# basic plan is to have a scale generator that looks something like this --

# scale generator title banner
# input Key (TextInput) and also a scale type select dropdown
# submit button
# extra text grid on the top after button is pressed
class GeneratorGrid(Widget):
    # def __init__(self):
    #     self.key = ""
    #     self.scale = ""

    def key_typed(self, value):
        self.key = value

    def scale_clicked(self, value):
        self.scale = value

class GeneratorApp(App):
    def build(self):
        return GeneratorGrid()

if __name__ == '__main__':
    GeneratorApp().run()