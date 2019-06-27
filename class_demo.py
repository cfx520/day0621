class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(str(self.name)+"is sitting")
    def roll_over(self):
        print(str(self.name)+"is rolling")
class car(object):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def descritive(self):
        print 'the car'+self.make+self.model
class elctric_car(car):
    def __init__(self,make,model,year):
        super(elctric_car,self).__init__(make,model,year)
with open('1.csv','r') as f:
    lines=f.readlines()
pistring=''
for i in lines:
    pistring+=i.rstrip()
print pistring
if __name__=='__main__':
    pass
    #mysdog=dog(12,23)
    #print mysdog.name
    #mysdog.sit()
    #mytesla=elctric_car('tesla','models','2016')
    #mytesla.descritive()