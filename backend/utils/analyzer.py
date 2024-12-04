from collections import Counter
from config.settings import FAILED_LOGIN_THRESHOLD
def analyze_data(log_entries):
    results = {}
    ip_counts = Counter(entry['ip'] for entry in log_entries)
    results['ip_counts'] = ip_counts.most_common()
    endpoint_counts = Counter(entry['endpoint'] for entry in log_entries)
    results['most_accessed_endpoint'] = endpoint_counts.most_common(1)[0]
    failed_logins = Counter(entry['ip'] for entry in log_entries if entry['status'] == '401')
    suspicious_ips = {ip: count for ip, count in failed_logins.items() if count > FAILED_LOGIN_THRESHOLD}
    results['suspicious_ips'] = suspicious_ips
    return results