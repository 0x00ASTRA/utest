# uTest: A Unit Testing Library with Halo Spinners

uTest is a simple and elegant unit testing library designed to enhance your testing experience with Halo spinners. Write and run tests with visually appealing spinners that provide real-time feedback on test execution.

## Features

- **Easy to Use**: Define and run tests with a simple decorator.
- **Visual Feedback**: Halo spinners provide visual feedback during test execution.
- **Customizable**: Extend and customize the library to fit your specific needs.

## Installation

To install uTest directly from GitHub, run the following command:

```bash
pip install git+https://github.com/0x00ASTRA/utest.git
```

To install it using PyPi, run the following command

```bash
pip install utest
```

## Usage

### Importing the Library

```python
from utest import utest, UtestSuite
```

### Defining Tests

Decorate your test functions with the `@utest` decorator:

```python
@utest
def test_example():
    assert 2 + 2 == 4, "Addition failed"
```

### Running Tests

Create a test suite, add your tests, and run them:

```python
test_suite = UtestSuite()
test_suite.add_test(test_example)
test_suite.run_tests()
```

### Full Example

Here's a full example combining the above snippets:

```python
# example.py
from utest import utest, UtestSuite

@utest
def test_example():
    assert 2 + 2 == 4, "Addition failed"

test_suite = UtestSuite()
test_suite.add_test(test_example)
test_suite.run_tests()
```

output:
```bash
Running tests:
Test test_example: PASSED
All tests completed.
```

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

### Wallets 🪙
| Icon | Token | Address                                      |
|------| ----- | -------------------------------------------- |
| ![[SOL.png]] | SOL   | 12Ymegdn9Gw27BoE9bkdH7TViDdmj4is1kpM7BWLuD9X |
| ![[LTC.png]] | LTC   | LeiSY4Frv5odEk16FgR6JMPNy7SurHwBN7           |
| ![[BTC.png]] | BTC   | 12kV7ixtjP7W8PowrgwsAQLafX1kzVg4PB           |
| ![[ETH.png]] | ETH   | 0x02c5e2ec62640771851D3BD0c283936A6481e678   |
| ![[DOGE.png]] | DOGE  | DLTzZUjJ8WwZ8rHNfeYTLcYALoRGu73s3t           |
| ![[NEOX.png]] | NEOX  | GNcbu5GuZKMUui8A9eZxGXhJurgSixNRfT           |
| ![[RVN.png]] | RVN   | RPCyf776AFX2qm3H3v77RnrvtX2QF2f1cg |

## License

This project is open-source and available under the [MIT No Attribution License](LICENSE).
