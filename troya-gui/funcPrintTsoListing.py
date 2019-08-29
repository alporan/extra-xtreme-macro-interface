import time


def main(t):
    ts = time.gmtime()
    print(time.strftime("%Y-%m-%d %H.%M.%S", ts))
    txt_name = "Q:\\Users\\a_oran\Desktop\\TSO Listing - " + time.strftime("%Y-%m-%d %H.%M.%S", ts) + ".txt"
    f = open(txt_name, "w+")
    index_x = -1
    matrix = []
    screen_output = t.tso_entry("<GETSCREEN>")
    screen_lines = screen_output.split('\n')
    for i in range(4, len(screen_lines)-1):
        matrix.append([])
        index_x += 1
        for j in range(0, len(screen_lines[i])):
            matrix[index_x].append(screen_lines[i][j])
    while "    Relocation Dictionary   " not in screen_output:
        screen_output = t.tso_entry("DOWN 27")
        screen_lines = screen_output.split('\n')
        for i in range(4, len(screen_lines)-1):
            matrix.append([])
            index_x += 1
            for j in range(0, len(screen_lines[i])):
                matrix[index_x].append(screen_lines[i][j])

    index_x = -1
    screen_output = t.tso_entry("TOP")
    screen_output = t.tso_entry("RIGHT")
    screen_lines = screen_output.split('\n')
    for i in range(4, len(screen_lines)-1):
        index_x += 1
        for j in range(38, len(screen_lines[i])):
            matrix[index_x].append(screen_lines[i][j])
    while "    Relocation Dictionary   " not in screen_output:
        screen_output = t.tso_entry("DOWN 27")
        screen_lines = screen_output.split('\n')
        for i in range(4, len(screen_lines)-1):
            index_x += 1
            for j in range(38, len(screen_lines[i])):
                matrix[index_x].append(screen_lines[i][j])

    for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                f.write(matrix[i][j])
            f.write("\n")
