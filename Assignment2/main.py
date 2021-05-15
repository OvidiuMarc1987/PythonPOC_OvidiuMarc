# Assignment 2 - Lists and Tuples Assignment
import random
shop_list = []


def generate_random_articles():
    articles = list(map(str, input("Type articles that you want in the store: \n").split()))
    print(articles)
    print(type(articles))

    size_of_articles = list(map(str, input("Type the size of the articles.\nEx. X S XS XL, etc.:\n").upper().split()))
    print(size_of_articles)
    print(type(size_of_articles))

    # shop = [(x, y) for x in articles for y in size_of_articles for a in range(399) ]
    shop = [
        (x, y)
        for _ in range(399)
        if (x := articles[int(random.randint(0, (len(articles)) - 1))])
        if (y := size_of_articles[random.randint(0, (len(size_of_articles)) - 1)])
        ]

    return shop


def show_shop():
    for (i, item) in enumerate(shop_list):
        print(i, item)


def sell_last_item():
    shop_list.pop()
    show_shop()
    print(f"Current size of shop {len(shop_list)}")


def sell_any_item():
    item_number = input(f"Type number of article to sell.\nFrom 0-{len(shop_list)}: ")
    shop_list.pop(int(item_number) - 1)
    show_shop()


def add_item():
    item_type = input("Insert new item type: ")
    item_size = input("Insert new item size: ")
    shop_list.append([item_type, item_size])
    show_shop()


def quit_shop():
    quit()


def option_menu():
    option_text = """
        Type number for option and press enter:
            1. Show shop content
            2. Sell last item of shop
            3. Sell any item from shop
            4. Restock shop with new items
            5. Quit
        """
    options = [
        show_shop,
        sell_last_item,
        sell_any_item,
        add_item,
        quit_shop
    ]
    print(option_text)
    selected_option = input("> ")

    if selected_option.isnumeric():
        print(f"Selected option is: {selected_option}")
        options[int(selected_option) - 1]()
    else:
        print("Not a valid option, please try again.")


def main():
    global shop_list
    shop_list = generate_random_articles()
    while True:
        option_menu()


if __name__ == "__main__":
    main()
