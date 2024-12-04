import re

def parse_log(file_path):
    log_entries = []
    with open(file_path, 'r') as file:
        for line in file:
            log_entries.append(line.strip())
    return log_entries
