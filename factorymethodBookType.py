from enum import Enum


class BookType(Enum):
    
    paper_version = 0,
    audiobook = 1,
    сombo_podpiska_month = 2


class Book:

    def __init__(self, price: float):
        self.__price = price # цена выбранного формата

    def get_price(self) -> float:
        return self.__price


class PaperBook(Book):
    def __init__(self):
        super().__init__(799)


class AudioBook(Book):
    def __init__(self):
        super().__init__(349)


class SubscriptionBookComboMonth(Book):
    def __init__(self):
        super().__init__(549)


def create_book(book_type: BookType) -> Book:
    """
    Factory Method
    """
    factory_dict = {
        BookType.paper_version: PaperBook,
        BookType.audiobook: AudioBook,
        BookType.сombo_podpiska_month: SubscriptionBookComboMonth
    }
    return factory_dict[book_type]()


if __name__ == '__main__':
    for book in BookType:
        my_book = create_book(book)
        print(f'Book type: {book}, price: {my_book.get_price()}')