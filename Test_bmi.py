
from lab2 import bmi

def test_bmi_under_weight():
 result = 0
 input=30
 result=bmi.calculate_bmi(1.6, input)
 test =-1
 assert (result == test)

def test_bmi_normal_weight():
 result = 0
 input = 55
 result=bmi.calculate_bmi(1.6, input)
 test =0
 assert (result == test)
def test_bmi_over_weight():
 result=0
 input=100
 result = bmi.calculate_bmi(1.6, input)
 test =1
 assert (result == test)

