## Linters
* Use [black](https://github.com/psf/black/) with default settings (max character length 88 lines).
* Use [flake8](https://github.com/PyCQA/flake8) to catch linting errors.
* Use [isort](https://github.com/timothycrosley/isort) to sort the imports.

    **=>** However, be careful while sorting imports of your flask application modules. Changing the order in flask `app/package/__init__.py` can mess up the codebase.

    ```python
    from flask import Blueprint

    package = Blueprint("package", __name__)

    from . import views
    ```

    **=>** Black is not compatible with isort. So it's better to run black after running isort.


## Functions

* Avoid mutable data types as default function/method aruments.

    ```python
    # bad
    def make_list(val, lst=[]):
        lst.append(val)
        return lst

    make_list(1)
    # => [1]
    make_list(2)
    # => [1, 2], instead of the new init [2]

    # good
    def make_list(val, lst=None):
        if lst is None:
            lst = []
        lst.append(val)
        return lst

    init_list(1)
    # => [1]
    init_list(2)
    # => [2]
    ```

* Call function paramaters by specifying their names

    ```python
    def point(x, y, z=None):
        # ...

    # bad - unclear what the params mean
    point(1, 0, 5)

    # good
    point(x=1, y=0, z=3)
    ```

## Imports

* Do not use wild card import

    ```python
    # bad
    from mod import *
    from package.mod import *

    # good
    from mod import func_0
    from package.mod import func_1
    ```

* Do not import unused modules (Flake8 will point out unused imports, make sure you remove them before committing).

* Sort the imports by import then from, and sort alphabetically (`isort` will automatically do this for you).

    ```python
    # bad
    from a_mod import foo
    import e_mod
    import b_mod
    from z_mod import bar, baz

    # good
    import b_mod
    import e_mod
    from a_mod import foo
    from z_mod import bar, baz
    ```

## Whitespaces
* Use soft tabs (space character) set to 4 spaces as per PEP8.

    ```python
    # bad
    def foo():
    ∙∙return bar

    # bad
    def foo():
    ∙return bar

    # good
    def foo():
    ∙∙∙∙return bar
    ```

## Naming Conventions

* Use snake_case when naming variables, functions, and instances. Use it for file names too as they will be used in imports.

    ```python
    # bad
    import myMod
    anOBJEct = {}
    thisIsAnObject = {}
    def ThisisAFunction():

    # good
    import my_mod
    anobject = {}
    this_is_an_object = {}
    def this_is_a_function():
    ```
* Use PascalCase only when naming classes.

    ```python
    # bad
    class exampleDummyFactory():
        # ...

    fact = exampleDummyFactory()

    # good
    class ExampleDummyFactory():
        # ...

    fact = ExampleDummyFactory()

* Avoid single letter names. Use descriptive and meaningful names - tell what the function does, or what data type an object is. Use description_object instead of object_description

    ```python
    # bad
    def a():
        # ...

    # good
    def analogy():
        # ...

    # bad - no convention to know what data type it is
    df_raw_data = pd.DataFrame(raw_data)
    id_dict_num = {"a": 1, "b": 2}

    # good - convention to tell data type by the last term
    raw_data_df = pd.DataFrame(raw_data)
    id_num_dict = {"a": 1, "b": 2}

    # bad - meaningless names, lost context
    LIST_1 = ["Jack", "Alice", "Emily"]
    # ... many lines of code later
    for item in LIST_1:
        add_person(item)

    # good
    NAME_LIST = ["Jack", "Alice", "Emily"]
    # ... many lines of code later
    for name in NAME_LIST:
        add_person(name)
    ```

* Use singular or base words in naming; avoid using plural and instead append singular with the data type.

    ```python
    # bad
    def moves_object(x, y):
        # ...

    # good
    def move_object(x, y):
        # ...

    # bad - inconsistent naming for same data type and usage
    teacher = ["Michael"]
    students = ["Jack", "Alice", "Emily"]
    books = pd.DataFrame({"title": ["lorem", "ipsum"]})

    for t in teacher:
        add_human(t)

    for student in students:
        add_human(student)

    for book in books:
        add_item(book) # wrong; iterate column name instead of book

    # good
    teacher_list = ["Michael"]
    student_list = ["Jack", "Alice", "Emily"]
    book_df = pd.DataFrame({"title": ["lorem", "ipsum"]})

    for teacher in teacher_list:
        add_human(teacher)

    for student in student_list:
        add_human(student)

    # naming as df suggests it shall be treated as a dataframe
    for idx, book in book_df.iterrow():
        add_item(book)

    ```


## Exception Handling

* Do not write bare try-except block

    ```python
    # bad
    try:
        do_something()
    except:
        pass

    # bad
    try:
        do_something()
    except Exception:
        pass
    ```

* In most cases, the caught exception type must be as specific as possible. Something like KeyError, or ConnectionTimeout, etc.

    ```python
    # good
    try:
        do_something()
    # Catch some very specific exception - KeyError, ValueError, etc.
    except ValueError:
        pass
    ```

* If some code path simply must broadly catch all exceptions - for example, the top-level loop for some long-running persistent process - then each such caught exception must write the full stack trace to a log or file, along with a timestamp. Not just the exception type and message, but the full stack trace.

    ```python
    # good
    def get_number():
        return int("foo")

    try:
        x = get_number()
    except ValueError:
        pass
    except Exception:
        logging.exception("Caught an error", exec_info=True)
    ```

## Logging
* Instantiate your logger in your package's `__init__.py` module. See how it's done in `requests` library [here.](https://github.com/kennethreitz/requests).

* Define a basic logging class

   ```python
    # Demo of a logger in __init_.py
    import logging

    logging.getLogger(__name__)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.FileHandler("packg/debug.log"), logging.StreamHandler()],
    )
* Import and use it like this
    ```python
    from . import logging

    def dumb_div(a):
        try:
            res = a // 0
        except ValueError:
            res = a // 1
        except Exception:
            logging.exception("Exception Occured")
            res = None

        return res

    dumb_div(5)
    ```

    Folder structure:
    ```
    packg
    ├── debug.log
    ├── __init__.py
    └── mod.py
    ```




## Testing
* Use [pytest](https://docs.pytest.org/en/latest/) to write your tests

* Strive to write many small [pure](https://stackoverflow.com/a/47245930/8963300) and [idempotent](https://stackoverflow.com/questions/1077412/what-is-an-idempotent-operation) functions, and minimize where mutations occur.

* Whenever you fix a bug, write a regression test. A bug fixed without a regression test is almost certainly going to break again in the future.

* Use direct assertations and explicit comparisons; avoid negations.

    ```python
    # bad - Other values can be falsy too: `[], 0, '', None`
    assert not result
    assert result_list

    # good
    assert result == False
    assert len(result_list) > 0
    ```

## Flask

### Project Structure

Try to follow **divisional structure** while designing your microservice APIs.
Here's an example of divisional structure in a Flask project.

```
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


## Being Pythonic
* [Pythonic Code Review](https://access.redhat.com/blogs/766093/posts/2802001)
* [Writing Great Code](https://www.oreilly.com/library/view/the-hitchhikers-guide/9781491933213/ch04.html)

## Reference
1. [The Most Diabolical Python Antipattern - Real Python](https://realpython.com/the-most-diabolical-python-antipattern/)
2. [Flask Project Structure - Explore Flask](https://exploreflask.com/en/latest/blueprints.html#divisional)
3. [Python Style Guide -Kengz](https://github.com/kengz/python)
