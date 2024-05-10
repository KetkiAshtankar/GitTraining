import pytest


def test_firstprogramone():
    print("Hi, This is my Second Line of code in Pytest")



@pytest.mark.xfail
def test_fourthprogram():
    msg = "Hello, I am here writing 4th line"
    assert msg == "Hi", "Test Case failed as strings do not match"

#
# Login in Linkedin
# I click on profile xfile
# Check for the keyword assertion
# close browser
#
# Before test - execution
# After test - post execution of method

