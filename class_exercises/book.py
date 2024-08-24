class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def display_info(self) -> None:
        print("_" * 40)
        print(f'Title: {self.title}\nAuthor: {self.author}\nYear of publish: {self.year}')
        print("_" * 40)


def main():
    b1 = Book('The poor', 'Victor Hogo', 1989)
    b2 = Book('Shahnameh', 'Ferdosi', 1415)

    b1.display_info()
    b2.display_info()


if __name__ == '__main__':
    main()
