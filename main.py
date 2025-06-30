from config import Config
from csv_parser import list_csv_files, read_csv, parse_csv
from exporter import print_data
from header_parser import extract_defines

headers = [
    Config.ABILITY_HEADER,
    Config.BATTLE_HEADER,
    Config.ITEM_HEADER,
    Config.MOVE_HEADER,
    Config.SPECIES_HEADER,
    Config.TRAINERCLASS_HEADER
]

def main():
    for header in headers:
        extract_defines(header)

    csv_files = list_csv_files(Config.INPUT_DIR)

    for file in csv_files:
        rows = read_csv(file)
        data = parse_csv(rows)
        print_data(data, Config.OUTPUT_FILE)

if __name__ == "__main__":
    main()
