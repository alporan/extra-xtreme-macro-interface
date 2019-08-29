import time


def main(t):
    ts = time.gmtime()
    print(time.strftime("%Y-%m-%d %H.%M.%S", ts))
    txt_name = "Q:\\Users\\a_oran\Desktop\\TROYA SCREEN - " + time.strftime("%Y-%m-%d %H.%M.%S", ts) + ".txt"
    f = open(txt_name, "w+")
    screen_output = t.troya_entry2("<GETSCREEN>")
    screen_lines = screen_output.split('\n')
    for i in range(0, len(screen_lines)-1):
            if not screen_lines[i].isspace():
                f.write(screen_lines[i])
                f.write("\n")
    while "|                                                         " in screen_output:
        screen_output = t.troya_entry2("MDR")
        screen_lines = screen_output.split('\n')
        for i in range(0, len(screen_lines)-1):
                if not screen_lines[i].isspace():
                    f.write(screen_lines[i])
                    f.write("\n")