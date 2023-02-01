def add_to_list(i: int, i_list: list = []) -> list:
    i_list.append(i)
    return i_list


print(add_to_list(1))
print(add_to_list(2))
print(add_to_list(3))


def add_to_list_2(i: int, i_list: list | None = None) -> list:
    if i_list is None:
        i_list = []
    i_list.append(i)
    return i_list


print(add_to_list_2(1))
print(add_to_list_2(2))
print(add_to_list_2(3))
