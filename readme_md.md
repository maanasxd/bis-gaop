# Vehicle Route Optimization using Genetic Algorithms

## 1. Background & Context

Logistics and delivery companies face the daily challenge of determining the most efficient routes for fleets of vehicles servicing multiple locations. Standard brute-force search methods become computationally impossible as the number of locations grows, because the number of possible routes increases exponentially. This constitutes an NP-hard problem known as the Travelling Salesperson Problem (TSP).

---

## 2. Problem Definition

Traditional exact algorithms, such as dynamic programming or brute-force search, fail to calculate optimal routes within a reasonable timeframe for large-scale delivery operations. Consequently, delivery fleets face significant operational inefficiencies:

* Increased fuel consumption and environmental impact
* Higher overall operational and fleet maintenance costs
* Longer transit times and delayed delivery schedules
* Accelerated vehicle wear-and-tear

---

## 3. Proposed Solution

This repository implements a **Genetic Algorithm (GA)** to solve the vehicle routing optimization problem by simulating the principles of natural selection and biological evolution.

### Algorithm Design & Workflow

```
[ Random Initialization ]
           │
           ▼
┌───────────────────────────┐
│ Evaluate Route Distance   │ ◄────────────────────────┐
└──────────┬────────────────┘                          │
           ▼                                           │
┌───────────────────────────┐                          │
│ Calculate Fitness Value   │                          │
└──────────┬────────────────┘                          │
           ▼                                           │ (Loop over N Generations)
┌───────────────────────────┐                          │
│   Tournament Selection    │                          │
└──────────┬────────────────┘                          │
           ▼                                           │
┌───────────────────────────┐                          │
│ Ordered Crossover (OX)    │                          │
└──────────┬────────────────┘                          │
           ▼                                           │
┌───────────────────────────┐                          │
│       Swap Mutation       │                          │
└──────────┬────────────────┘                          │
           ▼                                           │
┌───────────────────────────┐                          │
│ Form New Population       ├──────────────────────────┘
└──────────┬────────────────┘
           ▼
[ Output Best Route ]
```

### Core GA Components

1. **Solution Representation (Chromosome):** 
   Encodes routes using Permutation Encoding, where a candidate solution is represented as an ordered sequence of unique location IDs:
   $$\text{Chromosome} = [0, 4, 2, 7, 1, 5, 3, 6]$$

2. **Fitness Function:** 
   Evaluates solution quality inversely proportional to total round-trip Euclidean distance:
   $$\text{Fitness} = \frac{1}{\text{Total Route Distance}}$$

3. **Selection Mechanism:** 
   Utilizes **Tournament Selection** ($k=3$) to select superior candidates for reproduction while preserving population diversity.

4. **Crossover Operator:** 
   Applies **Ordered Crossover (OX)** to construct valid child offspring without introducing duplicate location IDs or illegal route sequences.

5. **Mutation Operator:** 
   Implements **Swap Mutation** by swapping the positions of two random delivery locations to introduce genetic variation and prevent premature convergence.

---

## 4. Constraints & Considerations

* **Computation Time vs. Route Quality:** Balances runtime execution limits against solution convergence accuracy over designated generations.
* **Avoidance of Local Optima:** Incorporates dynamic mutation tuning to maintain sufficient genetic variation and avoid local minima traps.
* **Scalability:** Engineered to evaluate benchmarks ranging from 10 to over 100 delivery locations within acceptable execution parameters.

---

## 5. Repository Structure & Deliverables

```text
├── ga_tsp/
│   ├── __init__.py
│   ├── ga_engine.py       # Core GA module (Initialization, Fitness, Selection, OX, Mutation)
│   └── utils.py           # Distance metrics & coordinate generators
├── main.py                # Pipeline execution script
├── visualization.py       # Plotting scripts for convergence & route graphs
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

### Key Deliverables
* **Modular Codebase:** Production-ready Python modules implementing object-oriented GA design.
* **Convergence Analysis:** Real-time distance convergence tracking across $N$ generations.
* **Route Visualization:** Graph rendering utilities to compare initial random routes against final optimized paths.

---

## 6. Execution Instructions

### Prerequisites
Python 3.8 or higher with standard numerical and visualization libraries:

```bash
pip install matplotlib numpy
```

### Running the Pipeline
Execute the main entry script to initiate the optimization process:

```bash
python main.py
```

### Sample Console Output

```text
--- Running GA for Vehicle Route Optimization (10 Cities) ---
Gen 001 | Current Best Distance: 42.85 | Overall Best: 42.85
Gen 010 | Current Best Distance: 31.12 | Overall Best: 31.12
Gen 050 | Current Best Distance: 24.03 | Overall Best: 24.03
Gen 100 | Current Best Distance: 18.45 | Overall Best: 18.45

--- Final Optimized Route ---
Path: 0 -> 4 -> 1 -> 9 -> 3 -> 7 -> 5 -> 2 -> 6 -> 8 -> 0
Minimum Distance: 18.45
```

---

## 7. License

This project is licensed under the [MIT License](LICENSE).