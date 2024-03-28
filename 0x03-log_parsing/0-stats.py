#!/usr/bin/env python3
"""
This is a module that parses logs by reading standard input/output
line by line and computing the metrics or statistics of the status codes
"""
import sys


def generate_stats(size: int, stat_code_dict: dict) -> None:
    """
    This is a function that generates the statistics or metrics for
    read standard inputs and outputs

    Args:
        size (int) the total size of the files
        stat_code_dict (dict) - dictionary of the allowed status codes

    Returns:
        Nothing
    """
    print(f"File size: {size}")
    for code, count in sorted(stat_code_dict.items()):
        if count != 0:
            print(f"{code}: {count}")


if __name__ == '__main__':
    """ Allowed Status codes """
    allowed_status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0}

    total_file_size = 0  # Total file size

    itr = 0  # iterator or counter of lines parsed

    try:
        for line in sys.stdin:
            file_size = 0  # get file size within the loop
            buff = line.split(' ')
            if len(buff) > 4:
                status_code = buff[-2]
                file_size += int(buff[-1])
                if status_code in allowed_status_codes.keys():
                    allowed_status_codes[status_code] += 1
                total_file_size += file_size  # increment total file size

                itr += 1
            if itr % 10 == 0:
                generate_stats(total_file_size, allowed_status_codes)
                itr = 0

    except (Exception, KeyboardInterrupt) as err:
        raise
    finally:
        generate_stats(total_file_size, allowed_status_codes)
