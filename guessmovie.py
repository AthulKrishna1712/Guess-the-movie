import random
movies=['avengers','matrix','deadpool','vikram vedha','jungle book','gol maal','black friday','drisyam','tare zameen paar','sixth sense']
def createquestion(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append("*")
    qn=''.join(str(x) for x in temp)
    return qn
def ispresent(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
def unlock(qn,movie,letter):
    ref=list(movie)
    qnlist=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if(qnlist[i]=='*'):
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new
def play():
    p1name=input("Player 1,Please enter your name: ")
    p2name=input("Player 2,Please enter your name: ")
    po1=0
    po2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            print(p1name,' your turn')
            pickedmovie=random.choice(movies)
            qn=createquestion(pickedmovie)
            print(qn)
            modqn=qn
            notsaid=True
            while(notsaid):
                letter=input('your letter: ')
                if(ispresent(letter,pickedmovie)):
                    modqn=unlock(modqn,pickedmovie,letter)
                    print(modqn)
                    d=int(input('press 1 to guess the movie and 2 to unlock another letter: '))
                    if d==1:
                        ans=input('your answer: ')
                        if ans==pickedmovie:
                            po1=po1+1
                            print('correct')
                            notsaid=False
                            print(p1name,',your score: ',po1)
                        else:
                            print('wrong answer,plz try again')
                else:
                    print(letter,' not found')
            c=input("Press 1 to continue and 0 to exit...")
            c=int(c)
            if(c==0):
                 print(p1name,",your score: ",po1)
                 print(p2name,",your score: ",po2)
                 print("Thanks for playing,Have a nice day...")
                 willing=False
        else:
            print(p2name,' your turn')
            pickedmovie=random.choice(movies)
            qn=createquestion(pickedmovie)
            print(qn)
            modqn=qn
            notsaid=True
            while(notsaid):
                letter=input('your letter: ')
                if(ispresent(letter,pickedmovie)):
                    modqn=unlock(modqn,pickedmovie,letter)
                    print(modqn)
                    d=int(input('press 1 to guess the movie and 2 to unlock another letter: '))
                    if d==1:
                        ans=input('your answer: ')
                        if ans==pickedmovie:
                            po2=po2+1
                            print('correct')
                            notsaid=False
                            print(p2name,',your score: ',po2)
                        else:
                            print('wrong answer,plz try again')
                else:
                    print(letter,' not found')
            c=input("Press 1 to continue and 0 to exit...")
            c=int(c)
            if(c==0):
                 print(p1name,",your score: ",po1)
                 print(p2name,",your score: ",po2)
                 print("Thanks for playing,Have a nice day...")
                 willing=False
        turn=turn+1
play()
                    