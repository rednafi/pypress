## Code Formatting
* Use black with default settings (max character length 88 lines)
* Use flake8 to catch linting errors

## Exception Handling

**Do not write bare try-except block**

Don't write this:

```python
try:
    do_something()
except:
    pass
```

Or this,
```python
try:
    do_something()
except Exception:
    pass
```

In most cases, the best choice is to catch a more specific exception. Something like this:

```python
try:
    do_something()
# Catch some very specific exception - KeyError, ValueError, etc.
except ValueError:
    pass
```

* If some code path simply must broadly catch all exceptions - for example, the top-level loop for some long-running persistent process - then each such caught exception must write the full stack trace to a log or file, along with a timestamp. Not just the exception type and message, but the full stack trace.
* For all other except clauses - which really should be the vast majority - the caught exception type must be as specific as possible. Something like KeyError, or ConnectionTimeout, etc.

```python

def get_number():
    return int('foo')
try:
    x = get_number()
except Exception as ex:
    logging.exception('Caught an error')
```

## Project Structure

Try to follow **divisional structure** while designing your microservice APIs.
Here's an example of divisional structure in a Flask project.

```python

yourapp/
    __init__.py
    admin/
        __init__.py
        views.py
        static/
        templates/
    home/
        __init__.py
        views.py
        static/
        templates/
    control_panel/
        __init__.py
        views.py
        static/
        templates/
    models.py
```
Read more on divisional structure [here.](https://exploreflask.com/en/latest/blueprints.html#divisional)


## Reference
1. [The Most Diabolical Python Antipattern - Real Python](https://realpython.com/the-most-diabolical-python-antipattern/)
2. [Flask Project Structure - Explore Flask](https://exploreflask.com/en/latest/blueprints.html#divisional)
