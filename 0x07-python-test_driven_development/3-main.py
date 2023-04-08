#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
<<<<<<< HEAD
=======
    
>>>>>>> ef26704ac60885b2335ad0c272c8d8f4d0db1815
if __name__ == "__main__":
    import doctest
    doctest.testmod()
