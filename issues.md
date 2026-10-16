# Static Code Analysis — Issues and Fixes

**Project:** Campus Shuttle Timetable and Fleet Tracker  
**File analyzed:** `shuttle_system.py`  
**Tools:** Pylint, Bandit, Flake8

## Issue Table

| Issue | Type | Original line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Mutable default argument | Bug / Pylint W0102 | 6 | `logs=[]` reused the same list across function calls, potentially sharing log entries. | Changed the default to `None` and initialized a new list inside the function. |
| Broad exception handling | Code quality / Bandit B110, Pylint W0702 | 29–30 | A bare `except` silently hid errors when calculating underused routes. | Removed the broad exception handling and explicitly validated trip data before calculating averages. |
| Insecure random selection warning | Security analysis / Bandit B311 | 35 | `random.choice()` triggered Bandit's warning about standard pseudo-random generators. | Replaced it with `secrets.choice()`. |
| Old string formatting | Code quality / Pylint C0209 | 13 | Percent-based string formatting was less consistent with modern Python formatting. | Replaced it with an f-string. |
| Missing docstrings | Code quality / Pylint C0114, C0116 | Multiple | The module and functions lacked descriptive documentation. | Added a module docstring and function docstrings. |
| Non-standard function name | Code quality / Pylint C0103 | 33 | `assignDriver` did not follow Python's snake_case naming convention. | Renamed it to `assign_driver` and updated its call. |
| Unused function parameter | Code quality / Pylint W0613 | 33 | The `route_id` parameter in the original driver assignment function was unused. | Removed the unnecessary parameter. |
| Global statement | Code quality / Pylint W0603 | 38 | The original synchronization function reassigned the global route dictionary. | Updated the existing dictionary with `clear()` and `update()` instead. |
| File handling and encoding | Code quality / Pylint W1514, R1732 | 39–42 | Files were opened without explicit encoding and without context managers. | Used `with open(...)` and specified UTF-8 encoding. |
| Formatting violations | Style / Flake8 E302, E305, E501 | Multiple | The original code had insufficient blank lines and a line exceeding the configured length limit. | Corrected blank-line spacing and wrapped long lines. |
| Bare `except` style violation | Style / Flake8 E722 | 29 | The original code used a bare exception clause. | Removed the bare exception clause and validated data explicitly. |
| Negative passenger count | Logical bug | 36 in original test flow | Negative passenger counts could distort route averages. | Added validation requiring non-negative integer passenger counts. |
| Invalid passenger-count type | Logical bug | 37 in original test flow | A text value such as `"full"` could be stored as a passenger count and break calculations. | Rejected invalid passenger-count types with a `ValueError`. |
| Removed route lookup | Runtime bug | 50 in original test flow | The program removed route R3 and subsequently tried to calculate its average, causing a `KeyError`. | Made average lookup handle missing routes and displayed an informative message. |
| Unknown route input | Runtime bug | 49 in original test flow | Entering an unknown route could cause a `KeyError`. | Checked that the requested route exists before displaying its trips. |
| Empty route average | Runtime bug | 20 in original function | Calculating an average for an empty trip list could cause division by zero. | Returned `None` when the route is missing or has no trips. |

## Verification Results

| Tool | Original result | Final result |
|---|---|---|
| Pylint | 6.25/10 | 10.00/10 |
| Bandit | 2 low-severity findings | No issues identified |
| Flake8 | Formatting violations reported | No violations reported |

**Conclusion:** The code was updated to improve readability, security-analysis results, formatting, input validation, and runtime reliability. All three static analysis tools were rerun after the changes.