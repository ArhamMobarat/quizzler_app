from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20,"italic")



class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR ,padx=20 ,pady=20)


        self.label = Label(text=f"Score: {self.quiz.score}",bg=THEME_COLOR,fg="White")
        self.label.grid(column=1,row= 0,)

        self.canvas = Canvas(width=300,height=250)
        self.question = self.canvas.create_text(
            150,
            125,
            width= 280,
            text="The question goes here",
            font=FONT)
        self.canvas.grid(column= 0,row= 1,columnspan=2,pady= 50)


        self.correct_image = PhotoImage(file="images/true.png")
        self.correct_button =Button(image=self.correct_image,command=self.true)
        self.correct_button.grid(column= 0,row= 2)

        self.incorrect_image = PhotoImage(file="images/false.png")
        self.incorrect_button = Button(image=self.incorrect_image,command=self.wrong)
        self.incorrect_button.grid(column= 1,row= 2)
        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.update()
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=quiz_text)
        else:
            self.canvas.itemconfig(self.question,text="You've reached the end of the quiz.")
            self.correct_button.config(state= "disabled")
            self.incorrect_button.config(state= "disabled")


    def true(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.update()
        else:
            self.canvas.config(bg="red")
            self.canvas.update()
        self.window.after(1000,self.next_question)
