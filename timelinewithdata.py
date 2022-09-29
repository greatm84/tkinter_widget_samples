import tkinter as tk

from ttkwidgets import TimeLine

# time line is 0 - 10

app_log_path = './temp/applog.txt'

window = tk.Tk()
menu = tk.Menu(window, tearoff=False)
menu.add_command(label="Some Action", command=lambda: print("Command Executed"))
# timeline.tag_configure("1", right_callback=lambda *args: print(args), menu=menu, foreground="green",
#                        active_background="yellow", hover_border=2, move_callback=lambda *args: print(args))

#
#
# timeline.create_marker("1", 1.0, 2.0, background="white", text="Change Color", tags=("1",), iid="1")
# timeline.create_marker("2", 2.0, 3.0, background="green", text="Change Category", foreground="white", iid="2",
#                        change_category=True)
# timeline.create_marker("3", 1.0, 2.0, text="Show Menu", tags=("1",))
# timeline.create_marker("4", 4.0, 5.0, text="Do nothing", move=False)

colors = [
    "white",
    "green",
    "red",
    "yellow",
    "blue",
    "cyan"
]

watch_task_list = [
    ['GetSampleCodeActivityListTask', ['TRIGGERED', 'SUCCESS +', 'ERROR']],
    ['GetGameItemListTask', ['TRIGGERED', 'SUCCESS +', 'ERROR']]
]

# first tag, second pair
watch_tag_and_pairs = [
    ['clientConnection', ['connection: start CloudGamePlayer', 'connection: disconnectClient']],
    ['AnboxWebStreamViewModel', ['onResume', 'onPause']]
]


def log_parser(line: str):
    for watch_task in watch_task_list:
        if watch_task[0] in line:
            for status in watch_task[1]:
                if status in line:
                    return watch_task[0], status

    for watch_pair in watch_tag_and_pairs:
        if watch_pair[1][0] in line:
            return watch_pair[0], "begin"
        elif watch_pair[1][1] in line:
            return watch_pair[0], " end"

    return None, None


categories = {}  # key : tag, value : color]
begin_store_dict = {}  # 넣는 형식 key:tag, value: time
status_list = []  # [tag, index]
pairs = []  # [tag, begin, end]

with open(app_log_path, 'r', encoding="UTF-8") as f:
    i = 0
    for file_line in f:
        tag, status = log_parser(file_line)
        if tag is not None:
            if tag not in categories:
                categories[tag] = colors[(len(categories) - 1) % (len(colors) - 1)]

            if status == "begin":
                if tag in begin_store_dict:  # 이미 하나 갖고 있다면 begin 후 begin
                    # 기존 것을 종료 해주고
                    pairs.append([tag, begin_store_dict[tag], i - 1])
                    begin_store_dict.pop(tag)
                else:
                    begin_store_dict[tag] = i
            elif status == "end":
                if tag in begin_store_dict:  # begin 이 있다면 pair로 묶음
                    pairs.append([tag, begin_store_dict[tag], i])
                    begin_store_dict.pop(tag)
                else:
                    # begin 이 없다면 처음부터 온것이므로 처음 값을 넣어줌
                    pairs.append([tag, 0, i])
            else:
                # just append to status_list
                status_list.append([tag, i])

        i = i + 1

    # loop가 끝났는데 begin만 남은 dict가 있다면 pair로 넣어줘야함 end는 끝으로 해서
    for tag, val in begin_store_dict.items():
        # remain begin tag
        pairs.append([tag, val, i])

timeline = TimeLine(
    window,
    categories={str(key): {"text": "{}".format(key)} for key in categories.keys()},
    height=100, extend=True, finish=float(i)
)

# for status_item in status_list:
#     tag, index = status_item
#     timeline.create_marker(tag, index, index + 0.5, background=categories[tag], text=tag)

for pair in pairs:
    tag, begin, end = pair
    timeline.create_marker(tag, begin, end, background=categories[tag], text=tag)

timeline.draw_timeline()
timeline.grid()
# window.after(2500, lambda: timeline.configure(marker_background="cyan"))
# window.after(5000, lambda: timeline.update_marker("1", background="red"))
# window.after(5000, lambda: print(timeline.time))
window.mainloop()
