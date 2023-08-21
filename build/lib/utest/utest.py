from halo import Halo
import functools

def utest(func):
    """Decorator to wrap test functions with a spinner."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with Halo(text='Running test...', spinner='dots'):
            try:
                func(*args, **kwargs)
                status = "PASSED"
            except AssertionError as e:
                status = f"FAILED - {e}"
        print(f"Test {func.__name__}: {status}")
    return wrapper

class UtestSuite:
    """Test suite class to manage and run unit tests."""

    def __init__(self):
        self.tests = []

    def add_test(self, test_func):
        """Add a test function to the suite."""
        self.tests.append(test_func)

    def run_tests(self):
        """Run all tests in the suite."""
        print("Running tests:")
        for test_func in self.tests:
            test_func()
        print("All tests completed.")
