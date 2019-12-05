import pandas as pd
dict = {}
terminals = []
variables = []
precedict={}
def grammarpar():
    file = open('input.txt')
    line = file.read().splitlines()



    for lines in line:
        k = lines.split('->')
        m = k[1].split('|')
        dict[k[0]] = m
    return dict
def variable():
    locdictv=grammarpar()
    for key in locdictv.keys():
        variables.append(key)

    return variables

def terminal():

    locdictt=grammarpar()
    lovar=variable()
    for key in locdictt.keys():
        lst = locdictt[key]
        for le in range(len(lst)):
            str=lst[le]
            myle = len(str)
            for j in range(myle):
                if(str[j] not in lovar and str[j] not in terminals):
                    terminals.append(str[j])
    return terminals
def checkop():
    locdict=grammarpar()
    locvar=variable()
    locter=terminal()
    a = True
    for key in locdict.keys():

        lst = locdict[key]
        for le in range(len(lst)):
            str = lst[le]
            myle = len(str)
            for j in range(myle-1):
                if (str[j] in locvar and str[j+1]  in locter or str[j+1] in locvar and str[j]  in locter):
                    continue
                else:
                    a=False
                    break

    if(a==True):
        return 1
    else:
        return 0
def precedence():
    prefile = open('opprec.txt')
    line = prefile.read().splitlines()

    for lines in line:
        k = lines.split('->')
        m = k[1].split('|')
        precedict[k[0]] = m
    k=precedict.keys()
    opdict={}
    newkey=[]
    rows=[]
    for i in range(len(k)):
        str='g'
        str1='f'
        nkey=str+k[i]
        nkey1=str1+k[i]

        newkey.append(nkey)
        rows.append(nkey1)

    for i in range(len(k)):
        var=k[i]
        oplst=[]
        for j in range(len(rows)):
            var1=k[j]

            c1=precedict[var]
            c2=precedict[var1]
            if(c1[0]==c2[0] and c1[1]=='N'):
                oplst.append('-')

            elif (c1[0] == c2[0] and c1[1] == 'L'):
                oplst.append('>')
            elif (c1[0] == c2[0] and c1[1] == 'R'):
                oplst.append('<')
            elif(c1[0]>c2[0]):
                oplst.append('<')
            else:
                oplst.append('>')
        opdict[newkey[i]]=oplst
    df= pd.DataFrame(opdict)
    index={}
    for le in range(len(rows)):
        index[le]=rows[le]
    df_new=df.rename(index)
    return df_new


def parsing():
    check=checkop()
    k=precedence()
    flag=0
    if(check==0):
        print "the grammar is not operator grammar and cannot get parsed"
    else:
        print "Enter The String To be Parsed"
        string=raw_input()
        newstr=string+'$'
        stack=[]
        stack.append('$')
        index=0
        while(len(stack)>0):
            top=stack[len(stack)-1]
            print stack
            com1='f'+top
            com2='g'+newstr[index]
            var1=k.loc[com1][com2]
            if(top=='$' and newstr[index]=='$'):
                flag=1
                stack.pop()
            else:
                if(var1=='<' or var1=='='):
                    stack.append(newstr[index])
                    index=index+1
                elif(var1=='-'):
                    flag = 0
                    break
                elif(top=='$' and len(stack)==2):
                    flag = 0
                    break
                else:
                    stack.pop()

    if(flag==0):
        print 'string cannont be parsed'
    else:
        print 'string is parsed'




m=precedence()
print m

parsing()
