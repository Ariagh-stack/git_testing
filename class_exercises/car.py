class Car:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self) -> str:
        return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}"


def main():
    my_car = Car("Lexus", "Strawberry", 2019)
    print(my_car.get_info())


if __name__ == "__main__":
    main()
