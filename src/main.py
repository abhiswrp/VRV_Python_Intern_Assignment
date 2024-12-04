from utils.parser import parse_log
from utils.analysis import count_requests_by_ip, most_frequent_endpoint, detect_suspicious_activity
from utils.output import write_to_csv

def main():
    log_file = "../data/sample.log"
    log_data = parse_log(log_file)

    requests_per_ip = count_requests_by_ip(log_data)
    most_accessed_endpoint = most_frequent_endpoint(log_data)
    suspicious_activity = detect_suspicious_activity(log_data)

    results = {
        "requests_per_ip": requests_per_ip,
        "most_accessed_endpoint": most_accessed_endpoint,
        "suspicious_activity": suspicious_activity
    }

    print("Requests Per IP:")
    for ip, count in requests_per_ip:
        print(f"{ip} - {count}")

    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed_endpoint[0]} (Accessed {most_accessed_endpoint[1]} times)")

    print("\nSuspicious Activity Detected:")
    for ip, count in suspicious_activity.items():
        print(f"{ip} - {count}")

    write_to_csv(results, "../results/log_analysis_results.csv")
    print("\nResults saved to ../results/log_analysis_results.csv")

if __name__ == "__main__":
    main()
