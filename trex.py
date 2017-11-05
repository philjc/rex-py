import re
import json
import argparse


def __parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', type=argparse.FileType('r'),
                        default='-', help="Input file to operate on")
    parser.add_argument('-o', '--output', type=argparse.FileType('w'),
                        default='-', help="Ouput file to write results to")
    parser.add_argument('pattern', type=str, help="Regex pattern to find")

    return parser.parse_args()


def __main():
    args = __parse_args()
    p = re.compile(args.pattern)

    for line in args.input:
        matched = p.search(line)
        if matched:
            print(json.dumps(matched.groupdict()), file=args.output)


if __name__ == "__main__":
    __main()
