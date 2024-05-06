from tests.test import *

try:
    with Test() as test:
        test.test_all()
except Exception as err:
    print("General error:", err)



