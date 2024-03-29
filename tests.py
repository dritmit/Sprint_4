import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('Длинное название, длиннее сорока символов')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_known_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_set_book_genre_unknown_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Pulp fiction')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

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
        assert library.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби']

    def test_get_books_with_specific_genre_unknown_genre(self, library):
        assert library.get_books_with_specific_genre('Pulp fiction') == []

    def test_get_books_genre_two_books(self, library):
        assert library.get_books_genre() == {'Гордость и предубеждение и зомби': 'Ужасы',
                                                  'Что делать, если ваш кот хочет вас убить': 'Комедии'}

    def test_get_books_for_children_not_in_age_rating_books(self, library):
        assert library.get_books_for_children() == ['Что делать, если ваш кот хочет вас убить']

    def test_get_books_for_children_in_age_rating_books(self, library):
        assert ['Гордость и предубеждение и зомби'] not in library.get_books_for_children()

    def test_add_book_in_favorites_new_book_in_books_genre_not_in_favourites(self, library):
        library.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert library.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_new_book_in_books_genre_already_in_favourites(self, library):
        library.add_book_in_favorites('Гордость и предубеждение и зомби')
        library.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert library.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_unknown_book(self, library):
        library.add_book_in_favorites('Гордость и предубеждение')
        assert library.get_list_of_favorites_books() == []


    def test_delete_book_from_favorites_known_book(self, library):
        library.add_book_in_favorites('Гордость и предубеждение и зомби')
        library.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert library.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_unknown_book(self, library):
        library.add_book_in_favorites('Гордость и предубеждение и зомби')
        library.delete_book_from_favorites('Гордость и предубеждение')
        assert library.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']
