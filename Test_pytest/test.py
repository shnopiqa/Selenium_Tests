import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass

    def test_second_smiling_faces(self, prepare_faces):
        pass

#
# Не забываем:
#
# если явно не указано scope - фикстара сработает 1 раз
# если явно указано scope="class" - вызовится по 1 разу для классов
# если явно указан autouse=True будет вызываться каждый раз для всех методов и функций
#
# речь именно про функции и метода, начинающиеся со слова test. Также, не забывайте про yield.
