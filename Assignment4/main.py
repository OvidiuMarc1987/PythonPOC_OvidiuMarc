from raw_data import raw_data, description
parsed_data = {}
list_of_countries = []


def get_raw_data(data, year_list):
    dictionary_data = {
        # str(country[0]): tuple(coverage for coverage in country[1])
        str(country[0]): [
                ##WORKS
                {'year': year, 'coverage': coverage_value[index].strip()}
                for index, year in enumerate(year_list, )
                for coverage_value in [country[1]] #if not (print(len(coverage_value)))
                ##
        ]
        # for key, country in enumerate(data)  # if not (print(country))
        for country in data  # if not (print(country))
    }
    print(dictionary_data)
    # for g in dictionary_data:
    #     for f in dictionary_data[g]:
    #         print(g, f)
    return dictionary_data


def get_data_for_specific_year(year, data):
    coverage_for_specific_year = [
        [country, coverage_data]
        for country in data
        for coverage_data in data[country]
        for coverage_data_values in coverage_data.values() if (year in coverage_data_values)
    ]
    # print(coverage_for_specific_year)
    return coverage_for_specific_year


def get_data_for_specific_country(selected_country, data):

    coverage_for_specific_country = [
        [country, coverage_data]
        for country in data
        for coverage_data in data[country] if (str(selected_country).upper() in country)
        # for coverage_data_values in coverage_data.values() if (year in coverage_data_values)
    ]
    # print(coverage_for_specific_year)
    return coverage_for_specific_country


def average_coverage_for_country(selected_country, data):
    sum_of_values = []
    result = get_data_for_specific_country(selected_country, data)
    for coverage in result:
        coverage_value = coverage[1]['coverage']
        if coverage_value.isnumeric():
            sum_of_values.append(int(coverage_value))
    print(f'Values {sum_of_values} and number of elements {len(sum_of_values)}')
    coverage_average = sum(sum_of_values) / len(sum_of_values)
    return coverage_average


def main():
    global parsed_data
    parsed_data = get_raw_data(raw_data, description[1])

    results_for_year = get_data_for_specific_year(input("Data for year: "), parsed_data)
    for result in results_for_year:
        print(result)

    global list_of_countries
    list_of_countries = [
        country[0]
        for country in raw_data
    ]
    results_for_country = get_data_for_specific_country(input(
        f"List of countries:\n{list_of_countries}\nType country: "), parsed_data)
    for result in results_for_country:
        print(result)

    results_average_coverage_for_country = average_coverage_for_country(input(
        f"List of countries:\n{list_of_countries}\nType country to retrieve average coverage: "), parsed_data)
    print(f'Average coverage for country: {results_average_coverage_for_country}')


if __name__ == "__main__":
    main()
