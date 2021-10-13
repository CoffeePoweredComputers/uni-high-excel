import os
import sys

from src import excelmath as em
from src import plot as plt


def main():

    #
    # Part 1: processing the users arguments
    #

    if len(sys.argv) > 4:
        print("Invalid number of arguments")
        exit(-1)

    if os.path.exists(sys.argv[1]) and os.path.isfile(sys.argv[1]) and sys.argv[1].endswith(".csv"):
        with open(sys.argv[1]) as fo:
            raw_data = fo.readlines()
    else:
        print("{} invalid path".format(sys.argv[1]))
        exit(-2)

    if sys.argv[2] == "row":
        processed_data = em.get_rows(raw_data)
    elif sys.argv[2] == "col":
        processed_data = em.get_cols(raw_data)
    else:
        print("Please enter either col or row")
        exit(-3)

    operations = ["get_sum", "get_stdev", "get_avg"]
    op_funcs = [em.get_sum, em.get_stdev, em.get_avg]

    for operation in sys.argv[3:]:

        if operation in operations:
            op_num = operations.index(operation)
            result = op_funcs[op_num](processed_data)
            print(result)
        else:
            print("{} is not a valid operation".format(operation))


if __name__ == "__main__":
    main()

