from classdefinitionsv3 import *
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.properties import StringProperty

main = MasterClass()

class ScreenManagement(ScreenManager):
    pass

class HomeScreen(Screen):
    pass

class PersonalDetails(Screen):
    pass
#    fullName = StringProperty('')
#    
#    def __init__(self,**kw):
#        super().__init__(**kw)
#        fullName = main.personal_details.FullName
        

class CustomDropDown(DropDown):
    pass

class GUIApp(App):
    
    def build(self):
        return ScreenManagement()

if __name__ == "__main__":
    app = GUIApp()
    app.run()
