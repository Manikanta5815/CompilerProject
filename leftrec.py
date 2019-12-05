def leftrecursion():
    file = open('input.txt')
    line = file.read().splitlines()
    dict={}
    errorprod={}
    for lines in line:

        k = lines.split('->')
        m=k[1].split('|')
        dict[k[0]]=m

    for keys in dict.keys():
        lst=dict[keys]
        le=len(lst)
        empt=[]
        for j in range(le):
            fir=lst[j][0]
            if(keys==fir):
                empt.append(lst[j])
                errorprod[keys]=empt

    for erkey in  errorprod.keys():
        erlst=errorprod[erkey]
        lst1=[]
        lst2=['e']
        diclst=dict[erkey]
        hei=len(diclst)
        new = erkey + "'"
        beta = diclst[hei - 1]
        newpr = beta + new
        lst1.append(newpr)
        for k in range(len(erlst)):
            alpha=erlst[k][1::]
            new1=alpha+new
            lst2.append(new1)
        dict[erkey] = lst1
        dict[new]=lst2

    print "e is notation for epsilon"
    for ke in dict.keys():
        mylst=dict[ke]
        rn=len(mylst)
        print ke + "->",
        for f in range(rn):
            if(f!=rn-1):
                print mylst[f]+"|",
            else:
                print mylst[f]
        print "\n"

leftrecursion()
