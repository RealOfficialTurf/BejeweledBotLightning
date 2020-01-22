import numpy as np
import pyautogui

def findcname(c):
    if c == 1333 or c == 1222:
        y = 'W'
    elif c == 1303 or c == 1202 or c == 1313:
        y = 'P'
    elif c == 1330 or c == 1320:
        y = 'Y'
    elif c == 1310 or c == 1321 or c == 1331 or c == 1332:
        y = 'O'
    elif c == 1300 or c == 1301:
        y = 'R'
    elif c == 1020 or c == 1030 or c == 1031 or c == 1131 or c == 1132:
        y = 'G'
    elif c == 1002 or c == 1013 or c == 1023 or c == 1033:
        y = 'B'
    else:
        y = '?'
    return y

if pyautogui.confirm(text="Press OK when you're in the main menu", title='', buttons=['OK', 'Cancel'])=='Cancel':
    close()

print('Ready')
impos = pyautogui.locateOnScreen('D:\Macro\Advanced\Bej3MainMenuTopLeft.png')
extra = pyautogui.locateOnScreen('D:\Macro\Advanced\Bej3MainMenuBottomRight.png')
print(impos,' ',extra)

if impos == None or extra == None:
    print('ERROR: Cannot find top-left or bottom-right of the game')
    pyautogui.confirm(text="ERROR: Cannot find top-left or bottom-right of the game", title='', buttons=['OK', 'Cancel'])
    close()
lightningboard = (334,83)
tilesize = 82
point1 = (40,19)
p5sec = (55,27)
p10sec = (67,35)
board = np.empty((8,8),dtype=np.uint8)
matches = np.empty((8,8,2),dtype=np.uint8)
if pyautogui.confirm(text="Open the game", title='', buttons=['OK', 'Cancel'])=='Cancel':
    close()
try:
    while True:
        unknowncount = 0
        #Check colors
        image = pyautogui.screenshot(region=(impos[0], impos[1], 1024, 768))
        for y in range(8):
            list = []
            for x in range(8):
                color = image.getpixel((lightningboard[0]+point1[0]+(tilesize*x),lightningboard[1]+point1[1]+(tilesize*y)))
                cpick = 1000+(color[0]//64)*100+(color[1]//64)*10+(color[2]//64)
                if cpick == 1333 or cpick == 1222: #White
                    board[x,y]=7
                elif cpick == 1303 or cpick == 1202 or cpick == 1313: #Purple
                    board[x,y]=6
                elif cpick == 1330 or cpick == 1320: #Yellow
                    board[x,y]=3
                elif cpick == 1310 or cpick == 1321 or cpick == 1331 or cpick == 1332: #Orange
                    board[x,y]=2
                elif cpick == 1300 or cpick == 1301: #Red
                    board[x,y]=1
                elif cpick == 1020 or cpick == 1030 or cpick == 1031 or cpick == 1131 or cpick == 1132: #Green
                    board[x,y]=4
                elif cpick == 1002 or cpick == 1013 or cpick == 1023 or cpick == 1033: #Blue
                    board[x,y]=5
                else:
                    board[x,y]=0
##                if board[x,y] > 0:
##                    color = image.getpixel((lightningboard[0]+p5sec[0]+(tilesize*x),lightningboard[1]+p5sec[1]+(tilesize*y)))
##                    cpick = 1000+(color[0]//64)*100+(color[1]//64)*10+(color[2]//64)
##                    if cpick == 1000:
##                        board[x,y]=board[x,y]+10
##                    color = image.getpixel((lightningboard[0]+p10sec[0]+(tilesize*x),lightningboard[1]+p10sec[1]+(tilesize*y)))
##                    cpick = 1000+(color[0]//64)*100+(color[1]//64)*10+(color[2]//64)
##                    if cpick == 1000:
##                        board[x,y]=board[x,y]+20
##                board[x,y] = findcolor(cpick)
                
                list.append(findcname(cpick))
                if board[x,y] == 0:
                    unknowncount=unknowncount+1
            print("".join(list))
        print("----------")
        print("Unknown Gem Count: ",unknowncount)
        bestx=8
        besty=8
        moveleft=True
        bestvalue=0
        for y in range(8):
            list = []
            for x in range(8):
                g1hx = 0
                g1hy = 0
                g2hx = 0
                g2hy = 0
                g1vx = 0
                g1vy = 0
                g2vx = 0
                g2vy = 0
                if x<7 and (board[x,y] != 0 and board[x+1,y] != 0): #Horizontal matches
                    g1h = board[x,y]
                    g2h = board[x+1,y]
                    if x>1 and (board[x-2,y] == board[x-1,y] and board[x-1,y] == g2h): #Right gem match
                        g2hx=2
                    if x<5 and (board[x+3,y] == board[x+2,y] and board[x+2,y] == g1h): #Left gem match
                        g1hx=2
                    if y>0:
                        if board[x,y-1] == g2h:
                            g2hy=g2hy+1
                        if board[x+1,y-1] == g1h:
                            g1hy=g1hy+1
                        if y>1:
                            if board[x,y-1] == g2h and board[x,y-2] == g2h:
                                g2hy=g2hy+1
                            if board[x+1,y-1] == g1h and board[x+1,y-2] == g1h:
                                g1hy=g1hy+1
                    if y<7:
                        if board[x,y+1] == g2h:
                            g2hy=g2hy+1
                        if board[x+1,y+1] == g1h:
                            g1hy=g1hy+1
                        if y<6:
                            if board[x,y+1] == g2h and board[x,y+2] == g2h:
                                g2hy=g2hy+1
                            if board[x+1,y+1] == g1h and board[x+1,y+2] == g1h:
                                g1hy=g1hy+1
                    
                if y<7 and (board[x,y] != 0 and board[x,y+1] != 0): #Vertical matches
                    g1v = board[x,y]
                    g2v = board[x,y+1]
                    if g1v == 0 or g2v == 0:
                        continue
                    if y>1 and (board[x,y-2] == board[x,y-1] and board[x,y-1] == g2v): #Bottom gem match
                        g2vy=2
                    if y<5 and (board[x,y+3] == board[x,y+2] and board[x,y+2] == g1v): #Top gem match
                        g1vy=2
                    if x>0:
                        if board[x-1,y] == g2v:
                            g2vx=g2vx+1
                        if board[x-1,y+1] == g1v:
                            g1vx=g1vx+1
                        if x>1:
                            if board[x-1,y] == g2v and board[x-2,y] == g2v:
                                g2vx=g2vx+1
                            if board[x-1,y+1] == g1v and board[x-2,y+1] == g1v:
                                g1vx=g1vx+1
                    if x<7:
                        if board[x+1,y] == g2v:
                            g2vx=g2vx+1
                        if board[x+1,y+1] == g1v:
                            g1vx=g1vx+1
                        if x<6:
                            if board[x+1,y] == g2v and board[x+2,y] == g2v:
                                g2vx=g2vx+1
                            if board[x+1,y+1] == g1v and board[x+2,y+1] == g1v:
                                g1vx=g1vx+1
                #Deciding matches
                if g1hy > 1 and g1hx > 1: #
                    g1h=1+g1hx*2
                elif g1hx > 1:
                    g1h=g1hx-1
                elif g1hy > 1:
                    g1h=1
                else:
                    g1h=0
                if g2hy > 1 and g2hx > 1:
                    g2h=1+g2hx*2
                elif g2hx > 1:
                    g2h=g2hx-1
                elif g2hy > 1:
                    g2h=1
                else:
                    g2h=0
                if x<7 and max(g1h,g2h) > bestvalue:
                    bestx=x
                    besty=y
                    moveleft=True
                    bestvalue = max(g1h,g2h)
                if g1vx > 1 and g1vy > 1: #
                    g1v=1+g1vy*2
                elif g1vy > 1:
                    g1v=g1vy-1
                elif g1vx > 1:
                    g1v=1
                else:
                    g1v=0
                if g2vx > 1 and g2vy > 1:
                    g2v=1+g2vy*2
                elif g2vy > 1:
                    g2v=g2vy-1
                elif g2vx > 1:
                    g2v=1
                else:
                    g2v=0
                if y<7 and max(g1v,g2v) > bestvalue:
                    bestx=x
                    besty=y
                    moveleft=False
                    bestvalue = max(g1v,g2v)
        #Move the gem
        if x!=8 and y!=8:
            pyautogui.moveTo(impos[0]+lightningboard[0]+point1[0]+(tilesize*bestx),impos[1]+lightningboard[1]+point1[1]+(tilesize*besty))
            if moveleft:
                pyautogui.press('d')
            else:
                pyautogui.press('s')
except KeyboardInterrupt:
    print('\n')
