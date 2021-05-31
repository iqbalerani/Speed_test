from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer
import random

root = Tk()
root.geometry("500x500")
root.config(bg="Black")

window = Tk()
window.geometry("550x550")
window.withdraw()

hs_file = open('highscore.txt', 'r+')
x=0

def game():
    global x
    if x == 0:
        root.withdraw()
        x = x+1
    window.deiconify()
    def check_result():
        j = error = 0
        answer = entry.get("1.0", 'end-1c')
        end = timer()
        time_taken = end - start
        #len diff
        if len(words[word]) >= len(answer):
            error = len(words[word])-len(answer)
            for i in answer: #take shorter sentence
                if i == words[word][j]:
                    pass
                else:
                    error+=1
                j+=1
        wpm = len(answer)/5
        wpm = wpm - error
        wpm = int(wpm/(time_taken/60))
        hs_file.seek(0)
        line = int(hs_file.readline())
        if wpm > line:
            hs_file.seek(0)
            hs_file.write(str(wpm))
            result = "Amazing! Your highscore is: "+str(wpm)+" WPM"
            messagebox.showinfo("Score", result)
        else:
            result = f"Your score is: {str(wpm)} WPM\nBetter luck next time!"
            messagebox.showinfo("Score", result)

    def finish():
        hs_file.close()
        window.destroy()
        root.destroy()

    words=["Lary is kind of kind maybe", "Tom is coming here.", "kids are not playing."]
    #words = ["Commenting on the government's 10 Billion Tree Tsunami Programme, PM Imran said that one billion trees have been planted since 2018. 'Nurseries have been created and we are hopeful that we will complete our goal by 2023,' he said, adding that this will also have an impact on people's livelihoods and on tourism."]
    word = random.randint(0, len(words)-1)


    x2 = Label(window, text=words[word], bg="black", fg="white", height=7, width=47, )
    x2.place(x=15, y=10)

    x3 = Button(window, text="Submit!", font="times 20", bg="#fc2828", command=check_result)
    x3.place(x=220, y=350)

    entry = Text(window)
    entry.place(x=100, y=180, height=150, width=350)

    b2 = Button(window, text="Done", font="times 13", bg="#ffc003", width=12, command=finish)
    b2.place(x=155, y=420)

    start = timer()

    window.mainloop()


x1 = Label(root, text="Lets test your typing speed!", bg="black", fg="white", font="times 20")
x1.place(x=100, y=50)

b1 = Button(root, text="Go!", width=12, bg='#fcba03', font='times 20', command=game)
b1.place(x=150, y=120)

hs_text = Label(root, text="Highscore", width=12, bg='#03fcf8', font="times 35")
hs_text.place(x=90, y=240)

hs = int(hs_file.readline())
hs_val = Label(root, text=str(hs)+" WPM", width=12, fg="#03fcf8", bg='black', font='times 30')
hs_val.place(x=110, y=320)


root.mainloop()


