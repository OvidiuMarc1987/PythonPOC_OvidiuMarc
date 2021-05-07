
def remove_element_from_tuple():
    print("###1st Task")
    tuple_elements = (1, 2, 3, 4)

    print(f"Elements in the tuple: {tuple_elements}")
    element_to_remove = int(input("Type element to remove from tuple: "))

    if element_to_remove in tuple_elements:
        temp_tuple = []
        for x in tuple_elements:
            if x == element_to_remove:
                continue
            else:
                if len(temp_tuple) == 0:
                    temp_tuple.insert(0, x)
                else:
                    temp_tuple.append(x)
                tuple_elements = tuple(temp_tuple)
    else:
        print("Inserted value does not exist in the tuple")
    print(f"Type: {str(type(tuple_elements))}, Content: {tuple_elements}")


def change_last_item_list():
    print("###2nd Task")
    original_list = [1, 2, 3, 4, "almost", "final"]
    print(f"Original list: {original_list}")
    original_list[-1] = "last"
    print(f"Edited list {original_list}")


def extract_strings_from_list():
    print("###3rd Task")
    slist = ['I', 'am', 1, 'list', 'of', 5, 'strings']
    print(f"Initial list: {slist}")
    extracted_strings_list = [x for x in slist if isinstance(x, str)]
    print(f"Extracted list: {extracted_strings_list}")


def generate_matrix():
    x = "x"
    line = "_"
    for i in range(3):
        for z in range(3):
            if z == i:
                print(x, end="")
            else:
                print(line, end="")
        print()


if __name__ == "__main__":
    # 1st task
    remove_element_from_tuple()
    # 2nd task
    change_last_item_list()
    # 3rd task
    extract_strings_from_list()
    # 4th task
    generate_matrix()