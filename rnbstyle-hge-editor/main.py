from config import Config
from file_manager import list_csv_files, read_csv
from csv_parser import parse_csv
from exporter import print_data
from header_parser import extract_defines

headers = [
    Config.SPECIES_HEADER,
    Config.MOVE_HEADER,
    Config.ITEM_HEADER,
    Config.ABILITY_HEADER,
    Config.TRAINERCLASS_HEADER
]

def main():
    defines = {}
    for header in headers:
        defines = extract_defines(header)

    csv_files = list_csv_files(Config.INPUT_DIR)

    for file in csv_files:
        rows = read_csv(file)
        data = parse_csv(rows)
        print_data(data, Config.OUTPUT_FILE)

if __name__ == "__main__":
    main()
