from get_operations import *

class Code:
    def __init__(self):
        self.start = []
        self.body = []
        self.end = []
    
    def add_start_end(self, file, start_last, end_first):
        with open(file) as infile:
            base_program_content = infile.readlines()
        
        # base_program_content = [line.strip() for line in base_program_content]
        
        self.start = base_program_content[:start_last]
        self.end = base_program_content[end_first:]

    def add_to_body(self, block):
        self.body += block

    def convert_to_c(self):
        cmds = self.body
        converted_content = get_final_program(cmds)

        return ''.join(self.start) + converted_content + ''.join(self.end)

    def _get_all_cmds(self):
        cmds = []
        cmds += self.start
        cmds += self.body
        cmds += self.end

        return self.start + self.body + self.end

    def add_if(self, condition, block):
        cmd = get_if(condition, block)
        self.body += cmd
    
    def add_for(self, var, start, end, block):
        cmd = get_for(var, start, end, block)
        self.body += cmd
    
    def add_while(self, condition, block):
        cmd = get_while(condition, block)
        self.body += cmd
    
    def add_assign(self, var, value):
        cmd = get_assign(var, value)
        self.body += cmd
    
    def add_assign_oper(self, var, type, a, b):
        cmd = get_assign_oper(var, type, a, b)
        self.body += cmd
    

    def __str__(self):
        return self.start + self.body + self.end




