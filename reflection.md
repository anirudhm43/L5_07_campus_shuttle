# Reflection — Static Code Analysis

## 1. What did you learn about static code analysis?

I learned that static code analysis can identify code quality issues, potential bugs, security-related patterns, and formatting violations without executing the program. Using Pylint, Bandit, and Flake8 together provided different perspectives on the same code.

## 2. How did the three tools differ?

Pylint identified code quality problems such as missing docstrings, mutable default arguments, naming conventions, and unnecessary global statements. Bandit highlighted potentially unsafe coding patterns, including broad exception handling and standard pseudo-random selection. Flake8 identified formatting issues such as incorrect blank-line spacing, long lines, and bare exception clauses.

## 3. Which fixes were most important, and why?

Fixing the mutable default argument prevented log lists from being unintentionally shared between function calls. Removing broad exception handling made errors easier to identify. Passenger-count validation prevented invalid data from entering route calculations, while handling missing routes and empty trip lists prevented runtime errors.

## 4. How did static analysis improve the program?

The analysis process improved readability, maintainability, and confidence in the code. Pylint's score increased from 6.25/10 to 10.00/10, Bandit reported no remaining issues, and Flake8 produced no violations. I also learned that static analysis does not detect every logical bug, so running the program and testing invalid inputs are still necessary.
