from koans_plugs import *


def test_slice_with_index():
    """
        Срез можно получить, обратившись к одному символу строки по его номеру
        (индексу)
    """
    str1= "Python anywhere"

    assert srt[7] = ___


def test_slice_with_negative_index():
    """
        Если задать отрицательный индекс, то номер символа будет отсчитываться с
        конца, начиная с -1
    """

    str1= "Python anywhere"

    assert srt[-4] = ___


def test_slice_with_substring():
    """
        Для среза подстроки нужно указать два параметра (индекса) - начала и конца фрагмента

        Срез берется до символа с индексом второго параметра, а значит он в
        подстроку не включается
    """

    str1= "Python anywhere"

    assert srt[2:9] = ___


def test_slice_with_diff_indexes():
    """
        Можно использовать положительные и отрицательные значения индексов в одном срезе
    """

    str1 = "Python anywhere"

    assert str1[1:-1] = ____


def test_slice_end_of_string():
    """
        Можно опустить второй параметр и взять срез до конца строки
    """

    str1= "Python anywhere"

    assert srt[3:] = ___


def test_slice_beginning_of_string():
    """
        Аналогично, можно опустить первый параметр и взять срез от начала строки

        Если опустить оба параметра, оставив двоеточие, то срез совпадет с данной строкой
    """

    str1= "Python anywhere"

    assert srt[:5] = ___


def test_slice_with_step():
    """
        Для среза можно задать третий параметр - шаг, с которым нужно брать символы

        По умолчанию шаг в срезе равен 1 (берется каждый символ) и не прописыпается в параметрах,
        но str1[2:6] можно перписать как str[2:6:1]
    """

    str1= "Python anywhere"

    assert srt[1:9:2] = ___

def test_slice_string_backwards():
    """
        Если задать шаг -1, то символы будут идти в обратном порядке
    """

    srt1 = "Python anywhere"

    assert srt[::-1] = ___
