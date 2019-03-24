import datetime
import docx
import pickle

now = datetime.datetime.now()

class Root:
    def __init__(self):
        self._root = self
    
    def get_parent(self):
        return self
    
    def get_root(self):
        return self._root
    
    #Whenever an attribute is set and its a node, then define the parent and the root
    def __setattr__(self,name,value):
        if isinstance(value, Node):
            value.set_parent(self)
            value.set_root(self._root)
            value.set_name(name)
        self.__dict__[name] = value
    
    
class Node:
    
    def set_name(self, name):
        self._name = name
    
    def set_parent(self, parent):
        self._parent = parent
        
    def set_root(self, root):
        self._root = root
        
    def get_name(self):
        return self._name
    
    def get_parent(self):
        return self._parent
    
    def get_root(self):
        return self._root
    
    def save(self):
        print('saving ' + self.get_name())
        #save class as self.name.pickle
        file = open(self.get_name()+'.pickle','wb')
        pickle.dump(self,file)
        file.close()
    
    def load(self):
#        print('loading ' + self.get_name())
        try:
            file = open(self.get_name()+'.pickle','rb')
            self = pickle.load(file)
            file.close()
            print('loaded ' + self.get_name())
        except Exception as e:
            print(e)
        
    
    #Whenever an attribute is set and its a node, then define the parent and the root
    def __setattr__(self,name,value):
        if isinstance(value, Node) and '_parent' not in value.__dict__:
            value.set_parent(self)
            value.set_root(self._root)
            value.set_name(name)
        self.__dict__[name] = value

class PersonalDetails(Node):
    def __init__(self):
        
        self.FullName = 'Name'
        self.MobileNo = 'MobileNo'
        self.PersonalEmail = 'PersonalEmail'
        self.InternshipOrJob = 'InternshipOrJob'
        self.AvailableTimePeriod = 'AvailableTimePeriod'

class CurrentDate():
    def __init__(self):
        self.year = now.year
        self.month = now.month
        self.day = now.day

#Datas is used to define the containers for information, like additional_infos containing additional info, etc
class Datas(Node):
    def add(self, name, info):
        setattr(self,name,info)
        
    def remove(self, name):
        delattr(self, name)
    
    def get(self, name):
        return getattr(self,name)
    
    def replace(self, name, info):
        setattr(self,name,info)

class IndividualProject(Node):
    def __init__(self):
        self.OverarchingTheme = 'Overarching Theme'
        self.CompanyWorked = 'Place experience was attained eg. SUTD'
        self.Country = 'Country where experience was gained'
        self.JobScope = 'What did you do, eg. Student'
        self.TimePeriodWorked = 'Period Spent Working in the Job'
        self.ExperiencePoints = Datas()

class CoverLetter(Node):
    def __init__(self):
        self.SkillsPara1 = 'Relevant Skills Paragraph 1'
        self.SkillsPara2 = 'Relevant Skills Paragraph 2'
        self.WhyThisCompany = 'Even so, I wish to push the boundaries of technology, and use cutting edge technology to improve people’s lives. I acknowledge I do not have the resources myself to make this dream come true, but I am excited at the prospect of doing so with the highly qualified team at Entropica Labs.'
        self.ClosingParagraph = 'I believe that my self-driven attitude, my ability to work in a team, and my passion of hardware and software development will be beneficial to Entropica Labs, and I do hope you consider me for an internship position.'

class Resume(Node):
    def __init__(self):
        self.individual_projects = Datas()
        self.additional_information = Datas()

class CompanyApplication(Node):
    
    def __init__(self):
        self.cover_letter = CoverLetter()
        self.resume = Resume()
        
class MasterClass(Root):
    
    def __init__(self, **kwargs):
        Root.__init__(self)
        self.personal_details = PersonalDetails()
        self.current_date = CurrentDate()
        self.company_applications = Datas()
        self.additional_infos = Datas()
        self.skills_paragraphs = Datas()
        self.individual_projects = Datas()
        self.load_all()
        pass
    
    def save_all(self):
        for (key,value) in self.__dict__.items():
            if isinstance(value,Node):
                value.save()
    
    def load_all(self):
        for (key,value) in self.__dict__.items():
            if isinstance(value,Node):
                value.load()        

#Test Code
#philip = MasterClass()
#philip.save_all()


    

