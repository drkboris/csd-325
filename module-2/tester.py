import tests
from week9_assignment import Trie

def run_tests():
    total_tests = passed_tests = 0

    for result, expected, message in tests.test_trie():
        total_tests += 1
        try:
            assert result == expected
            print(f"Test {total_tests}: Correct. ({message})")
            passed_tests += 1
        except AssertionError:
            print(f"Test {total_tests}: Incorrect. Expected: {expected}, Got: {result} ({message})")

    print(f"Passed {passed_tests} of {total_tests} tests.")

if __name__ == "__main__":
    run_tests()
