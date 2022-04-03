#calculator
from art import logo

#add
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_contibue = True
  
  while should_contibue:  
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
  if input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
    num1 = answer
  else:
    should_contibue = False
    calculator()

calculator()