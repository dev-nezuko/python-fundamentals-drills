"""
Junior Python Coding Assessment - Test Suite
=============================================

Run with: pytest
"""

from questions import (
    categorize_average,
    clean_text,
    filter_even_above,
    count_words,
)


# =============================================================================
# Tests for categorize_average
# =============================================================================

def test_categorize_average_medium():
    """Test medium category with typical scores."""
    assert categorize_average([40, 50, 60]) == (50, "medium")


def test_categorize_average_high():
    """Test high category with high scores."""
    assert categorize_average([90, 80, 100]) == (90, "high")


def test_categorize_average_low():
    """Test low category with low scores."""
    assert categorize_average([10, 20, 30]) == (20, "low")


def test_categorize_average_empty():
    """Test with empty list."""
    assert categorize_average([]) == (0, "low")


def test_categorize_average_single_score():
    """Test with a single score."""
    assert categorize_average([75]) == (75, "medium")


def test_categorize_average_boundary_50():
    """Test boundary at 50 (should be medium)."""
    assert categorize_average([50]) == (50, "medium")


def test_categorize_average_boundary_80():
    """Test boundary at 80 (should be high)."""
    assert categorize_average([80]) == (80, "high")


def test_categorize_average_boundary_49():
    """Test boundary at 49 (should be low)."""
    assert categorize_average([49]) == (49, "low")


def test_categorize_average_rounds_down():
    """Test that average is rounded down (integer division)."""
    # (10 + 11) / 2 = 10.5, should round down to 10
    assert categorize_average([10, 11]) == (10, "low")


# =============================================================================
# Tests for clean_text
# =============================================================================

def test_clean_text_typical():
    """Test typical case with extra spaces."""
    assert clean_text("  Hello   World  ") == "hello world"


def test_clean_text_uppercase():
    """Test conversion to lowercase."""
    assert clean_text("PYTHON") == "python"


def test_clean_text_many_spaces():
    """Test multiple consecutive spaces."""
    assert clean_text("  Too    Many   Spaces  ") == "too many spaces"


def test_clean_text_empty():
    """Test empty string."""
    assert clean_text("") == ""


def test_clean_text_only_spaces():
    """Test string with only spaces."""
    assert clean_text("     ") == ""


def test_clean_text_single_word():
    """Test single word with no spaces."""
    assert clean_text("hello") == "hello"


def test_clean_text_mixed_case():
    """Test mixed case conversion."""
    assert clean_text("HeLLo WoRLd") == "hello world"


def test_clean_text_already_clean():
    """Test already clean text."""
    assert clean_text("already clean") == "already clean"


def test_clean_text_leading_trailing_only():
    """Test with only leading and trailing spaces."""
    assert clean_text("  test  ") == "test"


# =============================================================================
# Tests for filter_even_above
# =============================================================================

def test_filter_even_above_typical():
    """Test typical case with mixed numbers."""
    assert filter_even_above([1, 2, 3, 4, 5, 6, 7, 8], 3) == [4, 6, 8]


def test_filter_even_above_threshold_match():
    """Test that threshold itself is excluded."""
    assert filter_even_above([10, 15, 20, 25], 10) == [20]


def test_filter_even_above_no_matches():
    """Test when no numbers match (all odd)."""
    assert filter_even_above([1, 3, 5, 7], 0) == []


def test_filter_even_above_empty():
    """Test with empty list."""
    assert filter_even_above([], 5) == []


def test_filter_even_above_all_match():
    """Test when all numbers match."""
    assert filter_even_above([4, 6, 8, 10], 2) == [4, 6, 8, 10]


def test_filter_even_above_negative_threshold():
    """Test with negative threshold."""
    assert filter_even_above([-4, -2, 0, 2, 4], -3) == [-2, 0, 2, 4]


def test_filter_even_above_all_below_threshold():
    """Test when all numbers are below threshold."""
    assert filter_even_above([2, 4, 6], 10) == []


def test_filter_even_above_preserves_order():
    """Test that order is preserved."""
    assert filter_even_above([8, 2, 6, 4], 1) == [8, 2, 6, 4]


def test_filter_even_above_zero_threshold():
    """Test with zero as threshold."""
    assert filter_even_above([0, 2, 4], 0) == [2, 4]


# =============================================================================
# Tests for count_words
# =============================================================================

def test_count_words_typical():
    """Test typical case with repeated words."""
    assert count_words(["apple", "banana", "apple"]) == {"apple": 2, "banana": 1}


def test_count_words_case_sensitive():
    """Test that counting is case-sensitive."""
    assert count_words(["hello", "Hello", "HELLO"]) == {
        "hello": 1,
        "Hello": 1,
        "HELLO": 1,
    }


def test_count_words_single():
    """Test single word."""
    assert count_words(["one"]) == {"one": 1}


def test_count_words_empty():
    """Test empty list."""
    assert count_words([]) == {}


def test_count_words_all_same():
    """Test when all words are the same."""
    assert count_words(["repeat", "repeat", "repeat"]) == {"repeat": 3}


def test_count_words_all_unique():
    """Test when all words are unique."""
    result = count_words(["one", "two", "three"])
    assert result == {"one": 1, "two": 1, "three": 1}


def test_count_words_multiple_repeats():
    """Test with multiple words repeating."""
    result = count_words(["a", "b", "a", "b", "a"])
    assert result == {"a": 3, "b": 2}

