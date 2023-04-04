from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
from kivymd.app import MDApp
from kivy.loader import Loader
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.button import MDRaisedButton
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivymd.uix.boxlayout import MDBoxLayout


Window.size = (500, 500)

    
class WelcomeWindow(Screen):
    def logger(self):
        self.ids.welcome_label.text = f"Welcome {self.ids.user.text}!"


    def clear(self):
        self.ids.welcome_label.text = ""
        self.ids.user.text = ""
        self.ids.password.text = ""
        pass


class RegistrationWindow(Screen):
    def clear(self):
        self.ids.first_name.text = ""   
        self.ids.last_name.text = ""
        pass


class ProfileWindow(Screen):
    pass


class AppointmentWindow(Screen):
    def show_keyboard(self, instance, value):
        if value:
            self.ids.keyboard.target = instance
            self.ids.keyboard.layout = 'qwerty'
    

class ProviderOneWindow(Screen):
    pass
    

class ProviderTwoWindow(Screen):
    pass
    

class ProviderThreeWindow(Screen):
    pass
    

class ProviderFourWindow(Screen):
    pass
    

class ProviderFiveWindow(Screen):
    pass
    

class B4B(MDApp):
    def build(self):    
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.accent_palette = "Red"
        self.theme_cls.primary_hue = "100"
        self.theme_cls.accent_hue = "900"
        return Builder.load_file("display.kv")


if __name__ == "__main__":
    B4B().run()