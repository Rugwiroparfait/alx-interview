Here's a `README.md` for the "0x03. Log Parsing" project:

---

# 0x03. Log Parsing

## Description

This project focuses on parsing and processing data streams in real-time using Python. The main goal is to create a script that reads from standard input (stdin), processes data in a specific format, and computes metrics based on the input data. The script handles log entries line by line and generates summaries after every 10 lines or upon receiving a keyboard interruption (CTRL + C).

## Concepts and Resources

### Key Concepts:
- **File I/O in Python:** 
  - Reading from `sys.stdin` line by line.
  - [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
  
- **Signal Handling in Python:**
  - Handling keyboard interruptions using signal handling.
  - [Python Signal Handling](https://docs.python.org/3/library/signal.html)
  
- **Data Processing:**
  - Parsing strings to extract specific data points.
  - Aggregating data to compute summaries.
  
- **Regular Expressions:**
  - Using regular expressions to validate the format of each line.
  - [Python Regular Expressions](https://docs.python.org/3/library/re.html)
  
- **Dictionaries in Python:**
  - Counting occurrences of status codes and accumulating file sizes.
  - [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
  
- **Exception Handling:**
  - Handling possible exceptions during file reading and data processing.
  - [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

### Additional Resources:
- Mock Technical Interview: [Resource Link]

## Requirements

- **Editors:** `vi`, `vim`, `emacs`
- **Python Version:** The project will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- **File Requirements:**
  - All files should end with a new line.
  - The first line of all files should be exactly `#!/usr/bin/python3`.
  - The code should follow the PEP 8 style (version 1.7.x).
  - All files must be executable.
  - The length of the files will be tested using `wc`.
  
## Task: Log Parsing

### Objective

Create a script (`0-stats.py`) that reads stdin line by line and computes metrics. The input format should be:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

### Functionality

- **Input Parsing:** 
  - Skip lines that do not match the expected format.
  
- **Metrics Calculation:** 
  - After every 10 lines and/or upon receiving a keyboard interruption (CTRL + C), print the following:
    - **Total file size:** Sum of all previous file sizes.
    - **Number of lines by status code:** 
      - Possible status codes: `200`, `301`, `400`, `401`, `403`, `404`, `405`, and `500`.
      - Print only the status codes that appear, in ascending order.

### Example

```bash
./0-generator.py | ./0-stats.py
```

Output:

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
...
```

### Files

- **GitHub Repository:** `alx-interview`
- **Directory:** `0x03-log_parsing`
- **File:** `0-stats.py`

## License

© 2024 ALX, All rights reserved.
