from PyQt5 import QtGui
import time


def main(terminal, mainGui):
    if len(mainGui.lineEdit.text()) == 4:
        last_item_no = 0
        changed_indicator = 0
        page_count = 0
        flight_no = mainGui.lineEdit.text()
        terminal.troya_entry("<CLEAR>")
        entry1 = "NEGO/DG1S-" + flight_no
        screen_output = terminal.troya_entry(entry1)
        screen_lines = screen_output.split('\n')
        while True:
            for i in range(0, len(screen_lines)):
                time.sleep(.02)
                if "Bottom            " in screen_lines[i]:
                    return
                if "TK  " + flight_no in screen_lines[i]:
                    line_no = int(screen_lines[i][3:7])
                    if line_no >= last_item_no:
                        print(line_no)
                        entry2 = "NEGO/DG1S/" + str(line_no)
                        screen_output2 = terminal.troya_entry(entry2)
                        result = screen_output2.find("AURF: ______ DURF:")
                        terminal.troya_entry("<CLEAR>")
                        if result != -1:
                            last_item_no = line_no
                            entry3 = "NEGO/XG1S/" + str(line_no)
                            terminal.troya_entry(entry3)
                            print(entry3)
                            changed_indicator = 1
                            break
            if changed_indicator != 1:
                terminal.troya_entry("<CLEAR>")
                screen_output = terminal.troya_entry(entry1)
                if page_count != 0:
                    for x in range(0, page_count):
                        if "More...    " not in screen_output:
                            return
                        screen_output = terminal.troya_entry("ZSCRL DOWN")
                if "More...    " not in screen_output:
                    return
                screen_output = terminal.troya_entry("ZSCRL DOWN")
                screen_lines = screen_output.split('\n')
                page_count += 1
            else:
                changed_indicator = 0
                terminal.troya_entry("<CLEAR>")
                screen_output = terminal.troya_entry(entry1)
                if page_count != 0:
                    for x in range(0, page_count):
                        if "More...    " not in screen_output:
                            return
                        screen_output = terminal.troya_entry("ZSCRL DOWN")
                screen_lines = screen_output.split('\n')
