THEME_COLOR = "#375362"
from cgitb import text
from tkinter import Label
from numpy import pad
from window import Window
from tkinter import *
from quiz_brain import QuizBrain

class QuizlerInterface:
   
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.win = Window(340,510,"Quizler")
        self.win.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_lable = Label(text="Score: 0", bg=THEME_COLOR, font=("Arial", 15))
        self.score_lable.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white", border=0, highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,  text="Quiz question goes HERE", width=250, font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false_img = PhotoImage(file="../pythonAdvanced/quizzler-app-start/images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, border=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=0)
        
        true_img = PhotoImage(file="../pythonAdvanced/quizzler-app-start/images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, border=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=1)

        self.next_quiz_question()
        self.win.mainloop()
        
    def next_quiz_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_lable.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')
        self.win.after(1500, self.next_quiz_question)



