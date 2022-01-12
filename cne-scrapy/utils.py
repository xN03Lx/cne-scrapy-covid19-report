def get_dni_list(payload):
    _ = [i.strip() for i in payload if len(i) >  0]
    valid_dni_list = set()
    for dni in _:
        if (is_valid_dni_format(dni)):
            valid_dni_list.add(dni.lower())
        else:
            from logger import logger
            logger.warning(f"--> {dni} is not a valid dni <--")
    return valid_dni_list

def get_dni_from_query(query):
    nacionality = query.get('nacionalidad', 'V')
    dni = query.get('cedula')
    return f"{nacionality}{dni}"

def is_valid_dni_format(dni):
    dni = dni.lower()
    if (dni.startswith('v') or dni.startswith('e')):
        current_nacionality = dni[0]
        _, dni_digits = dni.split(current_nacionality)
        if(dni_digits.isdigit()):
            return True
    if (dni.isdigit()):
        return True

def get_full_name_csv(dir_name, filename):
    import os
    return os.path.join(dir_name, filename)

def to_csv(output, payload):
    with open(output, 'w', newline='') as output_file:
        import csv
        dict_writer = csv.DictWriter(output_file, payload[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(payload)
