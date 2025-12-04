def on_on_chat():
    agent.teleport_to_player()
    agent.set_item(GLASS, 64, 1)
    agent.set_slot(1)
    for index in range(4):
        for index2 in range(4):
            for index3 in range(6):
                agent.move(FORWARD, 1)
                agent.place(DOWN)
            agent.turn(LEFT_TURN)
        agent.move(UP, 1)
    agent.set_item(OAK_WOOD_SLAB, 64, 2)
    agent.set_slot(2)
    index4 = 0
    while index4 < 4:
        index5 = 0
        while index5 < 6:
            agent.move(FORWARD, 1)
            agent.place(DOWN)
            index5 += 1
        agent.turn(LEFT_TURN)
        index4 += 1
    agent.move(FORWARD, 1)
    agent.move(LEFT, 1)
    index6 = 0
    while index6 < 4:
        index7 = 0
        while index7 < 4:
            agent.move(FORWARD, 1)
            agent.place(DOWN)
            index7 += 1
        agent.turn(LEFT_TURN)
        index6 += 1
    agent.move(FORWARD, 1)
    agent.move(LEFT, 1)
    index8 = 0
    while index8 < 4:
        index9 = 0
        while index9 < 2:
            agent.move(FORWARD, 1)
            agent.place(DOWN)
            index9 += 1
        agent.turn(LEFT_TURN)
        index8 += 1
    agent.set_item(SHROOMLIGHT, 64, 3)
    agent.set_slot(3)
    agent.move(FORWARD, 1)
    agent.move(LEFT, 1)
    agent.place(DOWN)
    agent.move(RIGHT, 4)
    agent.move(DOWN, 4)
    agent.turn(LEFT_TURN)
    agent.destroy(FORWARD)
    agent.move(FORWARD, 1)
    agent.destroy(DOWN)
    agent.move(DOWN, 3)
    agent.set_item(DARK_OAK_DOOR, 1, 4)
    agent.set_slot(1)
    agent.place(UP)
    agent.move(BACK, 1)
    agent.move(UP, 2)
    agent.set_slot(4)
    agent.place(FORWARD)
    agent.move(DOWN, 2)
    agent.set_slot(1)
    agent.turn(RIGHT_TURN)
    agent.move(LEFT, 1)
    agent.move(BACK, 3)
    index4 = 0
    while index4 < 4:
        index5 = 0
        while index5 < 6:
            agent.move(FORWARD, 1)
            agent.place(UP)
            index5 += 1
        agent.turn(LEFT_TURN)
        index4 += 1
    agent.move(FORWARD, 1)
    agent.move(LEFT, 1)
    index6 = 0
    while index6 < 4:
        index7 = 0
        while index7 < 4:
            agent.move(FORWARD, 1)
            agent.place(UP)
            index7 += 1
        agent.turn(LEFT_TURN)
        index6 += 1
    agent.move(FORWARD, 1)
    agent.move(LEFT, 1)
    index8 = 0
    while index8 < 4:
        index9 = 0
        while index9 < 2:
            agent.move(FORWARD, 1)
            agent.place(UP)
            index9 += 1
        agent.turn(LEFT_TURN)
        index8 += 1
    agent.move(FORWARD, 1)
    agent.move(LEFT, 1)
    agent.place(UP)
player.on_chat("dom", on_on_chat)
