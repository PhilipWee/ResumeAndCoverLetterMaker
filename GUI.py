import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
#from classdefinitions import *

class PersonalDetails(Widget):
    name = ObjectProperty(None)
    mobileNo = ObjectProperty(None)
    personalEmail = ObjectProperty(None)
    internshipOrJob = ObjectProperty(None)
    availableTimePeriod = ObjectProperty(None)

    def toggleJob(self):
        if self.internshipOrJob.text == 'Internship':
            self.internshipOrJob.text = 'Job'
        else:
            self.internshipOrJob.text = 'Internship'
    
    def savePersonalDetails(self):
        #Needs to be implemented
        print('The name is {} and the email is {}'.format(self.name.text,self.personalEmail.text))

class MyGUIApp(App):
    def build(self):
        return PersonalDetails()
    
if __name__ == '__main__':
    MyGUIApp().run()