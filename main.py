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
