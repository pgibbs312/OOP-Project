import pytest
from unittest.mock import patch, mock_open
from controllers.score import Score



DATA = """{"name": "test", "score": 100}"""

def test_check_from_json():
    """
    Makes sure that `open` is called with the correct file name in `from_json_`
    """
    with patch('builtins.open', mock_open(read_data=DATA)) as mock_file:
        # score1=Score("test", 100)
        score1= Score.from_json("test.json")

        assert "test.json" in tuple(mock_file.call_args)[0]



def test_load_from_json():
    """
    Patches `open` to load one food item in the manager, and check its attributes
    """
    with patch('builtins.open', mock_open(read_data=DATA)) as mock_file:
        # score1=Score("test", 100)
        score1=Score.from_json("test.json")

        assert score1.player_name == "test"
        assert score1.score == 100
        


def test_from_dict():
    DICT={"name": "test2", "score": 200}
    score1 = Score.from_dict(DICT)

    assert score1.player_name == "test2"
    assert score1.score == 200