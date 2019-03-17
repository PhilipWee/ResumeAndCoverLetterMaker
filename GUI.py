import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from classdefinitions import *
from kivy.properties import StringProperty
from kivy.lang.builder import Builder

def save(class_obj):
    print('saving ' + class_obj.name)
    #save class as self.name.pickle
    file = open(class_obj.name+'.pickle','wb')
    pickle.dump(class_obj,file)
    file.close()           
    
def load(file_name_without_extension):
    
    #try load self.name.txt
    file = open(file_name_without_extension+'.pickle','rb')      
    class_obj = pickle.load(file)
    file.close()     
    print('loaded ' + class_obj.name)
    return class_obj

class PersonalDetails(Widget):
    name = ObjectProperty(None)
    mobileNo = ObjectProperty(None)
    personalEmail = ObjectProperty(None)
    internshipOrJob = ObjectProperty(None)
    availableTimePeriod = ObjectProperty(None)
    
    def __init__(self):
        super().__init__()
        try:
            UpdatedDetails = load('UpdatedDetails')
            self.name.text = UpdatedDetails.FullName
            self.mobileNo.text = UpdatedDetails.MobileNo
            self.personalEmail.text = UpdatedDetails.PersonalEmail
            self.internshipOrJob.text = UpdatedDetails.InternshipOrJob
            self.availableTimePeriod.text = UpdatedDetails.AvailableTimePeiod
            print('Loaded Updated Details Successfully')
        except:
            print('Failed to load Updated Details, using defaults')

            
        

    def toggleJob(self):
        if self.internshipOrJob.text == 'Internship':
            self.internshipOrJob.text = 'Job'
        else:
            self.internshipOrJob.text = 'Internship'
    
    def savePersonalDetails(self):
        UpdatedDetails = Personal_Details()
        UpdatedDetails.FullName = self.name.text
        UpdatedDetails.MobileNo = self.mobileNo.text
        UpdatedDetails.PersonalEmail = self.personalEmail.text
        UpdatedDetails.InternshipOrJob = self.internshipOrJob.text
        UpdatedDetails.AvailableTimePeiod = self.availableTimePeriod.text
        save(UpdatedDetails)

project1 = Individual_Project()
project2 = Individual_Project()
project3 = Individual_Project()

list_of_projects = [project1,project2]

class IndividualProject(Widget):
    Builder.load_string('''
<IndividualProject>:
    overarchingTheme:overarchingTheme
    companyWorked:companyWorked
    country:country
    jobScope:jobScope
    timePeriodWorked:timePeriodWorked
    experiencePoints:experiencePoints
    
    GridLayout:
        size:root.width,root.height
        spacing:100
        cols:1
        
        Label:
            id:overarchingTheme
            text:'Overarching Theme'
            spacing:10
        
        GridLayout:
            cols:2
            spacing:10
            
            Label:
                id:companyWorked
                text:'Company Worked'
            
            Label:
                id:country
                text:'Country'
            
            Label:
                id:jobScope
                text:'Job Scope'
            
            Label:
                id:timePeriodWorked
                text: 'Time Period Worked'
        
        Label:
            id:experiencePoints
            text: 'Experience Points'
            spacing:10
                        ''')
    pass

class IndividualProjects(Widget):
    def __init__(self):
        super(IndividualProjects,self).__init__()
        for project in list_of_projects:
            CurrentProject = IndividualProject()
            
            CurrentProject.bind(minimum_height=CurrentProject.setter('height'))
            
            CurrentProject.overarchingTheme.text = project.OverarchingTheme
            CurrentProject.companyWorked.text = project.CompanyWorked
            CurrentProject.country.text = project.Country
            CurrentProject.jobScope.text = project.JobScope
            CurrentProject.timePeriodWorked.text = project.TimePeriodWorked
            CurrentProject.experiencePoints.text = '\n'.join(project.ExperiencePoints)
            
            self.gridLayout.scrollView.gridLayoutInner.add_widget(CurrentProject)
    


class MyGUIApp(App):
    def build(self):
        return IndividualProjects()
    
if __name__ == '__main__':
#    Shan = Master_Class()
#    Shan.add_company('gay')
#    Education = Overarching_Theme()
#    Shan.overarching_theme.append(Education)
#    for x in Shan.overarching_theme:
#        if x.OverarchingTheme == 'Education':
#            SUTD = Individual_Project()
#            x.IndividualProjects.append(SUTD)
    MyGUIApp().run()
    