
from collections import deque


def round_robin_scheduling(processes, time_quantum):

    # Check whether processes are available
    if not processes:
        raise ValueError("No processes available for scheduling.")

    # Validate time quantum
    if (
        not isinstance(time_quantum, int)
        or isinstance(time_quantum, bool)
        or time_quantum <= 0
    ):
        raise ValueError("Time quantum must be a positive integer.")

    # Reset previous scheduling results
    for process in processes:
        process.remaining_time = process.burst_time
        process.completion_time = None
        process.waiting_time = None
        process.turnaround_time = None

    # Sort processes by arrival time
    ordered_processes = sorted(
        processes,
        key=lambda process: process.arrival_time
    )

    # Create the ready queue
    ready_queue = deque()

    # Store Gantt chart execution details
    gantt_chart = []

    current_time = 0
    next_process_index = 0

    # Continue until all processes are completed
    while ready_queue or next_process_index < len(ordered_processes):

        # Add all processes that have arrived
        while (
            next_process_index < len(ordered_processes)
            and ordered_processes[next_process_index].arrival_time <= current_time
        ):
            ready_queue.append(
                ordered_processes[next_process_index]
            )

            next_process_index += 1

        # Handle CPU idle time
        if not ready_queue:

            next_arrival = ordered_processes[
                next_process_index
            ].arrival_time

            if current_time < next_arrival:

                gantt_chart.append({
                    "process_id": "IDLE",
                    "start_time": current_time,
                    "end_time": next_arrival
                })

                current_time = next_arrival

            continue

        # Select the first process in the queue
        current_process = ready_queue.popleft()

        # Record execution starting time
        start_time = current_time

        # Determine execution duration
        execution_time = min(
            time_quantum,
            current_process.remaining_time
        )

        # Execute the process
        current_time += execution_time

        # Update remaining burst time
        current_process.remaining_time -= execution_time

        # Save Gantt chart execution details
        gantt_chart.append({
            "process_id": current_process.process_id,
            "start_time": start_time,
            "end_time": current_time
        })

        # Add newly arrived processes to the queue
        while (
            next_process_index < len(ordered_processes)
            and ordered_processes[next_process_index].arrival_time <= current_time
        ):
            ready_queue.append(
                ordered_processes[next_process_index]
            )

            next_process_index += 1

        # Check whether the process has completed
        if current_process.remaining_time > 0:

            # Move unfinished process to the end of the queue
            ready_queue.append(current_process)

        else:

            # Calculate completion time
            current_process.completion_time = current_time

            # Calculate turnaround time
            current_process.turnaround_time = (
                current_process.completion_time
                - current_process.arrival_time
            )

            # Calculate waiting time
            current_process.waiting_time = (
                current_process.turnaround_time
                - current_process.burst_time
            )

    # Return execution details
    return gantt_chart
