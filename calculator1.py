from tkinter import *

def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    try:
        # replace custom symbols with python operators
        to_eval = operator.replace("÷", "/").replace("x", "*")
        sumup = str(eval(to_eval))
        text_Input.set(sumup)
        operator = sumup
    except Exception:
        text_Input.set("Error")
        operator = ""

cal = Tk()
cal.title("Calculator")
cal.configure(bg="#4b76a8")
cal.geometry("350x520")

operator = ""
text_Input = StringVar()

# Colors based on the provided image
bg_color = "#4b76a8"
num_bg = "#cdd5ec"
op_bg = "#ffffff"
c_bg = "#ffca28"
text_dark = "#2b3a67"
display_bg = "#6a8eb3"
display_text = "#ffe345"

# Base Button params
btn_base = {
    'font': ('Helvetica', 20, 'bold'),
    'bd': 0,
    'fg': text_dark,
    'relief': FLAT,
    'highlightthickness': 0
}

num_params = btn_base.copy()
num_params.update({'bg': num_bg, 'activebackground': '#b3bede'})

op_params = btn_base.copy()
op_params.update({'bg': op_bg, 'activebackground': '#e6e6e6'})

clear_params = btn_base.copy()
clear_params.update({'bg': c_bg, 'activebackground': '#e6b800'})

# Display
display_frame = Frame(cal, bg=display_bg, bd=0)
display_frame.grid(row=0, column=0, sticky="nsew", pady=(20, 15), padx=20)
display_frame.grid_columnconfigure(0, weight=1)
display_frame.grid_rowconfigure(0, weight=1)

txtDisplay = Entry(display_frame, font=('Helvetica', 40), textvariable=text_Input, bd=0, insertwidth=4,
                   bg=display_bg, fg=display_text, justify='right', disabledbackground=display_bg, disabledforeground=display_text)
txtDisplay.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)
txtDisplay.bind("<Key>", lambda e: "break") # Make it read-only but keep color active

# Button Frame
button_frame = Frame(cal, bg=bg_color)
button_frame.grid(row=1, column=0, sticky="nsew", padx=14, pady=(0, 20))

for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

# Button creation helper
def create_btn(text, row, col, params, cmd, rowspan=1):
    btn = Button(button_frame, text=text, command=cmd, **params)
    btn.grid(row=row, column=col, rowspan=rowspan, sticky="nsew", padx=6, pady=6)
    return btn

# Row 0
create_btn("C", 0, 0, clear_params, btnClearDisplay)
create_btn("%", 0, 1, op_params, lambda: btnclick("%"))
create_btn("÷", 0, 2, op_params, lambda: btnclick("÷"))
create_btn("x", 0, 3, op_params, lambda: btnclick("x"))

# Row 1
create_btn("7", 1, 0, num_params, lambda: btnclick(7))
create_btn("8", 1, 1, num_params, lambda: btnclick(8))
create_btn("9", 1, 2, num_params, lambda: btnclick(9))
create_btn("-", 1, 3, op_params, lambda: btnclick("-"))

# Row 2
create_btn("4", 2, 0, num_params, lambda: btnclick(4))
create_btn("5", 2, 1, num_params, lambda: btnclick(5))
create_btn("6", 2, 2, num_params, lambda: btnclick(6))
create_btn("+", 2, 3, op_params, lambda: btnclick("+"))

# Row 3
create_btn("1", 3, 0, num_params, lambda: btnclick(1))
create_btn("2", 3, 1, num_params, lambda: btnclick(2))
create_btn("3", 3, 2, num_params, lambda: btnclick(3))
create_btn("=", 3, 3, op_params, btnEqualsInput, rowspan=2)

# Row 4
create_btn("0", 4, 0, num_params, lambda: btnclick(0))
create_btn("00", 4, 1, num_params, lambda: btnclick("00"))
create_btn(".", 4, 2, num_params, lambda: btnclick("."))

# Main layout config
cal.grid_rowconfigure(0, weight=0)
cal.grid_rowconfigure(1, weight=1)
cal.grid_columnconfigure(0, weight=1)

cal.mainloop()
