from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizUserInterface
from tkinter import Tk, messagebox
import os


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizUserInterface(quiz)


# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")


master = Tk()
master.withdraw()
messagebox.showinfo("Quiz over", f"You've completed the quiz!\nYour final score was: {quiz.score}/{quiz.question_number}")
play_again = messagebox.askquestion("Quiz", "Would you like to play again?")

if play_again == "yes":
    if os.getcwd().split('\\')[-1] == 'Quiz game (GUI)':
        os.system("python main.py")
    else:
        os.chdir("Quiz game (GUI)")
        os.system("python main.py")
        os.chdir("..")