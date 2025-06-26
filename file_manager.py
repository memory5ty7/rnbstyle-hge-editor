import os
import csv

def list_csv_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".csv")]

def read_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        return list(csv.reader(f))

def write_asm(asm_lines, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(line + '\n' for line in asm_lines)
