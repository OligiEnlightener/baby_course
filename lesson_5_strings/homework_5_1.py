import string
import keyword


def is_valid_name(name: str) -> bool:
    if name:
        if keyword.iskeyword(name) or name[0].isdigit():
            return False
        else:
            underline_counter = 0
            for char in name:
                if char == "_":
                    underline_counter += 1
                elif char in string.punctuation:
                    return False
                elif char.isspace():
                    return False
                elif not char.islower() and not char.isdigit():
                    return False
            if 1 < underline_counter == len(name):
                return False
        return True
    else:
        return False


def test_variable_name():
    false_names = ["", "assert", "3m", "getValue", "get_Value", "Get_Value", "get!value", "get value", "___", "__", "3"]
    true_names = ["_test", "_", "__test", "x", "get_value", "some_super_puper_value", "m3", "assert_exception"]
    for name in false_names:
        assert is_valid_name(name) is False, name + ", index " + str(false_names.index(name))
    for name in true_names:
        assert is_valid_name(name) is True, name + ", index " + str(true_names.index(name))


test_variable_name()
