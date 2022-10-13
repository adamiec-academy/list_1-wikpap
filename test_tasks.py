import pytest
from task_1 import cross
from task_2 import chess_board
from task_3 import envelope
from task_4 import snowman, snowball
from task_5 import factorial, report
from test_data import CROSS_DATA, CHESS_BOARD_DATA, REPORT_DATA, FACTORIAL_DATA, SNOWMAN_DATA, \
    SNOWBALL_DATA, ENVELOPE_DATA


def _data_args(data):
    if not data:
        return
    size = len(data[0])
    names = []
    for entry in data:
        name = []
        for arg in range(size - 1):
            name.append(str(entry[arg]))
        names.append(", ".join(name))
    return names


@pytest.mark.parametrize("arg, output", CROSS_DATA, ids=_data_args(CROSS_DATA))
def test_task_1_cross(capfd, arg, output):
    cross(arg)
    out, _ = capfd.readouterr()
    assert out == output


@pytest.mark.parametrize("arg1, arg2, output", CHESS_BOARD_DATA, ids=_data_args(CHESS_BOARD_DATA))
def test_task_2_chessboard(capfd, arg1, arg2, output):
    chess_board(arg1, arg2)
    out, _ = capfd.readouterr()
    assert out == output


@pytest.mark.parametrize("arg, output", ENVELOPE_DATA, ids=_data_args(ENVELOPE_DATA))
def test_task_3_envelope(capfd, arg, output):
    envelope(arg)
    out, _ = capfd.readouterr()
    assert out == output


@pytest.mark.parametrize("arg1, arg2, output", SNOWBALL_DATA, ids=_data_args(SNOWBALL_DATA))
def test_task_4_snowball(capfd, arg1, arg2, output):
    snowball(arg1, arg2)
    out, _ = capfd.readouterr()
    assert out == output


@pytest.mark.parametrize("arg, output", SNOWMAN_DATA, ids=_data_args(SNOWMAN_DATA))
def test_task_4_snowman(capfd, arg, output):
    snowman(arg)
    out, _ = capfd.readouterr()
    assert out == output


@pytest.mark.parametrize("arg, output", FACTORIAL_DATA, ids=_data_args(FACTORIAL_DATA))
def test_task_5_factorial(arg, output):
    result = factorial(arg)
    assert result == output


def test_task_5_report(capfd):
    report()
    out, _ = capfd.readouterr()
    assert out == REPORT_DATA
