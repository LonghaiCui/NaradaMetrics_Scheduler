import json


if __name__ == '__main__':
    obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
    e_json = json.dumps(obj)

    print "%s"% obj
    print "%s"% e_json

    # i=5
    # print i
    # i=i+1
    # print i
    # s='''This is a multi-line string.
    # This is the second line.
    #      kjhkjhjkh'''
    # print s
    # #experresson
    # length = 5
    # breadth = 2
    # area = length * breadth
    # print 'Area is', area
    # print 'Perimeter is', 2 * (length + breadth)
    #
    # #!/usr/bin/python
    # # Filename: if.py
    #
    # number = 23
    #
    #
    # while(1):
    #     guess = int(raw_input('Enter an integer : '))
    #     if guess==number:
    #         print 'Congratulations, you guessed it.' # New block starts here
    #         print "(but you do not win any prizes!)" # New block ends here
    #         break;
    #     elif guess < number:
    #         print 'No, it is a little higher than that' # Another block
    #         # You can do whatever you want in a block ...
    #     else:
    #         print 'No, it is a little lower than that'
    #         # you must have guess > number to reach here
    #
    # print 'Done'
    # # This last statement is always executed, after the if statement is executed
    # for i in range(1,5):
    #     print i
    # else:
    #     print 'The for loop is over'

    # def sayHello():
    #     print "hello"
    # sayHello();

    # def printMax(a, b):
    #     if a > b:
    #         print a, 'is maximum'
    #     else:
    #         print b, 'is maximum'
    #
    # printMax(3, 4) # directly give literal values
    #
    # x = 5
    # y = 7
    # printMax(x,y);
    #
    # def func(x):
    #     print 'x is', x
    #     x = 2
    #     print 'Changed local x to', x
    #
    # x = 50
    # func(x)
    # print 'x is still', x

    #!/usr/bin/python
# Filename: func_global.py
#     x = 50
#     def func():
#         global x
#
#         print 'x is', x
#         x = 2
#         print 'Changed local x to', x
#
#
#     func()
#     print 'Value of x is', x

    #!/usr/bin/python
# Filename: func_default.py

    # def say(message, times = 1):
    #     print message * times
    #
    # say('Hello')
    # say('World', 5)

    #!/usr/bin/python
# Filename: func_key.py

    # def func(a, b=5, c=10):
    #     print 'a is', a, 'and b is', b, 'and c is', c
    #
    # func(3, 7)
    # func(25, c=24)
    # func(c=50, a=100)

    # def maximum(x, y):
    #     if x > y:
    #         return x
    #     else:
    #         return y
    #
    # print maximum(2, 3)


    #!/usr/bin/python
# Filename: func_doc.py

    # def printMax(x, y):
    #     '''Prints the maximum of two numbers.
    #
    #     The two values must be integers.'''
    #     x = int(x) # convert to integers, if possible
    #     y = int(y)
    #
    #     if x > y:
    #         print x, 'is maximum'
    #     else:
    #         print y, 'is maximum'
    #
    # printMax(3, 5)
    # print printMax.__doc__

    #!/usr/bin/python

    #
    # import sys
    #
    # print 'The command line arguments are:'
    # for i in sys.argv:
    #     print i
    #
    # print 'The PYTHONPATH is', sys.path, '\n'

# if __name__ == '__main__':
#     print 'This program is being run by itself'
# else:
#     print 'I am being imported from another module'

    # shoplist = ['apple','mango','carrot','banana']
    # print "I have", len(shoplist),'items to purchase'
    # print 'These items are:',
    # for item in shoplist:
    #     print item,
    # print '\nI also have to buy rice'
    # shoplist.append('rice')
    # print'My shopping list is now',shoplist
    # print'I will sort my list now'
    # shoplist.sort()
    # print 'Sorted shopping list is',shoplist
    #
    # print 'The first item I will buy is', shoplist[0]
    #
    # olditem=shoplist[0]
    # del shoplist[0]
    # print 'I bought the',olditem
    # print 'My shopping list is now',shoplist



    # ab = {       'Swaroop'   : 'swaroopch@byteofpython.info',
    #              'Larry'     : 'larry@wall.org',
    #              'Matsumoto' : 'matz@ruby-lang.org',
    #              'Spammer'   : 'spammer@hotmail.com',
    #              list        : [1,2,3],
    #              1           : [1,2,3,4],
    #              2           : [2,3],
    #              3           : ['a'','b'']
    #      }
    # print "Swaroop's address is", ab['Swaroop']
    #
    # ab['Guido']='guido@python.org'
    #
    # del ab['Spammer']
    # print '\n There are %d contacts in the address book\n'%len(ab)
    #
    # for name, address in ab.items():
    #     print 'Contact %s at %s' %(name,address)
    #
    # if 'Guido' in ab:
    #     print "\nGuido's address is %s " %(ab['Guido'])
    # ab[1].append(5)
    #
    #
    # print ab[1],len(ab[1])
    # ab[1].remove(3)
    # print ab[1],len(ab[1])
    #
    # z=[1,2]
    # for i in z:
    #     if i in ab.keys():
    #         print i,ab[i]
    #
    #
    #
    # print ab.has_key(1)
    #
    # print z[1],ab[1]
    # print "haha"
    #
    #
    #
    #
    #
    # print z[1],ab[1]
    # #print len(ab)
    #
    #
    #
    # print "come"
    # x=10
    # if ab.has_key(x):
    #     print ab[x],len(ab[x])
    # print "come "
    # ab[x]=[]
    # ab[x].append(x)
    # ab[x].append(100)
    #
    #
    #
    # print "go"
    # if ab.has_key(x):
    #     print ab[x]
    #     print len(ab[x])
    #
    #
    #
    # print "go"
    #
    # if ab.has_key(x):
    #     print ab[x]
    #     #print len(ab[x])
    #
    # ab[1].append(10000)
    # print ab[1]
    #
    # new = 1
    # if ab.has_key(new):
    #     ab[new].append(new)
    # else:
    #     ab[new]=[]
    #     ab[new].append(new)
    #
    # print ab[new]

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

        task_5 = Task(55, "MPA2", "MPA1", 2, 60, 0)
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

        scheduler.add_new_task(task_5)
        scheduler.print_schedule()
        scheduler.print_table()

    def test_schedule2(self):
        metric_1 = Metric(1, 60, [1, 2, 4, 5, 6, 9, 47, 48, 49, 50])
        metric_2 = Metric(2, 60, [1, 2, 4, 5, 6, 9, 47, 48, 49, 50])
        metrics = [metric_1, metric_2]

        task_1 = Task(1, u'200.0.0.1', u'200.0.0.2', 1, 1800, 0)
        task_2 = Task(2, u'200.0.0.1', u'200.0.0.2', 2, 3600, 0)
        task_3 = Task(3, u'200.0.0.2', u'200.0.0.1', 1, 2400, 0)
        task_4 = Task(4, u'200.0.0.2', u'200.0.0.1', 2, 1440, 0)
        task_5 = Task(5, u'200.0.0.2', u'200.0.0.1', 2, 3600, 0)

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
        scheduler.add_new_task(task_5)
        scheduler.print_schedule()
        #scheduler.print_table()

        scheduler.delete_task(task_2)
        scheduler.print_schedule()
        scheduler.delete_task(task_3)
        scheduler.print_schedule()
        #scheduler.print_table()

        scheduler.add_new_task(task_3)
        scheduler.print_schedule()

    #TODO How to verify the exception happened
    # def test_schedule_2_conflicting_tasks_one_period_cycle(self):
    #     metric_1 = Metric(1, 60, [1, 2, 4, 5, 6, 9, 47, 48, 49, 50])
    #     metric_2 = Metric(2, 60, [1, 2, 4, 5, 6, 9, 47, 48, 49, 50])
    #     metrics = [metric_1, metric_2]
    #     task_1 = Task(1, u'200.0.0.1', u'200.0.0.2', 1, 60, 1)
    #     task_2 = Task(2, u'200.0.0.1', u'200.0.0.2', 2, 60, 1)
    #     tasks = [task_1, task_2]
    #     scheduler = Scheduler(4, metrics)
    #     scheduler.add_tasks(tasks)
    #     scheduler.print_schedule()
    #     self.assertRaises(BaseException)
    #     #Exception("Some of the tasks can not be scheduled completely")
    #TODO Priority not correct
    def test_basic_schedule(self):
        #conflicts = {11: [11, 22], 22: [11, 22, 33], 33: [22, 33], 44: [], 55: [22], 66: []}
        metric_1 = Metric(11, 10, [11, 22])
        metric_2 = Metric(22, 10, [11, 22, 33])
        metric_3 = Metric(33, 5, [22, 33])
        metric_4 = Metric(44, 5, [])
        metrics = [metric_1, metric_2, metric_3, metric_4]
        #id, src, dst, metric_id, period, priority
        scheduler = Scheduler(4, metrics)
        task_1 = Task(1, u'200.0.0.1', u'200.0.0.2', 11, 60, 0)
        task_2 = Task(2, u'200.0.0.1', u'200.0.0.2', 22, 40, 1)
        task_3 = Task(3, u'200.0.0.1', u'200.0.0.2', 33, 20, 0)
        task_4 = Task(4, u'200.0.0.1', u'200.0.0.2', 44, 30, 1)
        tasks = [task_1, task_2, task_3, task_4]
        #table.print_table()
        scheduler.add_tasks(tasks)
        scheduler.print_schedule()
        #scheduler.schedules.
        for i in range(len(scheduler.schedules)):
            print(scheduler.schedules[i].metric_id, scheduler.schedules[i].src, scheduler.schedules[i].dst,
                  scheduler.schedules[i].start,
                  scheduler.schedules[i].duration, scheduler.schedules[i].period, scheduler.schedules[i].priority)
        self.assertEqual(11, scheduler.schedules[0].metric_id)
        self.assertEqual(0, scheduler.schedules[0].start)
        self.assertEqual(11, scheduler.schedules[1].metric_id)
        self.assertEqual(60, scheduler.schedules[1].start)
        self.assertEqual(22, scheduler.schedules[2].metric_id)
        self.assertEqual(10, scheduler.schedules[2].start)
        self.assertEqual(22, scheduler.schedules[3].metric_id)
        self.assertEqual(45, scheduler.schedules[3].start)
        self.assertEqual(22, scheduler.schedules[4].metric_id)
        self.assertEqual(85, scheduler.schedules[4].start)
        self.assertEqual(33, scheduler.schedules[5].metric_id)
        self.assertEqual(0, scheduler.schedules[5].start)
        self.assertEqual(33, scheduler.schedules[6].metric_id)
        self.assertEqual(20, scheduler.schedules[6].start)
        self.assertEqual(33, scheduler.schedules[7].metric_id)
        self.assertEqual(40, scheduler.schedules[7].start)
        self.assertEqual(33, scheduler.schedules[8].metric_id)
        self.assertEqual(60, scheduler.schedules[8].start)
        self.assertEqual(33, scheduler.schedules[9].metric_id)
        self.assertEqual(80, scheduler.schedules[9].start)
        self.assertEqual(33, scheduler.schedules[10].metric_id)
        self.assertEqual(100, scheduler.schedules[10].start)
        self.assertEqual(44, scheduler.schedules[11].metric_id)
        self.assertEqual(0, scheduler.schedules[11].start)
        self.assertEqual(44, scheduler.schedules[12].metric_id)
        self.assertEqual(30, scheduler.schedules[12].start)
        self.assertEqual(44, scheduler.schedules[13].metric_id)
        self.assertEqual(60, scheduler.schedules[13].start)
        self.assertEqual(44, scheduler.schedules[14].metric_id)
        self.assertEqual(90, scheduler.schedules[14].start)
        #self.assertEqual(11,scheduler.schedules[0].metric_id)




            # # #TODO Priority not correct
    # def test_basic_schedule(self):
    #     #conflicts = {11: [11, 22], 22: [11, 22, 33], 33: [22, 33], 44: [], 55: [22], 66: []}
    #     metric_1 = Metric(11, 10, [11, 22])
    #     metric_2 = Metric(22, 10, [11, 22, 33])
    #     metric_3 = Metric(33, 5, [22, 33])
    #     metric_4 = Metric(44, 5, [])
    #     metrics = [metric_1, metric_2, metric_3, metric_4]
    #     #id, src, dst, metric_id, period, priority
    #     scheduler = Scheduler(4, metrics)
    #     task_1 = Task(1, u'200.0.0.1', u'200.0.0.2', 11, 60, 1)
    #     task_2 = Task(2, u'200.0.0.1', u'200.0.0.2', 22, 40, 1)
    #     task_3 = Task(3, u'200.0.0.1', u'200.0.0.2', 33, 20, 10)
    #     task_4 = Task(4, u'200.0.0.1', u'200.0.0.2', 44, 30, 1)
    #     tasks = [task_1, task_2, task_3, task_4]
    #
    #     scheduler.add_tasks(tasks)
    #     scheduler.print_schedule()
    #     for i in range(len(scheduler.schedules)):
    #         print(scheduler.schedules[i].metric_id, scheduler.schedules[i].src, scheduler.schedules[i].dst,
    #               scheduler.schedules[i].start,
    #               scheduler.schedules[i].duration, scheduler.schedules[i].period, scheduler.schedules[i].priority)
    #     self.assertEqual(11, scheduler.schedules[0].metric_id)
    #     self.assertEqual(0, scheduler.schedules[0].start)
    #     self.assertEqual(11, scheduler.schedules[1].metric_id)
    #     self.assertEqual(60, scheduler.schedules[1].start)
    #     self.assertEqual(22, scheduler.schedules[2].metric_id)
    #     self.assertEqual(10, scheduler.schedules[2].start)
    #     self.assertEqual(22, scheduler.schedules[3].metric_id)
    #     self.assertEqual(45, scheduler.schedules[3].start)
    #     self.assertEqual(22, scheduler.schedules[4].metric_id)
    #     self.assertEqual(85, scheduler.schedules[4].start)
    #     self.assertEqual(33, scheduler.schedules[5].metric_id)
    #     self.assertEqual(0, scheduler.schedules[5].start)
    #     self.assertEqual(33, scheduler.schedules[6].metric_id)
    #     self.assertEqual(20, scheduler.schedules[6].start)
    #     self.assertEqual(33, scheduler.schedules[7].metric_id)
    #     self.assertEqual(40, scheduler.schedules[7].start)
    #     self.assertEqual(33, scheduler.schedules[8].metric_id)
    #     self.assertEqual(60, scheduler.schedules[8].start)
    #     self.assertEqual(33, scheduler.schedules[9].metric_id)
    #     self.assertEqual(80, scheduler.schedules[9].start)
    #     self.assertEqual(33, scheduler.schedules[10].metric_id)
    #     self.assertEqual(100, scheduler.schedules[10].start)
    #     self.assertEqual(44, scheduler.schedules[11].metric_id)
    #     self.assertEqual(0, scheduler.schedules[11].start)
    #     self.assertEqual(44, scheduler.schedules[12].metric_id)
    #     self.assertEqual(30, scheduler.schedules[12].start)
    #     self.assertEqual(44, scheduler.schedules[13].metric_id)
    #     self.assertEqual(60, scheduler.schedules[13].start)
    #     self.assertEqual(44, scheduler.schedules[14].metric_id)
    #     self.assertEqual(90, scheduler.schedules[14].start)
    #     self.assertEqual(11,scheduler.schedules[0].metric_id)