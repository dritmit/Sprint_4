import pytest
from main import BooksCollector


class TestBooksCollector:
    @pytest.fixture
    def library(self):
        self.library = BooksCollector()
        self.library.add_new_book('Гордость и предубеждение и зомби')
        self.library.add_new_book('Что делать, если ваш кот хочет вас убить')
        self.library.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        self.library.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        return self.library

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    def test_add_new_book_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('Длинное название, длиннее сорока символов')
        assert len(collector.books_genre) == 0

    def test_set_book_genre_known_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == 'Ужасы'

    def test_set_book_genre_unknown_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Pulp fiction')
        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Незнайка на Луне', 'Фантастика'],
            ['Тараканище', 'Ужасы'],
            ['Три медведя', 'Детективы'],
            ['Колобок', 'Мультфильмы'],
            ['Про Федота-стрельца, удалого молодца', 'Комедии']
        ]
    )
    def test_get_book_genre_all_known_genres(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_book_genre_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Алхимик')
        assert collector.get_book_genre('Алхимик') == ''

    def test_get_books_with_specific_genre_known_genre(self, library):
        specific_genre_books = self.library.get_books_with_specific_genre('Ужасы')
        assert specific_genre_books == ['Гордость и предубеждение и зомби']

    def test_get_books_with_specific_genre_unknown_genre(self, library):
        specific_genre_books = self.library.get_books_with_specific_genre('Pulp fiction')
        assert specific_genre_books == []

    def test_get_books_genre_two_books(self, library):
        assert self.library.get_books_genre() == {'Гордость и предубеждение и зомби': 'Ужасы',
                                                  'Что делать, если ваш кот хочет вас убить': 'Комедии'}

    def test_get_books_for_children_not_in_age_rating_books(self, library):
        assert self.library.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить']

    def test_get_books_for_children_in_age_rating_books(self, library):
        assert ['Гордость и предубеждение и зомби'] not in self.library.get_books_for_children()

    def test_add_book_in_favorites_new_book_in_books_genre_not_in_favourites(self, library):
        self.library.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert self.library.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_new_book_in_books_genre_already_in_favourites(self, library):
        self.library.add_book_in_favorites('Гордость и предубеждение и зомби')
        self.library.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert self.library.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_unknown_book(self, library):
        self.library.add_book_in_favorites('Гордость и предубеждение')
        assert self.library.get_list_of_favorites_books() == []


    def test_delete_book_from_favorites_known_book(self, library):
        self.library.add_book_in_favorites('Гордость и предубеждение и зомби')
        self.library.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert self.library.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_unknown_book(self, library):
        self.library.add_book_in_favorites('Гордость и предубеждение и зомби')
        self.library.delete_book_from_favorites('Гордость и предубеждение')
        assert self.library.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
