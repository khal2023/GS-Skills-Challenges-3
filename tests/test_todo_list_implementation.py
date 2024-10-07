import pytest
from lib.todo_list import *
from lib.todo import *

def test_add_todo():
    todolist = TodoList()
    todo1 = Todo("Take out trash")
    todo2 = Todo("Practice spanish")
    todo3 = Todo("Play clarinet")
    todolist.add(todo1)
    todolist.add(todo2)
    todolist.add(todo3)
    assert todolist.todos == [todo1, todo2, todo3]

def test_refuse_todos_of_wrong_type():
    todolist = TodoList()
    with pytest.raises(Exception) as e:
        todolist.add(1)
    assert str(e.value) == "Please enter a task of valid 'todo' type."

def test_return_imcomplete_tasks():
    todolist = TodoList()
    todo1 = Todo("Take out trash")
    todo2 = Todo("Practice spanish")
    todo3 = Todo("Play clarinet")
    todolist.add(todo1)
    todolist.add(todo2)
    todolist.add(todo3)
    assert todolist.incomplete() == ["Take out trash", "Practice spanish", "Play clarinet"]

def test_return_incomplete_tasks_when_one_is_complete():
    todolist = TodoList()
    todo1 = Todo("Take out trash")
    todo2 = Todo("Practice spanish")
    todo3 = Todo("Play clarinet")
    todolist.add(todo1)
    todolist.add(todo2)
    todolist.add(todo3)
    todo3.mark_complete()
    assert todolist.incomplete() == ["Take out trash", "Practice spanish"]

def test_return_completed_tasks():
    todolist = TodoList()
    todo1 = Todo("Take out trash")
    todo2 = Todo("Practice spanish")
    todo3 = Todo("Play clarinet")
    todolist.add(todo1)
    todolist.add(todo2)
    todolist.add(todo3)
    todo3.mark_complete()
    assert todolist.complete() == ["Play clarinet"]

def test_mark_all_as_complete():
    todolist = TodoList()
    todo1 = Todo("Take out trash")
    todo2 = Todo("Practice spanish")
    todo3 = Todo("Play clarinet")
    todolist.add(todo1)
    todolist.add(todo2)
    todolist.add(todo3)
    assert todolist.complete() == []
    todolist.give_up()
    assert todolist.complete() == ["Take out trash", "Practice spanish", "Play clarinet"]

def test_mark_all_as_complete_when_one_is_already_completed():
    todolist = TodoList()
    todo1 = Todo("Take out trash")
    todo2 = Todo("Practice spanish")
    todo3 = Todo("Play clarinet")
    todolist.add(todo1)
    todolist.add(todo2)
    todolist.add(todo3)
    todo3.mark_complete()
    todolist.give_up()
    assert todolist.complete() == ["Take out trash", "Practice spanish", "Play clarinet"]