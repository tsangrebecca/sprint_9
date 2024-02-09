from bloomdata_rebeccatsang.wallet import Wallet 
import pytest

# pytest fixture to define scenarios for repeated use in our tests
#   rmb to pass the fixture as parameters in the tests!
@pytest.fixture   # an @ is a decorator
def empty_wallet():
    return Wallet()

@pytest.fixture
def wallet_20():
    return Wallet(20)

def test_empty_wallet(empty_wallet):  # <--- have to fill this in
    # instead of always have to define a variable for future repeated use,
    #   we can use a pytest fixture
    # empty_wallet = Wallet()
    assert empty_wallet.balance == 0

def test_wallet_20(wallet_20):
    assert wallet_20.balance == 20

def test_wallet_20_spend_10(wallet_20):
    # wallet_20 = Wallet(20)
    assert wallet_20.spend_cash(10) == "remaining balance: 10"
    assert wallet_20.balance == 10

def test_spend_all_cash(wallet_20):
    # wallet_20 = Wallet(20)
    assert wallet_20.spend_cash(20) == 'remaining balance: 0'

