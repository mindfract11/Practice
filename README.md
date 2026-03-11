# Practice
The repository contains practice tasks for different topics in Python programming language.

# Setup 
Clone the repository and install the dependencies:

```bash
git clone https://github.com/mindfract11/Practice.git
cd Practice
```

Install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements/base.txt
```

# Run tests for tasks

```bash
pytest tests/
```

## Run a particular task

```bash
python tasks/task_1.py
```

## Run a particular test for a task

```bash
pytest tests/test_task_1.py
```

## Create a new branch for a task

```bash
git checkout -b task_<task_number>
```