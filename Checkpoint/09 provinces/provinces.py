import os

def main():

    path = os.path.abspath(__file__)
    file = os.path.dirname(path)
    text_list = read_list(f"{file}\provinces.txt")

    # Print the entire list.
    print(text_list)

    count_alberta = 0

    text_list.pop(0)
    text_list.pop()

    for list in text_list:
        if list == "AB":
            list = "Alberta"
        if list == "Alberta":
            count_alberta += 1

    print(f"Alberta occurs {count_alberta} times in the modified list.")


def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of text from the text file.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list


# Call main to start this program.
if __name__ == "__main__":
    main()