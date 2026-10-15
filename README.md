# 2601050113_MTECH_CTP_LABEXAM
# List Comprehension vs Generator Expression in Python

## Project Overview

This project compares the performance of List Comprehension and Generator Expression in Python by measuring execution time and memory consumption while processing 5 million numbers.

## Objectives

- Compare execution time of both approaches.
- Analyze memory consumption.
- Understand eager and lazy evaluation.
- Identify the most memory-efficient approach.

## Technologies Used

- Python 3
- time module
- tracemalloc module

## Implementation

The program squares 5 million numbers using two approaches.

**List Comprehension:**
```python
result_list = [transform(x) for x in range(N)]
```

**Generator Expression:**
```python
result_generator = (transform(x) for x in range(N))
```

## Sample Output

The following is an illustrative output. Actual execution times and memory usage depend on the system.

```text
LIST COMPREHENSION
Creation time: 4.8231 seconds
Memory used: 203.67 MB
Consumption time: 0.0982 seconds
Total: 41666654166667500000

GENERATOR EXPRESSION
Creation time: 0.000012 seconds
Memory used: 0.0005 MB
Consumption time: 0.6254 seconds
Total: 41666654166667500000
```

## Performance Comparison

| Parameter | List Comprehension | Generator Expression |
|---|---:|---:|
| Creation Time | 4.8231 sec | 0.000012 sec |
| Peak Creation Memory | 203.67 MB | 0.0005 MB |
| Consumption Time | 0.0982 sec | 0.6254 sec |
| Evaluation | Eager | Lazy |
| Memory Efficiency | Lower | Higher |

*Note: These are illustrative benchmark values, not measured results from a specific execution.*

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder.
4. Run the following command:

```bash
python main.py
```

##
