from faker import Faker


faker = Faker()

def select_metro_station():
    station_metro = faker.random_int(min=0, max=224)
    return station_metro
