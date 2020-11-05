from tkinter import *
import tkinter.font as font

win = Tk()
win.geometry('600x500')
win.title('COLOR GUESSING GAME')

colors = ['RED','BLUE','BLACK','BROWN','WHITE','YELLOW','GREEN','PINK','PURPLE','VIOLET','ORANGE']
helv40 = font.Font(family='Helvetica',size=24,weight='bold')
ar12 = font.Font(family='Arial',size=13,weight='bold')
bottom_frame = Frame(win)
bottom_frame.pack(side=BOTTOM)
bottom_frame1 = Frame(win)
bottom_frame1.pack(side=BOTTOM)

game_description="\nGame Description: Enter the color of the word displayed below\nNote: Don't enter the text itself"
header = Label(win,text='\nCOLOR GUESSING GAME',fg='RED',font=helv40)
header.pack(side=TOP)

sub_header=Label(win,text='\nWelcome to the game',font=font.Font(family='Arial',size=16,weight='bold'))
sub_header.pack()

des = Label(win,text=game_description,fg='grey',font=ar12)
des.pack()

game_score = Label(win,text='\nYour Score: '+ str(),fg='green',font=font.Font(family='Helvetica',size=18,weight='bold'))
game_score.pack()

game_time=Label(win,text='\nTime left: ',font=font.Font(family='Helvetica',size=18,weight='bold'),fg='blue')
game_time.pack()

entry = Entry(win,width=14,font=font.Font(family='Helvetica',size=14),justify='center')
entry.pack(pady=15,ipady=2)

start = Button(bottom_frame,text='Start',width=7,font=font.Font(family='Arial',size=16),fg='red')
reset = Button(bottom_frame,text='Reset',width=7,font=font.Font(family='Arial',size=16),fg='green')
start.pack(side=LEFT,pady=10)
reset.pack(side=LEFT,pady=10)

win.mainloop()