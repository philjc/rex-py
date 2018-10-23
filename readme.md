# trex

trex is a line-oriented data extraction utility that uses regex patterns to extract values from text. This is currently a POC written in [Python](https://www.python.org/) before I rewrite it in [Go](https://golang.org/) or [Rust](https://www.rust-lang.org).

### Usage
```
usage: trex.py [-h] [-i INPUT_FILE] [-o OUTPUT_FILE] [-f OUTPUT_FORMAT]
               pattern

positional arguments:
  pattern               Regex pattern to find

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input_file INPUT_FILE
                        Input file to operate on, DEFAULT: stdin
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Ouput file to write results to, DEFAULT: stdout
  -f OUTPUT_FORMAT, --output_format OUTPUT_FORMAT
                        Used to output formatted strings from matched named
                        groups
```
### Examples

```shell
$ echo "c_code: 1234, entry_id: abcd2," | pipenv run python trex.py "c_code: (?P<ccode>[^,]+), entry_id: (?P<entry>[^,]+)"

{"ccode": "1234", "entry": "abcd2"}
```

```shell
$ echo "c_code: 1234, entry_id: abcd2," | pipenv run python trex.py -f "{ccode}: {entry}" "c_code: (?P<ccode>[^,]+), entry_id: (?P<entry>[^,]+)"

1234: abcd2
```