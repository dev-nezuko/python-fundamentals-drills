# Four small Python practice problems

Start with a failing test, read the contract, and implement one function at a time. This repository is a beginner practice set: all four functions in `questions.py` intentionally raise `NotImplementedError`. It is not a completed application or a collection of reference answers.

The exercises are:

1. **`categorize_average`** — floor an average and apply category boundaries.
2. **`clean_text`** — normalize case and spacing.
3. **`filter_even_above`** — filter without changing order or the input list.
4. **`count_words`** — count case-sensitive words in a dictionary.

For example, after implementation, `filter_even_above([1, 2, 3, 4, 5, 6], 3)` should return `[4, 6]`. The supplied tests check examples and boundaries; the docstrings are the contract to work from.

## Your first run

Use Python 3.9 or newer for the built-in collection annotations:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
```

The reviewed starting state has **34 collected tests and 34 expected failures**, all from unimplemented functions. There were no test-collection errors. Do not mistake that baseline for a broken installation or a passing solution.

Work on a single function and rerun its tests:

```sh
python -m pytest -k categorize_average -v
```

Keep function names, parameters and return types. Use the standard library, leave the test expectations intact, and consider empty inputs, threshold equality, case sensitivity and input mutation while writing a solution. There is no need to build a web interface or install an application framework.

## What is and is not here

`questions.py` contains the four stubs; `test_questions.py` contains the tests. `pytest.ini` limits discovery to test modules, and `requirements.txt` declares pytest 7.4.3.

The previous README referred to `solutions.py`, but no such file exists. Its unusable answer-swapping helper was removed, along with unused fonts and desktop metadata. No answers were added, and the exercise functions and tests remain unchanged.

The baseline was checked with Python 3.11 and the isolated review environment's pytest 9; the exact pinned pytest environment was not separately installed. There is no recognition of broader engineering ability from this small test set. Use it as learning material or a clearly labeled assessment scaffold, and feature completed projects more prominently in a portfolio. No license file is present.
