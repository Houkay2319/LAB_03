import main
import math
import pytest_html

N_correct = 9
N_incorrect = '9'

a_correct = [5, 8, 1, 3, 9, 12, 0, math.pi]
a1_incorrect = [5, '8', 1, 3, '9', 12, 0]
a2_incorrect = 'Hello_world'

def test_Fibonacchi_on_correct_n():
    assert main.Fibonacchi(N_correct) == [1, 1, 2, 3, 5, 8, 13, 21, 34]

#def test_Fibonacchi_on_correct_n_and_incorrect_result():
    #assert main.Fibonacchi(N_correct) == [0, 1, 2, 3, 5, 8, 13, 21, 34]

#def test_Fibonacchi_on_incorrect_n():
    #assert main.Fibonacchi(N_incorrect) == [1, 1, 2, 3, 5, 8, 13, 21, 34]



def test_Puzirec_on_correct_a():
    assert main.Puzirec(a_correct) == [0, 1, 3, math.pi, 5, 8, 9, 12]


#def test_Puzirec_on_correct_a_and_incorrect_result():
    #assert main.Puzirec(a_correct) == [5, 8, 1, 3, 9, 12, 0]


#def test_Puzirec_on_incorrect_a1():
    #assert main.Puzirec(a1_incorrect) == [1, 1, 2, 3, 5, 8, 13, 21, 34]

#def test_Puzirec_on_incorrect_a2():
    #assert main.Puzirec(a2_incorrect) == [1, 1, 2, 3, 5, 8, 13, 21, 34]



def test_Calc_on_correct_n():
    assert main.Calc(8, 2, '+') == 10

#def test_Calc__on_correct_n_and_incorrect_result():
    #assert main.Calc(8, 2, '+') == 9

#def test_Calc__on_incorrect_n():
    #assert main.Calc('9', '1', '+') == 10
