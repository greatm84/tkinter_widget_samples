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

# TODO filter

class Filter:
    tag = ""
    findOrs = []  # find or filter
    findAnds = []  # find and filter
    removeOrs = []  # remove or filter
    removeAnds = []  # remove and filter

    def __int__(self, tag, find_ors=None, find_ands=None, remove_ors=None, remove_ands=None):
        if remove_ands is None:
            remove_ands = []
        if remove_ors is None:
            remove_ors = []
        if find_ands is None:
            find_ands = []
        if find_ors is None:
            find_ors = []
        self.tag = tag
        self.findOrs = find_ors
        self.findAnds = find_ands
        self.removeOrs = remove_ors
        self.removeAnds = remove_ands


# filter_pairs = [
#     Filter(tag="GetSampleCodeActivityListTask", find_ors=['TRIGGERED', 'SUCCESS +', 'ERROR']),
#     Filter(tag="")
# ]


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
    for file_line in f:
        log_parser(file_line)
        i = i + 1
