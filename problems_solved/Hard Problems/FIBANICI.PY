def fibonacci(n):
  """
  This function calculates the nth Fibonacci number using recursion.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage
num = 10
for i in range(num):
  print(fibonacci(i))