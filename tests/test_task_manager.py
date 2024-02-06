import pytest
from lib.task_manager import *

def test_initially_has_no_tasks():
    tracker = TaskManager()
    assert tracker.list_incomplete() == []

def test_add_tasks():
    tracker = TaskManager()
    tracker.add("do dishes")
    tracker.add("wash car")
    tracker.add("cook dinner")
    assert tracker.list_incomplete() == ["do dishes", "wash car", "cook dinner"]

def test_add_tasks_and_mark_1_as_complete():
    tracker = TaskManager()
    tracker.add("do dishes")
    tracker.add("wash car")
    tracker.add("cook dinner")
    tracker.mark_complete(1)
    assert tracker.list_incomplete() ==  ["do dishes",  "cook dinner"]

def test_mark_test_that_is_too_low():
    tracker = TaskManager()
    tracker.add("do dishes")
    with pytest.raises(Exception) as e:
        tracker.mark_complete(-1)
    assert str(e.value) == "No such task to complete"
    assert tracker.list_incomplete() == ["do dishes"]

def test_mark_test_that_is_too_high():
    tracker = TaskManager()
    tracker.add("do dishes")
    with pytest.raises(Exception) as e:
        tracker.mark_complete(3)
    assert str(e.value) == "No such task to complete"
    assert tracker.list_incomplete() == ["do dishes"]