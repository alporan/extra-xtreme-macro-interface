import time


def main(t):
    ts = time.gmtime()
    print(time.strftime("%Y-%m-%d %H.%M.%S", ts))
    txt_name = "Q:\\Users\\a_oran\Desktop\\TSO TorDump - " + time.strftime("%Y-%m-%d %H.%M.%S", ts) + ".txt"
    dot_line = ".  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  ."
    end_msg = "LINE 1,188"
    skip_column = 27
    f = open(txt_name, "w+")
########################################################################
# LEFT COLUMN                                                          #
########################################################################
    index_x = -1
    matrix = []
    screen_output = t.tso_entry("<GETSCREEN>")
    screen_lines = screen_output.split('\n')
    if dot_line in screen_lines[0]:
        skip_line = 5
    else:
        skip_line = 4
    for i in range(skip_line, len(screen_lines)):
        if dot_line not in screen_lines[i]:
            matrix.append([])
            index_x += 1
            for j in range(0, len(screen_lines[i])):
                matrix[index_x].append(screen_lines[i][j])
    while end_msg not in screen_output:
        screen_output = t.tso_entry("DOWN 27")
        screen_lines = screen_output.split('\n')
        for i in range(skip_line, len(screen_lines)):
            if dot_line not in screen_lines[i]:
                matrix.append([])
                index_x += 1
                for j in range(0, len(screen_lines[i])):
                    matrix[index_x].append(screen_lines[i][j])
########################################################################
#  RIGHT COLUMN                                                        #
########################################################################
    index_x = -1
    t.tso_entry("TOP")
    screen_output = t.tso_entry("RIGHT")
    screen_lines = screen_output.split('\n')
    for i in range(skip_line, len(screen_lines)):
        if dot_line not in screen_lines[i]:
            index_x += 1
            for j in range(skip_column, len(screen_lines[i])):
                matrix[index_x].append(screen_lines[i][j])
    while end_msg not in screen_output:
        screen_output = t.tso_entry("DOWN 27")
        screen_lines = screen_output.split('\n')
        for i in range(skip_line, len(screen_lines)):
            if dot_line not in screen_lines[i]:
                index_x += 1
                for j in range(skip_column, len(screen_lines[i])):
                    matrix[index_x].append(screen_lines[i][j])
########################################################################
#  PRINT TO FILE                                                       #
########################################################################
    for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                f.write(matrix[i][j])
            f.write("\n")
