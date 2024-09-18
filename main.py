import curses
import threading
import time
import sys

class Board:
    def __init__(self,board):
        self.Min_path=None
        self.lenth_x=len(board)
        self.lenth_y=len(board[0])
        self.board=[[0 for i in range(self.lenth_y)] for i in range(self.lenth_x)]
        self.aim=board
        self.Best_solution=[]
        self.checker(0,0,0,[])
        self.operator_list=[]
    
    def change(self,x,y):
        if(x<0 or y<0 or x>=self.lenth_x or y>=self.lenth_y):return
        self.operator_list.append((x,y))
        self.board[x][y]^=1
        change_stdscr(x,y)
        if(x+1<self.lenth_x):
            self.board[x+1][y]^=1
            change_stdscr(x+1,y)
        if(y-1>=0):
            self.board[x][y-1]^=1
            change_stdscr(x,y-1)
        if(x-1>=0):
            self.board[x-1][y]^=1
            change_stdscr(x-1,y)
        if(y+1<self.lenth_y):
            self.board[x][y+1]^=1
            change_stdscr(x,y+1)
    
    def withdraw(self):
        if(len(self.operator_list)):
            self.change(self.operator_list[-1][0],self.operator_list[-1][1])
            del self.operator_list[-1]
            del self.operator_list[-1]
            return 1
        return 0
    
    def show_best(self):
        global start_time
        global main_flag
        time.sleep(0)
        for i in self.Best_solution:
            if(main_flag):
                now=time.time()
                if(int(now-start_time)>limit_time):break
            self.change(i[0],i[1])
            time.sleep(1)
    
    def checker(self,x,y,temp_num,temp_solution):
        if(y==self.lenth_y):
            x+=1
            y=0
        if(x==self.lenth_x):
            if(self.board[self.lenth_x-1]==self.aim[self.lenth_x-1] and (self.Min_path==None or self.Min_path>temp_num)):
                self.Min_path=temp_num
                self.Best_solution=temp_solution+[]
            return
        if(x==0):
            self.checker(x,y+1,temp_num,temp_solution)
            self.board[x][y]^=1
            if(x+1<self.lenth_x):self.board[x+1][y]^=1
            if(y-1>=0):self.board[x][y-1]^=1
            if(x-1>=0):self.board[x-1][y]^=1
            if(y+1<self.lenth_y):self.board[x][y+1]^=1
            temp_solution.append((x,y))
            self.checker(x,y+1,temp_num+1,temp_solution)
            temp_solution.remove((x,y))
            self.board[x][y]^=1
            if(x+1<self.lenth_x):self.board[x+1][y]^=1
            if(y-1>=0):self.board[x][y-1]^=1
            if(x-1>=0):self.board[x-1][y]^=1
            if(y+1<self.lenth_y):self.board[x][y+1]^=1
        else:
            if(self.board[x-1][y]==self.aim[x-1][y]):self.checker(x,y+1,temp_num,temp_solution)
            else:
                self.board[x][y]^=1
                if(x+1<self.lenth_x):self.board[x+1][y]^=1
                if(y-1>=0):self.board[x][y-1]^=1
                if(x-1>=0):self.board[x-1][y]^=1
                if(y+1<self.lenth_y):self.board[x][y+1]^=1
                temp_solution.append((x,y))
                self.checker(x,y+1,temp_num+1,temp_solution)
                temp_solution.remove((x,y))
                self.board[x][y]^=1
                if(x+1<self.lenth_x):self.board[x+1][y]^=1
                if(y-1>=0):self.board[x][y-1]^=1
                if(x-1>=0):self.board[x-1][y]^=1
                if(y+1<self.lenth_y):self.board[x][y+1]^=1
    
    def printf(self):
        global stdscr
        global stdscrr
        for i in range(self.lenth_x):
            for j in range(self.lenth_y):
                color_=2
                if(self.board[i][j]):
                    color_=1
                for x in range(3*i+1,3*i+5):
                    for y in range(6*j+1,6*j+9):
                        if(3*i+2<=x<=3*i+3 and 6*j+3<=y<=6*j+6):stdscr.addstr(x, y, ' ', curses.color_pair(color_))
                        else:stdscr.addstr(x, y, ' ', curses.color_pair(3))
                if(self.aim[i][j]):
                    color_=1
                for x in range(3*i+1,3*i+5):
                    for y in range(6*j+1,6*j+9):
                        if(3*i+2<=x<=3*i+3 and 6*j+3<=y<=6*j+6):stdscr.addstr(x, y+6*self.lenth_y+4, ' ', curses.color_pair(color_))
                        else:stdscr.addstr(x, y+6*self.lenth_y+4, ' ', curses.color_pair(3))
        
    def printf_base1(self):
        global stdscr
        global stdscrr
        for i in range(self.lenth_x):
            for j in range(self.lenth_y):
                color_=2
                if(self.aim[i][j]):
                    color_=1
                for x in range(3*i+4,3*i+8):
                    for y in range(6*j+2,6*j+10):
                        if(3*i+5<=x<=3*i+6 and 6*j+4<=y<=6*j+7):stdscr.addstr(x, y, ' ', curses.color_pair(color_))
                        else:stdscr.addstr(x, y, ' ', curses.color_pair(3))
        for i in range(3):
            stdscr.addstr(3, 4+6*i, str(i))
        for j in range(3):
            stdscr.addstr(5+3*j, 1, str(j))
        stdscr.addstr(13, 6*self.lenth_y+5, 'After pressing (2,2)-->')
        
    def printf_base2(self):
        global stdscr
        global stdscrr
        for i in range(self.lenth_x):
            for j in range(self.lenth_y):
                color_=2
                if(self.aim[i][j]):
                    color_=1
                for x in range(3*i+4,3*i+8):
                    for y in range(6*j+2,6*j+10):
                        if(3*i+5<=x<=3*i+6 and 6*j+4<=y<=6*j+7):stdscr.addstr(x, y+6*self.lenth_y+26, ' ', curses.color_pair(color_))
                        else:stdscr.addstr(x, y+6*self.lenth_y+26, ' ', curses.color_pair(3))

    def clear(self):
        return self.board==self.aim
    
    def reset(self):
        self.board=[[0 for i in range(self.lenth_x)] for j in range(self.lenth_y)]
        self.operator_list.clear()
        self.printf()

class Button:
    def __init__(self,start_x=0,start_y=0,String=[]):
        self.start_x=start_x
        self.start_y=start_y
        self.end_x=start_x+len(String)
        self.end_y=start_y+len(String[0])
        self.String=String
    
    def printf(self):
        global stdscr
        global stdscrr
        for i in range(self.end_x-self.start_x):
            stdscr.addstr(self.start_x+i, self.start_y, self.String[i], curses.color_pair(2))

class Mouse_operation_tut(threading.Thread):
    global stdscrr
    global stdscr

    def Check(self):
        global ContinueFlag
        ans=ContinueFlag
        return ans
    
    def run(self):
        global stdscrr
        global stdscr
        global ContinueFlag
        global button_close
        global button_ShowBest
        global board
        while self.Check():
            curses.flushinp()#清空输入队列
            key = stdscr.getch()
            if key == curses.KEY_MOUSE:
                _, y, x, _, button = curses.getmouse()#鼠标在x行y列
                if(button_close.start_x<=x<button_close.end_x and button_close.start_y<=y<button_close.end_y):
                    break
                if(button_ShowBest.start_x<=x<button_ShowBest.end_x and button_ShowBest.start_y<=y<button_ShowBest.end_y):
                    board.reset()
                    stdscr.addstr(5, board.lenth_y*12+8, 'Best solution(row,colume): (1,1)(1,3)(2,2)(3,2)')
                    board.show_best()
                    board.reset()
            elif key == ord('q'):
                break
            elif key == ord('b'):
                board.reset()
                stdscr.addstr(5, board.lenth_y*12+8, 'Best solution(row,colume): (1,1)(1,3)(2,2)(3,2)')
                board.show_best()
                board.reset()
            else:
                pass
            time.sleep(0.05)

class Mouse_operation(threading.Thread):
    def Check(self):
        global ContinueFlag
        ans=ContinueFlag
        return ans

    def run(self):
        global stdscrr
        global stdscr
        global start_time
        global ContinueFlag
        global button_close
        global button_Reset
        global button_ShowBest
        global button_Withdraw
        global button_Notice
        global button_x
        global button_y
        global num
        global final
        global fail_num
        global main_flag
        end_flag=False
        final='lose'
        num=0
        while self.Check():
            # curses.flushinp()#清空输入队列
            key = stdscr.getch()
            # stdscr.addstr(0,0,'qwerqwer')
            # time.sleep(10)
            if key == curses.KEY_MOUSE:
                _, y, x, _, button = curses.getmouse()#鼠标在x行y列
                if(x%3!=1 and y%6!=1 and y%6!=2):
                    board.change((x-1)//3,(y-1)//6)
                    num+=1
                if(button_close.start_x<=x<button_close.end_x and button_close.start_y<=y<button_close.end_y):
                    main_flag=False
                    lose()
                    curses.flushinp()
                    stdscr.getch()
                    break
                if(button_Reset.start_x<=x<button_Reset.end_x and button_Reset.start_y<=y<button_Reset.end_y):
                    board.reset()
                    num=0
                if(button_Withdraw.start_x<=x<button_Withdraw.end_x and button_Withdraw.start_y<=y<button_Withdraw.end_y):
                    num-=board.withdraw()
                if(button_ShowBest.start_x<=x<button_ShowBest.end_x and button_ShowBest.start_y<=y<button_ShowBest.end_y):
                    # now=time.time()
                    # if(now-start_time>20):
                    if(fail_num>=fail_num_limit):
                        board.reset()
                        board.show_best()
                        board.reset()
                        num=0
            elif key == ord('q'):
                main_flag=False
                lose()
                curses.flushinp()
                stdscr.getch()
                break
            elif key == ord('b'):
                if(fail_num>=fail_num_limit):
                    board.reset()
                    board.show_best()
                    board.reset()
            elif key == ord('w'):
                num-=board.withdraw()
            elif key == ord('r'):
                board.reset()
                num=0
            elif key == ord(' '):
                x = stdscr.getch()
                if(x==ord('Q')):
                    # lose()
                    end_flag=True
                    break
                while not(ord('0')<=x<=ord('9')):
                    curses.flushinp()#清空输入队列
                    x = stdscr.getch()
                    if(x==ord('Q')):
                        # lose()
                        end_flag=True
                        break
                if(x==ord('Q')):
                    # lose()
                    end_flag=True
                    break
                stdscr.addstr(button_x.start_x, button_x.end_y, chr(x), curses.color_pair(2))
                y = stdscr.getch()
                if(y==ord('Q')):
                    # lose()
                    end_flag=True
                    break
                while not(ord('0')<=y<=ord('9')):
                    curses.flushinp()#清空输入队列
                    y = stdscr.getch()
                    if(y==ord('Q')):
                        # lose()
                        end_flag=True
                        break
                if(y==ord('Q')):
                    # lose()
                    end_flag=True
                    break
                stdscr.addstr(button_y.start_x, button_y.end_y, chr(y), curses.color_pair(2))
                board.change(int(chr(x)), int(chr(y)))
                num+=1
            elif key == ord('Q'):
                break
            if(board.clear()):
                final='win'
                if(num==board.Min_path):final='egg_win'
                time.sleep(0.5)
                break
            time.sleep(0.05)

class Screen_operation(threading.Thread):
    def Check(self):
        global ContinueFlag
        ans=ContinueFlag
        return ans
    
    def run(self):
        global stdscr
        global stdscrr
        global main_flag
        global first_flg
        while self.Check():
            # 获取当前窗口大小
            global start_time
            global stdscr
            global board
            if main_flag:
                global limit_time
                global fail_num
                global button_ShowBest
                now=time.time()
                # stdscr.addstr()
                if(int(fail_num)<fail_num_limit):
                    if(first_flg==True):
                        stdscr.addstr(button_ShowBest.end_x,button_ShowBest.start_y,f"                                                                                          ")
                        stdscr.addstr(button_ShowBest.end_x,button_ShowBest.start_y,f"You have to try {int(fail_num_limit-fail_num)} times before you can see the best solution.")
                else:
                    if(first_flg==True):
                        stdscr.addstr(button_ShowBest.end_x,button_ShowBest.start_y,f"                                                                                          ")
                        stdscr.addstr(button_ShowBest.end_x,button_ShowBest.start_y,f"Now you can see the best solution.")
                if(int(limit_time-now+start_time>=0)):
                    stdscr.addstr(0,board.lenth_y*6+5,f"                                                  ")
                    stdscr.addstr(0,board.lenth_y*6+5,f"You have {int(limit_time-now+start_time+1)} seconds.")
                else:
                    if(first_flg==True):
                        first_flg=False
                        lose()
                    curses.flushinp()
                    curses.ungetch('Q')
            Refresh_pad()
            time.sleep(0.05)

def startup():
    global stdscr
    global stdscrr
    stdscr.clear()
    current_row = 0
    menu = ['Play', 'Scoreboard', 'Tutorial', 'Exit']
    h, w = stdscrr.getmaxyx()
    cnt = 0
    while True:
        if cnt == 0: key = 1
        else:
            curses.flushinp()#清空输入队列
            key = stdscr.getch()
        cnt = 1
        stdscr.clear()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            if menu[current_row] == 'Play':
                welcome_start_page_of_play()
                return start_page_of_play()
            elif menu[current_row] == 'Scoreboard':
                start_page_of_scoreboard()
            elif menu[current_row] == 'Tutorial':
                start_page_of_tut()
            elif menu[current_row] == 'Exit':
                return 0
        stdscr.clear()
        for idx, row in enumerate(menu):
            x = w // 2 - len(row)//2
            y = h // 2 - len(menu)//2 + idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
def welcome_start_page_of_play():
    global stdscr
    global stdscrr
    # 计时模式
    # 难度选择模式
    stdscr.clear()
    start_txt = [
    '         _.=+._         ', 
    ":.\`--._/[_/~|;\_.--'/. ",
    "::.`.  ` __`\.-.(  .'.::", 
    "::::.`-:.`'..`-'/\'.:::::", 
    ":::::::.\ `--')/  ) ::::", 
    "          `--'          ",  
    ' ____            ___             _                     _       _____ _                     _                     _                ',
    '|  _ \  ___     / _ \ _ __    __| | ___    _ __   ___ | |_    |_   _| |__   ___ _ __ ___  (_)___   _ __   ___   | |_ _ __ _   _   ',
    "| | | |/ _ \   | | | | '__|  / _` |/ _ \  | '_ \ / _ \| __|     | | | '_ \ / _ \ '__/ _ \ | / __| | '_ \ / _ \  | __| '__| | | |  ",
    "| |_| | (_) |  | |_| | |    | (_| | (_) | | | | | (_) | |_ _    | | | | | |  __/ | |  __/ | \__ \ | | | | (_) | | |_| |  | |_| |_ ",
    "|____/ \___(_)  \___/|_|     \__,_|\___/  |_| |_|\___/ \__(_)   |_| |_| |_|\___|_|  \___| |_|___/ |_| |_|\___/   \__|_|   \__, (_)",
    "                                                                                                                          |___/   ",
    "", "", "press any button to continue..."]
    h, w = stdscrr.getmaxyx()
    for idx, row in enumerate(start_txt):
        x = max(w // 2 - len(row)//2,0)
        y = max(h // 2 - len(start_txt)//2 + idx,0)

        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(y, x, row)
        stdscr.attroff(curses.color_pair(4))
    stdscr.getch()
def start_page_of_play():
    global stdscr
    global stdscrr
    # 计时模式
    # 难度选择模式
    stdscr.clear()
    h, w = stdscrr.getmaxyx()
    # 难度选择
    current_row = 0
    menu = ['Easy', 'Medium', 'Hard']

    cnt = 0
    while True:
        curses.flushinp()#清空输入队列
        if cnt == 0: key = 1
        else: key = stdscr.getch()
        cnt = 1
        stdscr.clear()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            if menu[current_row] == 'Easy':
                temp=mission_selection()
                if(isinstance(temp, int)==False or temp==0):return temp
                else:return ('Easy',temp)
            elif menu[current_row] == 'Medium':
                temp=mission_selection()
                if(isinstance(temp, int)==False or temp==0):return temp
                else:return ('Medium',temp)
            elif menu[current_row] == 'Hard':
                temp=mission_selection()
                if(isinstance(temp, int)==False or temp==0):return temp
                else:return ('Hard',temp)
        elif key==ord('q'):
            return startup()
        stdscr.clear()
        for idx, row in enumerate(menu):
            x = max(w // 2 - len(row)//2,0)
            y = max(h // 2 - len(menu)//2 + idx,0)
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)
# scoreboard是一个二维数组
# def scoreboard_init():  # 只有scoreboard.txt为空时才初始化，之后自动跳过此函数
#     with open('scoreboard.txt', 'w') as file:
#         lines = file.read()
#         if lines != None:
#             for idx in range(1, 31):
#                 file.write(f"{idx} {', '.join(map(str, [0]))}\n")
# 完成每一局后更新scoreboard。 更新逻辑：此函数读取scoreboard.txt文件并转化为列表储存， 在更改完列表之后清空scoreboard.txt， 并再将更改后的列表写入scoreboard.txt          

def mission_selection():
    global stdscr
    global stdscrr
    stdscr.clear()
    missions = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
    current_row = 0
    h, w = stdscrr.getmaxyx()
    cnt = 0
    while True:
        if cnt == 0: 
            key = 1
        else:
            curses.flushinp()#清空输入队列
            key = stdscr.getch()
        cnt = 1
        stdscr.clear()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(missions) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            return int(missions[current_row])
        elif key==ord('q'):
            return start_page_of_play()
        stdscr.clear()
        for idx, row in enumerate(missions):
            x = max(w // 2 - len(row)//2,0)
            y = max(h // 2 - len(missions)//2 + idx,0)
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)

def start_page_of_scoreboard():
    global stdscr
    global stdscrr
    stdscr.clear()
    scoreboard = []
    with open('scoreboard.txt', 'r') as file:
        for line in file:
            mission_index, times = line.strip().split(' ', 1)
            scoreboard.append([mission_index, list(map(int, times.split(', ')))])
    for mission in scoreboard:
        mission[1].remove(0)
    scoreboard_1 = scoreboard[0:15]
    scoreboard_1.insert(0, ['Easy', ''])
    scoreboard_2 = scoreboard[15:30]
    scoreboard_2.insert(0, ['Medium', ''])
    scoreboard_3 = scoreboard[30:45]
    scoreboard_3.insert(0, ['Hard', ''])

    h, w = stdscrr.getmaxyx()
    for idx, row in enumerate(scoreboard_1):
        for i in range(len(row)):
        # 保证输出对称
            if i == 0:
                x = max(w // 2 - 40,0)
                y = max(h // 2 - len(scoreboard_1)//2 + idx,0)
            elif i == 1:
                x = max(w // 2 - 29,0)
                y = max(h // 2 - len(scoreboard_1)//2 + idx,0)
                
            stdscr.attron(curses.color_pair(4))
            stdscr.addstr(y, x, str(row[i]))
            stdscr.attroff(curses.color_pair(4))
        for idx, row in enumerate(scoreboard_2):
            for i in range(len(row)):
            # 保证输出对称

                if i == 0:
                    x = max(w // 2 - 10,0)
                    y = max(h // 2 - len(scoreboard_2)//2 + idx,0)
                elif i == 1:
                    x = max(w // 2 + 1,0)
                    y = max(h // 2 - len(scoreboard_2)//2 + idx,0)
                    
                stdscr.attron(curses.color_pair(4))
                stdscr.addstr(y, x, str(row[i]))
                stdscr.attroff(curses.color_pair(4))
        for idx, row in enumerate(scoreboard_3):
            for i in range(len(row)):
            # 保证输出对称
                if i == 0:
                    x = max(w // 2 + 20,0)
                    y = max(h // 2 - len(scoreboard_3)//2 + idx,0)
                elif i == 1:
                    x = max(w // 2 + 31,0)
                    y = max(h // 2 - len(scoreboard_3)//2 + idx,0)
                    
                stdscr.attron(curses.color_pair(4))
                stdscr.addstr(y, x, str(row[i]))
                stdscr.attroff(curses.color_pair(4))
    
    curses.flushinp()#清空输入队列
    stdscr.getch()

def scoreboard_updater(mode, mission_index, time):
    scoreboard = []
    num={"Easy":0,"Medium":1,"Hard":2}
    with open('scoreboard.txt', 'r') as file:
        for line in file:
            index, times = line.strip().split(' ', 1)
            scoreboard.append([index, list(map(int, times.split(', ')))])
    real_idx = 15 * num[mode] + mission_index - 1
    scoreboard[real_idx][1].append(time)
    scoreboard[real_idx][1].sort()
    with open('scoreboard.txt', 'w') as file:
        file.truncate(0)  #清空文件
        for mission in scoreboard:  #将更改后的列表再写入
            file.write(f"{mission[0]} {', '.join(map(str, mission[1][0:4]))}\n")
# 从startpage查看scoreboard

def start_page_of_tut():
    global stdscr
    global stdscrr
    global board
    global board1
    global board2
    global button_example
    global button_close
    global button_ShowBest
    stdscr.clear()
    stdscr.addstr(0, 0, '**Click on any block on the control panel, and the block itself and the four adjacent blocks (above, below, left, and right)')
    stdscr.addstr(2, 0, 'will change color(from white to black or from black to white).')
    stdscr.addstr(15, 0, '**You should complete the target pattern through the above-mentioned operation.')
    stdscr.addstr(17, 0, '**Each task has a limited time. If you exceed the limit time, it will be considered a failure.')
    stdscr.addstr(19, 0, '**After 5 failed attempts, you will have an opportunity to watch the best solution for one time.')
    stdscr.addstr(21, 0, '**Here is an example.')
    st_example=['Click to access an example(or press e)']
    board1=Board(board=read('base', 1))
    board2=Board(board=read('base', 2))
    board1.printf_base1()
    board2.printf_base2()
    button_example=Button(21, 20, String=st_example)
    button_example.printf() 
    
    curses.flushinp()#清空输入队列
    key = stdscr.getch()
    Mouse_control_tut=Mouse_operation_tut()
    while True:
        if key == ord('e'):
            stdscr.clear()
            board=Board(board=read('example', 1))
            board.printf()
            for i in range(board.lenth_x):
                stdscr.addstr(0, 3+6*i, str(i))
            for j in range(board.lenth_y):
                stdscr.addstr(2+3*j, 0, str(j))
            st_close=['Close(press q)']
            st_ShowBest=['Best solution(press b)']
            button_close=Button(start_x=1,start_y=board.lenth_y*12+8,String=st_close)
            button_ShowBest=Button(start_x=3,start_y=board.lenth_y*12+8,String=st_ShowBest)
            button_close.printf()
            button_ShowBest.printf()
            # Mouse_control_tut.run()
            Mouse_control_tut.start()
            Mouse_control_tut.join()
            break
        elif key == ord('q'):
            break
        elif key == curses.KEY_MOUSE:
            _, y, x, _, button = curses.getmouse()#鼠标在x行y列
            if(button_example.start_x<=x<button_example.end_x and button_example.start_y<=y<button_example.end_y):
                stdscr.clear()
                board=Board(board=read('example',1))
                board.printf()
                for i in range(board.lenth_x):
                    stdscr.addstr(0, 3+6*i, str(i))
                for j in range(board.lenth_y):
                    stdscr.addstr(2+3*j, 0, str(j))
                st_close=['Close(press q)']
                st_ShowBest=['Best solution(press b)']
                button_close=Button(start_x=1,start_y=board.lenth_y*12+8,String=st_close)
                button_ShowBest=Button(start_x=3,start_y=board.lenth_y*12+8,String=st_ShowBest)
                button_close.printf()
                button_ShowBest.printf()
                # Mouse_control_tut.run()
                Mouse_control_tut.start()
                Mouse_control_tut.join()
                break
            else:
                curses.flushinp()#清空输入队列
                key=stdscr.getch()
        else:
            curses.flushinp()#清空输入队列
            key=stdscr.getch()

def welcome():
    global stdscr
    global stdscrr
    stdscr.clear()
    welcome_txt = [' ______     ______     __    __     ______        ______     ______   ______     ______     ______   ______    ',
                   '/\  ___\   /\  __ \   /\ "-./  \   /\  ___\      /\  ___\   /\__  _\ /\  __ \   /\  == \   /\__  _\ /\  ___\   ',
                   '\ \ \__ \  \ \  __ \  \ \ \-./\ \  \ \  __\      \ \___  \  \/_/\ \/ \ \  __ \  \ \  __<   \/_/\ \/ \ \___  \  ',
                   ' \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \ \_____\     \/\_____\    \ \_\  \ \_\ \_\  \ \_\ \_\    \ \_\  \/\_____\ ',
                   '  \/_____/   \/_/\/_/   \/_/  \/_/   \/_____/      \/_____/     \/_/   \/_/\/_/   \/_/ /_/     \/_/   \/_____/ ',
                   '',
       '                                                                ',
       '                  press any button to continue...               ']
    h, w = stdscrr.getmaxyx()

    for idx, row in enumerate(welcome_txt):
        x = w // 2 - len(row)//2
        y = h // 2 - len(welcome_txt)//2 + idx
            
        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(y, x, row)
        stdscr.attroff(curses.color_pair(4))
    
    curses.flushinp()
    stdscr.getch()

def back_home():
    global stdscr
    global stdscrr
    stdscr.clear()
    goodbye_txt = [' _    _                                     _   _                 _             ___  ',
    '| |  | |                                   | | | |               | |           |__ \ ',
    '| |__| | __ ___   _____    __ _ _ __   ___ | |_| |__   ___ _ __  | |_ _ __ _   _  ) |',
    "|  __  |/ _` \ \ / / _ \  / _` | '_ \ / _ \| __| '_ \ / _ \ '__| | __| '__| | | |/ / ",
    "| |  | | (_| |\ V /  __/ | (_| | | | | (_) | |_| | | |  __/ |    | |_| |  | |_| |_|  ",
    "|_|  |_|\__,_| \_/ \___|  \__,_|_| |_|\___/ \__|_| |_|\___|_|     \__|_|   \__, (_)  ",
    "                                                                            __/ |    ",
    "                                                                           |___/     ",
    "", "", "",
    " ___  __     __      __   _   _   ___ ", "|  _| \ \   / /     / /  | \ | | |_  |",
    "| |    \ \_/ /     / /   |  \| |   | |", "| |     \   /     / /    | . ` |   | |",
    "| |      | |     / /     | |\  |   | |", "| |_     |_|    /_/      |_| \_|  _| |",
    "|___|                            |___|",]
    current_row = 0
    h, w = stdscrr.getmaxyx()

    for idx, row in enumerate(goodbye_txt):
        x = max(w // 2 - len(row)//2,0)
        y = max(h // 2 - len(goodbye_txt)//2 + idx,0)
        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(y, x, row)
        stdscr.attroff(curses.color_pair(4))
        
    curses.flushinp()#清空输入队列
    key = stdscr.getch()
    while(key!=ord('y') and key!=ord('n')):
        curses.flushinp()#清空输入队列
        key = stdscr.getch()
    if key == ord('y') or key == 89:
        stdscr.clear()
        return 1
    elif key == ord('n') or key == 78:
        stdscr.clear()
        return 0


def game_end():
    global stdscr
    global stdscrr
    stdscr.clear()
    goodbye_txt = [
    '     ______     __  __     ______        ______     __  __     ______    ',
    '    /\  == \   /\ \_\ \   /\  ___\      /\  == \   /\ \_\ \   /\  ___\   ',
    '    \ \  __<   \ \____ \  \ \  __\      \ \  __<   \ \____ \  \ \  __\   ',
    '     \ \_____\  \/\_____\  \ \_____\     \ \_____\  \/\_____\  \ \_____\ ',
    '      \/_____/   \/_____/   \/_____/      \/_____/   \/_____/   \/_____/ '
    ]
    current_row = 0
    h, w = stdscrr.getmaxyx()

    for idx, row in enumerate(goodbye_txt):
        x = max(w // 2 - len(row)//2,0)
        y = max(h // 2 - len(goodbye_txt)//2 + idx,0)
        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(y, x, row)
        stdscr.attroff(curses.color_pair(4))
        
    event = threading.Event()
    event.wait(2)

def init():
    global stdscr
    global stdscrr
    stdscrr = curses.initscr()
    stdscr = curses.newpad(1000, 1000)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(4, -1, -1)
    curses.cbreak()
    stdscr.keypad(True)
    curses.curs_set(False)
    curses.flushinp()
    curses.noecho()
    stdscr.clear()
    curses.mousemask(curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

def end():
    curses.flushinp()
    stdscr.keypad(False)
    curses.echo()
    curses.curs_set(True)
    curses.nocbreak()
    stdscr.clear()
    curses.endwin()

def read(level,num):
    map=[]
    with open(f'board/{level}/{num}','r')as file:
        for line in file:
            map.append([1-int(i) for i in line.rstrip()])
    return map

def change_stdscr(i,j):
    global stdscr
    global stdscrr
    color_=2
    if(board.board[i][j]):
        color_=1
    for x in range(3*i+2,3*i+4):
        for y in range(6*j+3,6*j+7):
            stdscr.addstr(x, y, ' ', curses.color_pair(color_))

def Egg():
    global stdscr
    global stdscrr
    stdscr.clear()
    filepath='egg_win/egg_win_'
    for i in range(1,3):
        with open(filepath+str(i), 'r') as file:
            stdscr.clear()
            content = file.read()
            stdscr.addstr(0, 0, content)
            # Refresh_pad()
            time.sleep(2.5)
    filepath='Image/ASCII-Image'
    for i in range(1,400,2):
        with open(filepath+str(i)+'.txt', 'r') as file:
            content = file.read()
            stdscr.addstr(0, 0, content)
            # Refresh_pad()
            time.sleep(0.05)

def Refresh_pad():
    global stdscrr
    global stdscr
    height, width = stdscrr.getmaxyx()
    stdscr.refresh(0,0,0,0,height-1,width-1)

def win():
    global stdscrr
    global stdscr
    stdscr.clear()
    with open('Mission_4/Kit.txt', mode = 'r') as f:
        win_txt = f.readlines()
    current_row = 0
    h, w = stdscrr.getmaxyx()
    for idx, row in enumerate(win_txt):
        x = max(w // 2 - len(row)//2,0)
        y = max(h // 2 - len(win_txt)//2 + idx,0)
            
        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(y, x, row)
        stdscr.attroff(curses.color_pair(4))
    curses.flushinp()
    stdscr.getch()

def lose():
    global stdscrr
    global stdscr
    stdscr.clear()
    with open('Mission_4/Dirk.txt', mode = 'r') as f:
        lose_txt = f.readlines()
    current_row = 0
    h, w = stdscrr.getmaxyx()
    for idx, row in enumerate(lose_txt):
        x = max(w // 2 - len(row)//2,0)
        y = max(h // 2 - len(lose_txt)//2 + idx,0)
            
        stdscr.attron(curses.color_pair(4))
        stdscr.addstr(y, x, row)
        stdscr.attroff(curses.color_pair(4))

def start_main():
    global stdscrr
    global stdscr
    return startup()

def main_main(difficulty,level):
    global stdscrr
    global stdscr
    global board
    global start_time
    global button_close
    global button_Reset
    global button_Notice
    global button_Withdraw
    global button_x
    global button_y
    global button_ShowBest
    global final
    global main_flag
    global first_flg
    first_flg=True
    stdscr.clear()
    
    board=Board(board=read(difficulty,level))
    main_flag=True
    for i in range(board.lenth_x):
        stdscr.addstr(0, 3+6*i, str(i))
    for j in range(board.lenth_y):
        stdscr.addstr(2+3*j, 0, str(j))
    st_close=['Close(press q)']
    st_reset=['Reset(press r)']
    st_ShowBest=['Best solution(press b)']
    st_withdraw=['withdraw(press w)']
    line1, line2, line3, line4, line5, line6= 'Notice: ', 'If you want to operate', 'by keyboard, please press', 'the space bar first before', 'each step and then type the', 'coordiante of the central block.'
    st_Notice = [f'{line1:<32}', f'{line2:<32}', f'{line3:<32}', f'{line4:<32}', f'{line5:<32}', f'{line6:<32}']
    st_x = ['x (row index): ']
    st_y = ['y (column index): ']
    button_close=Button(start_x=1,start_y=board.lenth_y*12+8,String=st_close)
    button_Reset=Button(start_x=3,start_y=board.lenth_y*12+8,String=st_reset)
    button_ShowBest=Button(start_x=5,start_y=board.lenth_y*12+8,String=st_ShowBest)
    button_Withdraw=Button(start_x=7,start_y=board.lenth_y*12+8,String=st_withdraw)
    button_Notice=Button(start_x=9,start_y=board.lenth_y*12+8,String=st_Notice)
    button_x=Button(start_x=16,start_y=board.lenth_y*12+8,String=st_x)
    button_y=Button(start_x=18,start_y=board.lenth_y*12+8,String=st_y)
    board.printf()
    button_close.printf()
    button_Reset.printf()
    button_ShowBest.printf()
    button_Withdraw.printf()
    button_Notice.printf()
    button_x.printf()
    button_y.printf()
    Mouse_control=Mouse_operation()
    # stdscr.addstr(0,0,'The min path is '+str(board.Min_path)+'.')
    start_time=time.time()
    Mouse_control.start()
    Mouse_control.join()
    end_time=time.time()
    total_time=-start_time+end_time
    main_flag=False
    return (final,int(total_time))
    # Screen_control.stop()


try:
    global main_flag
    global ContinueFlag
    global fail_num
    global fail_num_limit
    fail_num_limit=5
    ContinueFlag=True
    main_flag=False
    init()
    screen_control=Screen_operation()
    screen_control.start()
    welcome()
    while(True):
        mission=start_main()
        if(mission==0):break
        global limit_time
        if(mission[0]=='Easy'):limit_time=20
        elif(mission[0]=='Medium'):limit_time=40
        elif(mission[0]=='Hard'):limit_time=60
        fail_num=0
        flag=1
        while(flag):
            result=main_main(mission[0],mission[1])
            if(result[0]=='win'):
                scoreboard_updater(mission[0],mission[1],result[1])
                win()
                break
            if(result[0]=='egg_win'):
                scoreboard_updater(mission[0],mission[1],result[1])
                Egg()
                break
            fail_num+=1
            flag=back_home()
    game_end()
    # end()
    # sys.exit(0)  #正常退出程序
finally:
    ContinueFlag=False
    end()
    sys.exit(0)  #正常退出程序
