import csv
import os

# products.csv index numbers
PRODUCT_NUMBER_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2
#request.csv index numbers
PRODUCT_QUANTITY_INDEX = 1

############################

def main():
    # get the current folder path for referencing
    path = os.path.abspath(__file__)
    file = os.path.dirname(path)
    # Use the folder path to reference the different csv files
    products_dict = read_dict(f"{file}/products.csv", PRODUCT_NUMBER_INDEX)

    # Print the products_dict
    print("All Products:")
    print(products_dict)
    print()

    print("Requested Items:")

    # open request.csv and store a reference
    with open(f"{file}/request.csv") as request_file:

        # use csv module to create a reader object for csv file
        reader = csv.reader(request_file)

        # skip first row due to column headers
        next(reader)

        # read rows one by one and returns a list
        for row in reader:

            # for current row get product number and quantity
            product_number = row[PRODUCT_NUMBER_INDEX]
            product_quantity = row[PRODUCT_QUANTITY_INDEX]

            # retrieve the name and price for product from products_dict
            value = products_dict[product_number]
            product_name = value[PRODUCT_NAME_INDEX]
            product_price = value[PRODUCT_PRICE_INDEX]

            # print out the name, quantity and price for each row
            print(f"{product_name}: {product_quantity} @ {product_price}")

############################

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # create an empty dictionary to store data from csv
    dictionary = {}

    # Open csv file for reading and storing a reference
    with open(filename, "rt") as product_file:

        # use csv module to create a reader object for csv file
        reader = csv.reader(product_file)

        # skip the first row due to column headings
        next(reader)

        # read rows one by one and returns as a list
        for row in reader:

            # If current row is not blank add to dictionary
            if len(row) != 0:

                # sets the key for the dictionary for the current row
                key = row[key_column_index]

                # store data from row into the dictionary using key
                dictionary[key] = row

    #return the dictionary with the new data
    return dictionary

################################

# Call main to start program
if __name__ == "__main__":
    main()