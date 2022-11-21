def first_val_equals_to_last(list_of_numbers):
    val1 = list_of_numbers[0]
    last_value = list_of_numbers[len(list_of_numbers) - 1]
    if val1 == last_value:
        return True
    else:
        return False






if __name__ == '__main__':
    numbers_x = [10, 20,30, 40, 10]
    numbers_y = [75, 65, 35,75, 30]
    first_val_equals_to_last(numbers_x)
    print(first_val_equals_to_last(numbers_x))
    print(first_val_equals_to_last(numbers_y))




