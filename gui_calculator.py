import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

current_value = ""

def clicked(event):
    global current_value
    text = event.widget.cget("text")
    #print what button is clicked
    print(f"{text}")

    if text == "=":
        try:
            result = str(eval(current_value))
            entry_var.set(result)
            current_value = result #storing the result for further calculations
            print(result)
        except Exception as e:
            entry_var.set("Error")
            current_value = ""
    elif text == "C":
        current_value = ""
        entry_var.set("0")
    else:
        current_value += text
        entry_var.set(current_value)

#creates widget to display current value
entry_var = tk.StringVar()
entry_var.set("0") #initial value is at 0
entry = tk.Entry(root, textvar=entry_var, font=('Arial', 24), justify='right')
entry.pack(fill='both',ipadx=8,pady=10,padx=10)

#Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", ".", "=",
    "/"
]

#adding buttons to the frame
row = 0
col = 0
for button in buttons:
    btn = tk.Button(button_frame, text=button, font=('Arial', 18), height=2, width=5)
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", clicked) #binds 
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
