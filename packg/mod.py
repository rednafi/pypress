from . import logging

def some(a):
    try:
        res = a // 0
    except ValueError:
        res = a // 1
    except Exception:
        logging.exception('Error Occured')
        res = None

    return res


some(5)
