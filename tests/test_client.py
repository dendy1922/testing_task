from client import Client
import pytest
import logging



app_logger = logging.getLogger('app_logger')
app_logger.setLevel('DEBUG')
console_handler = logging.StreamHandler()
app_logger.addHandler(console_handler)

f = logging.Formatter(fmt='%(levelname)s - %(name)s - %(message)s')
console_handler.setFormatter(f)


def isPrime(number):
    """
    function that testing number.
    if number is prime return True, else return False
    """
    if number < 2:
        return False
    elif number == 2:
        return True

    for i in range(2, round(number**(0.5))+1):
        if number % i == 0:
            return False
        else:
            return True


@pytest.fixture
def get_conn():
    """
    pytest.fixture that get connection from a client to the server
    """
    app_logger.debug('Setup connection')
    cl = Client()
    data = cl.make_request('http://localhost:5000/number')
    return data['number']


def test_prime_number(get_conn):
    """
    tests request GET /number and checked that returning number is prime
    """
    app_logger.debug('Starting test')
    assert isPrime(get_conn)
    app_logger.debug('Ending test')
