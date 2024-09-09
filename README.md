# Introduction
Command-line argument parsing is an essential skill in Python programming, allowing developers to create flexible and user-friendly scripts. The `argparse` module, part of Python’s standard library, offers a powerful and intuitive way to handle command-line arguments. This article explores a practical example of using argparse through a simple Python script.

## What is Argparse
The `argparse` module is designed to manage command-line arguments for Python scripts. It enables you to specify the expected arguments, parse them when the script runs, and provide helpful error messages if the user inputs invalid data.

## Example Script Overview
In this example, we demonstrate how to use argparse to parse command-line arguments related to a person’s name and age. The script formats and displays a message based on the provided arguments.

### Script Example

```
import argparse

parser = argparse.ArgumentParser(
    description="Process some personal information.", allow_abbrev=False
)
parser.add_argument("-n", "--name", required=False, help="Name of the user")
parser.add_argument("-f", "--family", required=False, help="Family name of the user")
parser.add_argument("-a", "--age", type=int, required=False, help="Age of the user")
try:
    args = parser.parse_args()
    print(f"Name: {args.name}")
    print(f"Family: {args.family}")
    print(f"Age: {args.age}")
except SystemExit:
    print("invalid command")
    exit()

```

* Accepts `-n` or `--name` for the first name.
* Accepts `-f` or `--family` for the family name.
* Accepts `-a` or `--age` for the age.
* Outputs a formatted string based on the provided arguments.
```
parser = argparse.ArgumentParser(description='Example script.', allow_abbrev=False)
```
The ArgumentParser object is created with a description of the script. The `allow_abbrev=False` parameter ensures that arguments must be specified fully and not abbreviated.

### Adding Arguments
```
parser.add_argument('-n', '--name', type=str, help='Your first name.')
parser.add_argument('-f', '--family', type=str, help='Your family name.')
parser.add_argument('-a', '--age', type=int, help='Your age.')
```
Three optional arguments are defined: `--name`, `--family`, and `--age`. Each argument is associated with a help description and type.

### Parsing Arguments
```
try:
    args = parser.parse_args()
except SystemExit:
    print("Invalid command")
    exit()
```

The `parse_args()` method processes command-line inputs. If invalid arguments are provided, a `SystemExit` exception is caught, and an error message is printed.

### Generating Output
```
print(f"Name: {args.name}")
print(f"Family: {args.family}")
print(f"Age: {args.age}")
```
The script constructs an output message based on the provided arguments, handling various cases to generate an appropriate message or an “Invalid command” response.

### Running the Script
To run the script, use the following command:

```
$ python main.py -n [first name] -f [family name] -a [age]
```

Replace `[first name]`, `[family name]`, and `[age]` with your actual values. You can omit any of these options to see how the script responds.
#### For Example
```
$ python main.py -n Alice -f Smith --age 25
```