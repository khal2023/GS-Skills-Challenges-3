Todo recipe
```python 
def test_add_todo():
    todolist = TodoList
    todolist.add(todo("Take out trash"))
    todolist.add(todo("Practice spanish"))
    todolist.add(todo("Play clarinet"))
    assert todolist.incomplete() == ["Take out trash", "Pratice Spanish", "Play clarinet"]






```