from app.baby_name_app import *

def test_read_name_boy():
    result = len(read_names_from_file(filename="data/babynames_boys.csv"))
    assert result == 200

def test_read_name_girl():
    result = len(read_names_from_file(filename="data/babynames_girls.csv"))
    assert result == 200
