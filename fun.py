import pandas as pd
dict = {'gid': ["-", "<", "<", "<"],
        'g+': [">", ">", ">", "<"],
        'g*': ['>','<','>','<'],
        'g$':['>','>','>','-']}
df = pd.DataFrame(dict)
data_new= df.rename( index={0: 'fid',1:'f+',2:'f*',3:'f$'})
print data_new
graph1={}
columns=list(data_new)
rows=['fid','f+','f*','f$']
for i in rows:
    lst=[]
    for j in columns:
        if(data_new.loc[i,j]== '>'):
            lst.append(j)
        else:
            continue

    graph1[i]=lst

for i in columns:
    lst=[]
    for j in rows:
        if(data_new.loc[j,i]== '<'):
            lst.append(j)
        else:
            continue

    graph1[i]=lst
print graph1

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
        for newpath in newpaths:
            paths.append(newpath)
    return paths


lst1=find_all_paths(graph1,'fid','f$')
lst2= find_all_paths(graph1,'gid','f$')
list1=[]
list2=[]

max=0
for i in lst1:
    if(max<=len(i)):
        max=len(i)
        list1=i
    else:
        continue
print "the max path from fid"
print list1

max1=0
for i in lst2:
    if(max1<=len(i)):
        max1=len(i)
        list2=i
    else:
        continue
print "the max path from gid"
print list2
ansdict={}
for i in list1:
    ansdict[i]=len(list1)-list1.index(i)-1


for j in list2:
    if(j not in ansdict.keys()):
        ansdict[j]=len(list2)-list2.index(j)-1

print "the final ans in the form of dict not as dataframe"
print ansdict