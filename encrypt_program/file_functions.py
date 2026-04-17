def read_file(input_path):
    with open(input_path, 'r') as f:
        return f.read()


def write_file(output_path, content):
    with open(output_path, 'w') as f:
        f.write(content)
