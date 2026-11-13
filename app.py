import unittest
# Application code
def add(a,b):
  return a + b

def subtract(a,b):
  retturn a - b

def multiply(a,b):
  retturn a * b

#Automated test cases
class TestCalculator(unittest.TestCase):

  def test_add(self):
    self.assertEqual(add(20,20),40)

 def test_add(self):
    self.assertEqual(subtract(20,10),10)

 def test_add(self):
    self.assertEqual(multiply(6,7),99)

if __name__ == "__main__":
  print("Student Calculator Application")
  print("Addition:",add(20,20))
  print("Subtraction:",subtract(20,10))
  print("Multiplication:",multiply(6,7))
  print("\nExecuting Automated Tests...\n")
  unittest.main(argv=['first-arg-is-ignored'],exit=False)
