import pickle

class Gaylord(object):
    def __init__(self):
        self.Gay = gay()
        
    def print_gayness(self):
        print(str(self.Gay.gayness))
        
        
class gay(object):
    def __init__(self):
        self.gayness = 1000

ShanKai = Gaylord()
#ShanKai.Gay.gayness = 2000
#gaylist = open('gaylist.pickle', 'wb')
#pickle.dump(ShanKai,gaylist)
#gaylist.close()
        
#gaylist = open('gaylist.pickle', 'rb')
#ShanKai = pickle.load(gaylist)
#gaylist.close()

ShanKai.print_gayness
del ShanKai