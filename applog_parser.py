app_log_path = './temp/applog.txt'

watch_task_list = [
    ['GetSampleCodeActivityListTask', ['TRIGGERED', 'SUCCESS +', 'ERROR']],
    ['GetGameItemListTask', ['TRIGGERED', 'SUCCESS +', 'ERROR']]
]

watch_things = [

]


def log_parser(line: str):
    for watch_task in watch_task_list:
        if watch_task[0] in line:
            for status in watch_task[1]:
                if status in line:
                    print(watch_task[0] + " : " + status)
                    return


with open(app_log_path, 'r', encoding="UTF-8") as f:
    i = 0
    for line in f:
        log_parser(line)
        i = i + 1
