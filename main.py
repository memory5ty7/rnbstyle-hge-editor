from config import Config
from csv_parser import list_csv_files, read_csv, parse_csv
from export import print_data
from validity_checker import init_defines

def main():
    init_defines()

    csv_files = list_csv_files(Config.INPUT_DIR)

    for file in csv_files:
        rows = read_csv(file)
        data = parse_csv(rows)
        print_data(data, Config.OUTPUT_FILE)

if __name__ == "__main__":
    main()
