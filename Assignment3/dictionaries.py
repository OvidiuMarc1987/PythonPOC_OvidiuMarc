# import copy

dataset = []
years_from_file = []


def retrieve_data_from_file():
    # with open(str(input("Please type the name of the file: ")), 'r') as file:
    with open("hlth_silc_23.tsv", 'r') as file:
        raw_content = file.read().replace("\t", ",").replace(" ", "").split("\n")
        return raw_content


def parse_raw_data(datafromfile):
    raw_list = [
        tuple(i.replace(",", " ").split())
        for i in datafromfile
    ]
    raw_list.pop()
    global years_from_file
    years_from_file = raw_list[0][6:]
    raw_list.pop(0)

    data_list = [
        (country, *year, sex,)
        for sex, age, cbirth, lev_perc, unit, country, *year in raw_list
        if (str(lev_perc) == "VGOOD" and str(age) == "Y16-24" and (str(sex[0]) == "F" or str(sex[0]) == "M")
            and str(cbirth) == "NAT" and len(country) == 2 and str(unit) == "PC")
    ]
    # print(f"Number of elements: {len(data_list)}")
    return data_list


def dict_germany(parsed_data):
    dictionary = {
        str(year + str(sex[-1])): [sex[count + 1], sex[-1]]
        for count, year in enumerate(years_from_file)
        for sex in parsed_data if (str(sex[0]) == "DE")
    }

    # print(dictionary)
    return dictionary


def dict_allcountries(parsed_data):
    all_dictionary = {
        str(year + "_" + str(sex[-1]) + "_" + str(sex[count - count])): [sex[count - count], sex[count + 1], sex[-1]]
        for count, year in enumerate(years_from_file)
        for sex in parsed_data
    }

    # print(all_dictionary)
    return all_dictionary


def main():
    global dataset
    dataset = parse_raw_data(retrieve_data_from_file())
    # for i in dataset:
    #     print(i)
    # print(years_from_file)
    ger_dataset = dict_germany(dataset)
    print("one dict that groups all data by year_list for Germany > germany = {2017: [sex, health_index]} ")
    for i in ger_dataset:
        print(i, ger_dataset.get(i))
    print(dataset[6])
    print(dataset[44])

    all_countries_dataset = dict_allcountries(dataset)
    print("two dicts that group all data by country for each year_list")
    for x in all_countries_dataset:
        print(x, all_countries_dataset.get(x))


if __name__ == "__main__":
    main()
