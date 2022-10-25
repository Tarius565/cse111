

import os
from finance_program import write_cat_list, read_cat_list
from pytest import approx
import pytest


path = os.path.abspath(__file__)
file = os.path.dirname(path)


def test_write_file():
    """Verify that the write_file function works correctly."""
    lines = [["Income",	"andersen paycheck",	"Income",	"3600"],
["Car",	"gas",	"Expenditure",	"210"],
["Car",	"car insurance",	"Expenditure",	"350"],
["Electricity",	"SRP",	"Expenditure",	"120"],
["Water",	"Epcor",	"Expenditure",	"50"],
["Mortgage",	"Mortgage",	"Expenditure",	"1500"]
    ]
    filename = "test_file.csv"

    # Call the write_file function to
    # write a file named test_file.csv.
    write_cat_list(f"{file}/csv/{filename}", lines)

    # Read the contents of the test_file.csv file.
    with open(f"{file}/csv/{filename}", "rt") as infile:

        # Read all the characters in the file into a string.
        string = infile.read()

    # Split the string into a list of strings named
    # written. Each line of text from the text file
    # will be stored in its own element in the list.
    written = string.splitlines()

    # Delete the test_file.csv file.
    os.remove(f"{file}/csv/{filename}")

    new_lines = ["Income,andersen paycheck,Income,3600",
"Car,gas,Expenditure,210",
"Car,car insurance,Expenditure,350",
"Electricity,SRP,Expenditure,120",
"Water,Epcor,Expenditure,50",
"Mortgage,Mortgage,Expenditure,1500"
    ]

    # Verify that write_file correctly wrote the test_file.csv file.
    assert new_lines == written

def test_read_file():
    """Verify that the read_file function works correctly."""
    # Write a sample file with three lines
    filename = "lines.csv"
    headers =["category header","source header","type header","amount header"]
    lines = ["name", "source", "type","amount"]
    with open(f"{file}/csv/{filename}", "wt") as outfile:
        print(*headers, sep=",", file=outfile)
        print(*lines, sep=",", file=outfile)

    # Call read_file to read the sample file.
    read = read_cat_list(filename)

    # Delete the lines.txt file.
    os.remove(f"{file}/csv/{filename}")

    new_lines = (["name"], ["amount"], ["type"])

    # Verify that read_file read the file correctly.
    assert read == new_lines


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
