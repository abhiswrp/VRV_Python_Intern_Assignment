import csv

def generate_report(results, output_path):
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write IP Request Counts
        writer.writerow(['IP Address', 'Request Count'])
        writer.writerows(results['ip_counts'])
        
        # Write Most Accessed Endpoint
        writer.writerow([])
        writer.writerow(['Most Frequently Accessed Endpoint', 'Access Count'])
        writer.writerow(results['most_accessed_endpoint'])

        # Write Suspicious Activity
        writer.writerow([])
        writer.writerow(['IP Address', 'Failed Login Count'])
        writer.writerows(results['suspicious_ips'].items())
