def print_file(file_path):
    file = open(file_path, "r")
    content = file.read()
    file.close()
    print(content)

def read_file(file_path):
    file = open(file_path, "r")
    content = file.read()
    file.close()
    return content

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32