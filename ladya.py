def main1():
    n=int(input())
    field=[[x,y] for x in range(1,n+1) for y in range(1,n+1)]
    print(field)
    ferzi=[]
    if n%2==0:
        i=[1,1]
        ferzi.append(i)
        print([i[0]+1,i[1]+2])
        m=2
        while len(ferzi)<n:
            print(len)
            if [i[0]+1,i[1]+2] in field:
                i=[i[0]+1,i[1]+2]
                ferzi.append(i)
                print(i)
            elif [i[0]+1,1] in field:
                i=[i[0]+1,m]
                m+=2
                ferzi.append(i)
        print(ferzi)
    if n%2==1:
        i=[1,2]
        ferzi.append(i)
        print([i[0]+1,i[1]+2])
        m=1
        while len(ferzi)<n:
            print(len)
            if [i[0]+1,i[1]+2] in field:
                i=[i[0]+1,i[1]+2]
                ferzi.append(i)
                print(i)
            elif [i[0]+1,1] in field:
                i=[i[0]+1,m]
                m+=2
                ferzi.append(i)
        print(ferzi)
    
while True:
    main1()
    
