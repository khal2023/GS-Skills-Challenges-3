class Todo:
    def __init__(self, task):
        if type(task) == str:
            self.task = task
            self.complete = False
        else:
            raise Exception("Only strings allowed as input")

    def mark_complete(self):
        if not self.complete:
            self.complete = True
        else:
            raise Exception("This task has already been completed")