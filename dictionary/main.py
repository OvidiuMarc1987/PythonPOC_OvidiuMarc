from collections.abc import Mapping, Sequence, Iterable


def dictionaries_sets():
    mydictionary = {}
    example_dictionary = dict(one=1, two=2, three=3)
    iterable_example = zip(['one', 'two', 'three'],[1, 2, 3])
    population = [
        ('Berlin', 1234),
        ('Paris', 2345),
        ('London', 3456)
    ]

    population_as_a_dict = {city: citizen for city, citizen in population}
    print(population_as_a_dict)

    cities = [
        ('Berlin', 1234, 543),
        ('Paris', 2345, 654),
        ('London', 3456, 654)
    ]

    cities_by_name = {
        city: [citizen, size] for (city, citizen, size) in cities
    }

    print(cities_by_name)


def some_tuples():
    a, b, *rest = range(10)
    print(a, b, rest)

    for x, y in [(2, 3), (4, 5), (6, 7)]:
        print(x ** y)


if __name__ == '__main__':
    dictionaries_sets()
    some_tuples()
    dictionaries_sets()
