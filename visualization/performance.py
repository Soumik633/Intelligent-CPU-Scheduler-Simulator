
import pandas as pd


def calculate_performance(processes, gantt_chart):

    # Check whether processes are available
    if not processes:
        raise ValueError("No processes available for analysis.")

    # Check whether Gantt chart data is available
    if not gantt_chart:
        raise ValueError("No scheduling data available.")

    # Verify that all processes have completed
    for process in processes:

        if (
            process.completion_time is None
            or process.waiting_time is None
            or process.turnaround_time is None
        ):
            raise ValueError(
                f"Process {process.process_id} has not completed scheduling."
            )

    # Create process-wise performance records
    process_data = []

    for process in processes:

        process_data.append({
            "Process ID": process.process_id,
            "Arrival Time": process.arrival_time,
            "Burst Time": process.burst_time,
            "Priority": process.priority,
            "Completion Time": process.completion_time,
            "Waiting Time": process.waiting_time,
            "Turnaround Time": process.turnaround_time
        })

    # Convert process data into a Pandas DataFrame
    process_table = pd.DataFrame(process_data)

    # Calculate average waiting time
    average_waiting_time = process_table[
        "Waiting Time"
    ].mean()

    # Calculate average turnaround time
    average_turnaround_time = process_table[
        "Turnaround Time"
    ].mean()

    # Find total simulation starting and ending time
    simulation_start = min(
        item["start_time"] for item in gantt_chart
    )

    simulation_end = max(
        item["end_time"] for item in gantt_chart
    )

    # Calculate total simulation time
    total_simulation_time = simulation_end - simulation_start

    if total_simulation_time <= 0:
        raise ValueError("Invalid simulation time.")

    # Calculate CPU busy time (excluding idle periods)
    cpu_busy_time = sum(
        item["end_time"] - item["start_time"]
        for item in gantt_chart
        if item["process_id"] != "IDLE"
    )

    # Calculate CPU utilization
    cpu_utilization = (
        cpu_busy_time / total_simulation_time
    ) * 100

    # Calculate throughput
    throughput = (
        len(processes) / total_simulation_time
    )

    # Return all performance results
    return {

        "process_table": process_table,

        "average_waiting_time": average_waiting_time,

        "average_turnaround_time": average_turnaround_time,

        "cpu_utilization": cpu_utilization,

        "throughput": throughput,

        "cpu_busy_time": cpu_busy_time,

        "total_simulation_time": total_simulation_time
    }
