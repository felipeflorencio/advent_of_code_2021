from load_file import loadInput

def first():
    input_list = loadInput("day03")
    input_parsed = list(map(lambda i: i.replace("\n", ""), input_list))
    
    ## This we will now how much we should loop for each
    bit_count = len(list(input_parsed[0]))

    gamma_rate = ""
    epsilon_rate = ""

    for i in range(0,bit_count):
        count_one = 0
        count_zero = 0

        for j in input_parsed:
            if int(list(j)[i]) == 1:
                count_one += 1
            else:
                count_zero += 1

        if count_one > count_zero:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    decimal_gamma = int(gamma_rate,2)
    decimal_epsilon = int(epsilon_rate,2)

    return decimal_gamma * decimal_epsilon


def second():
    input_list = loadInput("day03")
    input_parsed = list(map(lambda i: i.replace("\n", ""), input_list))

    oxygen_generator_rating = filtered_for_bit(True, input_parsed)[0]
    CO2_scrubber_rating = filtered_for_bit(False, input_parsed)[0]

    decimal_oxygen = int(oxygen_generator_rating,2)
    decimal_CO2_scrubber = int(CO2_scrubber_rating,2)

    return decimal_oxygen * decimal_CO2_scrubber



def filtered_for_bit(positive, input_parsed):
    bit_count = len(list(input_parsed[0]))

    evaluate_list = input_parsed
    index = 0
    while len(evaluate_list) > 1:
        
        count_zero = 0
        count_one = 0
        for binary in evaluate_list:
            number = int(binary[index])
            if number == 1:
                count_one += 1
            else:
                count_zero += 1


        number_to_get = 0
        if positive:
            if count_one == count_zero:
                number_to_get = 1
            elif count_one > count_zero:
                number_to_get = 1
        else:
            if count_one < count_zero and len(evaluate_list) > 2:
                number_to_get = 1

        
        evaluate_list = list(filter(lambda x: int(list(x)[index]) == number_to_get, evaluate_list))

        index += 1    


    return evaluate_list


if __name__ == "__main__":
    print(f"Result first is: {first()}")
    print(f"Result second is: {second()}")