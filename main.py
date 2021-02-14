from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from CircularLinkedList import CircularLinkedList as CLL
chromatic_scale = CLL(("C",
                       "C#/Db",
                       "D",
                       "D#/Eb",
                       "E",
                       "F",
                       "F#/Gb",
                       "G",
                       "G#/Ab",
                       "A",
                       "A#/Bb",
                       "B"))
class GeneratorGrid(Widget):
  
  def __init__(self,**kwargs):
    super(GeneratorGrid,self).__init__(**kwargs)
    self.generated = ""
    self.key = ""
    self.scale = ""

  def key_typed(self, value):
    valid_keys = set(["A", "B", "C", "D", "E", "F", "G", "A#", "B#", "C#", "D#", "E#", "F#", "G#", "Ab", "Bb", "Cb", "Db", "Eb", "Fb", "Gb"])

    if value.title() in valid_keys:
      self.key = value
      self.ids.user_input.text = value.title()
    else:
      self.ids.user_input.text = 'Please type a valid key to start scale!'
    

  def scale_clicked(self, value):
    error_message = set(["We cannot proceed until you type a valid key -_-;;", 'Please type a valid key to start scale!', "WHAT IS WRONG WITH YOU!? \nDO YOU NO SPEAK ENGLISH??"])
    scales = set(["Major", "Minor", "Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian", "Pentatonic", "Fourths", "Fifths", "Relative Minor"])
    prior = self.ids.user_input.text
    res = ''
    
    if prior in error_message:
      res = "We cannot proceed until you type a valid key -_-;;"
    elif ' ' in prior:
      key, scale = prior.split()
      self.scale = value
      scale = value
      res = key + " " + scale
    elif prior in scales:
      self.ids.user_input.text = "" 
      self.scale = value
      res = value
    else:
      self.ids.user_input.text = "" 
      self.scale = value
      res = prior + " " + value
    

    self.ids.user_input.text = res.title()
  
  def generate(self):
    if self.key == "" or self.scale == "":
      self.ids.header.text = "INVALID ENTRY! TRY AGAIN BOOHOO"
    # this must equal the output of ScaleGenerator.py
    else:
      self.generated = chromatic_scale.generate_scale(self.key.title(), self.scale.lower())
      self.ids.header.text = self.generated

class GeneratorApp(App):
  def build(self):
    return GeneratorGrid()

if __name__ == '__main__':
  GeneratorApp().run()