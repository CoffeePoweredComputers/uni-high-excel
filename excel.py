import os
import sys

import excelmath as em


def main():

    #
    # Part 1: processing the users arguments
    #

    if len(sys.argv) < 4:
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

    operations = ["sum", "stdev", "avg"]
    op_funcs = [em.sum, em.stdev, em.avg]
    for operation in sys.argv[2:]:
        if 



if __name__ == "__main__":
    main()

