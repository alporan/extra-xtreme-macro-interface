import time


def main(t):
    ts = time.gmtime()
    print(time.strftime("%Y-%m-%d %H.%M.%S", ts))
    txt_name = "Q:\\Users\\a_oran\Desktop\\TRACE - " + time.strftime("%Y-%m-%d %H.%M.%S", ts) + ".txt"
    f = open(txt_name, "w+")
    f.write("\n***************************************\n")
    t.troya_entry("<CLEAR>")
    while "TRACE -- ENTER MESSAGE TO TRACE" not in t.troya_entry("<GETSCREEN>") or \
            "INVALID ACTION CODE" not in t.troya_entry("<GETSCREEN>"):
        time.sleep(.02)
        t.troya_entry("<CLEAR>")
        screen_output = t.troya_entry2("<ENTER>")
        screen_lines = screen_output.split('\n')
        for i in range(0, len(screen_lines)):
            if not screen_lines[i].isspace():
                f.write(screen_lines[i])
                f.write("\n")
        if "SE-" in t.troya_entry("<GETSCREEN>"):
            break
