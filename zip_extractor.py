"""
This script scans files for hidden zip files. If a file contains a zip file,
it will be extracted using the zip file's header and trailer file signatures.
"""

import argparse
import binascii

def parse_args():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-i', nargs=1,  metavar='input_file', required=True, help='Name/location of the input file')
    parser.add_argument('-o', nargs=1, metavar='output_file', default=["out.zip"], help='Name/location of the output file')
    args = parser.parse_args()
    return args

def extract_zip(in_file, out_file):
    zip_header = '504b0304'
    zip_trailer = '504b0506'
    with open(in_file, 'rb') as f:
        content = f.read()
    hex = binascii.hexlify(content)
    found = hex.split(zip_header)[1].split(zip_trailer)
    hex_string = zip_header + found[0] + zip_trailer + found[1][:36]
    binary_string = binascii.unhexlify(hex_string)
    f= open(out_file,"w+")
    f.write(binary_string)

def main():
    args = parse_args()
    filename = args.i[0]
    outfile = args.o[0]
    extract_zip(filename, outfile)

if __name__== "__main__":
  main()
