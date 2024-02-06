# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TaskManager:

    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   initialize todo_list []
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: string representing a single task
        pass # No code here yet

    def list_incomplete(self):
        # Returns:
        #   A list of all added tasks
        pass # No code here yet

    def mark_complete(self, index)
        # Parameters:
        #   index: representing the task to remove
        # side effects:
            #removes taks at index from list of tasks
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Initially there are no tasks
"""
tracker = TaskManager()
tracker.list_incomplete => []

"""
When we add a task
its added to the list of tasks
"""
tracker = TaskManager()
tracker.add("do dishes")
tracker.add("wash car")
tracker.add("cook dinner")
tracker.list_incomplete() 
    # => ["do dishes", "wash car", "cook dinner"]

"""
When we add multiple tasks 
and mark one as complete
it is removed from the task list
"""
tracker = TaskManager()
tracker.add("do dishes")
tracker.add("wash car")
tracker.add("cook dinner")
tracker.mark_complete(1)
tracker.list_incomplete() 
    # => ["do dishes", "cook dinner"]

"""
if we try and mark a task complete that doesnt exist
it raises an error
"""
tracker = TaskManager()
tracker.add("do dishes")
tracker.mark_complete(-1) #raises error "No such task to complete
tracker.list_complete()
    #=> ["do the dishes"]

"""
if we try and mark a task complete that doesnt exist
it raises an error
"""
tracker = TaskManager()
tracker.add("do dishes")
tracker.mark_complete(2)# raises an error "No such task to complete
tracker.list_complete()
    #=> ["do the dishes"]
```

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
