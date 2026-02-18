box=[['-','-','-'],['-','-','-'],['-','-','-']]
c=1
for i in box:
    for j in i:
        print(j,end=' ')
    print()
g=0
if(g==0):
    chance=input("Do you want to start first or shall I(I for you U for me):")
    g+=1
turn=1
while(c>0):
    #print(turn)
## Taking all the elements into the list
    tlist=[]
    for i in range(len(box)):
        tslist=[]
        for j in range(len(box[i])):
            tslist.append(box[i][j])
        tlist.append(tslist)
        
    for i in range(len(box)):
        tslist1=[]
        for j in range(len(box[i])):
            tslist1.append(box[j][i])
        tlist.append(tslist1)
         
    tslist2=[]
    for i in range(len(box)):
        for j in range(len(box[i])):
            if(i==j):
                tslist2.append(box[i][j])
                 
    tlist.append(tslist2)
    tlist3=[]
    j=2
    for i in range(0,len(box)):
        tlist3.append(box[i][j])
        j-=1
    tlist.append(tlist3)                      
    
    
## checking
    cc=0
    count=0
    for i in box:
        for j in i:
            if(j=='o' or j=='x'):
                count+=1
    
    for i in tlist:
        if((i[0]==i[1]==i[2]=='x') or (i[0]==i[1]==i[2]=='o')):
            cc+=1
    if(cc>0):
        print("game over")
        c=0
        if(chance=='U'):
            print("you won")
        else:
            print("I won")
        break
    else:
        
        if(count==9):
            print("it is a draw match")
            c=0
            break
        
        if(chance=='I'):
            print("Your chance")
            turn+=1
            
            xxx=0
            while(xxx==0):
                place=int(input("enter the number where you want to place the element:"))
                r=place//10
                co=place%10
                
                if(box[r-1][co-1]=='-'):
                    el=input("enter the element:")
                    box[r-1][co-1]=el
                    
                    for i in box:
                        for j in i:     
                            print(j,end=' ')
                        print()
                    xxx=1
                    break
                else:
                    print("the place was already filled")
                    xxx=0
                    continue
                    
            
            tlist=[]
            tslist=[]
            tslist1=[]
            tslist2=[]
            tslist3=[]
            chance='U'
            continue
        elif(chance=='U'):
            print("My chance")  
            if(turn==1):
                box[1][1]='o'
                turn+=1
                chance='I'
                tlist=[]
                tslist1=[]
                tslist2=[]
                tslist3=[]
                for i in box:
                    for j in i:
                        print(j,end=' ')
                    print() 
                continue
            else:
                xx=1 #for iterating through the priorities
                if(xx==1):
                    
                    l=0
                    for i in tlist:
                        if(l==1):
                            break
                        co=0
                        ind=0
                        cnil=0
                        for j in i:
                            if(j=='o'):
                                co+=1
                            elif(j=='-'):
                                cnil+=1
                                ind=i.index(j)
                        if(co==2 and cnil==1):
                            i[ind]='o'
                            
                            k=tlist.index(i)
                            if(k==0):
                                tlist[0][ind]='o'
                            elif(k==1):
                                tlist[1][ind]='o'
                            elif(k==2):
                                tlist[2][ind]='o'
                            elif(k==3):
                                tlist[ind][0]='o'
                            elif(k==4):
                                tlist[ind][1]='o'
                            elif(k==5):
                                tlist[ind][2]='o'
                            elif(k==6):
                                tlist[ind][ind]='o'
                            elif(k==7):
                                tlist[ind][2-ind]='o'                                 
                                
                            box[0],box[1],box[2]=tlist[0],tlist[1],tlist[2]
                            xx=0    
                            l=1
                            break
                        else:
                            xx=2
                if(xx==2):
                    
                    l=0
                    for i in tlist:
                        if(l==1):
                            break
                        cx=0
                        ind=0
                        cnil=0
                        for j in i: 
                            if(j=='x'): 
                                cx+=1
                            elif(j=='-'):
                                
                                cnil+=1
                                ind=i.index(j)
                    
                        if(cx==2 and cnil==1):
                            
                            k=tlist.index(i)
                            
                            i[ind]='o'
                            
                            
                           
                            if(k==0):
                                tlist[0][ind]='o'
                            elif(k==1):
                                tlist[1][ind]='o'
                            elif(k==2):
                                tlist[2][ind]='o'
                            elif(k==3):
                                tlist[ind][0]='o'
                            elif(k==4):
                                tlist[ind][1]='o'
                            elif(k==5):
                                tlist[ind][2]='o'
                            elif(k==6):
                                tlist[ind][ind]='o'
                            elif(k==7):
                                tlist[ind][2-ind]='o'
                                
                                
                            box[0],box[1],box[2]=tlist[0],tlist[1],tlist[2]
                            xx=0
                            l=1
                            break
                        else:
                            xx=3
                if(xx==3):
                    
                    l=0
                    for i in tlist:
                        if(l==1):
                            break
                        co=0
                        cx=0
                        ind=0
                        cnil=0
                        for j in i:
                            if(j=='o'):
                                co+=1
                            elif(j=='-'):
                                cnil+=1
                                ind=i.index(j)
                            else:
                                cx+=1
                                
                        if(co==1 and cx==0 and cnil==2):
                            k=tlist.index(i)
                            if(i[2]=='-'):
                                ind=2
                                i[ind]='o'
                            else:
                                i[ind]='o'
                                
                                
                                
                            if(k==0):
                                tlist[0][ind]='o'
                            elif(k==1):
                                tlist[1][ind]='o'
                            elif(k==2):
                                tlist[2][ind]='o'
                            elif(k==3):
                                tlist[ind][0]='o'
                            elif(k==4):
                                tlist[ind][1]='o'
                            elif(k==5):
                                tlist[ind][2]='o'
                            elif(k==6):
                                tlist[ind][ind]='o'
                            elif(k==7):
                                tlist[ind][2-ind]='o'
                            
                            box[0],box[1],box[2]=tlist[0],tlist[1],tlist[2]
                            xx=0
                            l=1
                            break
                        else:
                            xx=4
                if(xx==4):
                    l=0
                    for i in tlist:
                        if(l==1):
                            break
                        co=0
                        cx=0
                        ind=0
                        cnil=0
                        for j in i:
                            if(j=='o'):
                                co+=1
                            elif(j=='-'):
                                cnil+=1
                                ind=i.index(j)
                            else:
                                cx+=1
                                
                        if(co==1 and cx==1 and cnil==1):
                            k=tlist.index(i)
                            i[ind]='o'
                            
                            
                            if(k==0):
                                tlist[0][ind]='o'
                            elif(k==1):
                                tlist[1][ind]='o'
                            elif(k==2):
                                tlist[2][ind]='o'
                            elif(k==3):
                                tlist[ind][0]='o'
                            elif(k==4):
                                tlist[ind][1]='o'
                            elif(k==5):
                                tlist[ind][2]='o'
                            elif(k==6):
                                tlist[ind][ind]='o'
                            elif(k==7):
                                tlist[ind][2-ind]='o'
                            
                            
                            box[0],box[1],box[2]=tlist[0],tlist[1],tlist[2]
                            xx=0
                            l=1
                            break
                        else:
                            xx=5
                        if(xx==5):
                            l=0
                            for i in tlist:
                                if(l==1):
                                    break
                                cx=0
                                co=0 
                                cnil=0
                                ind=0
                                for j in i:
                                    if(j=='x'):
                                        cx+=1
                                    elif(j=='o'):
                                        co+=1
                                    elif(j=='-'):
                                        cnil+=1
                                        ind=i.index(j)
                                if(cx==0 and co==0 and cnil==3):
                                    k=tlist.index(i)
                                    if(tlist.index(i)==1):
                                        ind=1
                                        i[ind]='o'
                                    
                                    else:
                                        
                                        if(i[2]=='-'):
                                            ind=2
                                            i[ind]='o'
                    
                                    if(k==0):
                                        tlist[0][ind]='o'
                                    elif(k==1):
                                        tlist[1][ind]='o'
                                    elif(k==2):
                                        tlist[2][ind]='o'
                                    elif(k==3):
                                        tlist[ind][0]='o'
                                    elif(k==4):
                                        tlist[ind][1]='o'
                                    elif(k==5):
                                        tlist[ind][2]='o'
                                    elif(k==6):
                                        tlist[ind][ind]='o'
                                    elif(k==7):
                                        tlist[ind][2-ind]='o'
                                        
                                    box[0],box[1],box[2]=tlist[0],tlist[1],tlist[2]
                                    l=1
                                    xx=0
                                    break      
                                else:
                                    xx=6
                                
                        if(xx==6):
                            
                            l=0
                            for i in tlist:
                                if(l==1):
                                    break
                                cx=0
                                co=0 
                                cnil=0
                                ind=0
                                for j in i:
                                    if(j=='x'):
                                        cx+=1
                                    elif(j=='o'):
                                        co+=1
                                    elif(j=='-'):
                                        cnil+=1
                                        ind=i.index(j)
                                if(cx==1 and co==0 and cnil==2):
                                    if(tlist[1][1]=='-'):
                                        tlist[1][1]='o'
                                        box[0],box[1],box[2]=tlist[0],tlist[1],tlist[2]
                                    else:
                                        k=tlist.index(i)
                                        i[ind]='o'
                                        
                                        if(k==0):
                                            tlist[0][ind]='o'
                                        elif(k==1):
                                            tlist[1][ind]='o'
                                        elif(k==2):
                                            tlist[2][ind]='o'
                                        elif(k==3):
                                            tlist[ind][0]='o'
                                        elif(k==4):
                                            tlist[ind][1]='o'
                                        elif(k==5):
                                            tlist[ind][2]='o'
                                        elif(k==6):
                                            tlist[ind][ind]='o'
                                        elif(k==7):
                                            tlist[ind][2-ind]='o'
                                        
                                        box[0],box[1],box[2]=tlist[0],tlist[1],tlist[2]
                                    l=1
                                    xx=0
                                    break
                                        
                                        

                for i in box:
                    for j in i:
                        print(j,end=' ')
                    print()
                chance='I'  
