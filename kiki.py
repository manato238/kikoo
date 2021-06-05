
from kivy.app import App
from kivy.uix.label import Label

from kivy.core.text import LabelBase,DEFAULT_FONT
from kivy.resources import resource_add_path

#mojiwohyouji
class TextApp(App):
    def build(self):
        return Label(text='Hello')

TextApp().run()
