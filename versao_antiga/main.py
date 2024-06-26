import os
from Code import *
from aux import *

input_dir = './test_scripts'
output_dir = './outputs'
base_file = 'base_program.c'

def main():
    # Objeto codigo 
    code = Code()
    code.add_start_end(base_file, 4, -3)

    # Converte os scripts de teste
    test_scripts = os.listdir(input_dir)
    for script in test_scripts:
        input_file = os.path.join(input_dir, script)
        output_file = os.path.join(output_dir, script[:-4] + '.c')

        script_content = read_script(input_file)
        

        # Exemlo de uso ------------------------------
        cmds = []
        cmd_init1 = get_init('a', 10)
        cmd_init2 = get_init('b', 10)
        cmd_init3 = get_init('c', 10)
        cmd_ass1 = get_assign_oper('a', '+', 'b', 'c')
        cmd_ass2 = get_assign_oper('a', '-', 'b', 'c')
        cmd_for = get_for('i', 10, 1, [cmd_ass1, cmd_ass2]) 
        
        cmd_print_a = get_print('a')
        cmd_print_b = get_print('b')
        cmd_print_c = get_print('c')

        cmds += cmd_init1 + cmd_init2 + cmd_init3
        cmds += cmd_print_a + cmd_print_b + cmd_print_c
        cmds += get_for('j', 10, 1, cmd_for)
        cmds += cmd_print_a + cmd_print_b + cmd_print_c
        
        # --------------------------------------------

        code.add_to_body(cmds)

        converted_content = code.convert_to_c()
        
        generate_output(output_file, converted_content)

    


if __name__ == '__main__':
    main()