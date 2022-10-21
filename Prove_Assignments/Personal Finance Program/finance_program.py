
import tkinter as tk
from turtle import width


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Personal Finance")
    frm_main.pack(padx=550, pady=350, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    # """

    lsbx_category = tk.Listbox(frm_main)

    btn_clear = tk.Button(frm_main, text="Clear")
    btn_enter = tk.Button(frm_main, text="Enter")



    lsbx_category.grid(row=0, column=0)
    btn_clear.grid(row=1, column=0, ipadx=16, padx=3, pady=3, columnspan=5, sticky="nesw")
    btn_enter.grid(row=1, column=6, ipadx=16, padx=3, pady=3, columnspan=5, sticky="nesw")

    #  # Create a label that displays "Age:"
    # lbl_age = tk.Label(frm_main, text="Age:")

    # # Create a integer entry box where the user will enter her age.
    # ent_age = nent.IntEntry(frm_main, 12, 90, width=5)

    # # Create a label that displays "Rates:"
    # lbl_rates = tk.Label(frm_main, text="Rates:")

    # # Create labels that will display the results.
    # lbl_slow = tk.Label(frm_main, width=4)
    # lbl_fast = tk.Label(frm_main, width=4)

    # # Create the Clear button.
    # btn_clear = tk.Button(frm_main, text="Clear")

    # # Layout all the labels, entry boxes, and buttons in a grid.
    # lbl_age.grid(  row=0, column=0, padx=3, pady=3)
    # ent_age.grid(  row=0, column=1, padx=3, pady=3)
    # lbl_rates.grid(row=0, column=2, padx=(30,3), pady=3)
    # lbl_slow.grid( row=0, column=3, padx=3, pady=3)
    # lbl_fast.grid( row=0, column=4, padx=3, pady=3)
    # btn_clear.grid(row=1, column=0, padx=3, pady=3, columnspan=5, sticky="w")




if __name__ == "__main__":
    main()