
import tkinter as tk
import number_entry as nent


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

    # # Layout all the labels, entry boxes, and buttons in a grid.
    # lbl_age.grid(  row=0, column=0, padx=3, pady=3)
    # ent_age.grid(  row=0, column=1, padx=3, pady=3)
    # lbl_rates.grid(row=0, column=2, padx=(30,3), pady=3)
    # lbl_slow.grid( row=0, column=3, padx=3, pady=3)
    # lbl_fast.grid( row=0, column=4, padx=3, pady=3)
    # btn_clear.grid(row=1, column=0, padx=3, pady=3, columnspan=5, sticky="w")

    def enter(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        # try:
        #     width = ent_width.get()
        #     length = ent_length.get()

        #     area = width * length

        #     lbl_area_answer.config(text=f"{area:.0f}")
        #     lbl_status.config(text="")

        # except ValueError:
        #     lbl_status.config(text="error")
        #     lbl_area_answer.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        # ent_width.delete(0, tk.END)
        # ent_length.delete(0, tk.END)
        # lbl_area_answer.config(text="")
        # lbl_status.config(text="")
        # ent_width.focus()


    # Bind the enter function to the enter button so
    # that the enter function will be called when the
    # user clicks the enter button.
    btn_enter.config(command=enter)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)



if __name__ == "__main__":
    main()