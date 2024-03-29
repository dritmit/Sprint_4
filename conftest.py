import pytest
from main import BooksCollector


@pytest.fixture
def library():
    library = BooksCollector()
    library.add_new_book('Гордость и предубеждение и зомби')
    library.add_new_book('Что делать, если ваш кот хочет вас убить')
    library.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
    library.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
    return library
