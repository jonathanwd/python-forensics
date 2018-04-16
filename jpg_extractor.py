"""
This script scans files for hidden jpg files. If a file contains a jpg file,
it will be extracted using the jpg file's header and trailer file signatures.
"""

import argparse
import binascii

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', nargs=1,  metavar='input_file', required=True, help='Name/location of the input file')
    parser.add_argument('-o', nargs=1, metavar='output_file', default=["out.jpg"], help='Name/location of the output file')
    args = parser.parse_args()
    return args

def extract_jpg(in_file, out_file):
    jpg_header = 'ffd8ff'
    jpg_trailer = 'ffd9'
    with open(in_file, 'rb') as f:
        content = f.read()
    hex = binascii.hexlify(content)
    found = hex.split(jpg_header)[1].split(jpg_trailer)
    hex_string = jpg_header + found[0] + jpg_trailer
    binary_string = binascii.unhexlify(hex_string)
    f= open(out_file,"w+")
    f.write(binary_string)

def main():
    args = parse_args()
    filename = args.i[0]
    outfile = args.o[0]
    extract_jpg(filename, outfile)

if __name__== "__main__":
  main()
