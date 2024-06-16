import os
from Code import *

input_dir = './test_scripts'
output_dir = './outputs'
base_file = 'base_program.c'

def main():
    # Objeto codigo 
    code = Code()
    code.add_start_end(base_file, 4, 3)
    code.print_code()

    # Converte os scripts de teste
    test_scripts = os.listdir(input_dir)
    for script in test_scripts:
        input_file = os.path.join(input_dir, script)
        output_file = os.path.join(output_dir, script)

        script_content = read_script(input_file)
        

        # Exemlo de uso ------------------------------
        cmds = []
        cmd_ass1 = get_assign_oper('a', '+', 'b', 'c')
        cmd_ass2 = get_assign_oper('a', '-', 'b', 'c')
        cmd_for = ('i', 10, 10, [cmd_ass1, cmd_ass2]) 
        
        cmds += cmd_ass1
        cmds += get_for('i', 10, 10, cmd_for)
        cmds += cmd_ass2
        # --------------------------------------------

        code.add_to_body(cmds)

        converted_content = code.convert_to_c()
        
        generate_output(output_file, converted_content)

    

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

if __name__ == '__main__':
    main()