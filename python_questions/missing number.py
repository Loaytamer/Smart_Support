def missingNum(my_list):
    no_of_elements = len(my_list)
    total_sum = (no_of_elements+1) * (no_of_elements+2) / 2
    list_sum = sum(my_list)
    return total_sum - list_sum
