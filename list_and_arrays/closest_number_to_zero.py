def closest_to_zero(temperature_list):
    negative_numbers = [i for i in temperature_list if i < 0]
    positive_numbers = [i for i in temperature_list if i > 0]

    return min(positive_numbers)


temperature_list = [-5, -4, -2, 12, -40, 4, 2, 18, 11, 5]

closest_to_zero(temperature_list)
