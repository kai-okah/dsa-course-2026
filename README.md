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

The tests are intentionally simple and readable. They are written as `main.py` programs instead of a testing framework so that students can run, edit, and understand them easily.

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
python test_zone/stacks_and_queues/main.py
```

```bash
python test_zone/union_find/main.py
```

## What The Tests Check

The analysis-of-algorithms tests currently check binary search behavior such as:

- finding existing items
- missing items
- empty arrays
- one-item arrays
- first and last items
- even-sized arrays
- negative numbers
- duplicate values

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
