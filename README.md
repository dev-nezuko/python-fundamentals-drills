# Junior Python Coding Assessment

A beginner-level Python coding test for junior engineers (0–1 years of experience).

## Overview

This assessment evaluates your ability to:

- Write basic Python functions
- Use conditionals, loops, and simple data structures
- Read and understand docstrings and requirements
- Translate English requirements into working code

**Estimated time: 30–60 minutes**

---

## What You Receive

| File | Description |
|------|-------------|
| `questions.py` | Function stubs with docstrings describing each task |
| `test_questions.py` | Pytest tests to validate your solutions |
| `requirements.txt` | Python dependencies |
| `pytest.ini` | Pytest configuration |

> **Note for interviewers:** `solutions.py` and `run_solutions_test.py` are for internal use and should **not** be shared with candidates.

---

## For Interviewers

To verify the test suite works correctly against the reference solutions:

```bash
python run_solutions_test.py
```

This script temporarily swaps in `solutions.py`, runs all tests, and restores the original `questions.py` automatically.

---

## What You Must Do

1. Open `questions.py`
2. Read each function's docstring carefully — it describes what the function should do and includes examples
3. Replace each `raise NotImplementedError("Not implemented yet")` with your working implementation
4. Run the tests to check your work

### Rules

- ✅ **Do** implement all 4 functions in `questions.py`
- ✅ **Do** run the tests frequently to check your progress
- ❌ **Do not** change function names, parameters, or return types
- ❌ **Do not** modify the test file or configuration files
- ❌ **Do not** use external libraries beyond the standard library

**Goal: Make all tests pass.**

---

## How to Run the Tests

### 1. Create and activate a virtual environment

```bash
python -m venv .venv

# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the tests

```bash
pytest
```

You can also run tests with more detail:

```bash
pytest -v
```

---

## What's Being Evaluated

| Criteria | Description |
|----------|-------------|
| **Correctness** | Do all tests pass? |
| **Understanding** | Can you translate requirements into code? |
| **Fundamentals** | Do you understand functions, loops, conditionals, and collections? |
| **Readability** | Is your code clear and easy to follow? |

---

Good luck! 🐍

