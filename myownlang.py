#coding:utf-8

import sys

def interprete(code, vars, debug_mode):
    if type(code) is str:
        code = [code]
    ip = 0
    while 1:
        if debug_mode: print(" #exe: "+" ".join(["["*(i==ip)+code[i]+"]"*(i==ip) for i in range(len(code))]))
        if ip >= len(code):
            raise Exception("syntax error?")
        if code[ip] == "END":
            if debug_mode: print(" #var:", vars)
            return None
        elif code[ip] == "IF":
            dip_cond = process_bracket(code[ip+1:])
            cond = interprete(code[ip+1:ip+2+dip_cond], vars, debug_mode)
            dip_exec = process_bracket(code[ip+2+dip_cond:], curly=1)
            if cond == 1:
                interprete(code[ip+2+dip_cond+1:ip+2+dip_cond+dip_exec+1], vars, debug_mode)
            ip += 2+dip_cond+dip_exec
        elif code[ip] == "WHILE":
            dip_cond = process_bracket(code[ip+1:])
            cond = interprete(code[ip+1:ip+2+dip_cond], vars, debug_mode)
            dip_exec = process_bracket(code[ip+2+dip_cond:], curly=1)
            if cond == 1:
                interprete(code[ip+2+dip_cond+1:ip+2+dip_cond+dip_exec+1], vars, debug_mode)
                ip -= 1
            else:
                ip += 2+dip_cond+dip_exec
        elif code[ip] == "}":
            break
        elif code[ip] == "PRINT":
            dip = process_bracket(code[ip+1:])
            print(interprete(code[ip+1:ip+2+dip], vars, debug_mode))
            ip += dip+1
        elif code[ip] == "(":
            dip = process_bracket(code[ip:])
            return interprete(code[ip+1:ip+dip], vars, debug_mode)
        elif code[ip] == "INPUT":
            vars[code[ip+1]] = int(input())
            ip += 1
        elif code[ip] == "EVAL":
            code_eval = input()
            code_eval = code_eval.replace("\t", "").replace("    ", "").replace(")", " ) ").replace("(", " ( ").replace("\n", " ").split(" ")
            code_eval = [c for c in code_eval if c != ""]
            interprete(code_eval, vars, debug_mode)
        elif code[ip] == "DEFVAR":
            vars[code[ip+1]] = 0
            ip += 1
        elif code[ip] == "ASSIGN":
            dip = process_bracket(code[ip+2:])
            if code[ip+1] not in vars.keys():
                raise Exception("undefined variable: `%s` at position %d"%(code[ip+1], ip+1))
            vars[code[ip+1]] = interprete(code[ip+2:ip+3+dip], vars, debug_mode)
            ip += dip+2
        elif code[ip] in ("+", "-", "*", "/", "%", "&", "|", ">", "<", "==", "!=", "<=", ">="):
            dip1 = process_bracket(code[ip+1:])
            var1 = interprete(code[ip+1:ip+2+dip1], vars, debug_mode)
            dip2 = process_bracket(code[ip+2+dip1:])
            var2 = interprete(code[ip+2+dip1:ip+3+dip1+dip2], vars, debug_mode)
            if code[ip] == "+":
                return var1 + var2
            elif code[ip] == "-":
                return var1 - var2
            elif code[ip] == "*":
                return var1 * var2
            elif code[ip] == "/":
                return var1 // var2
            elif code[ip] == "%":
                return var1 % var2
            elif code[ip] == "&":
                return 1 if (var1 == 1 and var2 == 1) else 0
            elif code[ip] == "|":
                return 1 if (var1 == 1 or var2 == 1) else 0
            elif code[ip] == ">":
                return 1 if (var1 > var2) else 0
            elif code[ip] == "<":
                return 1 if (var1 < var2) else 0
            elif code[ip] == "<=":
                return 1 if (var1 <= var2) else 0
            elif code[ip] == ">=":
                return 1 if (var1 >= var2) else 0
            elif code[ip] == "==":
                return 1 if (var1 == var2) else 0
            elif code[ip] == "!=":
                return 1 if (var1 != var2) else 0
        elif code[ip] in vars.keys():
            return vars[code[ip]]
        elif code[ip].isdecimal():
            return int(code[ip])
        else:
            raise Exception("unknown operator: `%s` at position %d"%(code[ip], ip))
        ip += 1

def process_bracket(code, curly=0):
    level = 0
    if curly == 0:
        begin = "("
        end = ")"
    else:
        begin = "{"
        end = "}"
    for i,c in enumerate(code):
        if c == begin:
            level += 1
        elif c == end:
            level -= 1
        if level == 0:
            return i

def main(src, debug_mode=0):
    code = src.replace("\t", "").replace("    ", "").replace(")", " ) ").replace("(", " ( ").replace("\n", " ").split(" ")
    code = [c for c in code if c != ""]
    vars = {}
    interprete(code, vars, debug_mode)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if len(sys.argv) == 3 and sys.argv[2] == "1":
            debug_mode = 1
        else:
            debug_mode = 0
        main(sys.argv[1], debug_mode=debug_mode)