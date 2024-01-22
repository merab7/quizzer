from tkinter import*

THEME_COLOR = "#375362"

class QuizInTerface:
    def __init__(self) -> None:
         self.window = Tk()
         self.window.title("Quizzer")
         self.window.config(padx=20, pady=20, bg=THEME_COLOR)
         self.score_label = Label(text=f"score: ", bg=THEME_COLOR, font=("white", 16))
         self.score_label.grid(row=0, column=1)
         self.board = Canvas(bg="white", height=250, width=300)
         self.question_text = self.board.create_text(150, 125, text="Some question text", font=("Areal", 20, "italic"))
         self.board.grid(row=1, column=0,  columnspan=2, pady=50)
         self.x_img = PhotoImage(file ="./images/false.png")
         self.x_btn = Button(image=self.x_img, highlightthickness=0)
         self.x_btn.grid(row=2, column=0)
         self.true_img = PhotoImage(file = "./images/true.png")
         self.true_btn = Button(image=self.true_img, highlightthickness=0)
         self.true_btn.grid(row=2, column=1)
         
           
       





         self.window.mainloop()
    


