def main(city:str, pet:str):
    print(city+"_"+pet)

if __name__ == "__main__":
    print(" Welcome to Band Name Generator :) ")
    print(" I would like to ask two questions to generate a name for your band")
    city_name : str = input(" What is the name of your city? ")
    pet_name : str = input(" What was your pet's name? ")
    main(city=city_name, pet=pet_name)