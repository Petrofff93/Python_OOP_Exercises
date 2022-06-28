from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'
        return f'Task is already in the section {self.name}'

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f'Completed task {task.name}'
        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        initial = len(self.tasks)
        final = [x for x in self.tasks if not x.completed]
        return f'Cleared {initial - len(final)} tasks.'

    def view_section(self):
        result = f'Section {self.name}:\n'

        for task in self.tasks:
            result += f'{task.details()}\n'

        return result.strip()
