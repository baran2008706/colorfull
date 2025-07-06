from turtle import *
speed(0)
pensize(3)
clr=['red','blue','green','yellow','orange','purple','magenta','tomato','khaki']
n=72
for i in range(1,n+1):
    pencolor(clr[i%9])
    fd(150)
    if 1<=i<=n/4:
        write('sampad')
    elif n/4<i<=n/2+1 :
        write('smapad',align='right')
    goto(0,0)
    lt(360/n)
