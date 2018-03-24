if __name__ == '__main__':
    mylist=[]
    N = int(input())
    for counter in range (0,N):
        cmd=input()
        listcmd=cmd.split(' ')
        if listcmd[0]=="insert":
            position = (int)(listcmd[1])
            value = (int)(listcmd[2])
            mylist.insert(position,value)
        elif listcmd[0]=="print":
            print (mylist)
        elif listcmd[0]=="remove":
            value=(int)(listcmd[1])
            mylist.remove(value)
        elif listcmd[0]=="append":
            value=(int)(listcmd[1])
            mylist.append(value)
        elif listcmd[0]=="sort":
            mylist.sort()
        elif listcmd[0]=="pop":
            mylist.remove(mylist[-1])
        elif listcmd[0]=="reverse":
            mylist.reverse()