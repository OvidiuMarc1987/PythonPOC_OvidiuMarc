import random
first_set, second_set = (set(), )*2


def generate_random_sets():

    random_numbers = [
        int(number)
        for _ in range(20)
        if (number := int(random.randint(0, 40)))
    ]
    first_list_of_numbers, second_list_of_numbers = set(random_numbers[:10]), set(random_numbers[10:20])
    # <DEBUG PART
    # print(len(first_list_of_numbers))
    # print(len(second_list_of_numbers))
    # print(first_list_of_numbers, second_list_of_numbers)
    # >DEBUG PART
    if len(first_list_of_numbers) == 10 and len(second_list_of_numbers) == 10:
        return first_list_of_numbers, second_list_of_numbers
    else:
        return generate_random_sets()


def union_sets(first_param, second_param):
    print(f"Union: {first_param.union(second_param)}")


def intersection_sets(first_param, second_param):
    print(f"Intersection: {first_param.intersection(second_param)}")


def difference_sets(first_param, second_param):
    print(f"Difference: {first_param.difference(second_param)}")


def symmetric_sets(first_param, second_param):
    print(f"Symmetric: {first_param.symmetric_difference(second_param)}")


def quit_app():
    quit()


def option_menu(first_param, second_param):
    option_text = """
        Type number for option and press enter:
            1. Compute the union of two sets.
            2. Compute the intersection of two sets.
            3. Compute the difference between two　sets.
            4. Compute the symmetric difference between sets.
            5. Quit
        """
    options = [
        union_sets,
        intersection_sets,
        difference_sets,
        symmetric_sets,
        quit_app
    ]
    print(option_text)
    selected_option = input("> ")

    if selected_option.isnumeric():
        print(f"Selected option is: {selected_option}")
        if int(selected_option) == 5:
            options[int(selected_option) - 1]()
        options[int(selected_option) - 1](first_param, second_param)

    else:
        print("Not a valid option, please try again.")


def main():
    global first_set
    global second_set
    first_set, second_set = generate_random_sets()
    print(f"First set: {first_set}\nSecond set: {second_set}")
    print(f"First set type: {type(first_set)}\nSecond set type: {type(second_set)}")
    while True:
        option_menu(first_set, second_set)


if __name__ == "__main__":
    main()
