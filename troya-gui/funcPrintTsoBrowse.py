import time


def main(t):
    ts = time.gmtime()
    print(time.strftime("%Y-%m-%d %H.%M.%S", ts))
    txt_name = "Q:\\Users\\a_oran\Desktop\\TSO Browse - " + time.strftime("%Y-%m-%d %H.%M.%S", ts) + ".txt"
    f = open(txt_name, "w+")
    screen_output = t.tso_entry("<GETSCREEN>")
    screen_lines = screen_output.split('\n')
    for i in range(5, len(screen_lines)):
            if not screen_lines[i].isspace():
                f.write(screen_lines[i])
                f.write("\n")
    while "******************************** Bottom of Data ********************************" not in screen_output:
        screen_output = t.tso_entry("DOWN 27")
        screen_lines = screen_output.split('\n')
        for i in range(5, len(screen_lines)):
                if not screen_lines[i].isspace():
                    f.write(screen_lines[i])
                    f.write("\n")
