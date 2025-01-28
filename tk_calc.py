import tkinter as tk
import check_if_font as cif

cif.prog()

def main():
    gui = tk.Tk()

    gui.title("TkCalc")

    gui.geometry("360x320")

    gui.configure(bg="black")

    CalcEntry = tk.Entry(gui, bg="white", fg="black", font=("SF UI Text Heavy", 24), state='disabled')
    CalcEntry.pack()

    def update_entry(value):
        CalcEntry.config(state='normal')  # Enable entry for updating
        current_text = CalcEntry.get()    # Get current text in the entry
        CalcEntry.delete(0, tk.END)      # Clear current text
        CalcEntry.insert(0, current_text + value)  # Append new value to existing text
        CalcEntry.config(state='disabled')  # Disable entry again

    def percentage():
        CalcEntry.config(state='normal')  # Enable entry for updating
        current_text = CalcEntry.get()    # Get current text in the entry
        CalcEntry.delete(0, tk.END)      # Clear current text
        CalcEntry.insert(0, int(current_text) / 100)  # Append new value to existing text
        CalcEntry.config(state='disabled')  # Disable entry again

    def clear_entry():
        CalcEntry.config(state='normal')  # Enable entry for updating
        CalcEntry.delete(0, tk.END)      # Clear current text
        CalcEntry.config(state='disabled')  # Disable entry again

    def delete_entry():
        CalcEntry.config(state='normal')  # Enable entry for updating
        current_text = CalcEntry.get()    # Get current text in the entry
        CalcEntry.delete(0, tk.END)      # Clear current text
        current_text = current_text[:-1]
        CalcEntry.insert(0, current_text)  # Append new value to existing text
        CalcEntry.config(state='disabled')  # Disable entry again
    
    def enter():
        current_text = CalcEntry.get()    # Get current text in the entry
        CalcEntry.config(state='normal')  # Enable entry for updating
        solved_text = eval(current_text)
        CalcEntry.delete(0, tk.END)      # Clear current text
        CalcEntry.insert(0, solved_text)  # Append new value to existing text
        CalcEntry.config(state='disabled')  # Disable entry again

    button1 = tk.Button(gui, text=" 1 ", background="orange",  font=("SF UI Text Heavy", 12), command=lambda: update_entry("1"))
    button1.place(x=10,y=100)

    button4 = tk.Button(gui, text=" 4 ", background="orange",  font=("SF UI Text Heavy", 12), command=lambda: update_entry("4"))
    button4.place(x=10,y=150)

    button7 = tk.Button(gui, text=" 7 ", background="orange", font=("SF UI Text Heavy", 12), command=lambda: update_entry("7"))
    button7.place(x=10,y=200)

    button2 = tk.Button(gui, text=" 2 ", background="orange", font=("SF UI Text Heavy", 12), command=lambda: update_entry("2"))
    button2.place(x=100,y=100)

    button5 = tk.Button(gui, text=" 5 ", background="orange",  font=("SF UI Text Heavy", 12), command=lambda: update_entry("5"))
    button5.place(x=100,y=150)

    button8 = tk.Button(gui, text=" 8 ", background="orange",  font=("SF UI Text Heavy", 12), command=lambda: update_entry("8"))
    button8.place(x=100,y=200)

    button3 = tk.Button(gui, text=" 3 ", background="orange", font=("SF UI Text Heavy", 12), command=lambda: update_entry("3"))
    button3.place(x=200,y=100)

    button6 = tk.Button(gui, text=" 6 ", background="orange", font=("SF UI Text Heavy", 12), command=lambda: update_entry("6"))
    button6.place(x=200,y=150)

    button9 = tk.Button(gui, text=" 9 ", background="orange", font=("SF UI Text Heavy", 12), command=lambda: update_entry("9"))
    button9.place(x=200,y=200)

    button0 = tk.Button(gui, text="             0            ", background="orange", font=("SF UI Text Heavy", 12), command=lambda: update_entry("0"))
    button0.place(x=10,y=250)

    buttonDecimal = tk.Button(gui, text=" • ", background="orange", font=("SF UI Text Heavy", 12) , command=lambda: update_entry("."))
    buttonDecimal.place(x=202,y=250)

    buttonX = tk.Button(gui, text=" x ", background="black", foreground="white", font=("SF UI Text Heavy", 12) , command=lambda: update_entry("*"))
    buttonX.place(x=300,y=100)

    buttonDivision = tk.Button(gui, text=" ÷ ", background="black", foreground="white", font=("SF UI Text Heavy", 12) , command=lambda: update_entry("/"))
    buttonDivision.place(x=300,y=50)

    buttonMinus = tk.Button(gui, text=" - ", background="black", foreground="white", font=("SF UI Text Heavy", 12) , command=lambda: update_entry("-"))
    buttonMinus.place(x=302,y=150)

    buttonPlus = tk.Button(gui, text=" + ", background="black", foreground="white", font=("SF UI Text Heavy", 12) , command=lambda: update_entry("+"))
    buttonPlus.place(x=300,y=200)
    
    buttonPercentage = tk.Button(gui, text=" % ", background="grey", foreground="white", font=("SF UI Text Heavy", 12) , command=lambda: percentage())
    buttonPercentage.place(x=200,y=50)

    buttonPower = tk.Button(gui, text=" ^ ", background="grey", foreground="white", font=("SF UI Text Heavy", 12) , command=lambda: update_entry("**"))
    buttonPower.place(x=102,y=50)

    buttonClear = tk.Button(gui, text=" C ", background="grey", foreground="white", width=1, font=("SF UI Text Heavy", 12) , command=lambda: clear_entry())
    buttonClear.place(x=7,y=50)

    buttonDelete = tk.Button(gui, text=" AC ", background="grey", foreground="white", width=1, font=("SF UI Text Heavy", 12) , command=lambda: delete_entry())
    buttonDelete.place(x=27,y=50)


    buttonEqualTo = tk.Button(gui, text=" = ", background="black", foreground="white", font=("SF UI Text Heavy", 12) ,  command=lambda: enter())
    buttonEqualTo.place(x=300,y=250)

    gui.bind('<KeyPress-1>', lambda event: update_entry("1"))
    gui.bind('<KeyPress-2>', lambda event: update_entry("2"))
    gui.bind('<KeyPress-3>', lambda event: update_entry("3"))
    gui.bind('<KeyPress-4>', lambda event: update_entry("4"))
    gui.bind('<KeyPress-5>', lambda event: update_entry("5"))
    gui.bind('<KeyPress-6>', lambda event: update_entry("6"))
    gui.bind('<KeyPress-7>', lambda event: update_entry("7"))
    gui.bind('<KeyPress-8>', lambda event: update_entry("8"))
    gui.bind('<KeyPress-9>', lambda event: update_entry("9"))
    gui.bind('<KeyPress-0>', lambda event: update_entry("0"))
    gui.bind('<KeyPress-*>', lambda event: update_entry("*"))
    gui.bind('<KeyPress-/>', lambda event: update_entry("/"))
    gui.bind('<KeyPress-minus>', lambda event: update_entry("-"))
    gui.bind('<KeyPress-+>', lambda event: update_entry("+"))
    gui.bind('<KeyPress-.>', lambda event: update_entry("."))
    gui.bind('<KeyPress-^>', lambda event: update_entry("**"))
    gui.bind('<KeyPress-%>', lambda event: percentage())
    gui.bind('<Return>', lambda event: enter())
    gui.bind('<BackSpace>', lambda event: clear_entry())
    gui.bind('<Delete>', lambda event: delete_entry())

    gui.mainloop()

main()
