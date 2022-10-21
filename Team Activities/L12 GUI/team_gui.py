
import tkinter as tk
import number_entry as nent


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Area of a Rectangle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

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

    lbl_width = tk.Label(frm_main, text="Width:")
    lbl_length = tk.Label(frm_main, text="Length:")

    ent_width = nent.IntEntry(frm_main, 1, 99, width=5)
    ent_length = nent.IntEntry(frm_main, 10, 99, width=5)

    lbl_area = tk.Label(frm_main, text="Area:")

    lbl_area_answer = tk.Label(frm_main, width=4)

    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear")

    lbl_status = tk.Label(frm_main, text="")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_width.grid(  row=0, column=0, padx=3, pady=3)
    lbl_length.grid(  row=0, column=1, padx=3, pady=3)
    ent_width.grid(row=1, column=0, padx=3, pady=3)
    ent_length.grid(row=1, column=1, padx=3, pady=3)
    lbl_area.grid(row=0, column=2, padx=(30,3), pady=3)
    lbl_area_answer.grid( row=1, column=4, padx=3, pady=3)
    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=5, sticky="news")
    lbl_status.grid(row=3, columnspan=5)

    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            width = ent_width.get()
            length = ent_length.get()

            area = width * length

            lbl_area_answer.config(text=f"{area:.0f}")
            lbl_status.config(text="")

        except ValueError:
            lbl_status.config(text="error")
            lbl_area_answer.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_width.delete(0, tk.END)
        ent_length.delete(0, tk.END)
        lbl_area_answer.config(text="")
        lbl_status.config(text="")
        ent_width.focus()


    # Bind the calculate function to the age entry box
    # so that the calculate function will be called when
    # the user changes the text in the entry box.
    ent_width.bind("<KeyRelease>", calculate)
    ent_length.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_width.focus()

if __name__ == "__main__":
    main()