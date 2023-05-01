from tkinter import *
from tkmacosx import *
from time import *

class BLabel(object):
    b = "•"
    def __init__(self,master):
        self.l = Label(master, font="Lato 25")
    def add_option(self,text):
        if self.l.cget("text") == "":
            self.l.config(text=self.b+" "+text)
        else:
            self.l.config(text=self.l.cget("text") +"\n"+ self.b + " "+text)

class Question():
    def __init__(self, service, text, options, answer, explanation, others):
        self.service = service
        self.text = text
        self.options = options
        self.answer = answer
        self.explanation = explanation
        self.others = others


class Game():

    def click(self, event):
        x, y = event.x, event.y
        self.clickAt = self.canvasToGame((x,y))
        self.clicking.set(1)


    def __init__(self):
        self.window = Tk()
        self.window.geometry("1500x1000")
        question1 = Question("Meta (Facebook)",
                             "Guess which of these is included in the Meta terms of service?",
                             ["Meta can store your data even if you don't have an account",
                              "You can't sue Meta",
                              "Meta owns the intellectual property rights to anything you post",
                              "Meta can prevent users from leaving the site"], 0,
                             "Collecting user data even if user's haven't officially registered is fairly common. Many sites will have you sign their TOS's just to interact with their service and can thus immediatley begin collecting your data.",
                             ["Instagram", "Google"])
        question2 = Question("Reddit",
                             "Guess which of these is included in the Reddit terms of service?",
                             ["Reddit owns all data collected about you",
                              "Reddit can give 3rd parties access to your personal info",
                              "You forfeit your moral rights while using reddit",
                              "Reddit can store your data even if you don't have an account"], 2,
                             "Moral rights refers to your ownership of the work you author. it’s the right of authors to receive all non-monetary value from their work. It includes your right to receive credit for your work, to prevent your work from being altered without your permission, and to control who owns the work. Since moral rights are non-monetary, services can’t sell your work, but they can modify and distribute it without crediting you.",
                             ["Paypal", "Blizzard", "Spodify"])
        question3 = Question("Youtube",
                             "Guess which of these is included in the Youtube terms of service?",
                             ["Youtube can give 3rd parties access to your personal info",
                              "Youtube has the exclusive right to distribute content posted on it",
                              "You waive the right to sue Youtube",
                              "Youtube can keep deleted content"], 3,
                             "Just because you delete something doesn't mean it actually goes away. Services have no obligation to tell you if they are actually deleting content you want deleted, and in many cases content can persist long after the user tries to destroy it.",
                             ["Meta", "Paypal", "Pintrest", "Instagram", "Google"])
        question4 = Question("Uber",
                             "Guess which of these is included in the Uber terms of service?",
                             ["Uber can collect information about you even if you don't have an account",
                              "Uber will not disclose what data it has collected about a user",
                              "You waive the right to sue Uber",
                              "Uber can modify the terms of service without notifying users"], 2,
                             "Many TOS’s take away a users right to sue the service over disputes. Instead these services force disputes to be settled by private arbitration. This is good for the companies because it is generally faster and gives them more control over outcomes. However this can negatively affect consumers since It is more costly than legal action and has no appeal process.",
                             ["Tiktok", "Spodify", "Amazon", "Minecraft", "Microsoft"])
        question5 = Question("Google",
                             "Guess which of these is included in the Google terms of service?",
                             ["You can't express negative opinions about Google",
                              "Google owns any data they collect about you",
                              "You waive the right to sue Google",
                              "Google can modify the terms of service without notifying users"], 0,
                             "While this type of clause is fairly uncommon and questionably legal. Services still put langauge in TOS's that prevent users from sharing negative opinions about the service.",
                             ["Intel"])
        question6 = Question("Apple",
                             "Guess which of these is included in the Apple terms of service?",
                             ["Apple can track you even if you use Do Not Track headers",
                              "You can't express negative opinions about Apple",
                              "Apple can sell your personal data",
                              "You can't sue apple for more than $50"], 3,
                             "Many services put caps on the amount of they can be sued for. Usually this cap is equal to fees paid by the user and not a set value like in the case of Apple. These caps are generally legally enforcable in any case where the liability due is not extremely different from the cap.",
                             ["Google","Spodify","Paypal","Amazon","Instagram","Minecraft"])
        question7 = Question("Instagram",
                             "Guess which of these is included in the Instagram terms of service?",
                             ["Instagram can sell your data to 3rd parties",
                              "Instagram can create derivative works based on your content",
                              "Instagram can modify the terms of service without notifying users",
                              "Instagram owns user data collected from you"], 1,
                             "Some services include language to give them near complete control of anything you put on their site. Part of this control is the right to create derivative works, but it also includes a \'non-exclusive, royalty-free, transferable, sub-licensable, worldwide license to host, use, distribute, modify, run, copy, publicly perform or display, and translate\' any works published on the service.",
                             ["Meta"])
        question8 = Question("Amazon",
                             "Guess which of these is included in the Amazon terms of service?",
                             ["Amazon owns user data collected from you",
                              "Amazon can view your browser history.",
                              "Amazon can modify the terms of service without notifying users",
                              "Amazon isn't liable for any harm caused by the service"], 2,
                             "Services claim the right to change their terms without notification. However, several court cases have ruled that this practice is not legal and that new changes are not binding. While these clauses may not be enforceable in some cases, large services are still including them indicating that they shouldn’t be ignored.",
                             ["Apple"])
        question10 = Question("Tiktok",
                              "Guess which of these is included in the Tiktok terms of service?",
                              ["Tiktok can view your browser history",
                               "Tiktok owns user data collected from you",
                               "Tiktok can sell your data to 3rd parties",
                               "Tiktok can track you on other services"], 2,
                              "Many services sell your data to 3rd parties. It's one of the big things to look out for in TOS agreements because it's so widely done.",
                              ["Apple","Amazon","Spodify","Meta","Instagram", "Minecraft"])

        question9 = Question("Microsoft",
                             "Guess which of these is included in the Microsoft terms of service?",
                             ["Microsoft can view your browser history",
                              "Microsoft can sell your personal data to 3rd parties",
                              "Microsoft isn't liable for any harm caused by the service",
                              "Microsoft can track you even if you use Do Not Track headers"], 3,
                             "Using tools like private browsing does not always protect you from services collecting your data. DNT (Do Not Track) headers arn't legally enforceable so some services ignore them.",
                             ["Tiktok","Paypal","Reddit","Minecraft"])
        question11 = Question("Google (again)",
                             "Guess which of these is also included in the Google terms of service?",
                             ["Google can read your private emails",
                              "Google can view your browser history",
                              "Google can use your identy in ads targeted at other users",
                              "Google can track you on other services"], 5,
                             "While not necessarily the worst, Google's TOS covers a lot and is a good example of the broad abuses of user privacy that can be included in TOS agreements. It’s a reminder that signing away your rights isn’t something you do every once in a while to access some piece of software, it’s something you do every day and in many cases have no choice about.",
                             ["Meta"])
        self.questions = [question1, question2, question3, question5, question4, question6, question7, question8, question9, question10, question11]
        self.score = 0
        self.startScreen()




    def start(self):
        # self.startButton.config(relief=SUNKEN)
        # self.startButton.after(200, lambda: self.startButton.config(relief=RAISED))
        self.question(0)

    def question(self, num):
        self.clear()
        print("question")
        question = self.questions[num]
        l = Label(text=question.service, font="Lato 80 bold")
        l.place(relx=.5, anchor=CENTER, y=140)
        l = Label(text=question.text, font="Lato 40")
        l.place(relx=.5, anchor=CENTER, y=210)
        Button(self.window,
               text=question.options[0], activebackground="black",
               command=lambda: self.description(num, 0), height=70,
               width=800, font="Lato 25").place(relx=.5, anchor=CENTER, y=300 + 0 * 70)
        Button(self.window,
               text=question.options[1], activebackground="black",
               command=lambda: self.description(num, 1), height=70,
               width=800, font="Lato 25").place(relx=.5, anchor=CENTER, y=300 + 1 * 70)
        Button(self.window,
               text=question.options[2], activebackground="black",
               command=lambda: self.description(num, 2), height=70,
               width=800, font="Lato 25").place(relx=.5, anchor=CENTER, y=300 + 2 * 70)
        Button(self.window,
               text=question.options[3], activebackground="black",
               command=lambda: self.description(num, 3), height=70,
               width=800, font="Lato 25").place(relx=.5, anchor=CENTER, y=300 + 3 * 70)
        self.header(num)
        self.sides()
        self.window.mainloop()

    def header(self, num):
        l = Label(text='', bg='sky blue', height=4, relief="raised")
        l.pack(side="top", fill="x")
        l = Label(text="TOS The Game: Question " + str(num + 1), font="Lato 48 bold", bg='sky blue')
        l.place(relx=.5, anchor=CENTER, y=35)
        l = Label(text="Score " + str(self.score) + "/" + str(len(self.questions)), font="Lato 40",  bg='sky blue')
        l.place(relx=.93, anchor=CENTER, y=35)
        self.resetButton = Button(self.window,
                                  text="Reset", activebackground="black",
                                  command=self.startScreen, height=60, width=200, font="Lato 25",
                                  bg='sky blue', highlightbackground="sky blue")
        self.resetButton.place(relx=0, y=35, anchor=W)

    def sides(self):
        l = Label(text='', bg='royalblue1', width=15)
        l.pack(side="left", fill="y")
        l = Label(text='', bg='royalblue1', width=15)
        l.pack(side="right", fill="y")
        l = Label(text='', bg='black', width=1, font= "Times 1")
        l.pack(side="left", fill="y")
        l = Label(text='', bg='black', width=1, font= "Times 1")
        l.pack(side="right", fill="y")

    def description(self, num, guess):
        self.clear()
        print("description", guess)

        question = self.questions[num]
        l = Label(text=question.service, font="Lato 80 bold")
        l.place(relx=.5, anchor=CENTER, y=140)
        l = Label(text=question.text, font="Lato 40")
        l.place(relx=.5, anchor=CENTER, y=210)
        self.score += 1
        for i in range(4):

            if i == question.answer or question.answer==5:

                button = Button(self.window,
                                text=question.options[i], activebackground="black",
                                height=70, width=800, font="Lato 25", bg="lime")
                button.place(relx=.5, anchor=CENTER, y=300 + i * 70)
            elif i == guess:
                self.score -= 1
                button = Button(self.window,
                                text=question.options[i], activebackground="black",
                                height=70, width=800, font="Lato 25", bg="red")
                button.place(relx=.5, anchor=CENTER, y=300 + i * 70)
            else:
                button = Button(self.window,
                                text=question.options[i], activebackground="black",
                                height=70, width=800, font="Lato 25")
                button.place(relx=.5, anchor=CENTER, y=300 + i * 70)


        self.header(num)
        self.sides()
        l = Text(font="Lato 25", wrap=WORD, width=60)
        l.tag_configure("center", justify='center')
        l.insert(END, question.explanation)
        l.tag_add("center", "1.0", "end")
        l.place(relx=0.5, anchor=CENTER, y=900)

        l = Label(text="Services with similar features:", font="Lato 25 bold")
        l.place(relx=.5, anchor=CENTER, y=725)
        if len(question.others)>4:
            b = BLabel(master=self.window)
            i=0
            for i in range(4):
                b.add_option(question.others[i])
            b.l.place(relx=0.45, anchor=N, y=740)
            b = BLabel(master=self.window)
            for i in range(4,len(question.others)):
                b.add_option(question.others[i])
            b.l.place(relx=0.55, anchor=N, y=740)
        else:
            b = BLabel(master=self.window)
            for i in question.others:
                b.add_option(i)
            b.l.place(relx=0.5, anchor=N, y=740)

        if num+1 == len(self.questions):
            button = Button(self.window,
                                      text="Return To Start", activebackground="black",
                                      command=self.startScreen, height=60, width=300, font="Lato 25")
            button.place(relx=0.5, anchor=CENTER, y=900)
        else:
            button = Button(self.window,
                            text="Next Question", activebackground="black",
                            command=lambda: self.question(num + 1), height=60, width=300, font="Lato 25")
            button.place(relx=0.5, anchor=CENTER, y=900)
        self.window.mainloop()

    def endScreen(self):
        self.clear()
        print("end")

    def startScreen(self):
        self.clear()
        self.score = 0
        l = Label(text="TOS, The Game", font = "Lato 100 bold", bg="sky blue", relief="raised")
        l.pack(side="top", fill="x")
        l = Label(text="This game is designed to test how well you actually read the TOS agreements of services you probably signed up for",
                  font="Lato 40")
        l = Text(font="Lato 30", wrap=WORD, width=50)
        l.tag_configure("center", justify='center')
        l.insert(END, "This game is designed to test how well you actually read the TOS (Terms Of Service) agreements of services you've probably signed up for. "
                      +" You'll be asked a series of questions about what is or isn't included in the TOS agreements of common services."
                       +" The game will also give you a brief explanation of why it's included and will list other services with similar features in their TOS's.")
        l.tag_add("center", "1.0", "end")
        l.place(relx=0.5, anchor=CENTER, y=600)
        self.startButton = Button(self.window,
               text="Start", activebackground="black",
               command=self.start, height=100, width=500, font = "Lato 60")
        self.startButton.place(relx=.5, rely=.5, anchor=CENTER)
        self.sides()
        self.window.mainloop()

    def clear(self):
        for widget in self.window.winfo_children():
            widget.destroy()


if __name__ == '__main__':
    game1 =  Game()