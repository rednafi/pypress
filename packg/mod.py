from . import logging


def some(num0, num1, num2, num3, num4):
    """[summary]

    Args:
        num0 ([type]): [description]
        num1 ([type]): [description]
        num2 ([type]): [description]
        num3 ([type]): [description]
        num4 ([type]): [description]

    Returns:
        [type]: [description]
    """

    try:
        res = a // 0
    except ValueError:
        res = a // 1
    except Exception:
        logging.exception("Error Occured")
        res = None

    return res


some(5)
