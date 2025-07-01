import re

def extract_defines(header_path):
    defines = []
    with open(header_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r"#define\s+(\w+)\s+.+", line)
            if match:
                name = match.group(1)
                defines.append(name)
    return defines