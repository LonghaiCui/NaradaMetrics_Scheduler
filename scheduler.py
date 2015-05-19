#!/usr/local/bin/python
# Heuristic Bin Algorithm for Narada Metrics scheduler
# Author: Cui Longhai


class Metric:
    def __init__(self, id, duration, conflicts):
        self.id = id
        self.duration = duration
        self.conflicts = conflicts


class Task:
    """This class has the basic information of a measurement task"""
    def __init__(self, id, src, dst, metric_id, period, priority):
        self.id = id
        self.src = src
        self.dst = dst
        self.metric_id = metric_id
        self.period = period
        self.priority = priority


class ScheduleLine:
    """This class has all the information of a measurement job along"""
    def __init__(self, task_id, metric_id, src, dst, start, duration, period, priority):
        self.task_id = task_id
        self.metric_id = metric_id
        self.src = src
        self.dst = dst
        self.start = start
        self.duration = duration
        self.period = period
        self.priority = priority

    def __repr__(self):
        return 'task_id: %d metric_id:%d from %s to %s start : %d\n duration:%d period: %d,priority:%d' % (
            self.task_id, self.metric_id, self.src, self.dst, self.start, self.duration, self.period, self.priority)


#Design pattern - Decorator pattern
class Bin:
    """This class stores the basic information of the task
     along with other essential attributes to for the EDF algorithm"""
    def __init__(self, task, metric):
        self.task_id = task.id
        #self.metric_id = task.metric_id
        self.src = task.src
        self.dst = task.dst
        self.period = task.period
        self.metric = metric
        self.priority = task.priority
        self.jobs = []
        self.pointer = 0
        self.scheduled = False


class Job:
    """This class stores the basic information of the job"""
    def __init__(self, bin, deadline, start_time=None):
        self.task_id = bin.task_id
        self.duration = bin.metric.duration
        self.deadline = deadline
        self.start_time = start_time
        if self.start_time is None:
            self.end_time = None
        else:
            self.end_time = start_time + self.duration

    def __str__(self):
        return '[task_id:%d start_time:%d  end_time:%d]' % (
            self.task_id, self.start_time, self.end_time)


class Scheduler:
    def __init__(self, mla, metrics, schedules=None, percent=0.222):
        """Initialize the scheduler based on saved status"""
        self.mla = mla
        self.metric_map = {}
        for metric in metrics:
            self.metric_map[metric.id] = metric
        self.hyper = 0
        #This attribute indicates how many percentage of the time table is occupied
        self.percent = percent

        if schedules is None:
            self.schedules = []
            self.tasks = []
            self.time_table = {}
            print "There is no already scheduled tasks"
        else:
            print "Initializing the tasks in the scheduler"
            self.schedules = schedules
            self.tasks = []
            self.time_table = {}
            current_task_ids = []
            for schedule in schedules:
                if schedule.task_id not in current_task_ids:
                    job_id = 0
                    current_task_ids.append(schedule.task_id)
                    task = Task(schedule.task_id, schedule.src, schedule.dst, schedule.metric_id, schedule.period,
                                schedule.priority)
                    bin = Bin(task, self.metric_map[task.metric_id])
                    self.tasks.append(bin)
                    #print bin.task.id, bin.task.priority
                deadline = bin.metric.duration * (job_id + 1)
                job_id += 1
                job = Job(bin, deadline, start_time=schedule.start)
                job.start_time = schedule.start
                bin.jobs.append(job)
                bin.pointer += 1
            self._update_hyper_period()
            for i in range(len(self.tasks)):
                num_of_jobs = len(self.tasks[i].jobs)
                for j in range(num_of_jobs):
                    current_time = self.tasks[i].jobs[j].start_time
                    end_time = self.tasks[i].jobs[j].end_time
                    while current_time < end_time:
                        if self.time_table.has_key(current_time):
                            self.time_table[current_time].append(self.tasks[i].task_id)
                        else:
                            self.time_table[current_time] = []
                            self.time_table[current_time].append(self.tasks[i].task_id)
                        current_time += 1

    @staticmethod
    def _gcd(first, second):
        """calculate the greatest common divisor"""
        if first < second:
            first, second = second, first
        while second != 0:
            first, second = second, first % second
        return first

    @staticmethod
    def _lcm(first, second):
        """calculate the least common multiple"""
        gcd_num = Scheduler._gcd(first, second)
        return first * second / gcd_num

    def _update_hyper_period(self):
        """calculate the hyper period for the first tasks input"""
        periods = []
        for i in range(len(self.tasks)):
            periods.append(self.tasks[i].period)

        hyper = periods[0]
        for i in range(len(periods) - 1):
            hyper = Scheduler._lcm(hyper, periods[i + 1])
        self.hyper = hyper

        print("HYPER IS %ds" % (self.hyper))

    def _is_full(self):
        """Check if the table is occupied more than the defined percentage"""
        count = 0
        for current_time in range(self.hyper):
            if self.time_table.has_key(current_time):
                count += len(self.time_table[current_time])

        if count >= self.hyper * self.mla * self.percent:
            return True
        else:
            return False

    def print_table(self):
        """Print the table occupancy of each time stamps from 0 to hyper period"""
        print "Printing the table now"
        print "The hyper is ", self.hyper
        for i in range(self.hyper):
            if self.time_table.has_key(i):
                print(i + 1, len(self.time_table[i]), self.time_table[i])

    def _calculate_deadlines(self):
        #For each task in the pending job queue
        for i in range(len(self.tasks)):
            #Calculate the number of the jobs that need to be scheduled
            num_of_jobs = self.hyper / self.tasks[i].period
            #For each of the job in the current task
            for j in range(num_of_jobs):
                #Initial the deadline for the each job
                deadline = self.tasks[i].period * (j + 1)
                job = Job(self.tasks[i], deadline)
                self.tasks[i].jobs.append(job)

    def _get_task_by_id(self, task_id):
        for task in self.tasks:
            if task_id == task.task_id:
                return task

    def _no_conflict(self, task_id, scheduled_tasks):
        """check if current task has conflict with already scheduled tasks"""
        task = self._get_task_by_id(task_id)
        for scheduled_task_id in scheduled_tasks:
            scheduled_task = self._get_task_by_id(scheduled_task_id)
            if (task.src == scheduled_task.src or task.dst == scheduled_task.dst or
                        task.src == scheduled_task.dst or task.dst == scheduled_task.src):
                if task.metric.id in scheduled_task.metric.conflicts or scheduled_task.metric.id in task.metric.conflicts:
                    return False
        return True

    def mla_ok(self, scheduled_tasks, task_id):
        count = 0
        task = self._get_task_by_id(task_id)
        src = task.src
        dst = task.dst
        print src, dst
        for scheduled_task_id in scheduled_tasks:
            scheduled_task = self._get_task_by_id(scheduled_task_id)
            cur_src = scheduled_task.src
            cur_dst = scheduled_task.dst
            if (src == cur_src and dst == cur_dst) or (src == cur_dst and dst == cur_src):
                count += 1
        if count < self.mla:
            return True

    def add_tasks(self, tasks):
        """Add a batch of tasks to the schedule"""
        for task in tasks:
            bin = Bin(task, self.metric_map[task.metric_id])
            self.tasks.append(bin)
        self._update_schedule()

    def add_new_task(self, task):
        """Add a signal onTime measurement task to the schedule"""
        if self._is_full() is True:
            print("Can not add more tasks!")
            return False
        bin = Bin(task, self.metric_map[task.metric_id])
        self.tasks.append(bin)
        n = self.hyper / bin.period
        for j in range(n):
            deadline = bin.period * (j + 1)
            job = Job(bin, deadline)
            bin.jobs.append(job)
        for k in range(n):
            for i in range(bin.period * k, bin.period * (k + 1)):
                flag = 1
                for j in range(bin.metric.duration):
                    print("i + j", i + j)
                    if self.time_table.has_key(i + j) and len(
                            self.time_table[i + j]) < self.mla and self._no_conflict(
                            bin.task_id, self.time_table[i + j]) and (
                        i + j < self.hyper - 1 and i + bin.duration <= bin.period * (k + 1)):
                        pass
                    else:
                        flag = 0
                        break

                if flag == 1:
                    bin.jobs[k].start_time = i
                    bin.jobs[k].end_time = i + bin.duration
                    break

        for i in range(n):
            task_id = bin.task_id
            metric_id = bin.metric.id
            src = bin.src
            dst = bin.dst
            start = bin.jobs[i].start_time
            duration = bin.metric.duration
            period = bin.period
            priority = bin.priority
            schedule_line = ScheduleLine(task_id, metric_id, src, dst, start, duration, period, priority)
            self.schedules.append(schedule_line)

        #Update the table
        for i in range(len(self.tasks)):
            num_of_jobs = len(self.tasks[i].jobs)
            for j in range(num_of_jobs):
                current_time = self.tasks[i].jobs[j].start_time
                end_time = self.tasks[i].jobs[j].end_time
                while current_time < end_time:
                    if self.time_table.has_key(current_time):
                        self.time_table[current_time].append(self.tasks[i].task_id)
                    else:
                        self.time_table[current_time] = []
                        self.time_table[current_time].append(self.tasks[i].task_id)
                    current_time += 1

        return True

    def delete_task(self, task):
        """Delete the task from the task list and update the scheduler"""
        for i in range(len(self.tasks)):
            if self.tasks[i].task_id == task.id:
                num_of_jobs = len(self.tasks[i].jobs)
                print("num_of_jobs is  ", num_of_jobs)

        for i in range(len(self.schedules)):
            if self.schedules[i].task_id == task.id:
                start = i
                end = i + num_of_jobs
                del self.schedules[start:end]
                break

    def _update_schedule(self):
        """EDf algorithm to schedule the tasks for the first time"""
        #Initialize the hyper period
        self._update_hyper_period()
        #Initialize pending job queue
        pending_job_queue = []
        #Initialize released_times
        released_times = {}
        #Initialize the scheduled tasks
        scheduled_tasks = []
        #Initialize release_time_list with the ordered list of all release times in a hyper period
        release_time_list = []

        for i in range(len(self.tasks)):
            temp = 0
            while temp <= self.hyper:
                release_time_list.append(temp)
                temp += self.tasks[i].period
        release_time_list = list(set(release_time_list))
        release_time_list.sort()
        #Cacluate the deadlines for all jobs
        self._calculate_deadlines()

        #Add all newly released jobs at time to pending job queue in EDF order
        for x in release_time_list:
            pending_queue = []
            for i in range(len(self.tasks)):
                if x % self.tasks[i].period == 0:
                    pending_queue.append(self.tasks[i].task_id)
            released_times[x] = pending_queue

        #Beginning of the main algorithm
        current_time = 0
        while current_time < self.hyper:
            #Get the next scheduling time to pending-job-queue from rt-list and ft list
            if len(release_time_list) > 0:
                current_time = release_time_list.pop(0)
            #Repeat until hyper period ends
            if current_time == self.hyper:
                break
                #Initialize the temporary scheduled tasks in the current moment
            temp_scheduled_tasks = []

            #Add all newly released jobs at time to pending job queue in EDF order
            for task_id in scheduled_tasks:
                for i in range(len(self.tasks)):
                    if self.tasks[i].task_id == task_id:
                        if self.tasks[i].jobs[self.tasks[i].pointer - 1].end_time <= current_time:
                            temp_scheduled_tasks.append(task_id)
                            break
            for x in temp_scheduled_tasks:
                scheduled_tasks.remove(x)
            if released_times.has_key(current_time):
                pending_job_queue += released_times[current_time]
            temp_pjq = []
            temp_pjq_in_ordered_priority = []

            pending_job_queue_tasks = []
            for task_id in pending_job_queue:
                current_task = self._get_task_by_id(task_id)
                pending_job_queue_tasks.append(current_task)
            sorted(pending_job_queue_tasks, key=lambda task: task.priority)
            for task in pending_job_queue_tasks:
                temp_pjq_in_ordered_priority.append(task.task_id)
                #print task.task_id, task.priority
            pending_job_queue = temp_pjq_in_ordered_priority

            #For each job in pending job queue in EDF order
            for task_id in pending_job_queue:
                #If the current job does not conflict with any of already scheduled jobs and does not violate MLA
                if self._no_conflict(task_id, scheduled_tasks) and self.mla_ok(scheduled_tasks,
                                                                               task_id):
                    #Find the location of the job that for the task_id
                    num_of_jobs = 0
                    for i in range(len(self.tasks)):
                        if self.tasks[i].task_id == task_id:
                            num_of_jobs = i
                            break
                    pointer = self.tasks[num_of_jobs].pointer

                    #If current job meets the deadline
                    if current_time + self.tasks[num_of_jobs].metric.duration <= self.tasks[num_of_jobs].jobs[
                        pointer].deadline:
                        #Schedule this job and update start_time and end_time
                        self.tasks[num_of_jobs].jobs[pointer].start_time = current_time
                        self.tasks[num_of_jobs].jobs[pointer].end_time = current_time + self.tasks[
                            num_of_jobs].metric.duration
                        end_time = self.tasks[num_of_jobs].jobs[pointer].end_time
                        self.tasks[num_of_jobs].pointer += 1

                        #Update the scheduled tasks
                        scheduled_tasks.append(task_id)
                        #Add the task_id in the temporary pending_job_queue for the current moment
                        temp_pjq.append(task_id)
                        #Update released time
                        release_time_list.append(end_time)
                        release_time_list = list(set(release_time_list))
                        release_time_list.sort()
                    else:
                        temp_pjq.append(task_id)
                        self.tasks[num_of_jobs].pointer += 1
                        #Remove the scheduled jobs from pending_job_queue
            for x in temp_pjq:
                pending_job_queue.remove(x)

        #Check if any of the job start time is none, if so raise an exception
        for i in range(len(self.tasks)):
            num_of_jobs = len(self.tasks[i].jobs)
            for j in range(num_of_jobs):
                if self.tasks[i].jobs[j].start_time is None:
                    raise Exception("Some of the tasks can not be scheduled completely")

        #Format all the jobs to required objects schedule_line
        for i in range(len(self.tasks)):
            num_of_jobs = len(self.tasks[i].jobs)
            for j in range(num_of_jobs):
                job = self.tasks[i].jobs[j]
                task_id = self.tasks[i].task_id
                metric_id = self.tasks[i].metric.id
                src = self.tasks[i].src
                dst = self.tasks[i].dst
                start = self.tasks[i].jobs[j].start_time
                duration = self.tasks[i].metric.duration
                period = self.tasks[i].period
                priority = self.tasks[i].priority
                schedule_line = ScheduleLine(task_id, metric_id, src, dst, start, duration, period, priority)
                self.schedules.append(schedule_line)

        #Update the table
        for i in range(len(self.tasks)):
            num_of_jobs = len(self.tasks[i].jobs)
            for j in range(num_of_jobs):
                current_time = self.tasks[i].jobs[j].start_time
                end_time = self.tasks[i].jobs[j].end_time
                while current_time < end_time:
                    if self.time_table.has_key(current_time):
                        self.time_table[current_time].append(self.tasks[i].task_id)
                    else:
                        self.time_table[current_time] = []
                        self.time_table[current_time].append(self.tasks[i].task_id)
                    current_time += 1

    def get_schedule(self):
        """Return the schedule_lines"""
        return self.schedule_lines

    def print_schedule(self):
        """print the schedule"""
        print("=====================================")
        print("t_id, src,dst,start,duration,period,priority")

        for i in range(len(self.schedules)):
            print(self.schedules[i].task_id, self.schedules[i].src, self.schedules[i].dst, self.schedules[i].start,
                  self.schedules[i].duration, self.schedules[i].period, self.schedules[i].priority)
        print("=====================================")