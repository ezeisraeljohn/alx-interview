#!/usr/bin/python3

import sys
from collections import defaultdict


def print_stats(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    total_size = 0
    status_codes = defaultdict(int)
    count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 9:
                continue

            ip, _, _, date, request, _, status_code, file_size = (
                parts[0],
                parts[1],
                parts[2],
                parts[3],
                parts[4:7],
                parts[7],
                parts[8],
                parts[9],
            )
            if status_code.isdigit() and request == '"GET /projects/260 HTTP/1.1"':
                total_size += int(file_size)
                status_codes[int(status_code)] += 1

            count += 1
            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
