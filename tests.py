import unittest
import random
from scheduler import Task
from scheduler import Metric
from scheduler import Scheduler


class SchedulerTest(unittest.TestCase):
    def setUp(self):
        self.metric_1 = Metric(1, 1, [1, 2, 4, 5, 6, 9, 47, 48, 49, 50])
        self.metric_2 = Metric(2, 1, [1, 2, 4, 5, 6, 9, 47, 48, 49, 50])

    def test_basic_schedule1(self):
        task_1 = Task(11, "MPA1", "MPA2", 1, 30, 0)
        task_2 = Task(22, "MPA1", "MPA2", 2, 60, 0)
        task_3 = Task(33, "MPA2", "MPA1", 1, 40, 0)
        task_4 = Task(44, "MPA2", "MPA1", 2, 24, 0)

        metrics = [self.metric_1, self.metric_2]
        scheduler = Scheduler(4, metrics)

        tasks = [task_1, task_2, task_3, task_4]

        scheduler.add_tasks(tasks)
        scheduler.print_schedule()
        scheduler.print_table()

        self.assertEqual(11, scheduler.schedules[0].task_id)
        self.assertEqual(0, scheduler.schedules[0].start)
        self.assertEqual(11, scheduler.schedules[1].task_id)
        self.assertEqual(30, scheduler.schedules[1].start)
        self.assertEqual(11, scheduler.schedules[2].task_id)
        self.assertEqual(60, scheduler.schedules[2].start)
        self.assertEqual(11, scheduler.schedules[3].task_id)
        self.assertEqual(90, scheduler.schedules[3].start)
        self.assertEqual(22, scheduler.schedules[4].task_id)
        self.assertEqual(1, scheduler.schedules[4].start)
        self.assertEqual(22, scheduler.schedules[5].task_id)
        self.assertEqual(61, scheduler.schedules[5].start)
        self.assertEqual(33, scheduler.schedules[6].task_id)
        self.assertEqual(2, scheduler.schedules[6].start)
        self.assertEqual(33, scheduler.schedules[7].task_id)
        self.assertEqual(40, scheduler.schedules[7].start)
        self.assertEqual(33, scheduler.schedules[8].task_id)
        self.assertEqual(80, scheduler.schedules[8].start)
        self.assertEqual(44, scheduler.schedules[9].task_id)
        self.assertEqual(3, scheduler.schedules[9].start)
        self.assertEqual(44, scheduler.schedules[10].task_id)
        self.assertEqual(24, scheduler.schedules[10].start)
        self.assertEqual(44, scheduler.schedules[11].task_id)
        self.assertEqual(48, scheduler.schedules[11].start)
        self.assertEqual(44, scheduler.schedules[12].task_id)
        self.assertEqual(72, scheduler.schedules[12].start)
        self.assertEqual(44, scheduler.schedules[13].task_id)
        self.assertEqual(96, scheduler.schedules[13].start)


    def test_schedule2(self):
        metric_1 = Metric(1, 60, [1, 2, 4, 5, 6, 9, 47, 48, 49, 50])
        metric_2 = Metric(2, 60, [1, 2, 4, 5, 6, 9, 47, 48, 49, 50])
        metrics = [metric_1, metric_2]

        task_1 = Task(1, u'200.0.0.1', u'200.0.0.2', 1, 1800, 0)
        task_2 = Task(2, u'200.0.0.1', u'200.0.0.2', 2, 3600, 0)
        task_3 = Task(3, u'200.0.0.2', u'200.0.0.1', 1, 2400, 0)
        task_4 = Task(4, u'200.0.0.2', u'200.0.0.1', 2, 1440, 0)

        tasks = [task_1, task_2, task_3, task_4]
        scheduler = Scheduler(4, metrics)
        scheduler.add_tasks(tasks)
        scheduler.print_schedule()

        self.assertEqual(1, scheduler.schedules[0].task_id)
        self.assertEqual(0, scheduler.schedules[0].start)
        self.assertEqual(1, scheduler.schedules[1].task_id)
        self.assertEqual(1800, scheduler.schedules[1].start)
        self.assertEqual(1, scheduler.schedules[2].task_id)
        self.assertEqual(3600, scheduler.schedules[2].start)
        self.assertEqual(1, scheduler.schedules[3].task_id)
        self.assertEqual(5400, scheduler.schedules[3].start)
        self.assertEqual(2, scheduler.schedules[4].task_id)
        self.assertEqual(60, scheduler.schedules[4].start)
        self.assertEqual(2, scheduler.schedules[5].task_id)
        self.assertEqual(3660, scheduler.schedules[5].start)
        self.assertEqual(3, scheduler.schedules[6].task_id)
        self.assertEqual(120, scheduler.schedules[6].start)
        self.assertEqual(3, scheduler.schedules[7].task_id)
        self.assertEqual(2400, scheduler.schedules[7].start)
        self.assertEqual(3, scheduler.schedules[8].task_id)
        self.assertEqual(4800, scheduler.schedules[8].start)
        self.assertEqual(4, scheduler.schedules[9].task_id)
        self.assertEqual(180, scheduler.schedules[9].start)
        self.assertEqual(4, scheduler.schedules[10].task_id)
        self.assertEqual(1440, scheduler.schedules[10].start)
        self.assertEqual(4, scheduler.schedules[11].task_id)
        self.assertEqual(2880, scheduler.schedules[11].start)
        self.assertEqual(4, scheduler.schedules[12].task_id)
        self.assertEqual(4320, scheduler.schedules[12].start)
        self.assertEqual(4, scheduler.schedules[13].task_id)
        self.assertEqual(5760, scheduler.schedules[13].start)


    def test_schedule_2_conflicting_tasks_one_period_cycle(self):
        metric_1 = Metric(1, 60, [1, 2, 4, 5, 6, 9, 47, 48, 49, 50])
        metric_2 = Metric(2, 60, [1, 2, 4, 5, 6, 9, 47, 48, 49, 50])
        metrics = [metric_1, metric_2]
        task_1 = Task(1, u'200.0.0.1', u'200.0.0.2', 1, 60, 1)
        task_2 = Task(2, u'200.0.0.1', u'200.0.0.2', 2, 60, 1)
        tasks = [task_1, task_2]
        scheduler = Scheduler(1, metrics)
        self.assertRaises(Exception, scheduler.add_tasks, tasks)


    def test_bug_201(self):
        metric_1 = Metric(1, 60, [1, 2])
        metric_2 = Metric(2, 60, [1, 2])
        metrics = [metric_1, metric_2]
        #Throuhput
        task_1 = Task(1, '71.62.82.92', '70.62.55.250', 1, 3600, 1)
        #Route change
        task_2 = Task(2, '71.62.82.92', '70.62.55.250', 2, 1800, 1)
        #Throuhput
        task_3 = Task(3, '71.62.82.92', '76.209.75.242', 1, 3600, 1)
        #Route change
        task_4 = Task(4, '70.62.55.250', '76.209.75.242', 2, 3600, 1)
        #T
        task_5 = Task(5, '70.62.55.250', '76.209.75.242', 1, 3600, 1)
        #Tmetrics[mid].conflicts
        task_6 = Task(6, '76.209.75.242', '70.62.55.250', 1, 7200, 1)
        #Route change
        task_7 = Task(7, '76.209.75.242', '70.62.55.250', 2, 1800, 1)
        tasks = [task_1, task_2, task_3, task_4, task_5, task_6, task_7]
        scheduler = Scheduler(2, metrics)
        scheduler.add_tasks(tasks)
        scheduler.print_schedule()

        flag = 1
        for i in range(len(scheduler.schedules)):
            for j in range(len(scheduler.schedules)):
                if (scheduler.schedules[i].src == scheduler.schedules[j].src or scheduler.schedules[i].src ==
                    scheduler.schedules[j].dst
                    or scheduler.schedules[i].dst == scheduler.schedules[j].src or scheduler.schedules[i].dst ==
                    scheduler.schedules[j].dst):
                    mid = scheduler.schedules[i].metric_id
                    if scheduler.schedules[j].metric_id in metrics[mid - 1].conflicts and abs(
                                    scheduler.schedules[i].start - scheduler.schedules[j].start) < 60 \
                        and abs(scheduler.schedules[i].start - scheduler.schedules[j].start) != 0:
                        flag = 0
        self.assertEqual(1, flag)









