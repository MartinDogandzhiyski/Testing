from project.movie import Movie
from unittest import TestCase, main


class MovieTests(TestCase):

    def test_init(self):
        movie = Movie("Test", 1999, 6)
        self.assertEqual("Test", movie.name)
        self.assertEqual(1999, movie.year)
        self.assertEqual(6, movie.rating)
        self.assertEqual([], movie.actors)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ex:
            movie = Movie("", 1999, 6)
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_year_setter(self):
        with self.assertRaises(ValueError) as ex:
            movie = Movie("Test", 1886, 6)
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor_with_not_existing_name(self):
        movie = Movie("Test", 1999, 6)
        movie.actors = ['nurko', 'mitko', 'mu']
        movie.add_actor('viki')
        self.assertEqual(['nurko', 'mitko', 'mu', 'viki'], movie.actors)

    def test_add_actor_with_existing_name(self):
        movie = Movie("Test", 1999, 6)
        movie.actors = ['nurko', 'mitko', 'mu']
        result = movie.add_actor('mu')
        self.assertEqual(['nurko', 'mitko', 'mu'], movie.actors)
        self.assertEqual(f"mu is already added in the list of actors!", result)

    def test_gt_method_with_first_type_return(self):
        movie = Movie("Test", 1999, 6)
        movie_1 = Movie("Testing", 1997, 5)
        result = movie.__gt__(movie_1)
        self.assertEqual(f'"Test" is better than "Testing"', result)

    def test_gt_method_with_second_type_of_return(self):
        movie = Movie("Test", 1999, 6)
        movie_1 = Movie("Testing", 1997, 7)
        result = movie.__gt__(movie_1)
        self.assertEqual(f'"Testing" is better than "Test"', result)

    def test_repr(self):
        movie = Movie("Test", 1999, 6.554)
        movie.actors = ['nurko', 'mitko', 'mu']
        result = movie.__repr__()
        expected_result = f"Name: Test\n" \
               f"Year of Release: 1999\n" \
               f"Rating: 6.55\n" \
               f"Cast: nurko, mitko, mu"
        self.assertEqual(expected_result, result)



if __name__ == '__main__':
    main()
