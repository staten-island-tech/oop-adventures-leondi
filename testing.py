def gambling(quarters, play1, play2, play3):
    count1 = 35-play1
    count2 = 100-play2
    count3 = 10-play3
    numplays = 0
    while quarters > 0:
        quarters-=1
        if quarters <= 0:
            print("brokie")
            print(numplays)
            break
        numplays+=1
        count1-=1
        if count1 == 0:
            quarters+=30
            count1=35
        quarters-=1
        if quarters <= 0:
            print("brokie")
            print(numplays)
            break
        numplays+=1
        count2-=1
        if count1 == 0:
            quarters+=60
            count2=100
        quarters-=1
        if quarters <= 0:
            print("brokie")
            print(numplays)
            break
        numplays+=1
        count3-=1
        if count3 == 0:
            quarters+=9
            count3=10
# gambling(48, 3, 10, 4)

def gamblingbutbetter(quar, playslist):
    plays_num = 0
    countvars = [[35, 30, 35], [100, 60, 100], [10, 9, 10]]
    for i in range(3):
        countvars[i][0]-=playslist[i]
    while quar > 0:
        for i in range(3):
            plays_num+=1
            quar-=1
            countvars[i][0]-=1
            if countvars[i][0] == 0:
                quar+=countvars[i][1]
                countvars[i][0]=countvars[i][2]
    print(plays_num)
    print("die")
# gamblingbutbetter(77, [4, 9, 3])

def voronivil (villagelist):
    n = villagelist.len
    

voronivil([5,16, 0, 10, 4, 15])