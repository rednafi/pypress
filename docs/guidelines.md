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



## Reference
1. [The Most Diabolical Python Antipattern - Real Python](https://realpython.com/the-most-diabolical-python-antipattern/)
