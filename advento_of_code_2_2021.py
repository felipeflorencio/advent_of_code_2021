from load_file import loadInput

def first():
    input_list = loadInput("day02")
    input_parsed = list(map(lambda i: i.replace("\n", ""), input_list))
    
    forward = 0
    down = 0
    up = 0

    for i in input_parsed:
        parsed = i.split(" ")
        key = parsed[0]
        value = parsed[1]

        if key == "forward":
            forward += int(value)
        if key == "up":
            up += int(value)
        if key == "down":
            down += int(value)

    depth = up - down

    return abs(forward * depth)


def second():
    input_list = loadInput("day02")
    input_parsed = list(map(lambda i: i.replace("\n", ""), input_list))
    
    horizontal = 0
    aim = 0
    depth = 0

    for i in input_parsed:
        parsed = i.split(" ")
        key = parsed[0]
        value = parsed[1]

        if key == "forward":
            horizontal += int(value)
            depth += int(value) * aim
        if key == "up":
            aim -= int(value)
        if key == "down":
            aim += int(value)
     
    return abs(horizontal * depth)


if __name__ == "__main__":
    print(f"Result first is: {first()}")
    print(f"Result second is: {second()}")
