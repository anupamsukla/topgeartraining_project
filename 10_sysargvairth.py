import sys
sys.argv[1]=int(sys.argv[1])
sys.argv[2]=int(sys.argv[2])
c=sys.argv[1] + sys.argv[2]
print ('\n Addition of two numbers is', c)
c=sys.argv[1] - sys.argv[2]
print ('\n Subtraction of two numbers is', c)
c=sys.argv[1] * sys.argv[2] 
print ('\n Multiplication of two numbers is', c)
c=sys.argv[1] / sys.argv[2] 
print ('\n Division of two numbers is', c)
c=sys.argv[1] % sys.argv[2]
print ('\n modulus of two numbers is', c)
c=sys.argv[1] ** sys.argv[2]
print ('\n Exponentiation of two numbers is', c)
c=sys.argv[1] // sys.argv[2]
print ('\n Floor division of two numbers is', c)

