README:

This is a Python script that provides basic functionality to interact with a JSON-like file.

Usage:
1. Ensure that you have a JSON-like file to work with.
2. Update the 'file_path' variable in the script to point to the actual path of your JSON-like file.
3. Run the script using Python 3.

The script includes the following functions:

1. read_json_file(file_path)
   - Reads the contents of the JSON-like file specified by 'file_path'.
   - Attempts to parse the contents as a JSON-like object.
   - Returns the parsed data if successful, or False if the contents are not valid JSON-like.

2. is_json(data)
   - Checks if the provided data is a valid JSON-like object.
   - Returns True if the data is a dictionary, False otherwise.

3. is_dict(data)
   - Recursively checks if the provided data is a dictionary.
   - Returns True if the data is a dictionary, False otherwise.

4. write_file(file_path, data)
   - Writes the provided 'data' to the JSON-like file specified by 'file_path'.
   - The 'data' should be a valid JSON-like object.

5. dict_to_json_str(dictt)
   - Converts a dictionary to a JSON-like string representation.
   - Returns the JSON-like string.

6. to_rite_json_syntax(dictt, indent=0)
   - Recursively converts a dictionary to a JSON-like string representation with proper indentation.
   - Returns the JSON-like string.

7. question(message)
   - Prompts the user with the provided 'message'.
   - Returns the user's input as a string.

8. input_dict()
   - Prompts the user to input a dictionary key.
   - Allows the user to input attribute keys and values until they choose to exit.
   - Returns the resulting dictionary.

9. input_key_value()
   - Prompts the user to input an attribute key or choose to exit.
   - If the user chooses to exit, returns False.
   - Otherwise, prompts for a new value and returns a dictionary with the key-value pair.

10. change_itmes_dict(file_path, dictt, key)
    - Removes the provided 'key' from the 'dictt' dictionary.
    - Prompts the user to input a new dictionary and updates 'dictt' with the new data.
    - Writes the updated dictionary to the JSON-like file specified by 'file_path'.

11. show_dict_input_change_key(dictt)
    - Displays the keys of the 'dictt' dictionary.
    - Prompts the user to enter a key and returns the selected key.

12. operation_dict(file_path, key, dictt={})
    - Performs various operations on a dictionary within 'dictt' based on user input.
    - Available operations include showing the value of a key, deleting a key, updating a key, inserting a new key-value pair, reading the file again, and exiting the system.

13. operation_value(file_path, key, dictt)
    - Performs operations on a value within 'dictt' based on user input.
    - Available operations include showing the value, updating the value, reading the file again, and exiting.

14. main(file_path, dictt)
    - The main function that coordinates the program flow.
    - Checks if the 'dictt' dictionary is empty and terminates if it is.
    - Prompts the user to input a key from the 'dictt' dictionary.
    - Calls 'operation_dict' if the key's value is a dictionary, or 'operation_value' otherwise.

Please make sure to replace the 'file_path' variable in the script with the actual path to your JSON-like file before running the script.
