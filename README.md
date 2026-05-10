# DSA Course 2026

This repository is a learning companion for a Data Structures and Algorithms course.

It has two main parts:

- `course_sample_codes/`: original course sample code, included with permission.
- `test_zone/`: my own implementations, experiments, and beginner-friendly test runners.

The main idea is to make data structures easier to test and understand. Instead of only writing an implementation and hoping it works, the `test_zone` files print:

- the condition being tested
- the expected output
- the actual output
- whether the test passed or failed

This makes edge cases easier to see, especially for topics like stacks, queues, resizing arrays, linked lists, and union-find.

## Repository Structure

```text
dsa-course-2026/
├── course_sample_codes/
│   ├── Analysis of Algorithms/
│   ├── Elementary sort/
│   ├── Stacks Queues/
│   └── Union-Find/
├── test_zone/
│   ├── stacks_and_queues/
│   └── union_find/
├── README.md
├── NOTICE.md
└── LICENSE
```

## How To Run The Test Zone

From the repository root:

```bash
python test_zone/stacks_and_queues/main.py
```

```bash
python test_zone/union_find/main.py
```

The tests are intentionally simple and readable. They are written as `main.py` programs instead of a testing framework so that students can run, edit, and understand them easily.

## Project Goal

The goal is to build a small student-friendly collection of:

- course examples
- personal implementations
- test cases for common data structures
- edge cases that often cause bugs

Over time, this repository can grow into a useful reference for students who want to compare their own implementations against clear behavior tests.

## License

This repository is licensed under the MIT License. See `LICENSE`.

The course sample code is included with permission. See `NOTICE.md` for the distinction between course sample material and my own `test_zone` work.
