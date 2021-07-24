import json
import re


def search_exact_match(event):

    search_result = []

    try:
        cars_json = open('./data/cars.json')
        all_cars_array = json.load(cars_json)
        car_name_query_sanitised = event['car_name_query']

        for car in all_cars_array:
            car_name_sanitised = re.sub(r'[^A-Za-z0-9 ]+', '', car['Name'].lower())
            if car_name_sanitised == car_name_query_sanitised:
                search_result.append(car)
                break

        return search_result

    except Exception as error:
        print('Error searching for exact match: ', error)
        raise error


def search_similar_match(event):

    search_result = []

    try:
        cars_json = open('./data/cars.json')
        all_cars_array = json.load(cars_json)
        search_terms_set = set(event['car_name_query'].split())

        for car in all_cars_array:
            car_name_sanitised = re.sub(r'[^A-Za-z0-9 ]+', '', car['Name'].lower())
            car_name_set = set(car_name_sanitised.split())

            if (car_name_set & search_terms_set):
                search_result.append(car)

        return search_result

    except Exception as error:
        print('Error searching similar match: ', error)
        raise error