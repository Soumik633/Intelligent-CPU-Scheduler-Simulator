
from modules.process import Process
from modules.sjf import sjf_scheduling

# Create sample processes
processes = [
    Process("P1", 0, 5, 2),
    Process("P2", 1, 3, 1),
    Process("P3", 2, 1, 3),
    Process("P4", 3, 2, 2)
]

# Run SJF scheduling
gantt = sjf_scheduling(processes)

# Display Gantt chart
print("\nSJF Gantt Chart:")

for item in gantt:
    print(item)

# Display process performance
print("\nProcess Performance:")

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
