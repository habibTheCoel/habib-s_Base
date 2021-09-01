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
        
        
        





















        



    














