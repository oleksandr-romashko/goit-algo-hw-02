"""Task 3 Check for symmetric delimiters solution"""

import re


def is_delimiters_symmetric(inp: str):
    """
    Check if brackets in the string are symmetric using a stack-based approach.
    """
    # Guard against accidental non-strings
    if not isinstance(inp, str):
        return "Not symmetric"

    # Normalize input
    normalized = normalize_input(inp)

    # An empty normalized string is trivially symmetric
    if not normalized:
        return "Symmetric"

    # Define matching symbol pairs
    symbol_pairs = {")": "(", "]": "[", "}": "{"}
    opening_symbols = symbol_pairs.values()

    # Build stack
    stack: list[str] = []

    for symbol in normalized:
        if symbol in opening_symbols:
            # Opening symbol -> just push on the stack
            stack.append(symbol)
        elif symbol in symbol_pairs:
            # Closing symbol -> Check for matching pair
            if not stack:
                # Unbalanced = no matching pair
                return "Not symmetric"
            if stack.pop() != symbol_pairs[symbol]:
                # Matching pair is different a symbol
                return "Not symmetric"

    return "Symmetric" if not stack else "Not symmetric"


def normalize_input(string: str) -> str:
    """
    Remove all non-comparable characters and keep only bracket symbols.
    """
    return re.sub(r"[^\(\)\[\]\{\}]", "", string)


def run_tests() -> None:
    """Run tests for the is_delimiters_symmetric function with various bracket combinations."""
    test_cases = {
        "()": "Symmetric",  # Single pair of parentheses
        "([])": "Symmetric",  # Nested brackets
        "{[()]}": "Symmetric",  # Deep nesting of all bracket types
        "(]{)": "Not symmetric",  # Mismatched closing bracket
        "(((": "Not symmetric",  # Only opening brackets
        ")))": "Not symmetric",  # Only closing brackets
        "({[)]}": "Not symmetric",  # Wrong closing order
        "([]{})": "Symmetric",  # Flat sequence of matched brackets
        "( [ 1 + 2 ] * {3 / 4} )": "Symmetric",  # Brackets with expression and spaces
        "[(3 + 5) * (2 - 1)]": "Symmetric",  # Brackets with math expression
        "((2 + 3)": "Not symmetric",  # One missing closing parenthesis
        "(2 + 3))": "Not symmetric",  # One extra closing parenthesis
        " ": "Symmetric",  # No brackets at all = trivially symmetric
        "([][{}])": "Symmetric",  # Multiple sequences inside
        "[(])": "Not symmetric",  # Incorrect nesting order
        "(((())))": "Symmetric",  # Balanced deep nesting
        "([{}]))": "Not symmetric",  # One unmatched closing bracket
        "([{()}])": "Symmetric",  # Well-formed nested brackets
    }

    print("🔍 Running delimiter balance tests…")

    passed = 0
    for inp, expected in test_cases.items():
        result = is_delimiters_symmetric(inp)
        status = "PASS" if result is expected else "FAIL"
        print(f"[{status}] {inp!r:30} → {result} (expected: {expected})")
        if status == "PASS":
            passed += 1

    total = len(test_cases)
    print(f"\n✅ {passed}/{total} tests passed.")


if __name__ == "__main__":
    run_tests()
