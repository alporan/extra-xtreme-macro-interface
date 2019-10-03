from PyQt5 import QtGui


def main(terminal, mainGui):
    if len(mainGui.lineEdit.text()) == 6:
        terminal.troya_entry("<CLEAR>")
        durf_no = mainGui.lineEdit.text()
        entry = 'NEGO/////////' + durf_no
        screen_output = terminal.troya_entry(entry)
        result = screen_output.find("DURF:" + durf_no)
        print("***********************")
        print("DURF  : " + durf_no)
        if result != -1:
            result = screen_output.find("NEGO SPACE FLT(S) FOR")
            if result != -1:
                durf_date = screen_output[result + 22:result + 29]
                print("DATE  : " + durf_date)
                result = screen_output.find("-TK")
                if result != -1:
                    durf_flight = screen_output[result + 3:result + 7]
                    durf_gds = screen_output[result + 162:result + 164]
                    print("FLIGHT: TK" + durf_flight)
                    print("GDS   : " + durf_gds)
                    entry = "Nego/DG" + durf_gds + "-" + durf_flight
                    terminal.troya_entry("<CLEAR>")
                    screen_output = terminal.troya_entry(entry)
                    result = screen_output.find(durf_date)
                    result_count = result
                    ZSCRL_count = 0
                    while True:
                        if result != -1:
                            durf_line_no = int(screen_output[result - 17:result - 13])
                            entry2 = "Nego/DG" + durf_gds + "/" + str(durf_line_no)
                            terminal.troya_entry("<CLEAR>")
                            screen_output2 = terminal.troya_entry(entry2)
                            result2 = screen_output2.find("DURF: " + durf_no)
                            terminal.troya_entry("<CLEAR>")
                            terminal.troya_entry(entry)
                            for x in range(ZSCRL_count):
                                terminal.troya_entry("ZSCRL DOWN")
                            if result2 != -1:
                                print("NO    : " + str(durf_line_no))
                                print("OK - NEGO/XG" + durf_gds + "/" + str(durf_line_no))
                                break
                            else:
                                result = screen_output.find(durf_date, result_count + 20)
                                result_count = result
                        else:
                            if "More..." in screen_output:
                                screen_output = terminal.troya_entry("ZSCRL DOWN")
                                ZSCRL_count += 1
                                result = screen_output.find(durf_date)
                                result_count = result
                            else:
                                break
