# -*- coding: utf-8 -*-


Dep_List={
    'a':['b','c'],
    'b':['d','e'],
    'c':['b','f'],
    'd':[],
    'e':['f'],
    'f':[]
}

clr={}
prt={}
trv_time={}
dfs_trv_out =[]
for n in Dep_List.keys():
        clr[n]='W'
        prt[n]=None
        trv_time[n]=[-1,-1]
print(clr)
print(prt)
print(trv_time)

t=0 
def dfs(u):   
    global t
    clr[u]='G'
    trv_time[u][0]=t
    dfs_trv_out.append(u)   
    for v in Dep_List[u]: 
        if clr[v]=='W':
            prt[v]=u
            dfs(v)
            clr[u]='B'
            trv_time[u][1]=t
        t +=1   

print("The output")      
dfs('a')
print(clr)
print(prt)
print(trv_time)
print(dfs_trv_out)