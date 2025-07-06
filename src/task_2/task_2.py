"""Task 2 Check for palindrome solution"""

from collections import deque
import re


def is_palindrome(inp: str) -> bool:
    """
    Determine whether provided string is a palindrome (ignoring case, spaces, punctuation).

    Returns:
        - True if input string is a palindrome
        - False otherwise.
    """
    # Guard against accidental non-strings
    if not isinstance(inp, str):
        return False

    # Normalize input
    normalized = normalize_input(inp)

    # An empty string (or one‐character string) is trivially a palindrome
    if len(normalized) < 2:
        return True

    # Build deque
    char_deque = deque(normalized)

    # Compare ends
    while len(char_deque) > 1:
        left = char_deque.popleft()
        right = char_deque.pop()
        if left != right:
            return False

    return True


def normalize_input(string: str) -> str:
    """
    Remove all palindrome non-comparable characters.
    """
    return re.sub(r"[^A-Za-z0-9]", "", string).lower()


def run_tests() -> None:
    """Test the is_palindrome function with diverse cases."""
    test_cases = {
        "": True,  # ? empty string (debatable)
        "a": True,  # single character
        "level": True,  # odd-length palindrome
        "ab": False,  # simple non-palindrome
        "Madam": True,  # case-insensitive
        "A man a plan a canal Panama": True,  # ignores spaces
        "No lemon, no melon": True,  # ignores punctuation & spaces
        "Was it a car or a cat I saw?": True,  # ignores punctuation & spaces
        "12321": True,  # numeric palindrome
        "123, 321": True,  # numeric with punctuation
        "1234567890": False,  # numeric non-palindrome
        "hello olleh": True,  # with space in the middle
        "Hello, world!": False,  # not a palindrome
    }

    print("🔍 Running palindrome tests…")

    passed = 0
    for inp, expected in test_cases.items():
        result = is_palindrome(inp)
        status = "PASS" if result is expected else "FAIL"
        print(f"[{status}] {inp!r:30} → {result} (expected: {expected})")
        if status == "PASS":
            passed += 1

    total = len(test_cases)
    print(f"\n✅ {passed}/{total} tests passed.")


if __name__ == "__main__":
    run_tests()
