app_log_path = './temp/applog.txt'

watch_task_list = [
    ['GetSampleCodeActivityListTask', ['TRIGGERED', 'SUCCESS +', 'ERROR']],
    ['GetGameItemListTask', ['TRIGGERED', 'SUCCESS +', 'ERROR']]
]

# first tag, second pair
watch_tag_and_pairs = [
    ['connection', ['connection: start CloudGamePlayer', 'connection: disconnectClient']],
    ['AnboxWebStreamViewModel', ['onResume', 'onPause']]
]


def log_parser(line: str):
    for watch_task in watch_task_list:
        if watch_task[0] in line:
            for status in watch_task[1]:
                if status in line:
                    print(watch_task[0] + " : " + status)
                    break

    for watch_pair in watch_tag_and_pairs:
        if watch_pair[1][0] in line:
            print(watch_pair[0] + " begin")
        elif watch_pair[1][1] in line:
            print(watch_pair[0] + " end")


with open(app_log_path, 'r', encoding="UTF-8") as f:
    i = 0
    for line in f:
        log_parser(line)
        i = i + 1
