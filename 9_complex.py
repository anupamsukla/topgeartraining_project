import sys

a = complex(int(sys.argv[1]), int(sys.argv[2]))
b = complex(int(sys.argv[3]), int(sys.argv[4]))
c = a + b
print('Addition of two numbers is', c)
c = a-b
print ('Subtraction of two numbers is', c)
c = a * b 
print ('Multiplication of two numbers is', c)
c = a / b 
print ('Division of two numbers is', c)
