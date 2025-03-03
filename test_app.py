### Contient les tests unitaires de l'application
from app import say_hello

class TestApp(unittest.TestCase):
    def test_say_hello(self):
        # Cette fonction permet de tester un message
        self.assertEqual(say_hello("AWS"), "Hello, AWS")

if __name__ == "__main__":
    unitest.main()

