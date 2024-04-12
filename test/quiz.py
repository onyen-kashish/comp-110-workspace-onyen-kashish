def find_even(words: list[str]) -> str:
    idx: int = 0
    while idx < len(words):
        if len(words[idx]) % 2 == 0:
            return words[idx]
        idx += 1

    return ""


def remove_first_even(words: list[str]) -> None:
    idx: int = 0
    condition: bool = True
    while (idx < len(words)) and condition:
        if len(words[idx]) % 2 == 0:
            words.pop(idx)
            condition = False
        idx += 1


# def remove_first_even_and_send_back(words: list[str]) -> list[str]:
#     idx: int = 0
#     condition: bool = True
#     while (idx < len(words)) and condition:
#         if len(words[idx]) % 2 == 0:
#             words.pop(idx)
#             condition = False
#         idx += 1
#
#     return words


def plus_or_minus_n(inp: dict[str,int], n: int) -> None:
    updated_inp: dict[str,int] = []
    for key in inp:
        if(inp(key) % 2 == 0):
            inp(key) + n
        else:
            inp(key) - n