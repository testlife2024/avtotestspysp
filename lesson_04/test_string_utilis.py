import pytest
from string_utilis import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str_1, expected_1", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str_1, expected_1):
    assert string_utils.capitalize(input_str_1) == expected_1

@pytest.mark.parametrize("input_str_2, expected_2", [
    ("   b", "b"),
    ("b  ", "b  "),
    ("b", "b"),
])
def test_trim_positive(input_str_2, expected_2):
    assert string_utils.trim(input_str_2) == expected_2

@pytest.mark.parametrize("input_str_3_1,input_str_3_2, expected_3", [
    ("bbb", "b",True),
    ("bgg", "g", True),
    ("b2", "3", False),
])
def test_contains_positive(input_str_3_1, input_str_3_2, expected_3):
    assert string_utils.contains(input_str_3_1,input_str_3_2) == expected_3

@pytest.mark.parametrize("input_str_4_1,input_str_4_2, expected_4", [
    ("mmNm", "N","mmm"),
    ("PyCharm", "Py","Charm"),
    ("abc2", "2","abc"),
])
def test_delete_symbol_positive(input_str_4_1, input_str_4_2, expected_4):
    assert string_utils.delete_symbol(input_str_4_1,input_str_4_2) == expected_4



@pytest.mark.negative
@pytest.mark.parametrize("input_str_1, expected_1", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str_1, expected_1):
    assert string_utils.capitalize(input_str_1) == expected_1

@pytest.mark.parametrize("input_str_2, expected_2", [
    ("b", "b"),
    ("    ", ""),
    ("", ""),
])
def test_trim_negative(input_str_2, expected_2):
    assert string_utils.trim(input_str_2) == expected_2


@pytest.mark.parametrize("input_str_3_1,input_str_3_2, expected_3", [
    ("", "",True),
    (" ", "3",False),
    ("", "   ", False),
])
def test_contains_negative(input_str_3_1,input_str_3_2, expected_3):
    assert string_utils.contains(input_str_3_1, input_str_3_2) == expected_3

@pytest.mark.parametrize("input_str_4_1,input_str_4_2, expected_4", [
    ("", "   ",""),
    (" 123", " ","123"),
    ("PyCharm", "6", "PyCharm"),
])
def test_delete_symbol_negative(input_str_4_1,input_str_4_2, expected_4):
    assert string_utils.delete_symbol(input_str_4_1, input_str_4_2) == expected_4