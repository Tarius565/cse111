

from datetime import date
from genericpath import isfile
import os
import tkinter as tk
import csv


CATEGORY_INDEX = 0
FINANCE_SOURCE_INDEX = 1
CATEGORY_TYPE_INDEX = 2
CATEGORY_AMOUNT_INDEX = 3

path = os.path.abspath(__file__)
file = os.path.dirname(path)

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Personal Finance")
    frm_main.pack(padx=3, pady=4, fill=tk.BOTH, expand=1)

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

    # This function will be called each time
    # the user presses the "add" button.
    def add():
        """Calls and writes to a new csv file or a current csv file
        with the information provided within the entry areas.
        """
        # get the values in the entry areas to a variable
        month = month_option.get()
        year = ent_year.get()
        source = ent_source.get()
        amount = ent_amount.get()
        category = ent_category.get()
        cat_type = category_type.get()

        #store the headings if the file does not exist
        headings = ["category", "finance source", "category type", "amount"]

        #Create a list with the information from the entry sources
        finance_list = [[category, source, cat_type, amount]]
        csv_file = str(year)+"-"+str(month)

        
        write_cat_list(f"{file}/csv/{csv_file}.csv", finance_list, headings)


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        # ent_month.delete(0, tk.END)
        # ent_year.delete(0, tk.END)
        ent_source.delete(0, tk.END)
        ent_amount.delete(0, tk.END)
        category_type.set("")
        ent_category.delete(0, tk.END)

    def graph_calculate(event):

        name, amt, amt_type = read_cat_list(graph_x.get())

        change_graph(name, amt, amt_type)
        calculate(amt, amt_type)

    # This function will be called each time
    # the user changes the "Graph_x" option menu.
    def change_graph(name, amt, amt_type):
        """Changes the graph to view the selected file"""
        # Clear everything in the canvas before drawing
        cns_graph.delete("all")
        # The variables below size the bar graph
        y_gap_lower = 10  # The gap between lower canvas edge and x axis
        y_gap_top = 20 # The gap between the top canvas edge and x axis (leaves room for text)
        x_gap = 15  # The gap between left and right canvas edge and y axis
        j = 0
        max_val = 0
        x_var = len(amt)
        for i in range(x_var):
            if float(amt[i]) > max_val:
                max_val = float(amt[i])

        # A quick for loop to calculate the rectangle
        for x, y in enumerate(amt):

            # coordinates of each bar
            # left coordinate
            x0 =  x * ((graph_width - 2 * x_gap) / x_var) + x_gap * 2

            # Top coordinates
            y0 = (graph_height- y_gap_lower - y_gap_top) * (1 - float(y) / max_val) + y_gap_top

            # right coordinates
            x1 =  x * ((graph_width - 2 * x_gap) / x_var) + ((graph_width - 2 * x_gap) / x_var)

            # Bottom coordinates
            y1 = graph_height - y_gap_lower

            # Draw the bar
            if amt_type[j] == "Income":
                cns_graph.create_rectangle(x0, y0, x1, y1, fill="green")
            else:
                cns_graph.create_rectangle(x0, y0, x1, y1, fill="red")

            # Put the y value above the bar
            cns_graph.create_text(x0 + 2, y0, anchor=tk.SW, text=str(name[j]))
            j += 1


    # This function will be called each time
    # the user changes the "Graph_x" option menu.
    def calculate(amt, amt_type):
        """Sums the income and expenditures in the 
        selected file and displays the results under
        the graph"""
        income_tot = 0
        expenditure_tot = 0
        total = 0
        for j in range(len(amt)):
            if amt_type[j] == "Income":
                income_tot += float(amt[j])
            else:
                expenditure_tot += float(amt[j])
        
        total = income_tot - expenditure_tot

        lbl_income_amt.config(text=f"${income_tot}")
        lbl_expenditure_amt.config(text=f"${expenditure_tot}")
        lbl_total_amt.config(text=f"${total}")
        lbl_income_title.config(text="Total Income:")
        lbl_expenditure_title.config(text="Total Expenditure:")
        lbl_total_title.config(text="Total Amount (I-E):")


    category_type = tk.StringVar()
    month_option = tk.StringVar()
    graph_x = tk.StringVar()

    graph_width = 400
    graph_height = 400

    # defin a list for category type
    category_type_list = ["Income", "Expenditure"]
    month_list = [
        "January", 
        "February", 
        "March", 
        "April", 
        "May", 
        "June", 
        "July", 
        "August", 
        "September", 
        "October", 
        "November", 
        "December"
        ]
    graph_x_list = get_files_list(f"{file}/csv")

    # Create all the various widgets left of the graph frame
    lbl_month = tk.Label(frm_main, text="Month")
    lbl_year = tk.Label(frm_main, text="Year")
    opt_month = tk.OptionMenu(frm_main, month_option, "", *month_list)
    ent_year = tk.Entry(frm_main)
    lbl_finance_source = tk.Label(frm_main, text="Finance Source")
    lbl_finance_amount = tk.Label(frm_main, text="Finance Amount")
    ent_source = tk.Entry(frm_main)
    ent_amount = tk.Entry(frm_main)
    lbl_category = tk.Label(frm_main, text="Finance Category")
    ent_category = tk.Entry(frm_main)
    lbl_category_type = tk.Label(frm_main, text="Category Type")
    opt_category_type = tk.OptionMenu(frm_main, category_type, *category_type_list)
    btn_clear = tk.Button(frm_main, text="Clear",padx=20, pady=2)
    btn_add = tk.Button(frm_main, text="Add",padx=20, pady=2)


    frm_graph = tk.Frame(frm_main, borderwidth=3)
    # Create widgets for inside the graph frame
    cns_graph = tk.Canvas(frm_graph, width=graph_height, height=graph_width, bg='white')
    lbl_graph_x = tk.Label(frm_graph, text="Show the finances of:")
    opt_graph_x = tk.OptionMenu(frm_graph, graph_x, *graph_x_list, command=graph_calculate)
    lbl_income_title = tk.Label(frm_graph, text="")
    lbl_expenditure_title = tk.Label(frm_graph, text="")
    lbl_total_title = tk.Label(frm_graph, text="")
    lbl_income_amt = tk.Label(frm_graph, text="")
    lbl_expenditure_amt = tk.Label(frm_graph, text="")
    lbl_total_amt = tk.Label(frm_graph, text="")


    # Place all the various widgets in the frame
    lbl_month.grid(row=0, column=0, padx=3, pady=1)
    lbl_year.grid(row=0, column=1, padx=3, pady=1)
    opt_month.grid(row=1, column=0, padx=3, pady=1)
    ent_year.grid(row=1, column=1, padx=3, pady=1)
    lbl_finance_source.grid(row=2, column=0, padx=3, pady=1)
    lbl_finance_amount.grid(row=2, column=1, padx=3, pady=1)
    ent_source.grid(row=3, column=0, padx=3, pady=1)
    ent_amount.grid(row=3, column=1, padx=3, pady=1)
    lbl_category.grid(row=4, column=0, padx=3, pady=3)
    lbl_category_type.grid(row=4, column=1, padx=3, pady=3)
    ent_category.grid(row=5, column=0, padx=3, pady=1)
    opt_category_type.grid(row=5, column=1, padx=3, pady=1)
    btn_clear.grid(row=6, column=0, padx=3, pady=7, sticky="nesw")
    btn_add.grid(row=6, column=1, padx=3, pady=7, sticky="nesw")
    frm_graph.grid(row=0, column=3, rowspan=18, padx=4, pady=4)

    # Place variables inside the graph frame
    cns_graph.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
    lbl_graph_x.grid(row=1, column=0, padx=3, pady=3, sticky='w')
    opt_graph_x.grid(row=1, column=1, padx=3, pady=3, sticky='w')
    lbl_income_title.grid(row=2, column=0, padx=3, pady=3, sticky='n')
    lbl_expenditure_title.grid(row=2, column=1, padx=3, pady=3, sticky='n')
    lbl_total_title.grid(row=2, column=2, padx=3, pady=3, sticky='n')
    lbl_income_amt.grid(row=3,column=0, padx=3, pady=3, sticky='w')
    lbl_expenditure_amt.grid(row=3, column=1, padx=3, pady=3, sticky='w')
    lbl_total_amt.grid(row=3, column=2, padx=3, pady=3, sticky='e')


    # Bind the add function to the enter button so
    # that the add function will be called when the
    # user clicks the enter button.
    btn_add.config(command=add)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # opt_graph_x.config(command=graph_calculate)

def read_cat_list(filename):
    """Read the contents of a CSV file into a compound
    list and return the list.

    Parameters
        filename: the name of the CSV file to read.
    Return: a compound list that contains
        the amount of income and expenditures
        inside of the CSV file.
    """
    amt_list = []
    name_list = []
    amt_type_list = []

    with open(f"{file}/csv/{filename}", "rt") as csv_file:

         # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank,
            # append it to the compound_list.
            if len(row_list) != 0:

                # Append one row from the CSV
                # file to the compound list.
                name_list.append(row_list[CATEGORY_INDEX])
                amt_list.append(row_list[CATEGORY_AMOUNT_INDEX])
                amt_type_list.append(row_list[CATEGORY_TYPE_INDEX])
                

    return name_list, amt_list, amt_type_list

def write_cat_list(filename, compound_list, heading_list=None):
    """Write the contents of a list into a CSV file.
    
    Parameters
        filename: the name of the CSV file to write
        compound_list: the list to write to the CSV file
        heading_list: a list that contains the column headings.
            If heading_list is None, this function will not
            write headings to the CSV file.
        Return: nothing
        """

    # Check to see if the file exists
    # if file does not exist it creates the file and adds the headers
    if not os.path.exists(filename):
            with open(filename, "at", newline="") as csv_file:

                # Use the csv module to create a writer object and a reader object
                writer = csv.writer(csv_file)

                # Write the heading_list to the CSV file.
                if heading_list is not None:
                    writer.writerow(heading_list)

    # Open the csv file for writing and store a reference
    # to the opened file in a variable named csv_file:
    with open(filename, "at", newline="") as csv_file:

        # Use the csv module to create a writer object and a reader object
        writer = csv.writer(csv_file)

        # Write the contents of the list into the
        # CSV file, one row at a time.
        for row_list in compound_list:
            writer.writerow(row_list)
    
def get_files_list(dir_path):
    """Read the contents inside a folder and returns that list of content
    
    Parameters
        dir_path: the name of the path to search for files
    Return: the list of files
    """
    # Create blank list to be filled out
    csv_files = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            # append the file to the list
            csv_files.append(path)

    return csv_files

if __name__ == "__main__":
    main()