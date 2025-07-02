import argparse
from config import Config
from hgecsv.s_parser import parse_s
from hgecsv.export import print_data
from hgecsv.mon_parser import parse_mons, mons

def main():
    parser = argparse.ArgumentParser(description="Convert an hg-engine Trainers file to a correctly formatted Spreadsheet")
    parser.add_argument("filename", help=".s File to Convert to .csv")
    parser.add_argument("--output", "-o", help="Path to the output .csv file (optional)")
    
    args = parser.parse_args()

    try:
        parse_mons(Config.MONDATA_FILE, Config.LEARNSETS_FILE)

        with open(args.filename, 'r') as infile:
            rows = infile.read().splitlines()
            trainers = parse_s(rows)

        if args.output:
            outfile = args.output
        else:
            outfile = Config.DEFAULT_OUTPUT_FILE

        with open(outfile, 'w', encoding='utf-8', newline='') as outfile:
            print_data(trainers, outfile)

    except FileNotFoundError:
        print(f"Error: File '{args.filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()