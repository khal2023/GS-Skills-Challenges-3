import pytest
from lib.todo import *

def test_todo_init():
    todo = Todo("Take out trash")
    assert todo.task == "Take out trash"
    assert todo.complete == False

def test_todo_refuses_nonstrings():
    with pytest.raises(Exception) as e:
        todo = Todo(False)
    assert str(e.value) == "Only strings allowed as input"

def test_todo_marks_complete():
    todo = Todo("Take out trash")
    todo.mark_complete()
    assert todo.complete == True

def test_checks_if_task_is_already_complete():
    todo = Todo("Take out trash")
    todo.mark_complete()
    with pytest.raises(Exception) as e:
        todo.mark_complete()
    assert str(e.value) == "This task has already been completed"
