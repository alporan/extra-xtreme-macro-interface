import time


def main(t):
    ts = time.gmtime()
    print(time.strftime("%Y-%m-%d %H.%M.%S", ts))
    txt_name = "Q:\\Users\\a_oran\Desktop\\TSO Browse - " + time.strftime("%Y-%m-%d %H.%M.%S", ts) + ".txt"
    dot_line = ".  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  ."
    end_msg = "******** Bottom of Data ****************"
    f = open(txt_name, "w+")
    screen_output = t.tso_entry("<GETSCREEN>")
    screen_lines = screen_output.split('\n')
    if dot_line in screen_lines[0]:
        skip_line = 5
    else:
        skip_line = 4
    for i in range(skip_line, len(screen_lines)):
        f.write(screen_lines[i])
        f.write("\n")
    while end_msg not in screen_output:
        screen_output = t.tso_entry("DOWN 27")
        screen_lines = screen_output.split('\n')
        for i in range(skip_line, len(screen_lines)):
            if dot_line not in screen_lines[i]:
                f.write(screen_lines[i])
                f.write("\n")
