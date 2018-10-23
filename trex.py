import re
import json
import argparse


def __parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i",
        "--input_file",
        type=argparse.FileType("r"),
        default="-",
        help="Input file to operate on, DEFAULT: stdin",
    )
    parser.add_argument(
        "-o",
        "--output_file",
        type=argparse.FileType("w"),
        default="-",
        help="Ouput file to write results to, DEFAULT: stdout",
    )
    parser.add_argument(
        "-f",
        "--output_format",
        type=str,
        default=None,
        help="Used to output formatted strings from matched named groups",
    )
    parser.add_argument("pattern", type=str, help="Regex pattern to find")

    return parser.parse_args()


def __main():
    args = __parse_args()
    p = re.compile(args.pattern)

    for line in args.input_file:
        matched = p.search(line)
        if matched and args.output_format:
            print(
                args.output_format.format(**matched.groupdict()), file=args.output_file
            )

        elif matched:
            print(json.dumps(matched.groupdict()), file=args.output_file)


if __name__ == "__main__":
    __main()
