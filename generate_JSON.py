import random


def random_json_str():
    str1 = "{\n   " + \
        generate_json_str().replace('\n', '\n   ')[0:-3] + '}'
    return str1

def generate_json_str(count_inerr_dict=1,next_is_dict = True, indent=0):
    num_elements = random.randint(1, 3)
    res = ""
    indentation = "   " * indent
    for i in range(num_elements):
        key = f"key_{i + 1}"
        res += f"{indentation}{repr(key)}: "
        if count_inerr_dict < 3 and next_is_dict:
            res += "{\n"
            res += generate_json_str(count_inerr_dict + 1,True, indent + 1)
            res += f"{indentation}}},\n"
        else:
            if i == num_elements - 1:
                count_inerr_dict -= 1
            next_is_dict = True if count_inerr_dict == 1 else False
            value = f"value_{i + 1}"
            res += f"{repr(value)},\n"
    return res

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(str(data))


test_file_json = "test_json.txt"
test_json = random_json_str()
write_file( test_file_json, test_json)
print(random_json_str())
