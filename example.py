from scheduler import Task
from scheduler import Scheduler
from scheduler import Metric
import json

if __name__ == '__main__':
    json_file = open("tasks.json")
    tasks_loaded = json.load(json_file)
    metric_map = {}
    tasks = []
    for t in tasks_loaded:
        metric = t['metric']
        if not metric_map.get(metric['id']):
            metric_map[metric['id']] = Metric(metric['id'], metric['duration'], metric['conflicts'])
        tasks.append(Task(t['id'], t['src'], t['dst'], metric['id'], t['period'], t['priority']))

    scheduler3 = Scheduler(4, metric_map.values())
    scheduler3.add_tasks(tasks)
    print("Schedule for loaded tasks")
    scheduler3.print_schedule()
