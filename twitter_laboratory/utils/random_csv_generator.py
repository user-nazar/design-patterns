from random import randint
import csv

NAME = ["The first name", "The second name", "The third name", "The fourth name", "The fifth name",
        "The sixth name", "The seventh name", "The eighth name", "The ninth name", "The tenth name"]

DESCRIPTION = ["The first description", "The second description", "The third description", "The fourth description",
               "The fifth description", "The sixth description", "The seventh description", "The eighth description",
               "The ninth description", "The tenth description"]

QUANTITY = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]


def generate_data():
    with open('data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "description", "quantity"])
        for i in range(1000):
            request_data = []

            feature_app_id = i + 1
            request_data.append(feature_app_id)

            name = NAME[randint(0, 2)]
            request_data.append(name)

            description = DESCRIPTION[randint(0, len(DESCRIPTION) - 1)]
            request_data.append(description)

            quantity = QUANTITY[randint(0, len(QUANTITY) - 1)]
            request_data.append(quantity)

            writer.writerow(request_data)


generate_data()
