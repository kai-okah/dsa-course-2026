# DSA Course 2026

This repository is a learning companion for a Data Structures and Algorithms course.

It has two main areas:

- `course_sample_codes/`: original course sample code, included with permission.
- `test_zone/`: my own implementations, experiments, and beginner-friendly test runners.

The main idea is to make data structures and algorithms easier to test and understand. Instead of only writing an implementation and hoping it works, the `test_zone` files print:

- the condition being tested
- the expected output
- the actual output
- whether the test passed or failed

This makes edge cases easier to see, especially for topics like binary search, stacks, queues, resizing arrays, linked lists, and union-find.

## Repository Structure

```text
dsa-course-2026/
|-- course_sample_codes/
|   |-- Analysis of Algorithms/
|   |-- Elementary sort/
|   |-- Stacks Queues/
|   `-- Union-Find/
|-- test_zone/
|   |-- analysis_of_algorithms/
|   |-- elementary_sort/
|   |-- stacks_and_queues/
|   `-- union_find/
|-- LICENSE
|-- NOTICE.md
`-- README.md
```

## Course Sample Codes

The `course_sample_codes/` folder contains original sample code from the course.

Use these files as course references and examples. They are kept separate from `test_zone/` so it is clear which code comes from the course material and which code is part of my own testing and experimentation.

Current course sample topics:

- Analysis of Algorithms
- Elementary sort
- Stacks Queues
- Union-Find

## Test Zone

The `test_zone/` folder contains my own implementations and test runners.

The tests are intentionally simple and readable. Each topic has a small `main.py` file that only calls test runner functions. The actual test cases live in separate `test_*.py` files so `main.py` stays clean and easy to scan.

Current test-zone topics:

- `analysis_of_algorithms/`
- `stacks_and_queues/`
- `union_find/`

## How To Run The Tests

From the repository root:

```bash
python test_zone/analysis_of_algorithms/main.py
```

```bash
python test_zone/elementary_sort/main.py
```

```bash
python test_zone/stacks_and_queues/main.py
```

```bash
python test_zone/union_find/main.py
```

## Test File Pattern

Future test-zone folders should follow this pattern:

```text
topic_folder/
|-- implementation_file.py
|-- another_implementation_file.py
|-- test_helpers.py
|-- test_specific_topic.py
`-- main.py
```

The responsibilities should stay separate:

- implementation files contain the data structure or algorithm code
- `test_helpers.py` contains shared printing helpers like expected vs actual output
- `test_*.py` files contain the real test cases
- `main.py` imports the test runner functions and calls them

Example `main.py` style:

```python
from test_binary_search import run_binary_search_tests
from test_sum import run_sum_tests


def main():
    run_binary_search_tests()
    run_sum_tests()


if __name__ == "__main__":
    main()
```

## What The Tests Check

The analysis-of-algorithms tests currently check binary search and sum-counting behavior such as:

- finding existing items
- missing items
- empty arrays
- one-item arrays
- first and last items
- even-sized arrays
- negative numbers
- duplicate values
- 1-sum zero counts
- 2-sum zero pairs
- 3-sum zero triples
- fast 3-sum behavior on sorted input

The elementary-sort tests check behavior such as:

- date comparison
- date representation
- selection sort
- insertion sort
- shellsort
- sorting empty and one-item lists
- sorting duplicates and negative values
- sorting `Date` objects
- shuffle length and item preservation

The stack and queue tests check behavior such as:

- empty structures
- push, pop, enqueue, and dequeue
- FIFO order for queues
- LIFO order for stacks
- resizing behavior
- linked-list pointer edge cases
- size updates
- reuse after becoming empty

The union-find tests check behavior such as:

- initial component setup
- `find`
- `connected`
- `union`
- transitive connections
- repeated unions
- invalid indexes

Some tests may intentionally fail while an implementation is still being developed. A failing test is useful when it shows a real bug or unfinished behavior.

## Project Goal

The goal is to build a small student-friendly collection of:

- course examples
- personal implementations
- test cases for common data structures and algorithms
- edge cases that often cause bugs

Over time, this repository can grow into a useful reference for students who want to compare their own implementations against clear behavior tests.

## License

This repository is licensed under the MIT License. See `LICENSE`.

The course sample code is included with permission. See `NOTICE.md` for the distinction between course sample material and my own `test_zone` work.
