s1="""      ------
      |      |
             |
             |
             |
             |
      ------
      """
s2="""      ------
      |      |
      0      |
             |
             |
             |
      ------
      """
s3="""      ------
      |      |
      0      |
      |      |
             |
             |
      ------
      """
s4="""      ------
      |      |
      0      |
     /|      |
             |
             |
      ------
      """
s5="""      ------
      |      |
      0      |
     /|\\      |
             |
             |
      ------
      """
s6="""      ------
      |      |
      0      |
     /|\\      |
     /       |
             |
      ------
      """
s7="""      ------
      |      |
      0      |
     /|\\      |
     / \\      |
             |
      ------
      """
l=[s1,s2,s3,s4,s5,s6,s7]
import random
print("wellcome to hangman game ...\ntry to guess the word untill the hangman created\nyou have 7 attempts ")
ch=["rayan","bright","nanon","neo","shreya"]
print("this is your list ",ch)
at=7
c=0
rw=random.choice(ch)
lrw=list(rw)
rl=[]
word=["_"]*len(rw)
while at>0:
    print("word :")
    for i in word:
        print(i,end=" ")
    print('\n\n')
    print(l[c])
    g=input("\nguess a letter ").lower()
    if g in rl:
        print("u have allready guessed this letter ")
        continue
    rl.append(i)
    if g in rw:
        for i in range(len(rw)):
            if rw[i]==g:
                word[i]=g

        if "_" not in word:
            print("u guessed the word\n ",rw)
            print("your hangman\n",l[c])
            break
    else:
        at=at-1
        c=c+1
        print("wrong guess ...\nattempts remaining ",at)
        


if "_" in word:
    print("\nall atempts are completed ..")
    print("hang man > <  \n",l[-1])
    print('\nthe word is ',rw)
    
        
