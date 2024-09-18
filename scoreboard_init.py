def scoreboard_init():  # 只有scoreboard.txt为空时才初始化，之后自动跳过此函数
    with open('scoreboard.txt', 'w') as file:
        for idx in range(1, 16):
            file.write(f"{idx} {', '.join(map(str, [0]))}\n")
        for idx in range(1, 16):
            file.write(f"{idx} {', '.join(map(str, [0]))}\n")
        for idx in range(1, 16):
            file.write(f"{idx} {', '.join(map(str, [0]))}\n")
scoreboard_init()
