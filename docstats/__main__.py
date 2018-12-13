"""
@copyright: 2018 Data Wizard
"""

import os
import sys
from time import gmtime, strftime

from docx import Document


def main():
    """
    First version, run through
    :return:
    """
    if len(sys.argv) < 2:
        print("Please add directory containing docs as parameter")
        return

    suffix = ".docx"
    not_starts_with = "~$"
    total_count = 0
    expectation_book = 40 * 15 * 500

    for root, _, files in os.walk(sys.argv[1]):
        for name in files:
            if name.endswith(suffix) and not name.startswith(not_starts_with):
                # whatever
                full_path = root + "/" + name
                doc = Document(full_path)
                count = 0
                for para in doc.paragraphs:
                    count += len(para.text.split())
                total_count = total_count + count

                print(name + " " + str(count))
    print(total_count)
    print(str((expectation_book - total_count)) + " to go for a 500 book pages")
    print(str(total_count * 100 / expectation_book) + "% written")

    output_file = open('results.csv', 'a')
    output_file.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ";" + str(total_count) + "\n")
    output_file.close()


if __name__ == '__main__':
    main()
