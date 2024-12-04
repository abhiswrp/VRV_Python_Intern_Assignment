from utils.parser import parse_logs
from utils.analyzer import analyze_data
from utils.reporter import generate_report
from config import SAMPLE_LOG_PATH, CSV_OUTPUT_PATH

def main():
    log_entries = parse_logs(SAMPLE_LOG_PATH)
    results = analyze_data(log_entries)
    generate_report(results, CSV_OUTPUT_PATH)

if __name__ == "__main__":
    main()
