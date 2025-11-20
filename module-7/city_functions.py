# CSD325: Advanced Python
# Module 7.2 Assignment: Test Cases
# Isaac Ellingson
# 11/20/2025

def city_name(city: str, country: str, population: int = None, language: str = None):
    result = city + ", " + country

    if (population is not None):
        result += " - population " + str(population)

    if (language is not None):
        result += ", " + language

    return result


if __name__ == '__main__':
    print("City + Country: " + city_name("Santiago", " Chile"))
    print("City + Country + Pop: " + city_name("Santiago", "Chile", 5000000))
    print("City + Country + Language: " + city_name("Santiago", "Chile", language = "Spanish"))
    print("City + Country + Pop + Language: " + city_name("Santiago", "Chile", 5000000, "Spanish"))
