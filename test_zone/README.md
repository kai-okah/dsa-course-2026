# Test Zone

This folder contains my own implementations and test runners.

The goal is to make testing data structures beginner-friendly. Each `main.py` prints the condition being tested, the expected result, the actual result, and whether the result passed or failed.

## Current Topics

```text
test_zone/
├── stacks_and_queues/
└── union_find/
```

## Run The Tests

From the repository root:

```bash
python test_zone/stacks_and_queues/main.py
```

```bash
python test_zone/union_find/main.py
```

## What The Tests Check

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

## License

This folder is part of the MIT-licensed repository. See the root `LICENSE` file.
