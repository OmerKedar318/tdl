import tkinter


class Mission:
    def __init__(self, name, time, content, due):
        self.name = name
        self.content = content
        self.time = time
        self.due = due

    def get_due(self):
        return self.due

    def get_name(self):
        return self.name

    def get_time(self):
        return self.time

    def get_content(self):
        return self.content

    def set_name(self, name):
        self.name = name

    def set_time(self, time):
        self.time = time

    def set_content(self, content):
        self.content = content

    def set_due(self, due):
        self.due = due


def add_mission(events, mission):
    events.append(mission)


def main():
    events = []


if __name__ == '__main__':
    main()

