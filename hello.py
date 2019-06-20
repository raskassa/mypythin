

import datetime
import json

a=5
b=7
lstobj = [1,"hello","&", 3,"12abc",4,"#"]
rvsList = []
def myLoop() :
    i=0
    while i < 3 :
        print(i)
        i += 1

def multiples1() :
    sumof3and5 = 0
    for i in range (1,100) :
        if (i % 3 == 0) or (i % 5 == 0):
            sumof3and5 += i
            print(sumof3and5)
    return sumof3and5


def kassa1(intin) :
    yy = str(intin)
    if yy.isnumeric(): 
        intout = 5 * intin
    return intout

def mile_to_km(inmile) :
    kmout = inmile * 1.6
    return kmout

def array_manip(obj) : 
    #temp = obj[0]
    #obj[0], obj[1] = obj[1], temp
    iLstlen = len(obj) - 1
    iCounter = 0
    rvsList.clear()
    mystrStr = str()
    #reversing a string using a regular for loop
    for element in obj:
        print(element)
    
    for i in obj:
        rvsList.append(obj[iLstlen- iCounter])
        print(rvsList[iCounter])
        iCounter += 1
    
    #another way   
    rvsList.clear()
    for i in range(len(obj)):
        mystrStr = str(obj[iLstlen-i])
        mystrStr.r
        #remove non alphabet and non numbers
        if mystrStr.isalpha() or mystrStr.isnumeric():
            #if not mystrStr.isalnum()
            rvsList.append(obj[iLstlen-i])
    
    #using a while loop
    rvsList.clear()
    inum = iLstlen
    iindex = 0
    while inum >= 0 and inum <= iLstlen:
        rvsList.append(obj[inum])
        print (rvsList[iindex])
        inum += -1
        iindex += 1
    return rvsList
   
timenow = datetime.datetime.now()
print(timenow.strftime("%H") + ":" + timenow.strftime("%M")) 
#print(timenow)
#strInput = input("Please enter your first name : ")

#if a > b:
#    print("a is not greater than b")
#elif a == b:
#    print("a is the same as b")
#else:
#    print("a is less than b")

#print (kassa1(5))
#print(mile_to_km(20))
print(array_manip(lstobj))
#txtOrg = "Hello World" 
#txtRvs = txtOrg [::-1]
#print(txtRvs)
#
#myLoop()

#python code data to JSON
myjsondata = '{ "name":"John", "age":30, "city":"New York"}'
f = open("myjsonfile.json", "w")
f.write(myjsondata)
f.close()

# read JSON to python code:
y = open("myjsonfile.json", "r")
ytxt= y.read()
ztxt = json.loads(ytxt)
# the result is a Python dictionary:
print(ztxt) 
print(ztxt["age"]) 

# a Python object (dict):
#x = {
#  "name": "John",
#  "age": 30,
#  "city": "New York"
#}

# convert into JSON:
#y = json.dumps(x)