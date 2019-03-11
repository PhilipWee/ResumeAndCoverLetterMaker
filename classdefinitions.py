import datetime

now = datetime.datetime.now()

class Personal_Details(object):
    def __init__(self):
        self.Name = 'Name'
        self.MobileNo = 'MobileNo'
        self.PersonalEmail = 'PersonalEmail'
        self.InternshipOrJob = 'InternshipOrJob'
        self.AvailableTimePeriod = 'AvailableTimePeriod'

class Current_Date(object):
    def __init__(self):
        self.year = now.year
        self.month = now.month
        self.day = now.day

class Cover_Letter(object):
    def __init__(self):
        self.SkillsPara1 = 'Relevant Skills Paragraph 1'
        self.SkillsPara2 = 'Relevant Skills Paragraph 2'
        self.WhyThisCompany = 'Even so, I wish to push the boundaries of technology, and use cutting edge technology to improve people’s lives. I acknowledge I do not have the resources myself to make this dream come true, but I am excited at the prospect of doing so with the highly qualified team at Entropica Labs.'
        self.ClosingParagraph = 'I believe that my self-driven attitude, my ability to work in a team, and my passion of hardware and software development will be beneficial to Entropica Labs, and I do hope you consider me for an internship position.'

class Additional_Information(object):
    pass

class Overarching_Theme(object):
    def __init__(self):
        self.OverarchingTheme = 'Overarching Theme eg. Education'
        self.CompanyWorked = 'Place experience was attained eg. SUTD'
        self.Country = 'Country where experience was gained'
        self.Jobscope = 'What did you do, eg. Student'
        self.TimePeriodWorked = 'Period Spent Working in the Job'
        self.ExperiencePoints = ['Got 3.1 GPA','something else','something else', 'something else', 'something else']

    
class Resume(object):
    def __init__(self):
        self.overarching_theme = [Overarching_Theme()]
        self.additional_information = ['point1','point2','point3','point4','point5']



class Company_Application(object):
    def __init__(self, CompanyName):
        self.CompanyName = CompanyName
        self.cover_letter = Cover_Letter()
        self.resume = Resume()


#The Class File to end all classes
class Master_Class(object):
    def __init__(self):
        self.personal_details = Personal_Details()
        self.current_date = Current_Date()
        self.company_applications = {}
        #Additional info, skills para, overarchging themes and individual projects need to be implemented
        self.additional_information = []
        self.skills_paragraphs = []
        self.overarching
        
    def add_company(self,CompanyName):
        if CompanyName not in self.company_applications:
            Name = CompanyName
            Company = Company_Application(CompanyName)
            self.company_applications[Name] = Company

        
philip = Master_Class()
Shan = Master_Class()


Shan.add_company('gay')
print(Shan.company_applications['gay'].resume.overarching_theme[0].Country)
