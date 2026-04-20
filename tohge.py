from config import Config
from csvhge.csv_parser import list_csv_files, read_csv, parse_csv
from csvhge.export import print_data
from csvhge.file_manager import create_backup

import sys

def main():
    if Config.CREATE_BACKUP == True:
        create_backup(Config.OUTPUT_FILE, Config.BACKUP_FILE)

    debug = False

    if "debug" in sys.argv:
        debug = True

    total_data = []

    if Config.USE_CSV_ORDER:
        csv_files = Config.csv_order
    else:
        csv_files = list_csv_files(Config.INPUT_DIR)


    for file in csv_files:
        print(f"Processing file: {file}")
        rows = read_csv(file)
        data = parse_csv(rows, debug)
        total_data += data

    print_data(data, Config.OUTPUT_FILE)

if __name__ == "__main__":
    main()
