# Intelligent CPU Scheduler Simulator

A Python desktop application for simulating CPU scheduling algorithms and visualizing their execution. Users can add processes through a Tkinter graphical interface, select a scheduling algorithm, view process-level performance results, and inspect an embedded Gantt chart.

## Features

- Add processes using Arrival Time, Burst Time, and Priority.
- Automatically generate process IDs (P1, P2, P3, ...).
- Run **First-Come, First-Served (FCFS)** scheduling.
- Run **Shortest Job First (SJF)** scheduling.
- Run **Priority Scheduling**.
- Display Completion Time, Waiting Time, and Turnaround Time for each process.
- Display Average Waiting Time, Average Turnaround Time, CPU Utilization, and Throughput.
- Visualize execution using a Matplotlib Gantt chart embedded in the dashboard.
- Delete a selected process, clear all processes, or reset simulation results.

> **Current algorithm support:** The dashboard currently offers FCFS, SJF, and Priority Scheduling. Round Robin is not included in the current dashboard.

## Technology Stack

- **Python** – application and scheduling logic
- **Tkinter / ttk** – desktop graphical user interface
- **Matplotlib** – Gantt chart visualization
- **Pandas** – process performance table and calculations

## Project Structure

```text
Intelligent_CPU_Scheduler/
├── assets/
│   └── fcfs_gantt_chart.png
├── gui/
│   ├── __init__.py
│   └── dashboard.py
├── modules/
│   ├── __init__.py
│   ├── fcfs.py
│   ├── priority.py
│   ├── process.py
│   └── sjf.py
├── tests/
│   ├── __init__.py
│   ├── test_gantt_chart.py
│   ├── test_performance.py
│   ├── test_priority.py
│   ├── test_process.py
│   ├── test_scheduler.py
│   └── test_sjf.py
├── visualization/
│   ├── __init__.py
│   ├── gantt_chart.py
│   └── performance.py
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

`__pycache__/` folders and `.pyc` files are generated automatically by Python and are intentionally omitted from this source tree.

## Requirements

- Python
- `pip`
- The packages listed in `requirements.txt`

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Intelligent_CPU_Scheduler
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your repository URL.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
```

**Linux / WSL:**

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / WSL:**

```bash
source .venv/bin/activate
```

### 4. Install the dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

On Ubuntu-based Linux/WSL systems, install Tkinter if it is not already available:

```bash
sudo apt update
sudo apt install python3-tk
```

## Run the Application

From the project root directory, execute:

```bash
python main.py
```

`main.py` creates the Tkinter root window and launches `CPUSchedulerDashboard` from `gui/dashboard.py`.

## How to Use

1. Launch the application with `python main.py`.
2. Enter Arrival Time, Burst Time, and Priority.
3. Click **Add Process**. A process ID is generated automatically.
4. Add the remaining processes.
5. Select **FCFS**, **SJF**, or **Priority** from the algorithm dropdown.
6. Click **Run Simulation**.
7. Review the process result table and performance metric cards.
8. Inspect the Gantt chart.
9. Use **Delete Selected** or **Clear All** to manage input processes.
10. Use **Reset Results** to clear the results and chart while keeping the input processes.

## Performance Metrics

| Metric | Meaning |
|---|---|
| Completion Time (CT) | Time at which a process finishes execution |
| Waiting Time (WT) | Time a process spends waiting in the ready queue |
| Turnaround Time (TAT) | Time from a process's arrival until its completion |
| Average Waiting Time | Average waiting time across all processes |
| Average Turnaround Time | Average turnaround time across all processes |
| CPU Utilization | Percentage of the measured time for which the CPU is busy |
| Throughput | Number of completed processes per unit of time |

## Project Modules

| File | Responsibility |
|---|---|
| `main.py` | Application entry point |
| `gui/dashboard.py` | Builds the GUI, accepts inputs, invokes scheduling, and displays results |
| `modules/process.py` | Defines the process data model |
| `modules/fcfs.py` | FCFS scheduling implementation |
| `modules/sjf.py` | SJF scheduling implementation |
| `modules/priority.py` | Priority scheduling implementation |
| `visualization/performance.py` | Calculates process performance data and summary metrics |
| `visualization/gantt_chart.py` | Creates the Gantt chart |
| `tests/` | Test scripts for process handling, scheduling, performance, and chart functionality |
| `assets/` | Static project assets |

## Testing

Test scripts are stored in `tests/`. From the project root and with the project virtual environment activated, run individual test modules:

```bash
python -m tests.test_process
python -m tests.test_sjf
python -m tests.test_priority
python -m tests.test_performance
python -m tests.test_gantt_chart
```

## Notes

- Run the application from the project root so package imports resolve correctly.
- Do not commit `.venv/`, `__pycache__/`, or `.pyc` files.
- Update `requirements.txt` whenever project dependencies change.
- The active dashboard supports FCFS, SJF, and Priority Scheduling.

## License

See the repository's `LICENSE` file for the applicable license terms.
