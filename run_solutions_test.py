#!/usr/bin/env python3
"""
Test Suite Validator for Interviewers
======================================

This script runs the test suite against the reference solutions
to verify that all test cases pass correctly.

Usage:
    python run_solutions_test.py

This is useful for:
- Verifying the test suite is correct after modifications
- Confirming solutions are valid before sharing with candidates
"""

import subprocess
import sys
import shutil
from pathlib import Path


def main() -> int:
    """Run the test suite against solutions.py."""
    project_dir = Path(__file__).parent
    questions_file = project_dir / "questions.py"
    solutions_file = project_dir / "solutions.py"
    backup_file = project_dir / "questions.py.bak"

    # Verify required files exist
    if not solutions_file.exists():
        print("❌ Error: solutions.py not found")
        return 1

    if not questions_file.exists():
        print("❌ Error: questions.py not found")
        return 1

    print("=" * 60)
    print("Running test suite against solutions.py")
    print("=" * 60)
    print(flush=True)

    try:
        # Backup the original questions.py
        print("📦 Backing up questions.py...", flush=True)
        shutil.copy2(questions_file, backup_file)

        # Replace questions.py with solutions.py
        print("🔄 Swapping in solutions.py...", flush=True)
        shutil.copy2(solutions_file, questions_file)

        # Run pytest
        print("🧪 Running tests...\n", flush=True)
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "-v", str(project_dir)],
            cwd=project_dir,
        )

        return result.returncode

    except Exception as e:
        print(f"❌ Error: {e}")
        return 1

    finally:
        # Always restore the original questions.py
        if backup_file.exists():
            print("\n🔄 Restoring original questions.py...")
            shutil.move(backup_file, questions_file)
            print("✅ Restored successfully")


if __name__ == "__main__":
    sys.exit(main())

