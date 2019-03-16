import pickle

class Gaylord(object):
    def __init__(self):
        self.Gay = gay()
        self.load()
        
    def load(self):
        gaylist = open('gaylist.pickle', 'rb')
        self = pickle.load(gaylist)
        gaylist.close()
        
    def save(self):
        ShanKai = Gaylord()
        ShanKai.Gay.gayness = 2000
        gaylist = open('gaylist.pickle', 'wb')
        pickle.dump(ShanKai,gaylist)
        gaylist.close()
        
        
        
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

print(ShanKai.Gay.gayness)
del ShanKai