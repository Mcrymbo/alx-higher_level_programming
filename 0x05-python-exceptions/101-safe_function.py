def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except Exception as ex:
        sys.stderr.write("Exception: {}\n".format(ex))
        res = None
    return (res)
