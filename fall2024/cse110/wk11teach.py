class Worker:
    def __init__(self, name, id, job, salary):
        self.name = name
        self.id = id
        self.job =  job
        self.salary = salary

workers = []

with open('hr_system.txt') as hr_doc:
    for line in hr_doc:
        arguments = line.split(' ')
        workers.append(Worker(arguments[0],arguments[1],arguments[2],float(arguments[3])))

for worker in workers:
    if worker.job.lower() == 'engineer':
        worker.salary+=24000
    print(f'{worker.name} (ID: {worker.id}), {worker.job} - ${worker.salary/24:.2f}')