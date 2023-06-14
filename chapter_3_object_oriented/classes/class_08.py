import os 

os.system('cls')

class MyError(Exception): ...

class AnotherError(Exception): ...

def throw_error():
    exception_ = MyError('Testing error class.')
    exception_.add_note('Testing notes.')
    exception_.add_note('You got it wrong.')

    raise exception_

try:
    throw_error()
except (MyError, AnotherError) as error:
    print(error.__class__.__name__)
    print(error.args)

    exception_ = AnotherError("I will throw the error again!")
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('One more note.')

    raise exception_