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
        if isinstance(item, dict):
            is_dict(dict(item))


def test_read_json_file():
    file_path = 'test.json'  # Replace with the path to your test JSON file
    data = read_json_file(file_path)
    assert isinstance(data, dict) or data is False


def test_is_json():
    # Test with valid JSON
    valid_data = {'key': 'value'}
    assert is_json(valid_data) == True

    # Test with invalid JSON
    invalid_data = 'not a dictionary'
    assert is_json(invalid_data) == False


def test_is_dict():
    # Test with valid dictionary
    valid_dict = {'key': 'value'}
    assert is_dict(valid_dict) == None

    # Test with invalid dictionary
    invalid_dict = {'key': {'nested_key': 'nested_value'}}
    assert is_dict(invalid_dict) == None


def test_dict_to_json_str():
    dictt = {'key1': 'value1', 'key2': {'nested_key': 'nested_value'}}
    expected_output = "{\n   'key1': 'value1',\n   'key2': {\n      'nested_key': 'nested_value'\n   }\n}"
    assert dict_to_json_str(dictt) == expected_output

# Add more tests for other functions if needed


if __name__ == '__main__':
    test_read_json_file()
    test_is_json()
    test_is_dict()
    test_dict_to_json_str()
    # Call other test functions here if added
