# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def number_data_types():
    print(2 / 3)


def string_data_types():
    suffix = "na"
    prefix = "Ba"
    print(prefix + "na" + suffix)
    word = prefix + "na" + suffix
    print(word)
    print(word[0:3])
    print(word[-2:])


def list_data_types():
    pass


def fibonacci():
    a, b = 0, 1
    while b < 20:
        print(b)
        a, b = b, a + b


def flow_control():

    animals = ["dog", "cat", "cow"]
    for animal in animals:
        print(animal)
        print(animals.index(animal))


def call_function():
    x = 11

    def another_func(x):
        print(x + 11)
    print(x)
    return another_func


if __name__ == '__main__':
    print_hi('PyCharm')
    number_data_types()
    string_data_types()
    list_data_types()
    fibonacci()
    flow_control()
    a = call_function()
    a(2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
