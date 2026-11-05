
def fcfs_scheduling(processes):

    # Check whether the process list is empty
    if not processes:
        raise ValueError("No processes available for scheduling.")

    # Reset previous scheduling results
    for process in processes:
        process.remaining_time = process.burst_time
        process.completion_time = None
        process.waiting_time = None
        process.turnaround_time = None

    # Sort processes by arrival time.
    # Python's sorted() preserves input order when arrival times are equal.
    ordered_processes = sorted(
        processes,
        key=lambda process: process.arrival_time
    )

    current_time = 0

    # Store execution details for the Gantt chart
    gantt_chart = []

    # Execute processes one by one
    for process in ordered_processes:

        # Determine process starting time
        start_time = max(current_time, process.arrival_time)

        # Handle CPU idle time
        if current_time < process.arrival_time:

            gantt_chart.append({
                "process_id": "IDLE",
                "start_time": current_time,
                "end_time": process.arrival_time
            })

        # Calculate completion time
        completion_time = start_time + process.burst_time

        # Calculate turnaround time
        turnaround_time = completion_time - process.arrival_time

        # Calculate waiting time
        waiting_time = turnaround_time - process.burst_time

        # Update process information
        process.completion_time = completion_time
        process.turnaround_time = turnaround_time
        process.waiting_time = waiting_time
        process.remaining_time = 0

        # Store execution information for Gantt chart
        gantt_chart.append({
            "process_id": process.process_id,
            "start_time": start_time,
            "end_time": completion_time
        })

        # Update current CPU time
        current_time = completion_time

    # Return Gantt chart execution data
    return gantt_chart
