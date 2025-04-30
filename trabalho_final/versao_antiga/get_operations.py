#   Operacoes na linguagem C

# Inicializacao
def get_init(var, value):
    cmd = []
    cmd.append(f'int {var} = {value}')
    return cmd

# Operacoes de controle de fluxo
def get_if(condition, cmds):
    return _get_flow("if", condition, cmds)

def get_if_else(condition, cmds_if, cmds_else):
    new_cmds = []
    new_cmds.append(_get_flow("if", condition, cmds_if))
    new_cmds.append(_get_flow("else", "", cmds_else))
    return new_cmds

def get_while(condition, cmds):
    return _get_flow("while", condition, cmds)

def get_for(iter, condition, step, cmds):
    new_cmds = []
    condition = f'int {iter} = 0; {iter} < {condition}; {iter}+={step}'
    new_cmds = _get_flow("for", condition, cmds)
    return new_cmds

def _get_flow(type, condition, cmds):
    cmds = single_items_to_string(cmds)
    new_cmds = []
    new_cmds.append(f'{type} ({condition}) {{')
    new_cmds.append(cmds)
    new_cmds.append('}')
    return new_cmds

def single_items_to_string(cmds):
    new_cmds = []
    for cmd in cmds:
        if(type(cmd) == list):
            new_cmds.append(single_items_to_string(cmd))
        else:
            new_cmds.append(cmd)
    return new_cmds

# Operacao de atribuicao
def get_assign(var, expression):
    cmd = []
    cmd.append(f'{var} = {expression}')
    return cmd

# Operacoes aritmeticas
def get_operation(type, a, b):
    expression = f'{a} {type} {b}'
    return expression

def get_assign_oper(var, type, a, b):
    cmd = get_assign(var, get_operation(type, a, b))
    return cmd

# Formatacao
def _add_semicolons_and_newlines(cmds):
    new_cmds = []
    for cmd in cmds:
        if(type(cmd) == str):
            new_cmds.append(cmd)
            if(len(cmd) != 0):
                if(
                    cmd[-1] not in ['{', '}', ';'] and
                    cmd[0] != '#'
                ):
                    new_cmds.append(';')

            new_cmds.append('\n')
        else:
            new_cmds.append(_add_semicolons_and_newlines(cmd))
    return new_cmds

def _add_tab(cmd, depth):
    return '\t' * depth + cmd

def _add_layered_tabs(cmds, depth=1):
    new_cmds = []
    for cmd in cmds:
        print(cmd)
        if isinstance(cmd, list):
            if len(cmd) > 1:
                new_cmds.append(_add_layered_tabs(cmd, depth + 1))
            else:
                new_cmds.append(_add_tab(cmd[0], depth))
        else:
            new_cmds.append(_add_tab(cmd, depth))
    return new_cmds

def _join_all(cmds):
    new_cmds = []
    for cmd in cmds:
        if(type(cmd) == list):
            new_cmds.append(_join_all(cmd))
        else:
            new_cmds.append(cmd)
    return ''.join(new_cmds)

# Extra

def get_print(var):
    cmd = []
    cmd.append(f'printf("{var}: %d\\n", {var})')
    return cmd


# Finalizacao
def get_final_program(cmds):
    cmds = _add_layered_tabs(cmds)
    cmds = _add_semicolons_and_newlines(cmds)

    code = _join_all(cmds)
    
    return code



