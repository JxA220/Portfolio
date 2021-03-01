from tkinter import *
import parser

root = Tk()
root.title("Calculadora")

display = Entry(root)
display.grid(row = 0, columnspan = 6,sticky = W+E)

# Função para obter numeros

i = 0

def get_number(n):
    global i
    display.insert(i,n)
    i += 1

# Funcion de operações matemáticas

def get_operation(operators):
    global i
    operator_len = len(operators)
    display.insert(i,operators)
    i += operator_len

# Funcão de eliminacão (AC)

def clear():
    display.delete(0,END)

# Função de eliminação de um digito

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear()
        display.insert(0,display_new_state)
    else:
        clear()
        display.insert(0,"Error")

# Funcion de calculo

def result():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear()
        display.insert(0,result)
    except:
        clear()
        display.insert(0,"Error")



#Botões numéricos

Button(root,text="1",command = lambda:get_number(1)).grid(row = 1, column = 0,sticky = W+E)
Button(root,text="2",command = lambda:get_number(2)).grid(row = 1, column = 1,sticky = W+E)
Button(root,text="3",command = lambda:get_number(3)).grid(row = 1, column = 2,sticky = W+E)

Button(root,text="4",command = lambda:get_number(4)).grid(row = 2, column = 0,sticky = W+E)
Button(root,text="5",command = lambda:get_number(5)).grid(row = 2, column = 1,sticky = W+E)
Button(root,text="6",command = lambda:get_number(6)).grid(row = 2, column = 2,sticky = W+E)

Button(root,text="7",command = lambda:get_number(7)).grid(row = 3, column = 0,sticky = W+E)
Button(root,text="8",command = lambda:get_number(8)).grid(row = 3, column = 1,sticky = W+E)
Button(root,text="9",command = lambda:get_number(9)).grid(row = 3, column = 2,sticky = W+E)
Button(root,text="0",command = lambda:get_number(0)).grid(row = 4, column = 1,sticky = W+E)

#Botones operacionais

Button(root,text="AC",command = lambda: clear()).grid(row = 4, column = 0,sticky = W+E)
Button(root,text="%",command = lambda: get_operation("%")).grid(row = 4, column = 2,sticky = W+E)
Button(root,text="+",command = lambda: get_operation("+")).grid(row = 1, column = 3,sticky = W+E)
Button(root,text="-",command = lambda: get_operation("-")).grid(row = 2, column = 3,sticky = W+E)
Button(root,text="*",command = lambda: get_operation("*")).grid(row = 3, column = 3,sticky = W+E)
Button(root,text="/",command = lambda: get_operation("/")).grid(row = 4, column = 3,sticky = W+E)
Button(root,text="<-",command = lambda:undo()).grid(row = 1, column = 4,columnspan = 2,sticky = W+E)
Button(root,text="exp",command = lambda: get_operation("**")).grid(row = 2, column = 4,sticky = W+E)
Button(root,text="^2",command = lambda: get_operation("**2")).grid(row = 2, column = 5 ,sticky = W+E)
Button(root,text="(",command = lambda: get_operation("(")).grid(row = 3, column = 4,sticky = W+E)
Button(root,text=")",command = lambda: get_operation(")")).grid(row = 3, column = 5,sticky = W+E)
Button(root,text="=",command = lambda: result()).grid(row = 4, column = 4,sticky = W+E,columnspan = 2)

if __name__ == '__main__':
    root.mainloop()
