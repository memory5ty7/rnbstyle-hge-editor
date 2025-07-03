import re
from config import Config

trainerGenders = []

def extract_trainer_genders(filepath):
    global trainerGenders

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'const u8 sTrainerGenders\[\] = \{(.*?)\};', content, re.DOTALL)
    if not match:
        raise ValueError("sTrainerGenders array not found")

    array_block = match.group(1)

    pattern = r'\[\s*(TRAINERCLASS_[A-Z0-9_]+)\s*\]\s*=\s*(TRAINER_MALE|TRAINER_FEMALE|TRAINER_DOUBLE)'
    entries = re.findall(pattern, array_block)

    trainerGenders = {k: v for k, v in entries}

extract_trainer_genders(Config.TRGENDER_FILE)