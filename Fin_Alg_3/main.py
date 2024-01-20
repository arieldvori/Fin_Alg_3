# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def weighted_round_robin(rights: list[float], valuations: list[list[float]], y: float):
    items = len(valuations[0])
    items_list = [1] * items
    fair_rights = [1] * len(rights)
    curr_items = [0] * len(rights)
    while items > 0:
        for i in range(0, len(rights)):
            fair_rights[i] = rights[i] / (curr_items[i] + y)
        max_right = max(fair_rights)
        max_index = fair_rights.index(max_right)  # index of the player with the right to choose
        for j in range(0, len(valuations[0])):
            max_desire = max(valuations[max_index])
            max_d_item = valuations[max_index].index(max_desire)
            if items_list[max_d_item] == 1:
                curr_items[max_index] += 1
                items_list[max_d_item] = 0
                print(f"player {max_index} takes item {max_d_item} "
                      f"with value {valuations[max_index][max_d_item]} ")
                valuations[max_index][max_d_item] = 0
                break
            else:
                valuations[max_index][max_d_item] = 0
        items -= 1


rights = [1, 2, 4]
valuations = [
    [11, 11, 22, 33, 44],  # Individual A's valuations for items 1, 2, 3, 4
    [11, 22, 44, 55, 66],  # Individual B's valuations for items 1, 2, 3, 4
    [11, 33, 22, 11, 66]
]
y = 0.5

# Individual C's valuations for items 1, 2, 3, 4

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    weighted_round_robin(rights, valuations, y)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
