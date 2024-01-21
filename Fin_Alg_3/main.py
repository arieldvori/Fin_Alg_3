def weighted_round_robin(rights: list[float], valuations: list[list[float]], y: float):
    """
    >>> weighted_round_robin([1, 2, 4],[[11, 11, 22, 33, 44],[11, 22, 44, 55, 66],[11, 33, 22, 11, 66]],0.5) # diff items diff rights
    player 2 takes item 4 with value 66
    player 1 takes item 3 with value 55
    player 2 takes item 1 with value 33
    player 0 takes item 2 with value 22
    player 2 takes item 0 with value 11
    >>> weighted_round_robin([1, 1, 1],[[11, 11, 11, 11],[22, 22, 22, 22],[33, 33, 33, 33]],0.5) #same items same rights
    player 0 takes item 0 with value 11
    player 1 takes item 1 with value 22
    player 2 takes item 2 with value 33
    player 0 takes item 3 with value 11
    >>> weighted_round_robin([1, 1, 1],[[11, 11, 22, 33],[11, 22, 44, 55],[11, 33, 22, 11]],0.5) #diff items same rights
    player 0 takes item 3 with value 33
    player 1 takes item 2 with value 44
    player 2 takes item 1 with value 33
    player 0 takes item 0 with value 11
    >>> weighted_round_robin([1, 2, 4],[[11, 11, 11, 11],[22, 22, 22, 22],[33, 33, 33, 33]],0.5) #same items diff rights
    player 2 takes item 0 with value 33
    player 1 takes item 1 with value 22
    player 2 takes item 2 with value 33
    player 0 takes item 3 with value 11
    """
    items = len(valuations[0])
    items_list = [1] * items  # create a list for indication if the item is taken
    fair_rights = [1] * len(rights)  # create a list to save the calculation of who needs to choose the next item
    curr_items = [0] * len(rights)  # create a list to save how many items each player have

    while items > 0:  # when there is still items to choose from
        for i in range(0, len(rights)):  # run over the players
            fair_rights[i] = rights[i] / (curr_items[i] + y)  # calculate the rights according to the formula
        max_right = max(fair_rights)  # save the right of the player which have the max right
        max_index = fair_rights.index(max_right)  # index of the player with the max right to choose next
        for j in range(0, len(valuations[0])):  # run over the items
            max_desire = max(valuations[max_index])  # get the desired value of the player who needs to choose
            max_d_item = valuations[max_index].index(max_desire)  # get the desired index of the player who needs to
            # choose
            if items_list[max_d_item] == 1:  # if item is still available
                curr_items[max_index] += 1  # add 1 to the items count of this player
                items_list[max_d_item] = 0  # make the item not available
                print(f"player {max_index} takes item {max_d_item} "
                      f"with value {valuations[max_index][max_d_item]} ")
                break  # to  calculate the proper right again
            else:
                valuations[max_index][max_d_item] = 0
        items -= 1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
