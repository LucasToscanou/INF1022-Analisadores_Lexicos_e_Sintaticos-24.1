def generate_output(output_file, script_content):
    try:
        with open(output_file, 'w') as outfile:
            outfile.write(''.join(script_content))
    except IOError:
        print("An error occurred while writing the file.")

def read_script(input_file):
    try:
        with open(input_file) as infile:
            return infile.readlines()
    except IOError:
        print("An error occurred while reading the file.")
        return None
