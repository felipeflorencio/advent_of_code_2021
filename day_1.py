
def first():
    input_list = []
    
    with open("day01.txt", "r") as input:
        input_list = list(map(int, input.readlines()))

    day1 = 0
    for (i, value) in enumerate(input_list):
        if value > input_list[i-1]:
            day1 += 1

    return day1


def second():
    input_list = []
    
    with open("day01.txt", "r") as input:
        input_list = list(map(int, input.readlines()))

    day1_partTwo = 0
    for (i, value) in enumerate(input_list):

        if (i + 3) >= len(input_list):
            break

        first_measure = (value + input_list[i+1] + input_list[i+2])
        second_measure = (input_list[i+1] + input_list[i+2] + input_list[i+3])
        if second_measure > first_measure:
            day1_partTwo += 1

    return day1_partTwo


if __name__ == "__main__":
    print(f"Result first is: {first()}")
    print(f"Result second is: {second()}")
