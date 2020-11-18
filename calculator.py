import tkinter as tk

root=tk.Tk()

canvas=tk.Canvas(root,height=500,width=300,bg="green")
canvas.pack()
frame1=tk.Frame(canvas,bg="white")
frame1.place(relwidth=0.9,relheight=0.15,relx=0.05,rely=0.05)
frame2=tk.Frame(canvas,bg="yellow")
frame2.place(relwidth=0.9,relx=0.05,relheight=0.75,rely=0.23)

operator=""
text_input=tk.StringVar()
class but:
    def __init__(self,relx,rely,text,):
        self.relx=relx
        self.rely=rely
        self.text=text
        if text=="=":
            self.btn=tk.Button(frame2,bd=5,text=self.text,font=60,command=lambda:self.com(self.text))
            self.btn.place(relheight=0.2,relwidth=1,relx=self.relx,rely=self.rely)
        else:
            self.btn=tk.Button(frame2,bd=5,text=self.text,font=40,command=lambda:self.com(self.text))
            self.btn.place(relheight=0.2,relwidth=0.25,relx=self.relx,rely=self.rely)  
        
    def com(self,text):
        if text=="C":
            global operator
            operator=""
            text_input.set("")
            lable=tk.Label(frame1,font=40,textvariable=text_input,bg="white")
            lable.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
        elif text=="=":
            sum=str(eval(operator))
            text_input.set(sum)
        else:
            operator=operator+str(self.text)
            text_input.set(operator)
            lable=tk.Label(frame1,font=40,textvariable=text_input,bg="white")
            lable.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

lab=but(0,0,1)
lab=but(0.25,0,2)
lab=but(0.5,0,3)
lab=but(0.75,0,"+")
lab=but(0,0.2,4)
lab=but(0.25,0.2,5)
lab=but(0.5,0.2,6)
lab=but(0.75,0.2,"-")
lab=but(0,0.4,7)
lab=but(0.25,0.4,8)
lab=but(0.5,0.4,9)
lab=but(0.75,0.4,"*")
lab=but(0,0.6,0)
lab=but(0.25,0.6,"C")
lab=but(0.5,0.6,"%")
lab=but(0.75,0.6,"/")
lab=but(0.0,0.8,"=")

tk.mainloop()