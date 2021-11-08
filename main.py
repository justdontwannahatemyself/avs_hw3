import datetime
import sys
import string

from extender import *

error_message1 = "incorrect command line!\n" \
                 "  Waited:\n" \
                 "     command -f infile outfile01 outfile02\n" \
                 "  Or:\n" \
                 "     command -n number outfile01 outfile02\n"

error_message2 = "incorrect qualifier value!\n" \
                 "  Waited:\n" \
                 "     command -f infile outfile01 outfile02\n" \
                 "  Or:\n" \
                 "     command -n number outfile01 outfile02\n"

if __name__ == '__main__':
    start = datetime.datetime.now()
    if len(sys.argv) != 5:
        print(error_message1)
        exit()

    if sys.argv[1] == "-f":
        input_file_name = sys.argv[2]
        try:
            container = Container()
            container.read_file(input_file_name)
            container.print()
        except Exception as e:
            print(e)
            exit()
    elif sys.argv[1] == "-n":
        num = int(sys.argv[2])
        if not 0 < num <= 10000:
            print(f"Incorrect number of animals = {num}. Set 0 < number <= 10000")
            exit()
        container = Container()
        container.in_random(num)
        container.print()

    else:
        print("Incorrect command line! You must write: python main <inputFileName> <outputFileName1> <outputFileName2>")
        exit()

    output_file_name1 = sys.argv[3]
    output_file_name2 = sys.argv[4]

    print('==> Start')

    ofile = open(output_file_name1, 'w')
    container.write(ofile)
    ofile.close()

    ofile = open(output_file_name2, 'w')
    container.shell_sort()
    ofile.write("Sorted container:\n")
    container.write(ofile)
    ofile.close()

    print('==> Finish')
    print(datetime.datetime.now() - start)