class Student:

    def __init__(self, name, age, total_score):
        self.name = name
        self.age = age
        self.total_score = total_score

    def increment_score(self):
        if self.total_score >= 90:
            self.total_score = 100
        return self.total_score

    def average_score(self, lst: list):
        return sum(lst) / len(lst)

    def display(self):
        print("_" * 40)
        print(f"Name: {self.name}\nAge: {self.age}\nTotal score: {self.total_score}")
        print("_" * 40)


def main():
    st1 = Student("John", 18, 93)
    st2 = Student("Smith", 17, 56)

    st1.lst_for_scores = [15, 16, 14, 20, 20, 16.5]
    st2.lst_for_scores = [19, 17, 11, 19.5, 20, 14.5]

    st1.display()
    st2.display()

    print(f"{st1.name}, Your final score is {st1.increment_score()}")
    print()
    print(f"{st1.name}, Your average score is {st1.average_score(st1.lst_for_scores)}")
    print("*" * 20)
    print(f"{st2.name}, Your final score is {st2.increment_score()}")
    print()
    print(f"{st2.name}, Your average score is {st1.average_score(st2.lst_for_scores)}")


if __name__ == '__main__':
    main()















