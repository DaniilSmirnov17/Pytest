import pytest
from functions import add, get_user_full_name,divide, is_valid_password, get_age_group, calculate_cart_total,get_value_from_dict, Wallet, InsufficientFundsError
def test_add():
    """Проверяем, что функция add() правильно складывает два числа."""
    assert add(2, 3) == 5
    assert add(2, 2) == 4
    assert add(10, -5) == 5
@pytest.fixture
def sample_user_data():
    """Фикстура, которая возвращает словарь с данными пользователя."""
    return {
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jane.doe@example.com"
    }
def test_get_user_full_name_with_fixture(sample_user_data):
    assert get_user_full_name(sample_user_data) == "Jane Doe"
def test_user_has_email_with_fixture(sample_user_data):
    assert "email" in sample_user_data
test_cases = [
    (1, 2, 3), # Обычное сложение
    (-1, -1, -2), # Сложение отрицательных чисел
    (5, 0, 5), # Сложение с нулем
    (-1, 1, 0), # Противоположные числа
    (3.5, 2.5, 6.0) # Сложение чисел с плавающей точкой
]
@pytest.mark.parametrize("a, b, expected", test_cases)
def test_add_parametrized(a, b, expected):
    """Проверяем функцию add() с разными наборами данных."""
    assert add(a, b) == expected
def test_divide_by_zero_raises_error():
    """Проверяем, что деление на ноль вызывает ValueError."""
    with pytest.raises(ValueError):
        divide(10, 0)
@pytest.mark.skip(reason="Эта функция еще в разработке")
def test_new_feature():
    assert False
@pytest.mark.xfail(reason="Известный баг с точностью float, тикет #123")
def test_float_precision_bug():
    assert (0.1 + 0.2) == 0.3
@pytest.mark.math
def test_add():
    """Проверяем, что функция add() правильно складывает два числа."""
    assert add(2, 3) == 5
    assert add(2, 2) == 4
    assert add(10, -5) == 5
@pytest.mark.math
@pytest.mark.parametrize("a, b, expected", test_cases)
def test_add_parametrized(a, b, expected):
    """Проверяем функцию add() с разными наборами данных."""
    assert add(a, b) == expected
@pytest.mark.user_profile
def test_get_user_full_name_with_fixture(sample_user_data):
    assert get_user_full_name(sample_user_data) == "Jane Doe"
@pytest.mark.user_profile
def test_user_has_email_with_fixture(sample_user_data):
    assert "email" in sample_user_data
    
#Задача №1
def test_password_correct_length():
    """Пароль корректной длины (например, 10 символов)"""
    assert is_valid_password("qwertyuiop") is True
def test_password_too_short():
    """Пароль слишком короткий (например, 5 символов)"""
    assert is_valid_password("qwert") is False
def test_password_norm_length():
    """Пароль на граничной длине (ровно 8 символов)"""
    assert is_valid_password("qwertyui") is True

#Задача №2
@pytest.mark.parametrize("age, expected_group", [
    (12, "ребенок"),
    (13, "подросток"),
    (17, "подросток"),
    (18, "взрослый")  
])
def test_get_age_group(age, expected_group):
    assert get_age_group(age) == expected_group
    
#Задача №3
@pytest.fixture
def simple_cart():
    return [
        {"name": "Книга", "price": 500.0, "quantity": 2},
        {"name": "Ручка", "price": 50.0, "quantity": 3},
        {"name": "Блокнот", "price": 200.0, "quantity": 1}
    ]
def test_calculate_cart_total(simple_cart):
    expected_total = 1350.0
    assert calculate_cart_total(simple_cart) == expected_total
def test_cart_tovar(simple_cart):
    tovar_name = [item["name"] for item in simple_cart]
    assert "Блокнот" in tovar_name

#Задача №4
def test_get_value_success():
    sample_dict = {"name": "Даниил", "age": 20}
    assert get_value_from_dict(sample_dict, "name") == "Даниил"
def test_get_value_key_error():
    sample_dict = {"name": "Даниил", "age": 20}
    with pytest.raises(KeyError):
        get_value_from_dict(sample_dict, "email")
    
#Задача №5
@pytest.fixture
def wallet():
    return Wallet(initial_balance=20.0)
def test_wallet_deposit_success(wallet):
    wallet.deposit(10.0)
    assert wallet.balance == 30.0
def test_wallet_withdraw_success(wallet):
    wallet.withdraw(5.0)
    assert wallet.balance == 15.0
def test_wallet_withdraw_insufficient_funds(wallet):
    with pytest.raises(InsufficientFundsError):
        wallet.withdraw(50.0)
@pytest.mark.parametrize("method_name, amount", [
    ("__init__", -10.0),
    ("deposit", -10.0),
    ("deposit", 0.0),
    ("withdraw", -10.0),
    ("withdraw", 0.0),
])
def test_wallet_invalid_values_raise_value_error(method_name, amount):
    with pytest.raises(ValueError):
        if method_name == "__init__":
            Wallet(initial_balance=amount)
        elif method_name == "deposit":
            w = Wallet(initial_balance=20.0)
            w.deposit(amount)
        elif method_name == "withdraw":
            w = Wallet(initial_balance=20.0)
            w.withdraw(amount)