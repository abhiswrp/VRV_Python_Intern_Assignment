import csv

def write_to_csv(results, file_name):
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write Requests per IP
        writer.writerow(["IP Address", "Request Count"])
        writer.writerows(results["requests_per_ip"])
        writer.writerow([])

        # Write Most Accessed Endpoint
        writer.writerow(["Most Accessed Endpoint", "Access Count"])
        writer.writerow(results["most_accessed_endpoint"])
        writer.writerow([])

        # Write Suspicious Activity
        writer.writerow(["IP Address", "Failed Login Count"])
        writer.writerows(results["suspicious_activity"].items())
