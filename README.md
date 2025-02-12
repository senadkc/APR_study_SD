# APR for Python -- S.D

A Python-based tokenization and error classification system that leverages machine learning models for syntax error detection and correction.

## Installation & Setup

1. Replace the default `tokenize.py` file in Python's Lib directory with the `tokenize.py` provided in this repository.
	**Note:** Before running `full-test.py`, you can automatically apply necessary changes by executing `tokenize-change`.
	tokenize-change.py will back up the default tokenize.py file (which comes with Python) as tokenize.bak before applying changes. You can restore it later if needed. However, please ensure that the backup has been created successfully.
2. Install the required dependencies:
   ```bash
   pip install numpy tensorflow scikit-learn
   ```

## Features

- **Token ID Mapping:** The system includes predefined token ID mappings for analysis.
- **Error Classification:**
  - The `correct_type_model` is used for error type classification.
  - Training data includes `wrong_token_codes`, `extra_token_codes`, and `missing_token_codes`.
- **Token Prediction:**
  - The `token_predict_model` predicts incorrect tokens.
  - Training data comes from the `correct_codes` directory.
- **Test Datasets:**
  - The `correct_ibm` dataset was modified to create:
    - `extra_token_data-ibm`
    - `wrong_token_data-ibm`
    - `missing_token_data-ibm`
    - `indentation_error_data-ibm`
  - These datasets were used for system testing.
  - Additional test cases: `indentation_test`, `extra-test`, `wrong-test`, and `missing-test`.

## Usage

1. Run the script with the Python interpreter:
   ```bash
   python full-test.py
   ```
2. The system will:
   - Analyze code for syntax errors
   - Classify and predict errors
   - Apply corrections where possible

## Notes
- Ensure that all necessary model files (`correct_type_model`, `token_predict_model`) are correctly placed before running the system.
- If any issues arise, verify file paths and dataset placements.

## Token ID Table

Below is a list of different token types and their corresponding IDs. This table can be used to define specific words or symbols in a particular language or system.

| ID  | Token |
|-----|-----------------------------|
| 0   | VAR |
| 1   | INT |
| 2   | FLOAT_EXPONANT_COMPLEX |
| 3   | FLOAT_EXPONANT |
| 4   | COMPLEX |
| 5   | FLOAT |
| 6   | DOT |
| 7   | LONG |
| 8   | HEXA |
| 9   | OCTA |
| 10  | BINARY |
| 11  | LEFT_PARENTHESIS |
| 12  | RIGHT_PARENTHESIS |
| 13  | COLON |
| 14  | COMMA |
| 15  | SEMICOLON |
| 16  | AT |
| 17  | PLUS |
| 18  | MINUS |
| 19  | STAR |
| 20  | SLASH |
| 21  | VBAR |
| 22  | AMPER |
| 23  | LESS |
| 24  | GREATER |
| 25  | EQUAL |
| 26  | PERCENT |
| 27  | LEFT_SQUARE_BRACKET |
| 28  | RIGHT_SQUARE_BRACKET |
| 29  | LEFT_BRACKET |
| 30  | RIGHT_BRACKET |
| 31  | BACKQUOTE |
| 32  | EQUAL_EQUAL |
| 33  | NOT_EQUAL |
| 34  | LESS_EQUAL |
| 35  | GREATER_EQUAL |
| 36  | TILDE |
| 37  | CIRCUMFLEX |
| 38  | LEFT_SHIFT |
| 39  | RIGHT_SHIFT |
| 40  | DOUBLE_STAR |
| 41  | PLUS_EQUAL |
| 42  | MINUS_EQUAL |
| 43  | AT_EQUAL |
| 44  | STAR_EQUAL |
| 45  | SLASH_EQUAL |
| 46  | PERCENT_EQUAL |
| 47  | AMPER_EQUAL |
| 48  | VBAR_EQUAL |
| 49  | CIRCUMFLEX_EQUAL |
| 50  | LEFT_SHIFT_EQUAL |
| 51  | RIGHT_SHIFT_EQUAL |
| 52  | ELLIPSIS |
| 53  | RIGHT_ARROW |
| 54  | DOUBLE_STAR_EQUAL |
| 55  | DOUBLE_SLASH |
| 56  | DOUBLE_SLASH_EQUAL |
| 57  | COMMENT |
| 58  | UNICODE_STRING |
| 59  | INTERPOLATED_STRING |
| 60  | RAW_STRING |
| 61  | BINARY_STRING |
| 62  | UNICODE_RAW_STRING |
| 63  | BINARY_RAW_STRING |
| 64  | INTERPOLATED_RAW_STRING |
| 65  | SUM_INTENDED |
| 66  | null |
| 67  | endl |
| 68  | AND |
| 69  | AS |
| 70  | ABS |
| 71  | ASSERT |
| 72  | AWAIT |
| 73  | ASYNC |
| 74  | APPEND |
| 75  | BREAK |
| 76  | BIN |
| 77  | BOOL |
| 78  | CLASS |
| 79  | CONTINUE |
| 80  | CLEAR |
| 81  | COUNT |
| 82  | CAPITALIZE |
| 83  | DEF |
| 84  | DEL |
| 85  | DICT |
| 86  | ELIF |
| 87  | ELSE |
| 88  | EXEC |
| 89  | END |
| 90  | EXTEND |
| 91  | FINALLY |
| 92  | FALSE |
| 93  | FOR |
| 94  | FROM |
| 95  | FIND |
| 96  | FUNCTOOLS |
| 97  | FILTER |
| 98  | GET |
| 99  | GLOBAL |
| 100 | HEX |
| 101 | NONLOCAL |
| 102 | IF |
| 103 | IMPORT |
| 104 | IN |
| 105 | IS |
| 106 | INPUT |
| 107 | INDEX |
| 108 | ISDIGIT |
| 109 | INSERT |
| 110 | ISUPPER |
| 111 | ISLOWER |
| 112 | ITEMS |
| 113 | JOIN |
| 114 | KEYS |
| 115 | LAMBDA |
| 116 | LEN |
| 117 | LOWER |
| 118 | LIST |
| 119 | NOT |
| 120 | NONE |
| 121 | NEWLINE |
| 122 | MAP |
| 123 | OR |
| 124 | PASS |
| 125 | PRINT |
| 126 | POP |
| 127 | RAISE |
| 128 | RETURN |
| 129 | RANGE |
| 130 | ROUND |
| 131 | REPLACE |
| 132 | RFIND |
| 133 | REDUCE |
| 134 | REMOVE |
| 135 | REVERSE |
| 136 | STR |
| 137 | SPLIT |
| 138 | SORTED |
| 139 | SORT |
| 140 | TRUE |
| 141 | TUPLE |
| 142 | TIME |
| 143 | TYPE |
| 144 | TABSPACE |
| 145 | UPPER |
| 146 | UPDATE |
| 147 | VALUES |
| 148 | WHILE |
| 149 | SINGLE_QUOTE |
| 150 | DOUBLE_QUOTE |
| 151 | STRING |
| 152 | STRING5 |
| 153 | STRING6 |
| 154 | STRING7 |
| 155 | NEWLINE0 |
| 156 | TABSPACE0 |
| 157 | EXCLAMATION |

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14861774.svg)](https://doi.org/10.5281/zenodo.14861774)
