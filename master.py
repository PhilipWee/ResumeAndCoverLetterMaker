import docx
Name = 'Philip Andrew Wee De Wang'
MobileNo = '84381245'
PersonalEmail = 'philip_andrew@mymail.sutd.edu.sg'
CompanyWorked = 'Singapore University of Technology and Education'
JobScope = 'Student'
Country = 'Singapore'
TimePeriodWorked = 'Jan 16 to Mar 16'
OverarchingTheme = 'EDUCATION'
ExperiencePoints = ['well thats pretty gay','\n really','\n gay']


def getText(filename):
    doc = filename
    fullText = []
    for para in doc.paragraphs:
        para = para.text
    return '\n'.join(fullText)

Resume = docx.Document('Resume Template.docx')
#for para in Resume.paragraphs:
#    for run in para.runs:
#        print(run.text)
#        run.text = run.text.format(Name = Name, 
#                                   MobileNo = MobileNo, 
#                                   PersonalEmail = PersonalEmail, 
#                                   LinkedIn = '',
#                                   OverarchingTheme = OverarchingTheme,
#                                   JobScope = JobScope,
#                                   Country = Country,
#                                   TimePeriodWorked = TimePeriodWorked,
#                                   CompanyWorked = CompanyWorked,
#                                   ExperiencePoint = ExperiencePoint)
        
def OverarchingThemeMaker(OverarchingTheme,
                          CompanyWorked,
                          Country,
                          JobScope,
                          TimePeriodWorked,
                          ExperiencePoints):
    Output = docx.Document('Overarching Theme Template.docx')
    for para in Output.paragraphs:
        for run in para.runs:
            #print(run.text)
            run.text = run.text.format(OverarchingTheme = OverarchingTheme,
                                       JobScope = JobScope,
                                       Country = Country,
                                       TimePeriodWorked = TimePeriodWorked,
                                       CompanyWorked = CompanyWorked,
                                       ExperiencePoint = ExperiencePoints[0])
    for i in range(1, len(ExperiencePoints)):
        Output.paragraphs[-1].add_run(ExperiencePoints[i])
    return Output
    
print(getText(OverarchingThemeMaker(OverarchingTheme,
                                  CompanyWorked,
                                  Country,
                                  JobScope,
                                  TimePeriodWorked,
                                  ExperiencePoints)))
OverarchingThemeMaker(OverarchingTheme,
                                  CompanyWorked,
                                  Country,
                                  JobScope,
                                  TimePeriodWorked,
                                  ExperiencePoints).save('Resume Output.docx')


