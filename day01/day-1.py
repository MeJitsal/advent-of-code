# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

def code(rotations):
    current = 50
    zero_count = 0
    dial_size = 100

    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == 'R':
            current = (current + distance) % dial_size
        else:
            current = (current - distance) % dial_size

        # Check after every rotation
        if current == 0:
            zero_count += 1

    return zero_count

if __name__ == "__main__":
    # example = open('input-example.txt')
    input = open('input.txt').read().split('\n')
    print(code(input))