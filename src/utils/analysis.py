from collections import Counter, defaultdict
import re

def count_requests_by_ip(log_data):
    ip_counter = Counter()
    for entry in log_data:
        match = re.match(r'^([\d\.]+)', entry)
        if match:
            ip_counter[match.group(1)] += 1
    return ip_counter.most_common()

def most_frequent_endpoint(log_data):
    endpoint_counter = Counter()
    for entry in log_data:
        match = re.search(r'"[A-Z]+\s(/[\w\/\-]*)', entry)
        if match:
            endpoint_counter[match.group(1)] += 1
    return endpoint_counter.most_common(1)[0] if endpoint_counter else ("N/A", 0)

def detect_suspicious_activity(log_data, threshold=10):
    failed_attempts = defaultdict(int)
    for entry in log_data:
        if '401' in entry:
            match = re.match(r'^([\d\.]+)', entry)
            if match:
                failed_attempts[match.group(1)] += 1
    return {ip: count for ip, count in failed_attempts.items() if count > threshold}
