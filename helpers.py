def get_input(label, default_value):
    return_value = input(f'%s [%g]: ' % (label, default_value))
    if return_value == '':
        return default_value
    return return_value
