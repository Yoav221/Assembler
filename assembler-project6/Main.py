import sys
from hack_assembler import Assembler


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    # Get input path from command line argument
    input_path = sys.argv[1]

    # Generate output path in same directory as input file
    # If input is "path/to/file.asm", output will be "path/to/file.hack"
    output_path = input_path.replace('.asm', '.hack')

    # Create and run assembler
    assembler = Assembler(input_file=input_path, output_file=output_path)
    assembler.translate()


if __name__ == "__main__":
    main()