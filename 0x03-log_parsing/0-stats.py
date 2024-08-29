#!/usr/bin/python3
import sys
import signal

# Global variables to store the total file size and status code counts
total_file_size = 0
status_code_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}


def print_stats():
    """
    Print the accumulated statistics.
    """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))


def signal_handler(sig, frame):
    """
    Handle the CTRL+C signal by printing the stats and exiting.
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 7:
            ip_address = parts[0]
            status_code = parts[-2]
            file_size = parts[-1]

            # Update total file size
            try:
                total_file_size += int(file_size)
            except ValueError:
                continue

            # Update status code count
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            line_count += 1

            # Every 10 lines, print the stats
            if line_count == 10:
                print_stats()
                line_count = 0

except KeyboardInterrupt:
    # Handle any remaining lines and print final stats
    print_stats()
    sys.exit(0)

# Final stats after all input is processed
print_stats()
