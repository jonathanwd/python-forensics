"""
This script scans files for hidden files. The user specifies a header and trailer
signature. If a file contains a file with matching signatures, it will be extracted.
"""

import argparse
import binascii

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', nargs=1,  metavar='input_file', required=True, help='Name/location of the input file')
    parser.add_argument('-o', nargs=1, metavar='output_file', default=["out"], help='Name/location of the output file')
    args = parser.parse_args()
    return args

def extract_file(in_file, out_file, header, trailer, additional_bytes):
    with open(in_file, 'rb') as f:
        content = f.read()
    hex = binascii.hexlify(content)
    found = hex.split(header)[1].split(trailer)
    trailing_hex = additional_bytes * 2
    hex_string = header + found[0] + trailer + found[1][:int(trailing_hex)]
    binary_string = binascii.unhexlify(hex_string)
    f= open(out_file,"w+")
    f.write(binary_string)

def main():
    args = parse_args()
    filename = args.i[0]
    outfile = args.o[0]
    header = raw_input("Enter the file signature header (no spaces): ").lower()
    trailer = raw_input("Enter the file signature trailer (no spaces): ").lower()
    additional_bytes = raw_input("Enter the number of additional bytes after the file signature trailer: ")
    extract_file(filename, outfile, header, trailer, additional_bytes)

if __name__== "__main__":
  main()
