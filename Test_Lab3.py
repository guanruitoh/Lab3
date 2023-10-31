import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_morethanten():
    result =[]
    input_arr =[66,66,66,44,44,44,44,44,44,44,44,44]

    result=Lab3.bubble_sort(input_arr,len(input_arr))
    assert (result==1)

def test_bubble_sort_zero():
    result=[]
    input_arr=[]
    result=Lab3.bubble_sort(input_arr,len(input_arr))
    assert (result==0)
def test_bubble_sort_nonintegers():
    input_arr=['w',3,3,3]
    for value in input_arr:
        assert (Lab3.bubble_sort(input_arr,isinstance(value,int))==2)