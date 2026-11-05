
class Process:

    def __init__(self, process_id, arrival_time, burst_time, priority):

        # Validate process details
        if not process_id:
            raise ValueError("Process ID cannot be empty.")

        if arrival_time < 0:
            raise ValueError("Arrival time cannot be negative.")

        if burst_time <= 0:
            raise ValueError("Burst time must be greater than zero.")

        if priority <= 0:
            raise ValueError("Priority must be greater than zero.")

        # Basic process information
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

        # Scheduling information
        self.remaining_time = burst_time
        self.completion_time = None
        self.waiting_time = None
        self.turnaround_time = None

    def display(self):
        print("Process ID:", self.process_id)
        print("Arrival Time:", self.arrival_time)
        print("Burst Time:", self.burst_time)
        print("Priority:", self.priority)
        print("Remaining Time:", self.remaining_time)
        print("Completion Time:", self.completion_time)
        print("Waiting Time:", self.waiting_time)
        print("Turnaround Time:", self.turnaround_time)
