from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

# basic plan is to have a scale generator that looks something like this --

# scale generator title banner
# input Key (TextInput) and also a scale type select dropdown
# submit button
# extra text grid on the top after button is pressed
class MyGridLayout(GridLayout):
  def __init__(self, **kwargs):
    # call grid layout in the constructor
    super(MyGridLayout, self).__init__(**kwargs)

    self.cols = 1
    # input box
    self.key = TextInput(multiline=False)
    self.header = Label(text="Let's generate any scale!")
    self.add_widget(self.header)
    self.add_widget(self.key)

    # submit button and bind button
    self.submit = Button(text="Generate Key!")
    self.submit.bind(on_press=self.press)
    self.add_widget(self.submit)
  
  def press(self,instance):
    key = self.key.text

class ScaleGenerator(App):
  def build(self):
    return MyGridLayout()

if __name__ == '__main__':
  ScaleGenerator().run()