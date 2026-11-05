
from modules.process import Process
from modules.round_robin import round_robin_scheduling


# Create sample processes
processes = [
    Process("P1", 0, 5, 2),
    Process("P2", 1, 3, 1),
    Process("P3", 2, 1, 3),
    Process("P4", 3, 2, 2)
]

# Set time quantum
time_quantum = 2

# Run Round Robin scheduling
gantt = round_robin_scheduling(
    processes,
    time_quantum
)

# Display Gantt chart
print("\nROUND ROBIN GANTT CHART")

for item in gantt:
    print(item)

# Display process performance
print("\nPROCESS PERFORMANCE")

for p in processes:
    print(
        p.process_id,
        "CT:", p.completion_time,
        "WT:", p.waiting_time,
        "TAT:", p.turnaround_time
    )

# Calculate average waiting time
avg_waiting = sum(
    p.waiting_time for p in processes
) / len(processes)

# Calculate average turnaround time
avg_turnaround = sum(
    p.turnaround_time for p in processes
) / len(processes)

print("\nAverage Waiting Time:", avg_waiting)

print("Average Turnaround Time:", avg_turnaround)
