
import matplotlib.pyplot as plt

from modules.process import Process
from modules.fcfs import fcfs_scheduling
from visualization.gantt_chart import create_gantt_chart


# Create sample processes
processes = [
    Process("P1", 2, 3, 1),
    Process("P2", 7, 2, 2)
]


# Execute FCFS scheduling
gantt = fcfs_scheduling(processes)


# Generate Gantt chart
fig, ax = create_gantt_chart(
    gantt,
    "FCFS Scheduling Gantt Chart"
)


# Save chart as an image
fig.savefig(
    "assets/fcfs_gantt_chart.png",
    dpi=200,
    bbox_inches="tight"
)


# Display chart
plt.show()
