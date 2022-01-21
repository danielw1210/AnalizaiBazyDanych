import pytest
from app import bubble_sort


testdata = [([1,2,3,4,5,6,7],[1,2,3,4,5,6,7]),
            ([2,4,5,7,1,3,6],[1,2,3,4,5,6,7]),
            ([4,3,2,1],[1,2,3,4]),
            ([7,4,1,3,6,2,5],[1,2,3,4,5,6,7])]


@pytest.mark.parametrize('list, ordered_list', testdata)
def test_bubble_sort(list, ordered_list):
    assert bubble_sort(list) == ordered_list