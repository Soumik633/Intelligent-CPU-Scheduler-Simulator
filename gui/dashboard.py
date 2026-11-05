

import tkinter as tk

from tkinter import ttk, messagebox



import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



from modules.process import Process

from modules.fcfs import fcfs_scheduling

from modules.sjf import sjf_scheduling


from modules.priority import priority_scheduling



from visualization.performance import calculate_performance

from visualization.gantt_chart import create_gantt_chart





class CPUSchedulerDashboard:



    def __init__(self, root):



        self.root = root



        self.root.title("Intelligent CPU Scheduler Simulator")

        self.root.geometry("1180x820")

        self.root.minsize(950, 700)

        self.root.configure(bg="#F3F5F9")



        self.processes = []

        self.next_process_number = 1



        self.chart_canvas = None

        self.current_figure = None



        self.configure_styles()

        self.create_dashboard()



    # --------------------------------------------------

    # STYLE CONFIGURATION

    # --------------------------------------------------



    def configure_styles(self):



        style = ttk.Style(self.root)



        try:

            style.theme_use("clam")

        except tk.TclError:

            pass



        style.configure(

            "App.TFrame",

            background="#F3F5F9"

        )



        style.configure(

            "Card.TLabelframe",

            background="white",

            padding=10

        )



        style.configure(

            "Card.TLabelframe.Label",

            background="white",

            foreground="#1E293B",

            font=("Arial", 11, "bold")

        )



        style.configure(

            "Title.TLabel",

            background="#F3F5F9",

            foreground="#172554",

            font=("Arial", 21, "bold")

        )



        style.configure(

            "Subtitle.TLabel",

            background="#F3F5F9",

            foreground="#64748B",

            font=("Arial", 10)

        )



        style.configure(

            "TButton",

            font=("Arial", 10),

            padding=7

        )



        style.configure(

            "Accent.TButton",

            background="#2563EB",

            foreground="white",

            font=("Arial", 10, "bold"),

            padding=9

        )



        style.map(

            "Accent.TButton",

            background=[("active", "#1D4ED8")]

        )



        style.configure(

            "Danger.TButton",

            background="#DC2626",

            foreground="white",

            padding=7

        )



        style.configure(

            "Treeview",

            background="white",

            foreground="#1E293B",

            rowheight=27,

            font=("Arial", 9),

            fieldbackground="white"

        )



        style.configure(

            "Treeview.Heading",

            background="#E2E8F0",

            foreground="#1E293B",

            font=("Arial", 9, "bold"),

            padding=6

        )



    # --------------------------------------------------

    # MAIN DASHBOARD

    # --------------------------------------------------



    def create_dashboard(self):



        container = ttk.Frame(

            self.root,

            padding=15,

            style="App.TFrame"

        )



        container.grid(

            row=0,

            column=0,

            sticky="nsew"

        )



        self.root.columnconfigure(0, weight=1)

        self.root.rowconfigure(0, weight=1)



        container.columnconfigure(0, weight=1)

        container.rowconfigure(4, weight=1)



        self.create_header(container)

        self.create_control_section(container)

        self.create_tables(container)

        self.create_metrics(container)

        self.create_chart_section(container)



        self.status_var = tk.StringVar(

            value="Ready. Add processes to begin."

        )



        status_label = ttk.Label(

            container,

            textvariable=self.status_var,

            background="#F3F5F9",

            foreground="#64748B",

            font=("Arial", 9)

        )



        status_label.grid(

            row=5,

            column=0,

            sticky="w",

            pady=(8, 0)

        )



    # --------------------------------------------------

    # HEADER

    # --------------------------------------------------



    def create_header(self, parent):



        header = ttk.Frame(

            parent,

            style="App.TFrame"

        )



        header.grid(

            row=0,

            column=0,

            sticky="ew",

            pady=(0, 12)

        )



        ttk.Label(

            header,

            text="INTELLIGENT CPU SCHEDULER",

            style="Title.TLabel"

        ).pack(anchor="w")



        ttk.Label(

            header,

            text=(

                "Simulate CPU scheduling algorithms "

                "and analyze their performance."

            ),

            style="Subtitle.TLabel"

        ).pack(anchor="w", pady=(4, 0))



    # --------------------------------------------------

    # PROCESS INPUT AND ALGORITHM CONTROLS

    # --------------------------------------------------



    def create_control_section(self, parent):



        section = ttk.Frame(

            parent,

            style="App.TFrame"

        )



        section.grid(

            row=1,

            column=0,

            sticky="ew",

            pady=(0, 10)

        )



        section.columnconfigure(0, weight=2)

        section.columnconfigure(1, weight=1)



        # Process management section

        input_frame = ttk.LabelFrame(

            section,

            text="Process Management",

            style="Card.TLabelframe"

        )



        input_frame.grid(

            row=0,

            column=0,

            sticky="nsew",

            padx=(0, 8)

        )



        for column in range(4):

            input_frame.columnconfigure(column, weight=1)



        ttk.Label(

            input_frame,

            text="Arrival Time"

        ).grid(row=0, column=0, sticky="w")



        ttk.Label(

            input_frame,

            text="Burst Time"

        ).grid(row=0, column=1, sticky="w")



        ttk.Label(

            input_frame,

            text="Priority"

        ).grid(row=0, column=2, sticky="w")



        self.arrival_entry = ttk.Entry(

            input_frame,

            width=12

        )



        self.arrival_entry.grid(

            row=1,

            column=0,

            sticky="ew",

            padx=(0, 5),

            pady=5

        )



        self.burst_entry = ttk.Entry(

            input_frame,

            width=12

        )



        self.burst_entry.grid(

            row=1,

            column=1,

            sticky="ew",

            padx=5,

            pady=5

        )



        self.priority_entry = ttk.Entry(

            input_frame,

            width=12

        )



        self.priority_entry.grid(

            row=1,

            column=2,

            sticky="ew",

            padx=5,

            pady=5

        )



        ttk.Button(

            input_frame,

            text="Add Process",

            style="Accent.TButton",

            command=self.add_process

        ).grid(

            row=1,

            column=3,

            sticky="ew",

            padx=(5, 0),

            pady=5

        )



        ttk.Label(

            input_frame,

            text="Process IDs are generated automatically (P1, P2, P3...).",

            foreground="#64748B"

        ).grid(

            row=2,

            column=0,

            columnspan=4,

            sticky="w",

            pady=(4, 0)

        )



        # Algorithm selection section

        algorithm_frame = ttk.LabelFrame(

            section,

            text="Scheduling Controls",

            style="Card.TLabelframe"

        )



        algorithm_frame.grid(

            row=0,

            column=1,

            sticky="nsew"

        )



        ttk.Label(

            algorithm_frame,

            text="Select Algorithm"

        ).grid(

            row=0,

            column=0,

            sticky="w"

        )



        self.algorithm_var = tk.StringVar(value="FCFS")



        self.algorithm_combo = ttk.Combobox(

            algorithm_frame,

            textvariable=self.algorithm_var,

            values=[

                "FCFS",

                "SJF",

                "Priority"

            ],

            state="readonly",

            width=18

        )



        self.algorithm_combo.grid(

            row=1,

            column=0,

            sticky="ew",

            pady=5

        )

        # Simulation buttons

        button_frame = ttk.Frame(algorithm_frame)



        button_frame.grid(

            row=2,

            column=0,

            sticky="ew"

        )



        ttk.Button(

            button_frame,

            text="Run Simulation",

            style="Accent.TButton",

            command=self.run_simulation

        ).pack(

            side="left",

            fill="x",

            expand=True,

            padx=(0, 4)

        )



        ttk.Button(

            button_frame,

            text="Reset Results",

            command=self.reset_results

        ).pack(

            side="left",

            fill="x",

            expand=True

        )



        # Process management buttons

        management_frame = ttk.Frame(input_frame)



        management_frame.grid(

            row=3,

            column=0,

            columnspan=4,

            sticky="w",

            pady=(5, 0)

        )



        ttk.Button(

            management_frame,

            text="Delete Selected",

            command=self.delete_process

        ).pack(side="left", padx=(0, 5))



        ttk.Button(

            management_frame,

            text="Clear All",

            style="Danger.TButton",

            command=self.clear_all_processes

        ).pack(side="left")



    # --------------------------------------------------

    # PROCESS AND RESULT TABLES

    # --------------------------------------------------



    def create_tables(self, parent):



        tables_frame = ttk.Frame(

            parent,

            style="App.TFrame"

        )



        tables_frame.grid(

            row=2,

            column=0,

            sticky="nsew",

            pady=(0, 10)

        )



        tables_frame.columnconfigure(0, weight=1)

        tables_frame.columnconfigure(1, weight=1)



        # Input process table

        process_frame = ttk.LabelFrame(

            tables_frame,

            text="Input Process Table",

            style="Card.TLabelframe"

        )



        process_frame.grid(

            row=0,

            column=0,

            sticky="nsew",

            padx=(0, 5)

        )



        process_columns = (

            "pid",

            "arrival",

            "burst",

            "priority"

        )



        self.process_tree = ttk.Treeview(

            process_frame,

            columns=process_columns,

            show="headings",

            height=4,

            selectmode="browse"

        )



        headings = {

            "pid": "Process ID",

            "arrival": "Arrival Time",

            "burst": "Burst Time",

            "priority": "Priority"

        }



        for column, heading in headings.items():



            self.process_tree.heading(

                column,

                text=heading

            )



            self.process_tree.column(

                column,

                width=100,

                anchor="center"

            )



        self.process_tree.pack(

            fill="both",

            expand=True

        )



        # Performance result table

        result_frame = ttk.LabelFrame(

            tables_frame,

            text="Process Performance Results",

            style="Card.TLabelframe"

        )



        result_frame.grid(

            row=0,

            column=1,

            sticky="nsew",

            padx=(5, 0)

        )



        result_columns = (

            "pid",

            "ct",

            "wt",

            "tat"

        )



        self.result_tree = ttk.Treeview(

            result_frame,

            columns=result_columns,

            show="headings",

            height=4

        )



        result_headings = {

            "pid": "Process ID",

            "ct": "Completion Time",

            "wt": "Waiting Time",

            "tat": "Turnaround Time"

        }



        for column, heading in result_headings.items():



            self.result_tree.heading(

                column,

                text=heading

            )



            self.result_tree.column(

                column,

                width=100,

                anchor="center"

            )



        self.result_tree.pack(

            fill="both",

            expand=True

        )



    # --------------------------------------------------

    # PERFORMANCE METRIC CARDS

    # --------------------------------------------------



    def create_metrics(self, parent):



        metrics_frame = ttk.Frame(

            parent,

            style="App.TFrame"

        )



        metrics_frame.grid(

            row=3,

            column=0,

            sticky="ew",

            pady=(0, 10)

        )



        for column in range(4):

            metrics_frame.columnconfigure(column, weight=1)



        metric_details = [

            ("Average Waiting Time", "waiting"),

            ("Average Turnaround Time", "turnaround"),

            ("CPU Utilization", "utilization"),

            ("Throughput", "throughput")

        ]



        self.metric_labels = {}



        for index, (title, key) in enumerate(metric_details):



            card = ttk.LabelFrame(

                metrics_frame,

                text=title,

                style="Card.TLabelframe"

            )



            card.grid(

                row=0,

                column=index,

                sticky="nsew",

                padx=4

            )



            value_label = ttk.Label(

                card,

                text="--",

                foreground="#2563EB",

                background="white",

                font=("Arial", 17, "bold"),

                anchor="center"

            )



            value_label.pack(

                fill="both",

                expand=True,

                pady=5

            )



            self.metric_labels[key] = value_label



    # --------------------------------------------------

    # GANTT CHART SECTION

    # --------------------------------------------------



    def create_chart_section(self, parent):



        chart_frame = ttk.LabelFrame(

            parent,

            text="CPU Scheduling Gantt Chart",

            style="Card.TLabelframe"

        )



        chart_frame.grid(

            row=4,

            column=0,

            sticky="nsew"

        )



        self.chart_holder = ttk.Frame(

            chart_frame,

            style="App.TFrame"

        )



        self.chart_holder.pack(

            fill="both",

            expand=True

        )



        self.chart_placeholder = ttk.Label(

            self.chart_holder,

            text="Run a simulation to display the Gantt chart.",

            foreground="#64748B",

            background="#F3F5F9",

            font=("Arial", 12)

        )



        self.chart_placeholder.pack(expand=True)




    # --------------------------------------------------

    # ADD NEW PROCESS

    # --------------------------------------------------



    def add_process(self):



        try:



            arrival_time = int(

                self.arrival_entry.get().strip()

            )



            burst_time = int(

                self.burst_entry.get().strip()

            )



            priority = int(

                self.priority_entry.get().strip()

            )



        except ValueError:



            messagebox.showerror(

                "Invalid Input",

                "Please enter valid integer values for all fields."

            )



            return



        if arrival_time < 0:



            messagebox.showerror(

                "Invalid Arrival Time",

                "Arrival time cannot be negative."

            )



            return



        if burst_time <= 0:



            messagebox.showerror(

                "Invalid Burst Time",

                "Burst time must be greater than zero."

            )



            return



        if priority <= 0:



            messagebox.showerror(

                "Invalid Priority",

                "Priority must be greater than zero."

            )



            return



        process_id = f"P{self.next_process_number}"



        try:



            process = Process(

                process_id,

                arrival_time,

                burst_time,

                priority

            )



        except ValueError as error:



            messagebox.showerror(

                "Process Error",

                str(error)

            )



            return



        self.processes.append(process)



        self.next_process_number += 1



        self.process_tree.insert(

            "",

            "end",

            iid=process_id,

            values=(

                process_id,

                arrival_time,

                burst_time,

                priority

            )

        )



        self.arrival_entry.delete(0, tk.END)

        self.burst_entry.delete(0, tk.END)

        self.priority_entry.delete(0, tk.END)



        self.arrival_entry.focus()



        self.reset_results(update_status=False)



        self.status_var.set(

            f"{process_id} added successfully."

        )



    # --------------------------------------------------

    # DELETE SELECTED PROCESS

    # --------------------------------------------------



    def delete_process(self):



        selected = self.process_tree.selection()



        if not selected:



            messagebox.showwarning(

                "No Selection",

                "Please select a process to delete."

            )



            return



        selected_id = selected[0]



        self.processes = [

            process for process in self.processes

            if process.process_id != selected_id

        ]



        self.process_tree.delete(selected_id)



        self.reset_results(update_status=False)



        self.status_var.set(

            f"{selected_id} deleted successfully."

        )



    # --------------------------------------------------

    # CLEAR ALL PROCESSES

    # --------------------------------------------------



    def clear_all_processes(self):



        self.processes.clear()



        self.next_process_number = 1



        for item in self.process_tree.get_children():

            self.process_tree.delete(item)



        self.reset_results(update_status=False)



        self.status_var.set(

            "All processes cleared."

        )



    # --------------------------------------------------

    # RUN CPU SCHEDULING SIMULATION

    # --------------------------------------------------



    def run_simulation(self):



        if not self.processes:



            messagebox.showwarning(

                "No Processes",

                "Please add at least one process before simulation."

            )



            return



        algorithm = self.algorithm_var.get()



        try:



            # Create fresh process objects for every simulation

            simulation_processes = [



                Process(

                    process.process_id,

                    process.arrival_time,

                    process.burst_time,

                    process.priority

                )



                for process in self.processes

            ]



            # Execute selected algorithm

            if algorithm == "FCFS":



                gantt = fcfs_scheduling(

                    simulation_processes

                )



            elif algorithm == "SJF":



                gantt = sjf_scheduling(

                    simulation_processes

                )




            elif algorithm == "Priority":



                gantt = priority_scheduling(

                    simulation_processes

                )



            else:



                raise ValueError(

                    "Please select a valid scheduling algorithm."

                )



            # Calculate performance

            performance = calculate_performance(

                simulation_processes,

                gantt

            )



            # Display results

            self.display_results(performance)



            # Display Gantt chart

            self.display_gantt_chart(

                gantt,

                algorithm

            )



            self.status_var.set(

                f"{algorithm} simulation completed successfully."

            )



        except (ValueError, TypeError) as error:



            messagebox.showerror(

                "Simulation Error",

                str(error)

            )



        except Exception as error:



            messagebox.showerror(

                "Unexpected Error",

                f"An error occurred:\n{error}"

            )



    # --------------------------------------------------

    # DISPLAY PROCESS PERFORMANCE

    # --------------------------------------------------



    def display_results(self, performance):



        for item in self.result_tree.get_children():

            self.result_tree.delete(item)



        process_table = performance["process_table"]



        for _, row in process_table.iterrows():



            self.result_tree.insert(

                "",

                "end",

                values=(

                    row["Process ID"],

                    int(row["Completion Time"]),

                    int(row["Waiting Time"]),

                    int(row["Turnaround Time"])

                )

            )



        self.metric_labels["waiting"].configure(

            text=f'{performance["average_waiting_time"]:.2f}'

        )



        self.metric_labels["turnaround"].configure(

            text=f'{performance["average_turnaround_time"]:.2f}'

        )



        self.metric_labels["utilization"].configure(

            text=f'{performance["cpu_utilization"]:.2f}%'

        )



        self.metric_labels["throughput"].configure(

            text=f'{performance["throughput"]:.4f}'

        )



    # --------------------------------------------------

    # DISPLAY GANTT CHART INSIDE TKINTER

    # --------------------------------------------------



    def display_gantt_chart(self, gantt, algorithm):



        # Remove previous chart

        self.clear_chart()



        # ADJUSTMENT 1:

        # Hide placeholder before displaying the new chart

        self.chart_placeholder.pack_forget()



        # Generate Matplotlib chart

        fig, ax = create_gantt_chart(

            gantt,

            f"{algorithm} Scheduling Gantt Chart"

        )



        fig.set_size_inches(11, 2.7)

        fig.tight_layout()



        # Embed chart inside Tkinter

        self.chart_canvas = FigureCanvasTkAgg(

            fig,

            master=self.chart_holder

        )



        self.chart_canvas.draw()



        self.chart_canvas.get_tk_widget().pack(

            fill="both",

            expand=True

        )



        self.current_figure = fig



    # --------------------------------------------------

    # CLEAR GANTT CHART

    # --------------------------------------------------



    def clear_chart(self):



        if self.chart_canvas is not None:



            self.chart_canvas.get_tk_widget().destroy()



            self.chart_canvas = None



        if self.current_figure is not None:



            plt.close(self.current_figure)



            self.current_figure = None



        if not self.chart_placeholder.winfo_exists():

            return



        self.chart_placeholder.pack_forget()



        self.chart_placeholder.pack(expand=True)



    # --------------------------------------------------

    # RESET PERFORMANCE RESULTS

    # --------------------------------------------------



    def reset_results(self, update_status=True):



        for item in self.result_tree.get_children():

            self.result_tree.delete(item)



        for label in self.metric_labels.values():

            label.configure(text="--")



        self.clear_chart()



        if update_status:



            self.status_var.set(

                "Simulation results have been reset."

            )





# ------------------------------------------------------

# APPLICATION ENTRY FOR DIRECT DASHBOARD TESTING

# ------------------------------------------------------



def main():



    root = tk.Tk()



    app = CPUSchedulerDashboard(root)



    root.mainloop()





if __name__ == "__main__":



    main()
