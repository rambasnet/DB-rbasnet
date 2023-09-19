import sys

def add(num1: float, num2: float) -> float:
  """Add two numbers.

  Args:
      num1 (float): first operand
      num2 (float): 2nd operad

  Returns:
      float: sum of num1 and num2
  """
  return num1+num2

def vars(name:str="Jake", age:int=10) -> str:
  """test function

  Args:
      name (str, optional): customer name. Defaults to "Jake".
      age (int, optional): customer. Defaults to 10.

  Returns:
      str: some answer
  """
  if age < 18:
    print('You\'re not allowed to vote!')
    print(f'{name=} {age=}')
  elif age >= 18 and age < 21:
    print("You can't drint alcohol in the US")
  else:
    print("You're allowed to vote")
  
  return "answer"

def test():
  ans = "yes"
  while True:
    #ans = input("Enter yes|no: ")
    sys.stdout.write('Enter yes|no: ')
    sys.stdout.flush()
    #sys.stdout.write('\n')
    ans = sys.stdin.readline().strip()
    print(f'{ans=}')
    
    if ans == 'no':
      break
    else:
      continue

if __name__ == "__main__":
  test()