from tkinter import Label, Tk
import time
app_window = Tk()
app_window.title("C# Corner Digital CLock")
app_window.geometry("580x200")
app_window.resizable(1,1)

text_font= ("Lato", 100, 'bold')
background = "red"
foreground= "white"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def dclock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)
   label.after(200, dclock)

dclock()
app_window.mainloop()