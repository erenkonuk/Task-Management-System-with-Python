import datetime

class Task:
    def __init__(self, title):
        self.title = title
        self.description = ""
        self.due_date = None
        self.start_date = None
        self.priority = 0
        self.notes = [""]
        self.links = []
        self.images = []
        self.alarm = None
        self.tags = []
        self.completed = False
        self.status = "Pending"

    def is_due(self):
        if self.due_date:
            return datetime.datetime.now() > self.due_date
        return False

    def set_start_date(self, date):
        if isinstance(date, datetime.datetime):
            self.start_date = date
        else:
            print("Invalid date format")

    def update_status(self):
        if self.is_due():
            self.status = "Overdue"
        elif self.completed:
            self.status = "Completed"
        elif self.start_date and datetime.datetime.now() >= self.start_date:
            self.status = "In Progress"

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

    def complete_task(self):
        self.completed = True
        self.update_status()

    def edit_task(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

class ToDoList:
    def __init__(self, category="General"):
        self.tasks = []
        self.category = category

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
            task.update_status()
        else:
            print("Invalid task type")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def view_tasks(self):
        for task in self.tasks:
            print(f"Title: {task.title}, Status: {task.status}, Due Date: {task.due_date}")

    def view_tasks_filtered_by_completion(self, completed=True):
        for task in self.tasks:
            if task.completed == completed:
                print(f"Title: {task.title}, Status: {task.status}, Due Date: {task.due_date}")

    def get_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

class TaskManager:
    def __init__(self):
        self.lists = []

    def create_list(self, category):
        todo_list = ToDoList(category)
        self.lists.append(todo_list)

    def get_list(self, category):
        for list_ in self.lists:
            if list_.category == category:
                return list_
        return None

    def view_tasks_by_category(self, category):
        target_list = self.get_list(category)
        if target_list:
            target_list.view_tasks()
        else:
            print(f"No tasks under '{category}' category")

    def view_all_tasks(self):
        for list_ in self.lists:
            print(f"Category: {list_.category}")
            list_.view_tasks()
            print("----------")

if __name__ == "__main__":
    manager = TaskManager()

    # Test the functionality:
    manager.create_list("Work")
    work_list = manager.get_list("Work")

    task1 = Task("Complete Project A")
    task1.due_date = datetime.datetime(2023, 10, 20)
    task1.set_start_date(datetime.datetime(2023, 10, 1))
    task1.add_tag("urgent")
    work_list.add_task(task1)

    task2 = Task("Attend Meeting")
    task2.due_date = datetime.datetime(2023, 10, 15)
    task2.add_tag("important")
    work_list.add_task(task2)

    manager.view_tasks_by_category("Work")
