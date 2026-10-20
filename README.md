# 🧠 AI/ML Engineering Journey

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![NumPy](https://img.shields.io/badge/NumPy-2.2-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

**A rigorous, production-grade learning journey through modern Artificial Intelligence, Machine Learning, Deep Learning, and MLOps.**  
Curriculum followed: *Apna College — Prime AI/ML Batch*.

[Explore Notebooks](#-curriculum--progress-tracker) • [Repository Structure](#-repository-architecture) • [Getting Started](#-getting-started)

</div>

---

## 📌 About This Repository

This repository documents my complete hands-on learning roadmap in **Artificial Intelligence & Machine Learning**. Rather than just running basic scripts, every topic is developed with:

1. **Granular Pedagogical Structure**: Every operation has a dedicated markdown explanation (mathematics, architectural rules, real-world ML use cases) paired directly above its executable code cell.
2. **Modular Isolation**: Each lecture and problem set is contained within its own dedicated notebook or script, eliminating messy monolithic files.
3. **Engineering Rigor**: Deep benchmarking on real memory usage (`sys.getsizeof` vs `nbytes`), execution latency (Vectorization vs Loops), and edge-case handling.

---

## 🗺️ Curriculum & Progress Tracker

### 🔹 Phase 1: Python Core Foundations (`python/`)
- [x] **Lecture 1**: Variables, Data Types, Operators (Arithmetic, Relational, Assignment, Logical) & Type Casting
- [x] **Lecture 2**: Conditional Statements (`if-elif-else`), Ladder logic & Number divisibility
- [x] **Lecture 3**: Lists & Tuples (Mutability, Built-in methods, Palindrome algorithms)
- [x] **Lecture 4**: Dictionaries & Sets (Nested structures, Hashmaps, Safe `.get()`, Unique sets)
- [x] **Lecture 5**: Loops & Control Flow (`while`, `for`, `range()`, `break`, `continue`, `pass`, Factorial & Series sum)
- [x] **Lecture 6**: Functions & Recursion (DRY principles, Default parameters, Stack memory & Base cases)
- [x] **Lecture 7**: File I/O (`open()`, Context managers `with open()`, Word replace, Stream parsing)
- [x] **Lecture 8**: Object-Oriented Programming (Classes, Objects, `__init__`, Abstraction, Encapsulation & Private attributes)

### 🔹 Phase 2: Real-World Data Pipelines & Analytics (`notebooks/day8/`)
- [x] **Assignment 1**: E-Commerce Data Cleaning Pipeline (JSON deserialization, Word-to-Number rating mapping, Whitespace sanitization, Null handling, Case-insensitive deduplication)
- [x] **Assignment 2**: Store Metrics & Analytics Engine (Average store rating, Poor rating percentage calculation, Customer sentiment)
- [x] **Assignment 3**: Rule-Based Recommendation Engine (Brand loyalty vs Competitor alternative recommendations based on satisfaction score)

### 🔹 Phase 3: High-Performance Numerical Computing with NumPy (`notebooks/day9/`)
- [x] **Lecture 1 & 2**: NumPy Setup, `ndarray` architecture, 1D array creation & Memory inspection
- [x] **Lecture 3**: Performance Benchmark — 1 Crore Elements Time Test (Vectorized C-speed) & Memory consumption (RAM bytes test)
- [x] **Lecture 4**: Creating Arrays from Lists, The Homogeneity Rule & Type Coercion (`<U11`), 2D Matrix (3x3 grid)
- [x] **Lecture 5**: Built-in Creation Methods (`zeros`, `ones`, `full`, `eye`, `arange`, `linspace`)
- [x] **Lecture 6**: Array Properties & Type Casting (`shape`, `size`, `dtype`, `ndim`, `arr.astype()`)
- [x] **Lecture 7**: Reshaping & Flattening (`arr.reshape()`, Golden rule of total elements, `arr.flatten()` for neural networks)
- [x] **Lecture 8**: Array Indexing (1D coordinates, 2D matrix indexing, Fancy Indexing, Boolean Masking)
- [x] **Lecture 9**: Slicing on Arrays (1D & 2D slicing, Step slicing, Sub-matrix extraction, Features-Target split)
- [ ] **Lecture 10**: Memory Mechanics — Copy vs View in Array Slicing
- [ ] **Lecture 11**: Multi-dimensional Arrays & Operations along Axes (`axis=0`, `axis=1`, 3D tensors)
- [ ] **Lecture 12**: Data Types & Downcasting for High-Volume Memory Optimization
- [ ] **Lecture 13**: Vectorization & Broadcasting Rules, Standard Vector Normalization $(\frac{x - \mu}{\sigma})$
- [ ] **Lecture 14**: Mathematical Functions (Aggregation, Power, Logarithmic, Exponential, Rounding)

### 🔹 Phase 4: Data Wrangling with Pandas *(Upcoming)*
- [ ] DataFrames & Series Structures
- [ ] Handling Missing Data & Imputation
- [ ] GroupBy, Merging, Joining & Pivoting
- [ ] Time-Series Analysis

### 🔹 Phase 5: Classical Machine Learning *(Upcoming)*
- [ ] Math for ML (Linear Algebra, Statistics & Probability)
- [ ] Supervised Learning (Linear Regression, Logistic Regression, Decision Trees, SVM)
- [ ] Unsupervised Learning (K-Means Clustering, PCA)
- [ ] Model Evaluation Metrics (Precision, Recall, F1-Score, Bias-Variance Tradeoff)

### 🔹 Phase 6: Deep Learning & Modern GenAI *(Upcoming)*
- [ ] Perceptrons, Artificial Neural Networks (ANN), CNNs, RNNs
- [ ] Transformers & Natural Language Processing (NLP)
- [ ] Retrieval-Augmented Generation (RAG) Architecture
- [ ] LLM Fine-Tuning & OpenAI API Integration
- [ ] MLOps: Docker, Kubernetes & Flask Model Deployment

---

## 📁 Repository Architecture

```text
aiml-journey/
├── README.md               # Portfolio documentation & live curriculum roadmap
├── .gitignore              # Ignores autosave checkpoints, cache, and virtual environments
│
├── notebooks/              # Modular Jupyter tutorial notebooks
│   ├── day8/               # Real-world e-commerce data pipeline & analytics assignments
│   │   ├── assignment_1.ipynb
│   │   ├── assignment_2.ipynb
│   │   ├── assignment_3.ipynb
│   │   └── store_data.json
│   │
│   └── day9/               # NumPy: Granular, lecture-by-lecture tutorial notebooks
│       ├── lec_1_2_intro.ipynb
│       ├── lec_3_list_vs_array.ipynb
│       ├── lec_4_array_creation.ipynb
│       ├── lec_5_builtin_methods.ipynb
│       ├── lec_6_array_properties.ipynb
│       ├── lec_7_reshaping_array.ipynb
│       └── lec_8_indexing.ipynb
│
└── python/                 # Core Python reference scripts with clean documentation
    ├── lec_1.py            # Basics, Operators, Type conversion
    ├── lec_2.py            # Conditionals (if-elif-else)
    ├── lec_3.py            # Lists, Tuples, Palindrome check
    ├── lec_4.py            # Dictionaries & Sets
    ├── lec_5.py            # Loops (while, for, range, break, continue)
    ├── lec_6.py            # Functions & Recursion
    ├── lec_7.py            # File I/O
    └── lec_8.py            # Object Oriented Programming (OOPs)
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+ (Recommended: Python 3.13)
- Git installed on your system

### Installation & Setup
```bash
# 1. Clone the repository
git clone https://github.com/yousufkidiya17/aiml-journey.git

# 2. Navigate into the directory
cd aiml-journey

# 3. Create and activate a virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install numpy ipykernel
```

---

## 👤 Author

**Mohammed Yousuf**  
*Student Builder & Aspiring AI/ML Engineer*  
- GitHub: [@yousufkidiya17](https://github.com/yousufkidiya17)  
- LinkedIn: [Mohammed Yousuf](https://www.linkedin.com/in/mohd-yousuf-a9648b2b0/)  

---

<div align="center">
<i>"Consistency in code is the foundation of mastery."</i>
</div>
