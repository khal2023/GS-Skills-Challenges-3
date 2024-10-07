from lib.todo import *

class TodoList:
    def __init__(self):
        self.todos = []
        
    def add(self, todo):
        if isinstance(todo, Todo):
            self.todos.append(todo)
        else:
            raise Exception("Please enter a task of valid 'todo' type.")

    def incomplete(self):
        return [todo.task for todo in self.todos if not todo.complete]

    def complete(self):
        return [todo.task for todo in self.todos if todo.complete]

    def give_up(self):
        for todo in self.todos:
            if not todo.complete:
                todo.mark_complete()