from tkinter import *
from tkinter import ttk
from tkinter import messagebox

screen = Tk()
screen.title("Student Grading System")
screen.configure(bg="pink")
frame = Frame(screen,bg="pink")
screen.geometry("500x500")
screen.resizable(False,False)
label = Label(screen,text="Student Grading System",fg='yellow',bg='green',font=('Calibri',25,'bold'),width='200',height='1')
label.pack()
frame.pack()


def is_valid_roll_number(roll_number):
    try:
        roll_number = int(roll_number)
        if roll_number < 1:
            return False
        return True
    except ValueError:
        return False

def is_valid_score(score):
    try:
        score = int(score)
        if 0 <= score <= 100:
            return True
        return False
    except ValueError:
        return False


def enter_data():
    global sec_no
    global stu_name
    global stu_class
    global sub_1
    global sub_2
    global sub_3
    global sub_4
    global sub_5
    global sub_6
    global sum  
    global average
    global first 
    global remarks
    
    rollno = int(entry_1.get())
    if not is_valid_roll_number(rollno):
        messagebox.showerror("Error", "Invalid roll number. Please enter a valid integer roll number.")
        return
    
    name = entry_2.get()
    clas = entry_3.get()
    telugu = int(entry_4.get())
    hindi = int(entry_5.get())
    english = int(entry_6.get())
    maths = int(entry_7.get())
    science = int(entry_8.get())
    social = int(entry_9.get())
    total = telugu + hindi + english + maths + science + social 
    avg = total / 6
    decimal_value = round(avg,2)
    
    
    
    if not all(is_valid_score(score) for score in [telugu, hindi, english, maths, science, social]):
        messagebox.showerror("Error", "Invalid subject scores. Please enter valid integer scores between 0 and 100.")
        return
    
    sec_no = Label(label_frame_2,text=f"{rollno}",bg="pink",fg="red")
    sec_no.grid(row=0,column=1)
    
    stu_name = Label(label_frame_2,text=f"{name}",bg="pink",fg="red")
    stu_name.grid(row=1,column=1)
    
    stu_class = Label(label_frame_2,text=f"{clas}",bg="pink",fg="red")
    stu_class.grid(row=2,column=1)
    
    sub_1 = Label(label_frame_2,text=f"{telugu}",bg="pink",fg="red")
    sub_1.grid(row=3,column=1)
    
    sub_2 = Label(label_frame_2,text=f"{hindi}",bg="pink",fg="red")
    sub_2.grid(row=4,column=1)
    
    sub_3 = Label(label_frame_2,text=f"{english}",bg="pink",fg="red")
    sub_3.grid(row=5,column=1)
    
    sub_4 = Label(label_frame_2,text=f"{maths}",bg="pink",fg="red")
    sub_4.grid(row=6,column=1)
    
    sub_5 = Label(label_frame_2,text=f"{science}",bg="pink",fg="red")
    sub_5.grid(row=7,column=1)
    
    sub_6 = Label(label_frame_2,text=f"{social}",bg="pink",fg="red")
    sub_6.grid(row=8,column=1)
    
    sum = Label(label_frame_3,text=f"{total}",bg="pink",fg="red")
    sum.grid(row=0,column=1)
    
    average = Label(label_frame_3,text=f"{decimal_value}",bg="pink",fg="red")
    average.grid(row=2,column=1)
    
    
    
    if(total >= 510):
        first = Label(label_frame_3,text="A",bg="pink",fg="red")
        first.grid(row=1,column=1)
        remarks = Label(label_frame_3,text="Excellent",bg="pink",fg="red")
        remarks.grid(row=3,column=1)
    elif(total >= 450):
        first = Label(label_frame_3,text="B",bg="pink",fg="red")
        first.grid(row=1,column=1)
        remarks = Label(label_frame_3,text="Not Bad",bg="pink",fg="red")
        remarks.grid(row=3,column=1)
    elif(total >= 360):
        first = Label(label_frame_3,text="C",bg="pink",fg="blue")
        first.grid(row=1,column=1)
        remarks = Label(label_frame_3,text="Need To Improve",bg="pink",fg="red")
        remarks.grid(row=3,column=1)
    elif(total >= 260):
        first = Label(label_frame_3,text="D",bg="pink",fg="red")
        first.grid(row=1,column=1)
        remarks = Label(label_frame_3,text="Better Luck Next Time",bg="pink",fg="red")
        remarks.grid(row=3,column=1)
    else:
        first = Label(label_frame_3,text="")
        first.grid(row=1,column=1)
        remarks = Label(label_frame_3,text="")
        remarks.grid(row=3,column=1)
    messagebox.showinfo("Info","Grade Generated Successfully")
           
def clear_elements():
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    entry_3.delete(0,END)
    entry_4.delete(0,END)
    entry_5.delete(0,END)
    entry_6.delete(0,END)
    entry_7.delete(0,END)
    entry_8.delete(0,END)
    entry_9.delete(0,END)
    sec_no.config(text="")
    stu_name.config(text="")
    stu_class.config(text="")
    sub_1.config(text="")
    sub_2.config(text="")
    sub_3.config(text="")
    sub_4.config(text="")
    sub_5.config(text="")
    sub_6.config(text="")
    sum.config(text="")
    average.config(text="")
    first.config(text="")
    remarks.config(text="")
    messagebox.showinfo("Info","All Fields Cleared Successfully")
    
    
label_frame_1 = LabelFrame(frame,text="Student Information",bg='pink',fg="blue")
label_frame_1.grid(row=0,column=0)

label_1 = Label(label_frame_1,text="Roll-No:",bg="pink",fg="blue")
label_1.grid(row=0,column=0)

label_2 = Label(label_frame_1,text="Name:",bg="pink",fg="blue")
label_2.grid(row=1,column=0)

label_3 = Label(label_frame_1,text="Class:",bg="pink",fg="blue")
label_3.grid(row=2,column=0)

label_4 = Label(label_frame_1,text="Telugu:",bg="pink",fg="blue")
label_4.grid(row=3,column=0)

label_5 = Label(label_frame_1,text="Hindi:",bg="pink",fg="blue")
label_5.grid(row=4,column=0)

label_6 = Label(label_frame_1,text="English:",bg="pink",fg="blue")
label_6.grid(row=5,column=0)

label_7 = Label(label_frame_1,text="Maths:",bg="pink",fg="blue")
label_7.grid(row=6,column=0)

label_8 = Label(label_frame_1,text="Science:",bg="pink",fg="blue")
label_8.grid(row=7,column=0)

label_9 = Label(label_frame_1,text="Social:",bg="pink",fg="blue")
label_9.grid(row=8,column=0)

entry_1 = Entry(label_frame_1)
entry_1.grid(row=0,column=1)

entry_2 = Entry(label_frame_1)
entry_2.grid(row=1,column=1)

entry_3 = ttk.Combobox(label_frame_1,values=[1,2,3,4,5,6,7,8,9,10],width=17)
entry_3.grid(row=2,column=1)

entry_4 = Entry(label_frame_1)
entry_4.grid(row=3,column=1)

entry_5 = Entry(label_frame_1)
entry_5.grid(row=4,column=1)

entry_6 = Entry(label_frame_1)
entry_6.grid(row=5,column=1)

entry_7 = Entry(label_frame_1)
entry_7.grid(row=6,column=1)

entry_8 = Entry(label_frame_1)
entry_8.grid(row=7,column=1)

entry_9 = Entry(label_frame_1)
entry_9.grid(row=8,column=1)

for widgets in label_frame_1.winfo_children():
    widgets.grid_configure(padx=10,pady=5)
    
# Label Frame -2

label_frame_2 = LabelFrame(frame,text="Grade/Percentage/Total",bg="pink")
label_frame_2.grid(row=0,column=1)

label_a = Label(label_frame_2,text="Roll-No:",bg="pink",fg="blue")
label_a.grid(row=0,column=0)

label_b = Label(label_frame_2,text="Name:",bg="pink",fg="blue")
label_b.grid(row=1,column=0)

label_c = Label(label_frame_2,text="Class:",bg="pink",fg="blue")
label_c.grid(row=2,column=0)

label_d = Label(label_frame_2,text="Telugu:",bg="pink",fg="blue")
label_d.grid(row=3,column=0)

label_e = Label(label_frame_2,text="Hindi:",bg="pink",fg="blue")
label_e.grid(row=4,column=0)

label_f = Label(label_frame_2,text="English:",bg="pink",fg="blue")
label_f.grid(row=5,column=0)

label_g = Label(label_frame_2,text="Maths:",bg="pink",fg="blue")
label_g.grid(row=6,column=0)

label_h = Label(label_frame_2,text="Science:",bg="pink",fg="blue")
label_h.grid(row=7,column=0)

label_i = Label(label_frame_2,text="Social:",bg="pink",fg="blue")
label_i.grid(row=8,column=0)

for widgets in label_frame_2.winfo_children():
    widgets.grid_configure(padx=10,pady=5)

label_frame_3 = LabelFrame(frame,text="Percentage/Grade/Total",bg="pink",fg="blue")
label_frame_3.grid(row=1,column=0,sticky='EW',pady=10)

label_j = Label(label_frame_3,text="Total:",bg="pink",fg="blue")
label_j.grid(row=0,column=0)

label_k = Label(label_frame_3,text="Grade:",bg="pink",fg="blue")
label_k.grid(row=1,column=0)

label_l = Label(label_frame_3,text="Percentage:",bg="pink",fg="blue")
label_l.grid(row=2,column=0)

label_m = Label(label_frame_3,text="Remarks:",bg="pink",fg="blue")
label_m.grid(row=3,column=0)


button_submit = Button(frame,text="Submit",command=enter_data,bg="pink",fg="blue")
button_submit.grid(row=2,column=0,sticky=W)

button_clear = Button(frame,text="Clear",command=clear_elements,bg="pink",fg="blue")
button_clear.grid(row=2,column=1,sticky=E)
screen.mainloop()