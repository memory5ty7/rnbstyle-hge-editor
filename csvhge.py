from config import Config
from csvhge.csv_parser import list_csv_files, read_csv, parse_csv
from csvhge.export import print_data
from csvhge.validity_checker import init_defines
from csvhge.file_manager import create_backup

def main():
    init_defines()

    if Config.CREATE_BACKUP == True:
        create_backup(Config.OUTPUT_FILE, Config.BACKUP_FILE)

    csv_files = list_csv_files(Config.INPUT_DIR)

    for file in csv_files:
        rows = read_csv(file)
        data = parse_csv(rows)
        print_data(data, Config.OUTPUT_FILE)

if __name__ == "__main__":
    main()
