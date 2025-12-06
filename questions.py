"""
Junior Python Coding Assessment - Candidate File
=================================================

Instructions:
- This is the ONLY file you should modify.
- Read each function's docstring carefully for requirements and examples.
- Replace `raise NotImplementedError("Not implemented yet")` with your code.
- Do NOT change function names, parameters, or return types.
- Do NOT modify the test file.
- Your goal is to make all tests pass.

Good luck!
"""


def categorize_average(scores: list[int]) -> tuple[int, str]:
    """
    Calculate the average of a list of scores and categorize it.

    Requirements:
    - Calculate the average of all scores in the list.
    - Round the average DOWN to the nearest integer (use integer division).
    - Categorize the average:
        - "low" if average is less than 50
        - "medium" if average is 50 to 79 (inclusive)
        - "high" if average is 80 or above
    - Return a tuple of (average, category).
    - If the list is empty, return (0, "low").

    Examples:
        >>> categorize_average([40, 50, 60])
        (50, 'medium')
        >>> categorize_average([90, 80, 100])
        (90, 'high')
        >>> categorize_average([10, 20, 30])
        (20, 'low')
        >>> categorize_average([])
        (0, 'low')

    Difficulty: Beginner
    """
    # TODO: Implement this function
    raise NotImplementedError("Not implemented yet")


def clean_text(text: str) -> str:
    """
    Clean up a user input string.

    Requirements:
    - Remove leading and trailing whitespace.
    - Convert the entire string to lowercase.
    - Replace multiple consecutive spaces with a single space.
    - Return the cleaned string.

    Examples:
        >>> clean_text("  Hello   World  ")
        'hello world'
        >>> clean_text("PYTHON")
        'python'
        >>> clean_text("  Too    Many   Spaces  ")
        'too many spaces'
        >>> clean_text("")
        ''

    Difficulty: Beginner
    """
    # TODO: Implement this function
    raise NotImplementedError("Not implemented yet")


def filter_even_above(numbers: list[int], threshold: int) -> list[int]:
    """
    Filter a list to keep only even numbers greater than a threshold.

    Requirements:
    - Return a new list containing only numbers that are:
        1. Even (divisible by 2 with no remainder)
        2. Greater than the given threshold (not equal to)
    - Preserve the original order of elements.
    - If no numbers match, return an empty list.
    - Do not modify the original list.

    Examples:
        >>> filter_even_above([1, 2, 3, 4, 5, 6, 7, 8], 3)
        [4, 6, 8]
        >>> filter_even_above([10, 15, 20, 25], 10)
        [20]
        >>> filter_even_above([1, 3, 5, 7], 0)
        []
        >>> filter_even_above([], 5)
        []

    Difficulty: Beginner
    """
    # TODO: Implement this function
    raise NotImplementedError("Not implemented yet")


def count_words(words: list[str]) -> dict[str, int]:
    """
    Count how many times each word appears in a list.

    Requirements:
    - Return a dictionary where:
        - Each key is a word from the list
        - Each value is how many times that word appears
    - Words are case-sensitive ("Hello" and "hello" are different).
    - If the list is empty, return an empty dictionary.

    Examples:
        >>> count_words(["apple", "banana", "apple"])
        {'apple': 2, 'banana': 1}
        >>> count_words(["hello", "Hello", "HELLO"])
        {'hello': 1, 'Hello': 1, 'HELLO': 1}
        >>> count_words(["one"])
        {'one': 1}
        >>> count_words([])
        {}

    Difficulty: Beginner
    """
    # TODO: Implement this function
    raise NotImplementedError("Not implemented yet")

