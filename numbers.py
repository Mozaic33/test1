#!/usr/bin/python
# Tested with python 2.7, doesn't work with python 3.5
# Written by Adrian Maftei , adrian.maftei@endava.com
import sys
import time


def usage ():
    """Print correct script usage."""
    print "Usage : {} <number1> <number2>".format(sys.argv[0])
    exit(1)
    
    
def timestamped(func):
    """Add pythonic timestamp to function when used as decorator."""
    def timestamp(*args, **kw):
        formatted_time = time.strftime('%d %b %Y %H:%M:%S', time.localtime())
        result = func(*args, **kw)

        print '{} called at {}'.format(func.__name__, formatted_time)
        return result

    return timestamp    

    
def check_arguments( args ):
    """Check number of arguments and print usage if not correct."""
    # Check number of arguments
    if len ( args ) != 2:
        usage()

        
def arguments_to_natural( args ):  
    """Convert the list of arguments to integer and return new list."""
    numbers=[]
    for arg in args: 
        # Try to cast to integer
        try:
            arg = int(arg)
        except ValueError:
            print "{} is not a interger".format(arg)
            usage()
        else:
            if arg <0:
                print "{} lower than 0".format(arg)
                usage()
            else :
                numbers.append(arg)
    # Return new list
    return numbers
   
   
@timestamped   
def calculate_square_of_sum( num ):
    """Calculate square of the sum of numbers <= parameter."""
    # non Pythonic, but easier to understand
    # Xrange is better than range for python 2
    # sum = 0;
    # for n in xrange(1, num+1):
        # sum+=n;
    # return sum*sum
    
    # More pythonic
    return sum( xrange(1, num+1)) ** 2
    
    
@timestamped
def calculate_prod_of_squares( num ):
    """Calculate product of the squared numbers <= parameter."""
    # non Pythonic, but easier to understand
    # Xrange is better than range for python 2
    #prod = 1
    #for n in xrange(1, num+1):
    #   prod*=n*n
    #return prod 
    
    # No longer considered pythonic in python 3, but as reference of advanced function usage
    # Use reduce function with lambda and list generator
    return reduce(lambda x,y: x*y, [n**2 for n in xrange(1, num+1)])        
    
    
# Application main entry point 
def main():
    # sys.arv[0] is the script name, remove it 
    numbers = sys.argv[1:]
    
    # Req 1
    check_arguments ( numbers )
    
    # Req 2
    numbers = arguments_to_natural( numbers )
    
     
    # Req 5 Non-pythonic timestamp
    # formatted_time = time.strftime('%d %b %Y %H:%M:%S', time.localtime())
    # print "calculate_square_of_sum called at {}".format(formatted_time)

    # Req 3    
    square_of_sum=calculate_square_of_sum(numbers[0])
    print "Square of sum of numbers lower or equal to {} is {}".format(numbers[0], square_of_sum)  

    # Req 5 Non-pythonic timestamp
    # formatted_time = time.strftime('%d %b %Y %H:%M:%S', time.localtime())
    # print "calculate_prod_of_squares called at {}".format(formatted_time)    
    
    # Req 4  
    prod_of_squares=calculate_prod_of_squares(numbers[1])
    print "Product of squares of numbers lower or equal to {} is {}".format( numbers[1], prod_of_squares)    
     
   
if __name__ == "__main__": 
    main()