from pathlib import Path

def create_backup(original_path, backup_path):
    original_file = Path(original_path)
    backup_file = Path(backup_path)

    if not backup_file.exists():
        with original_file.open('rb') as src, backup_file.open('wb') as dst:
            dst.write(src.read())
            print(f"Backup created at: {backup_file}")