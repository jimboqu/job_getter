from tkinter import *
from Job import Job

class JobInterface:

    def __init__(self, job: Job):
        self.job = job
        self.window = Tk()
        self.title = "Job Picker"
        self.window.config(pady=20, padx=20)

        self.mainTitle = Label(text="Job Picker", font=("Helvetica", 20, "bold"))
        self.mainTitle.grid(column=0, row=0, columnspan=2)

        #Enter job label and input box
        self.input_title = Label(text="Enter Job", font=(("Helvetica", 10, "bold")))
        self.input_title.grid(column=0, row=1)
        self.job_input = Entry(width=20, font=("Helvetica", 10))
        self.job_input.grid(column=0, row=2)

        #Submit button for job
        self.submit_button = Button(text="Submit", command=self.attempt)
        self.submit_button.grid(column=0, row=3)

        #This job box and title

        self.input_title = Label(text=f"Next Job is ", font=(("Helvetica", 10, "bold")))
        self.input_title.grid(column=1, row=1)
        self.next_job = Canvas(width=400, height=265, bg="white")
        self.display_job(self)
        self.next_job.grid(column=1, row=2)

        #This job done button
        self.job_done = Button(text="Job Done", command=self.done_job)
        self.job_done.grid(column=1, row=3)


        self.window, mainloop()

    def attempt(self):
        job = self.job_input.get()
        self.job.add_job(job)
        self.job.add_shuffle(job)

    def done_job(self):
        new_job = Job.replace_job()
        self.display_job(new_job)

    def display_job(self, job):
        # clear area
        self.next_job.delete('all')
        self.next_job.create_text(90, 130, text=f"{Job.job_list[0]}", fill="black", font=('Helvetica 20 bold'))