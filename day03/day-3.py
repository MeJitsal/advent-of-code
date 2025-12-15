# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

from typing import List


def digits(n: int) -> List[int]:
    return [int(ch) for ch in str(abs(n))]


def two_digit_numbers(d: List[int]) -> List[int]:
    # all ordered pairs (i < j) turned into 2-digit numbers
    return [10 * d[i] + d[j]
            for i in range(len(d))
            for j in range(i + 1, len(d))]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        nums = [int(line.strip()) for line in f if line.strip()]
    total=0

    for n in nums:
        d = digits(n)
        two_digit_list = two_digit_numbers(d)
        m= max(two_digit_list) 

        total += m
    print(total)
