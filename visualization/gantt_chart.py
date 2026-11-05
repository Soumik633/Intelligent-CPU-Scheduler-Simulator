
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def create_gantt_chart(gantt_chart, title="CPU Scheduling Gantt Chart"):

    # Check whether Gantt chart data is available
    if not gantt_chart:
        raise ValueError("No Gantt chart data available.")

    # Validate and prepare execution segments
    segments = []

    for item in gantt_chart:

        if not all(
            key in item
            for key in ["process_id", "start_time", "end_time"]
        ):
            raise ValueError("Invalid Gantt chart data.")

        process_id = str(item["process_id"])
        start_time = item["start_time"]
        end_time = item["end_time"]

        if end_time <= start_time:
            raise ValueError("Execution end time must be greater than start time.")

        segments.append({
            "process_id": process_id,
            "start_time": start_time,
            "end_time": end_time
        })

    # Define colours for different processes
    color_palette = [
        "#2563EB",
        "#16A34A",
        "#D97706",
        "#9333EA",
        "#0891B2",
        "#BE185D",
        "#4D7C0F",
        "#475569",
        "#B45309",
        "#0F766E"
    ]

    # Assign a different colour to each process
    process_ids = list(dict.fromkeys(
        item["process_id"]
        for item in segments
        if item["process_id"] != "IDLE"
    ))

    process_colors = {}

    for index, process_id in enumerate(process_ids):
        process_colors[process_id] = color_palette[
            index % len(color_palette)
        ]

    # Create Matplotlib figure
    fig, ax = plt.subplots(figsize=(13, 3.5))

    # Draw every execution segment
    for item in segments:

        process_id = item["process_id"]
        start_time = item["start_time"]
        end_time = item["end_time"]

        duration = end_time - start_time

        # Use grey colour for CPU idle time
        if process_id == "IDLE":
            color = "#D1D5DB"
            text_color = "#111827"
        else:
            color = process_colors[process_id]
            text_color = "white"

        # Create the Gantt chart block
        rectangle = Rectangle(
            (start_time, 0.25),
            duration,
            0.5,
            facecolor=color,
            edgecolor="white",
            linewidth=2
        )

        ax.add_patch(rectangle)

        # Display process ID inside the block
        ax.text(
            start_time + duration / 2,
            0.5,
            process_id,
            ha="center",
            va="center",
            color=text_color,
            fontsize=10,
            fontweight="bold"
        )

    # Collect all starting and ending timestamps
    time_points = sorted(
        set(
            [item["start_time"] for item in segments]
            + [item["end_time"] for item in segments]
        )
    )

    # Configure chart axes
    ax.set_xlim(
        min(time_points),
        max(time_points)
    )

    ax.set_ylim(0, 1)

    ax.set_xticks(time_points)

    ax.set_yticks([0.5])
    ax.set_yticklabels(["CPU"])

    # Add title and labels
    ax.set_title(
        title,
        fontsize=15,
        fontweight="bold",
        pad=15
    )

    ax.set_xlabel(
        "Execution Time",
        fontsize=11
    )

    # Display time grid
    ax.grid(
        axis="x",
        linestyle="--",
        alpha=0.4
    )

    ax.set_axisbelow(True)

    # Remove unnecessary borders
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.spines["left"].set_visible(False)

    # Adjust chart layout
    plt.tight_layout()

    # Return figure and axes for later GUI integration
    return fig, ax
