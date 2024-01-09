import argparse
import sys

from src.CalcRating import CalcRating
from src.TextDataReader import TextDataReader
from src.XMLDataReader import XMLDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    # reader = TextDataReader()
    reader = XMLDataReader()
    students = reader.read(path)
    print("Students: ", students)

    calc = CalcRating(students)

    rating = calc.calc()
    print("Rating: ", rating)

    q1 = calc.q1()
    print("Q1: ", q1)

if __name__ == "__main__":
    main()
