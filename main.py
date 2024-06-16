import os

input_dir = './test_scripts'
output_dir = './outputs'

def main():
    test_scripts = os.listdir(input_dir)
    for script in test_scripts:
        input_file = os.path.join(input_dir, script)
        output_file = os.path.join(output_dir, script)

        content = read_script(input_file)
        converted_content = convert(content)
        # generate_output(output_file, converted_content)


def read_script(input_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()

    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except IOError:
        print("An error occurred while reading or writing the file.")

    return content

def generate_output(output_file, content):
    try:
        with open(output_file, 'w') as outfile:
            outfile.write(content)
    except IOError:
        print("An error occurred while writing the file.")

def convert(content):
    print(content)

if __name__ == '__main__':
    main()