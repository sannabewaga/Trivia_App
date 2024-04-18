from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"




class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window =Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg= THEME_COLOR)
        self.canvas = Canvas(width=300,height=250)
        self.canvas_text = self.canvas.create_text(150,125,text="something soemhting",font = ("Ariel",10,"italic"),width = 270)
        self.canvas.grid(row = 1, column = 0, columnspan = 2)

        self.label = Label(text= f"Score: {self.quiz.score}", bg=THEME_COLOR, pady=20)
        self.label.grid(row = 0, column = 1)
        true_image = PhotoImage(file = "images/true.png")
        self.button_true = Button(image=true_image,command=self.right_pressed)
        self.button_true.grid(row = 2 , column = 0,padx=30,pady=30)
        false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_image, command=self.wrong_pressed)
        self.button_false.grid(row=2, column=1, padx=30, pady=30)
        self.get_next_q()

        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg = "white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text,text = q_text)
        else:
            self.canvas.itemconfig(self.canvas_text,text="QUIZ HAS ENDED")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")
    def right_pressed(self):
        right =self.quiz.check_answer("True")

        if right:
            self.canvas.config(bg= "green")
            self.quiz.score+=1
            self.label.config(text=f"Score: {self.quiz.score}")


        else:
            self.canvas.config(bg="red")
        self.window.after(1000,func=self.update)
    def wrong_pressed(self):
        right =self.quiz.check_answer("False")
        if right:
            self.canvas.config(bg= "green")
            self.quiz.score+=1
            self.label.config(text=f"Score: {self.quiz.score}")


        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.update)

    def update(self):
        self.canvas.config(bg="white")
        self.get_next_q()
