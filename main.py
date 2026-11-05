import tkinter as tk
from gui.dashboard import CPUSchedulerDashboard


def main():
    # Create the main application window
    root = tk.Tk()

    # Initialize the CPU Scheduler Dashboard
    CPUSchedulerDashboard(root)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()