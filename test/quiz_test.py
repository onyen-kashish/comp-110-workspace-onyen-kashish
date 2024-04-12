from test.quiz import find_even, remove_first_even, remove_first_even_and_send_back


def test_find_even() -> None:
    wordlist: list[str] = ["hello", "test"]
    assert find_even(wordlist) == "test"


def test_find_even_check_empty() -> None:
    wordlist: list[str] = ["hello", "test123"]
    assert find_even(wordlist) == ""


def test_remove_first_even_use_case() -> None:
    wordlist: list[str] = ["hello", "bye", "word"]
    assert remove_first_even(wordlist) is None

# def test_remove_first_even_and_send_back() -> None:
#     wordlist: list[str] = ["hello", "bye", "word"]
#     assert remove_first_even_and_send_back(wordlist)  == ["hello", "bye"]
