def aliceWins(colors):
    alice_turn = True
    color_list = list(colors)

    while True:
        valid_move = False
        for i in range(1, len(color_list) - 1):
            if (alice_turn and color_list[i] == 'A' and color_list[i - 1] == 'A' and color_list[i + 1] == 'A') or \
               (not alice_turn and color_list[i] == 'B' and color_list[i - 1] == 'B' and color_list[i + 1] == 'B'):
                color_list.pop(i)
                valid_move = True
                alice_turn = not alice_turn
                break

        if not valid_move:
            break  

    return not alice_turn