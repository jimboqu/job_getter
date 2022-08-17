import random

class Job:

    job_list = []

    def __init__(self):
        self.job_list = self.import_jobs()

    def import_jobs(self):
        with open("list.txt") as data:
            self.jobs = data.readlines()
            for job in self.jobs:
                job.strip("\n")
                Job.job_list.append(job)
            job_list = [job.strip() for job in Job.job_list]
            random.shuffle(Job.job_list)
            return Job.job_list

    def add_shuffle(self, new_job):
        self.job_list.append(new_job)
        print(self.job_list)
        #reshuffle the job list with the new jobs.

    def add_job(self, job):
        with open("list.txt", mode="a") as data:
            data.write(f"\n{job}")

    def replace_job():
        Job.job_list.pop(0)
        print (Job.job_list[0])
        return Job.job_list[0]
        #remove the first job in the list. print new job.





