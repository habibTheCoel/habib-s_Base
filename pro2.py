import datetime
o = open("Texts/9.txt" , "r",encoding="utf8")

ass  =  o.read()




 


def fun(a) : 
    l = ["." , "," , "'" , "!" , "?" , "/", "\n"]
    last = 0 
    li = []

    c = 0
    for i in a :
        c +=1
        if i in l :
            if a[c-2] != " " :
                li.append(a[last:c-1])
            
            li.append(i)
        elif i == " " :
            if a[c-2] != " " and  a[c-2] not in l :
                li.append(a[last:c-1])
            if a[c] != " "  :
                last = c
                
   
    return li

li = fun(ass)
print(len(ass))
print(len(li))


la = []


def kik(a , la) :
    
    bi = []
    
    for i in a :
        c = 0
        if i not in la :
            la.append(i)
            for k in a :
                if i == k :
                    c += 1 
            bi.append(c)
            
            
    return la,bi

x = datetime.datetime.now()

kok = kik(li,la)

y = datetime.datetime.now()

print(y-x)

la = []                   
        
for i in range(len(kok[1])) :
    if kok[1][i] in range(20,200):
        la.append(kok[0][i])
        
        
        
x = datetime.datetime.now()        

kak = kik(li,la)

y = datetime.datetime.now()
        
print(y-x)      
        
        
        





















"""
for i in li :
    if i != "#" :
        cout = 0
    
        for k in li :
            cout += 1
        
            if k != "#" :
            
                if i == k : 
                    print("this" ,i)
                    print(cout-1)
                    li[cout-1] == "#"

"""
    

    

"""
org = []
lis = []

for i in li :
    cout = 0
    if i not in org :
        org.append(i)
        pip = []
        for k in li :
            cout += 1
            if i == k :
                pip.append(cout)
            
        lis.append(pip)
        



o = []

for i in lis :
    o.append(len(i))
    

ink = " yes"

while ink != "ex":

    pip = input( "pip  ")
    
    for i in lis[org.index(pip)] :
        print(li[i-2],li[i-1],li[i],li[i+1]) 

    ink = input("end") 
    par1 = int(input("1  "))
    par2 = int(input("2  "))
    c = 0
    
    for i in o :
        c +=1 
    
        if i in range(par1,par2):
            print(org[c-1],o[c-1])
"""    
 
    



   
"""

for i in lis[org.index("Mars")] :
    print(li[i-1],li[i],li[i+1])
"""
             

        



    














