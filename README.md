# Stress Testing Application for Competitive Programming

This script automates stress testing by comparing the outputs of a **correct** solution and a **potentially incorrect** solution on randomly generated test cases. It helps identify edge cases where the incorrect solution fails.

---

## Features
- Automates the generation of test cases.
- Compares outputs of two solutions (`correct.py` and `wrong.py`).
- Saves failing test cases for debugging.
- Supports multiple programming languages: C, C++, Java, Python.

---

## Files
1. **`test.py`**: The main script to run the stress tests.
2. **`generator.py`**: Generates random test cases.
3. **`correct.py`**: The correct solution.
4. **`wrong.py`**: The solution being tested for errors.
5. **`run_test.bat`**: Batch script for easy execution on Windows.

---

## Usage

### Prerequisites
- Python installed on your system.
- Required compilers (if testing C, C++, or Java solutions).

### Running the Script
1. Place all required files (`test.py`, `generator.py`, `correct.py`, `wrong.py`) in the same directory.
2. Use the batch file for simplified execution:
   ```cmd
   ./run_test
   ```
   For Ubuntu
   ```cmd
   bash run_test.sh
