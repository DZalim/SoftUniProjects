from project.task import Task

class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: Task):
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True

        return f"Completed task {task_name}"

    def clean_section(self):
        count_tasks = 0

        for task in self.tasks:
            if task.completed:
                count_tasks += 1
                self.tasks.remove(task)

        return f"Cleared {count_tasks} tasks."

    def view_section(self):
        info = f"Section {self.name}:\n"
        info += '\n'.join(task.details() for task in self.tasks)

        return info


