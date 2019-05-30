from TDD_Simple_Calculator import add
from TDD_Simple_Calculator import multiply

def test_add_zero():
	result = add(0,0)
	assert result == 0

def test_add_negatives():
	result = add(-1,-1)
	assert result == -2

def test_add_positives():
	result = add(4,5)
	assert result == 9

def test_add_unknown_number():
	result = add(1,2,3,4)
	assert result == 10

def test_multiply_two():
	result = multiply(1,2)
	assert result == 2

def test_multiply_unknown_number():
	result = multiply(1,2,3,4)
	assert result == 24