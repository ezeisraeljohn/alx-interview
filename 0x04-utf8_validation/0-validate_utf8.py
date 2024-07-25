#!/usr/bin/python3

def validUTF8(data):
    """Validates a data whether or not it is a validUTF8"""
    num_bytes = 0

    # Masks to check UTF-8 encoding
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine number of bytes based on the first byte
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue  # Single byte character (num_bytes == 0)

            if num_bytes == 1 or num_bytes > 4:
                return False  # Invalid number of bytes

        else:
            # Check for follow-up bytes, they should start with 10
            if not (num & mask1 and not (num & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
