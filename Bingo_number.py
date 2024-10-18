import tkinter as tk
import random

class Bingo:
    def __init__(self,root):
        self.root=root
        self.root.title("ビンゴの番号表示システム")
        
        self.used=set()
        self.history=[]
        
        self.label=tk.Label(root,text="",font=("Arial", 200))
        self.label.pack(pady=70)

        self.history_label=tk.Label(root,text="履歴",font=("Arial", 14))
        self.history_label.pack(pady=20)

        self.button=tk.Button(root,text="番号を出す",command=self.next,font=("Arial", 24))
        self.button.pack(pady=20)

    def next(self):
        if len(self.used)<75:
            number = random.randint(1,75)
            while number in self.used:
                number = random.randint(1,75)
            self.used.add(number)
            self.history.append(number)
            self.label.config(text=str(number))
            self.update()
        else:
            self.label.config(text="終了")

    def update(self):
        self.history_label.config(text="履歴:"+",".join(map(str, self.history)))

if __name__=="__main__":
    root=tk.Tk()
    application=Bingo(root)
    root.mainloop()

