
def sjf_scheduling(processes):

    # Check whether the process list is empty
    if not processes:
        raise ValueError("No processes available for scheduling.")

    # Reset previous scheduling results
    for process in processes:
        process.remaining_time = process.burst_time
        process.completion_time = None
        process.waiting_time = None
        process.turnaround_time = None

    # Sort processes by arrival time
    pending_processes = sorted(
        processes,
        key=lambda process: process.arrival_time
    )

    current_time = 0

    # Store execution details for Gantt chart
    gantt_chart = []

    # Continue until every process is completed
    while pending_processes:

        # Find processes that have already arrived
        available_processes = [
            process for process in pending_processes
            if process.arrival_time <= current_time
        ]

        # Handle CPU idle time
        if not available_processes:

            next_arrival = pending_processes[0].arrival_time

            gantt_chart.append({
                "process_id": "IDLE",
                "start_time": current_time,
                "end_time": next_arrival
            })

            current_time = next_arrival

            continue

        # Select the process with the shortest burst time
        # Ties are resolved by earlier arrival time and input order
        selected_process = min(
            available_processes,
            key=lambda process: process.burst_time
        )

        # Remove the selected process from pending processes
        pending_processes.remove(selected_process)

        # Calculate execution details
        start_time = current_time

        completion_time = start_time + selected_process.burst_time

        turnaround_time = (
            completion_time - selected_process.arrival_time
        )

        waiting_time = (
            turnaround_time - selected_process.burst_time
        )

        # Update process information
        selected_process.completion_time = completion_time
        selected_process.turnaround_time = turnaround_time
        selected_process.waiting_time = waiting_time
        selected_process.remaining_time = 0

        # Store execution details for Gantt chart
        gantt_chart.append({
            "process_id": selected_process.process_id,
            "start_time": start_time,
            "end_time": completion_time
        })

        # Update current CPU time
        current_time = completion_time

    return gantt_chart
