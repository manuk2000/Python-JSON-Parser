def read_json_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        data = eval(contents)
        return data
    

# def is_json(data):
#     try:
#         is_dict(data)
#         return True
#     except:
#         return False
    
# def is_dict(data):
#     values = dict(data).values()
#     index = 0
#     for item in values:
#         dictt = dict(item)
#         is_json(dictt)



# file_path = 'tmp.txt'  # Replace with the actual path to your JSON-like file
# dictt = read_json_file(file_path)
ope = "a"
match ope:
    case "2":
        pass