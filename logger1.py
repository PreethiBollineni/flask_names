import logging
logging.basicConfig(level=logging.DEBUG,filename="new1.log",filemode='w')
LOGGER=logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

def factorial(n):
    print(n)
    fact=1
    for i in range(2,n+1):
        LOGGER.debug(f'i={i}')
        fact*=i
        LOGGER.debug(f'fact={i}')
a=factorial(5)
print(a)
