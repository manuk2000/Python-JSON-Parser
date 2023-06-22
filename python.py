def read_json_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        try:
            data = eval(contents)
            return data if is_json(data) else False
        except:
            return False

def is_json(data):
    try:
        is_dict(data)
        return True
    except:
        return False


def is_dict(data):
    values = dict(data).values()
    for item in values:
        if isinstance(item , dict):
            is_dict(dict(item))


def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(str(data))


def dict_to_json_str(dictt):
    str1 = "{\n   " + \
        to_rite_json_syntax(dictt).replace('\n', '\n   ')[0:-3] + '}'
    return str1


def to_rite_json_syntax(dictt, indent=0):
    res = ""
    indentation = "   " * indent
    for key, value in dictt.items():
        res += f"{indentation}{repr(key)}: "
        if isinstance(value, dict):
            res += "{\n"
            res += to_rite_json_syntax(value, indent + 1)
            res += f"{indentation}}},\n"
        else:
            res += f"{repr(value)},\n"
    return res


def question(message):
    return input(message)


def input_dict():
    key_dict = input("\ninput dict key: ")
    attribut_dict = {}
    while True:
        tmp_dict_instanse = input_key_value()
        if tmp_dict_instanse == False:
            break
        attribut_dict.update(tmp_dict_instanse)
    res_dict = {key_dict: attribut_dict}
    return res_dict


def input_key_value():
    key = input("\ninput attribut key or exit: ")
    if key == 'exit':
        return False
    value = input("\ninput new value: ")
    return {key: value}


def change_itmes_dict(file_path, dictt, key):
    del dictt[key]
    dict_tmp = input_dict()
    dictt.update(dict_tmp)
    json_str = dict_to_json_str(dictt)
    write_file(file_path, json_str)


def show_dict_input_change_key(dictt):
    print("\nshow attributes: \n")
    print(list(dictt.keys()) if isinstance(dictt, dict) else dictt)
    key = input("\nEnter the full name : ")
    return key if key in list(dictt.keys()) else show_dict_input_change_key(dictt)


def operation_dict(file_path, key, dictt={}):
    question_message = """Enter number option:
1: show key
2: del
3: update
4: inset 
5: read again fail
6: exit system
"""
    operation = question(question_message)
    match operation:
        case '1':
            main(file_path, dictt.get(key))
            # show value of key
            pass
        case '2':
            del dictt[key]
            json_str = dict_to_json_str(dictt)
            write_file("tmp.txt", json_str)
            operation_dict(file_path, key, dictt)
            # del
        case '3':
            change_itmes_dict(file_path, dictt, key)
            operation_dict(file_path, key, dictt)
            # del & insert
        case '4':
            dict_tmp = input_dict()
            dictt.update(dict_tmp)
            json_str = dict_to_json_str(dictt)
            write_file("tmp.txt", json_str)
            operation_dict(file_path, key, dictt)
            # insert
        case '5':
            main(file_path, dictt)
            # read of file of call main
        case '6':
            return
            # exit
        case _:
            print("Command not fond : ")
            operation_dict(file_path, key, dictt)


def operation_value(file_path, key, dictt):
    question_message = """Enter number option:
1: show value 
2: update value
3: read again fail 
4: exit
"""
    operation = question(question_message)
    match operation:
        case '1':
            print(dictt.get(key))
            operation_value(file_path, key, dictt)
            # show value of key
        case '2':
            value = input("input new value: ")
            dictt[key] = value
            operation_value(file_path, key, dictt)
            # update value
        case '3':
            return
        case _:
            main(file_path, dictt)
            # read again fail


def main(file_path, dictt):
    if not dictt:
        print("file no JSON")
        return
    key = show_dict_input_change_key(dictt)
    if isinstance(dictt.get(key), dict):
        operation_dict(file_path, key, dictt)
    else:
        operation_value(file_path, key, dictt)


file_path = 'tmp.txt'  # Replace with the actual path to your JSON-like file
dictt = read_json_file(file_path)
main(file_path, dictt)
