
from modules.process import Process
from modules.fcfs import fcfs_scheduling
from visualization.performance import calculate_performance


# Create sample processes
processes = [
    Process("P1", 0, 5, 2),
    Process("P2", 1, 3, 1),
    Process("P3", 2, 1, 3),
    Process("P4", 3, 2, 2)
]


# Execute FCFS scheduling
gantt = fcfs_scheduling(processes)


# Calculate performance
results = calculate_performance(processes, gantt)


# Display process performance table
print("\nPROCESS PERFORMANCE TABLE")

print(
    results["process_table"].to_string(
        index=False,
        columns=[
            "Process ID",
            "Arrival Time",
            "Burst Time",
            "Completion Time",
            "Waiting Time",
            "Turnaround Time"
        ]
    )
)


# Display average waiting time
print("\nAverage Waiting Time:",
      round(results["average_waiting_time"], 2))


# Display average turnaround time
print("Average Turnaround Time:",
      round(results["average_turnaround_time"], 2))


# Display CPU utilization
print("CPU Utilization:",
      round(results["cpu_utilization"], 2), "%")


# Display throughput
print("Throughput:",
      round(results["throughput"], 4))


# Display CPU busy time
print("CPU Busy Time:",
      results["cpu_busy_time"])


# Display total simulation time
print("Total Simulation Time:",
      results["total_simulation_time"])
