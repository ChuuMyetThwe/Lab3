import Lab2.bmi as bmi

def test_bmi_normal_weight():

    input_weight = 57
    input_height = 1.73
    result = bmi.calculate_bmi(input_height, input_weight)
    assert (result == 0)

def test_bmi_over_weight():

    input_weight = 70
    input_height = 1.6
    result = bmi.calculate_bmi(input_height, input_weight)
    assert (result == 1)

def test_bmi_under_weight():
    input_weight = 45
    input_height = 1.73
    result = bmi.calculate_bmi(input_height, input_weight)
    assert (result == -1)

