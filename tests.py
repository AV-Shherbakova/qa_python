import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        "book_title, expected_count",
        [
            ['1984', 1],
            ['Моби Дик', 1]
        ]
    )
    def test_add_new_book_expected_count(self, book_title, expected_count):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        collector.add_new_book(book_title)
        assert len(collector.books_genre) == expected_count

    @pytest.mark.parametrize(
        "book_title, genre, expected_genre",
        [
            ['Моби Дик', 'Фантастика', 'Фантастика'],
            ['1984', 'Драма', ''],
            ['Сияние', 'Ужасы', 'Ужасы'],
            ['Моби Дик', 'Неизвестный жанр', '']
        ]
    )
    def test_set_book_genre(self, book_title, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, genre)
        assert collector.get_book_genre(book_title) == expected_genre

    def test_get_book_genre_by_book_name(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_book_genre('Сияние') == 'Ужасы'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == ['1984']

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_books_genre() == {'1984': 'Фантастика'}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Залив')
        collector.set_book_genre('Залив', 'Фантастика')
        collector.add_new_book('Призрак дома на холме')
        collector.set_book_genre('Призрак дома на холме', 'Ужасы')
        result = collector.get_books_for_children()
        assert result == ['Залив']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert '1984' in collector.favorites

    def test_add_book_in_favorites_not_in_genre(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Неизвестная книга')
        assert 'Неизвестная книга' not in collector.favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert '1984' not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert collector.get_list_of_favorites_books() == ['1984']
