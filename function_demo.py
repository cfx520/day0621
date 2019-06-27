#encoding:utf-8
def function1():
    print "hello"
def function2(name):
    print "hello,"+name
def describe_pet(animal_name,animal_type):
    print "I have a pet named"+animal_name
    print "the pet is " +animal_type
def getname(firstname,lastname):
    fullname=firstname+" "+lastname
    return fullname.title()
## 返回一个字典
def getdictionname(firstname,lastname,age=""):
    fullname={'firstname':firstname,'lastname':lastname}
    if age:
        fullname['age']=age
    return fullname
"""while True:
    firstname=raw_input('firstname')
    if firstname=='q':
        break
    lastname=raw_input('lastname')
    if lastname=='q':
        break
    print getdictionname(firstname,lastname)"""
def getlistuser(names):
    for i in names:
        print "hello,"+i
undesign=['iphone','huawei','sunxing','zhongxing']
design=[]
while undesign:
    pop=undesign.pop()
    design.append(pop)
for i in design:
    print i
def undesign(undesign,design):
    while undesign:
        pop=undesign.pop()
        design.append(pop)
    return design
def result(design):
    for i in design:
        print i
def make_pizza(*name):
    for i in name:
        print i
def demo_list(first,last,**usr_info):
    pro={}
    pro['first']=first
    pro['last']=last
    for key,value in usr_info.items():
        pro[key]=value
    return pro
if __name__ == '__main__':
    #names=['zs','ls','wangwu']
    #a=undesign(names,[])
    #result(a)
    #make_pizza(names,1,2,3)
    print demo_list('zs','li',age= 23, location =66)