#encoding=utf-8
#   1
#name=input("qing")
#print name

# 2
"""curent_number=7
while curent_number>0:
    print curent_number
    curent_number=curent_number-1"""

### 3
"""active=True
while active:
    message=raw_input('CC: ')
    #print message
    if message=='quit':
        active=False
    else:
        print message
"""
### 4
"""number=0
while number<10:
    number+=1
    if number%2==0:
        continue
    print number"""

#### 5
"""unconfidence_user=['Tom','bob','Jone','Jerry']
confidence_user=[]
while unconfidence_user:
    pop=unconfidence_user.pop()
    print pop.title()
    confidence_user.append(pop)
for i in confidence_user:
    print i"""

#### 6
"""pets=['dog','cat','fish','goldfish','cat','dog']
while 'cat' in pets:
    pets.remove('cat')
print pets"""

### 7
responses={}
polling_active=True
while polling_active:
    name=raw_input("请输入名字：")
    response=raw_input("which mountain would you like to climb someday?")
    responses[name]=response
    repeat=raw_input("would you like to let another person response? yes/no")
    if repeat=='no':
        polling_active=False
for name,response in responses.items():
    print name+" would like to climb "+response