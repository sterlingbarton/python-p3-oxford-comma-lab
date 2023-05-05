def oxford_comma(items):
    if len(items) == 2:
        return " and ".join(items)
    elif len(items) >= 3:
        return ", ".join(items[:-1]) + ", and " + items[-1]
    else:
        return ", ".join(items)
