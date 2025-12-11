# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///


def parse_ranges(lines: list[str]) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []

    for line in lines:
        # skip empty lines
        if not line.strip():
            continue

        # each line may have multiple comma-separated ranges
        for part in line.split(","):
            part = part.strip()
            if not part:
                continue  # skip empty entries
            left, right = part.split("-")
            low = int(left)
            high = int(right)
            ranges.append((low, high))

    return ranges

def invalid_ids(ranges):
    total_invalid_id=0
    for low, high in ranges:
        low_len=len(str(low))
        high_len=len(str(high))
        for length in range (low_len, high_len+1):
            if length%2==1: #is it even?
                continue
            half_len=length//2

            if half_len==1:
                start=1
            else:
                start = 10**(half_len-1)
            
            end=10**half_len-1

            for half in range(start, end + 1):
                n = int(str(half) * 2)
                if n > high:
                    break
                if n >= low:
                    total_invalid_id += n
    return total_invalid_id



if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().splitlines()

    input = parse_ranges(input)
    total = invalid_ids(input)
    print(total)
