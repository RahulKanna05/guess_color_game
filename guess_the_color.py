from tkinter import *
import tkinter.font as font
import random

colors = ['RED','BLUE','BLACK','BROWN','WHITE','YELLOW','GREEN','PINK','PURPLE','VIOLET','ORANGE']
timer = 60
score = 0
displayed_word_color = ''

def start_game():
    global displayed_word_color
    if(timer==60):
        start_countdown()
        displayed_word_color = random.choice(colors).lower()
        word = random.choice(colors)
        display_word.config(text=word,fg=displayed_word_color)
        entry.bind('<Return>',display_next_word)
        
def start_countdown():
    global timer
    if(timer>=0):
        game_time.config(text='Time left: '+str(timer)+'s')
        timer-=1
        game_time.after(1000,start_countdown)
        if(timer==-1):
            game_time.config(text="Game Over!!!")

def display_next_word(event):
    global displayed_word_color,score,timer
    if timer >0:
        if displayed_word_color == entry.get().lower():
            score +=1
            game_score.config(text='Your Score: '+ str(score))
        entry.delete(0,END)
        displayed_word_color = random.choice(colors).lower()
        word = random.choice(colors)
        display_word.config(text=word, fg=displayed_word_color)

def reset_game():
    global timer,score,displayed_word_color
    timer = 60
    score = 0
    displayed_word_color = ''
    game_score.config(text='Your Score: ' + str(score))
    display_word.config(text='')
    game_time.config(text='Time Left: -')
    entry.delete(0,END)

win = Tk()
win.geometry('600x550')
win.title('COLOR GUESSING GAME')


helv40 = font.Font(family='Helvetica',size=24,weight='bold')
ar12 = font.Font(family='Arial',size=13,weight='bold')
bottom_frame = Frame(win)
bottom_frame.pack(side=BOTTOM)

game_description="\nGame Description: Enter the color of the word displayed below\nNote: Don't enter the text itself"
header = Label(win,text='\nCOLOR GUESSING GAME',fg='RED',font=helv40)
header.pack(side=TOP)

sub_header=Label(win,text='\nWelcome to the game',font=font.Font(family='Arial',size=16,weight='bold'))
sub_header.pack()

des = Label(win,text=game_description,fg='grey',font=ar12)
des.pack()

game_score = Label(win,text='Your Score: '+ str(score),fg='green',font=font.Font(family='Helvetica',size=18,weight='bold'))
game_score.pack(pady=10)

display_word = Label(win,font=font.Font(family='Helvetica',size=16))
display_word.pack()

game_time=Label(win,text='Time left: -',font=font.Font(family='Helvetica',size=18,weight='bold'),fg='blue')
game_time.pack(pady=10)

entry = Entry(win,width=14,font=font.Font(family='Helvetica',size=14),justify='center')
entry.pack(pady=15,ipady=2)

start = Button(bottom_frame,text='Start',width=7,font=font.Font(family='Arial',size=16),fg='red',command=start_game)
reset = Button(bottom_frame,text='Reset',width=7,font=font.Font(family='Arial',size=16),fg='green',command=reset_game)
start.pack(side=LEFT,pady=10)
reset.pack(side=LEFT,pady=10)

win.mainloop()