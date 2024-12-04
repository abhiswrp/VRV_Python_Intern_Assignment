import re

def parse_logs(file_path):
    log_entries = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'(?P<ip>\d+\.\d+\.\d+\.\d+) .* "(?P<method>\w+) (?P<endpoint>\S+).*" (?P<status>\d+)', line)
            if match:
                log_entries.append(match.groupdict())
    return log_entries
