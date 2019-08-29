import win32com.client


class TerminalConnector:

    def __init__(self):
        self.SYSTEM = "UNKNOWN"                                     # Set initial status
        self.System = win32com.client.Dispatch("EXTRA.System")      # Get Attachmate Extra Object
        self.timeout = 10000
        self.counter = 0

    def get_session_count(self):
        try:
            if self.System.Sessions.count == 0:
                print("NO ACTIVE SESSION.")                         # No active session is present
                return 0
            return self.System.Sessions.count                       # Return session count
        except Exception:
            print("UNABLE TO DETECT SESSIONS.")                     # Error during session count
            return 0

    def get_session_list(self):
        session_count = self.get_session_count()
        index = 1
        session_list = []
        while index <= session_count:
            session_list.append(str(self.System.Sessions(index)))
            index += 1
        return session_list

    def connect_session(self, sessionName):
        global active_session
        index = 1
        # print("AVAILABLE SESSIONS: ")
        while index <= self.get_session_count():
            # print(self.System.Sessions(index))
            if str(self.System.Sessions(index)) == sessionName:
                active_session = self.System.Sessions(index)
                # print("ACTIVE SESSION CHANGED TO ===> " + str(active_session))
                return True
                break
            index += 1
        return False                                                # Requested session is not found

    def get_screen_troya(self):
        self.response = active_session.screen.GetStringEx(0, 0, 24, 80, 120, 0, 0, 0)
        self.response = self.response[:1920]
        self.response = '\n'.join(self.response[i:i + 80] for i in range(0, len(self.response), 80))
        # self.response = self.response.rstrip()
        # self.response = self.response.lstrip()
        return self.response

    def get_screen_troya2(self):
        self.response = active_session.screen.GetStringEx(0, 0, 20, 80, 120, 0, 0, 0)
        self.response = self.response[:1600]
        self.response = '\n'.join(self.response[i:i + 80] for i in range(0, len(self.response), 80))
        return self.response

    def get_screen_tso(self):
        self.response = active_session.screen.GetStringEx(0, 0, 32, 80, 120, 0, 0, 0)
        self.response = self.response[:2560]
        self.response = '\n'.join(self.response[i:i + 80] for i in range(0, len(self.response), 80))
        return self.response

    def troya_entry(self,data):

        if "<GETSCREEN>" in data:
            pass
        elif "<CLEAR>" in data:
            active_session.Screen.Sendkeys("<CLEAR>")
        elif "<ENTER>" in data:
            active_session.Screen.Sendkeys(str(data))
        elif "<TAB>" in data:
            active_session.Screen.Sendkeys(str(data))
        else:
            active_session.Screen.Sendkeys(str(data) + "<ENTER>")

        while active_session.Screen.OIA.XStatus != 0:                   # TROYA CEVAP SURESINDE BEKLEMESI ICIN EKLENDI.
            self.counter += 1
            if self.counter > self.timeout:
                print("ekrandan data alınamadı")
                pass
        response = self.get_screen_troya()
        return response

    def troya_entry2(self,data):

        if "<GETSCREEN>" in data:
            pass
        elif "<CLEAR>" in data:
            active_session.Screen.Sendkeys("<CLEAR>")
        elif "<ENTER>" in data:
            active_session.Screen.Sendkeys(str(data))
        elif "<TAB>" in data:
            active_session.Screen.Sendkeys(str(data))
        else:
            active_session.Screen.Sendkeys(str(data) + "<ENTER>")

        while active_session.Screen.OIA.XStatus != 0:                   # TROYA CEVAP SURESINDE BEKLEMESI ICIN EKLENDI.
            self.counter += 1
            if self.counter > self.timeout:
                print("ekrandan data alınamadı")
                pass
        response = self.get_screen_troya2()
        return response

    def tso_entry(self,data):

        if "<GETSCREEN>" in data:
            pass
        elif "<ENTER>" in data:
            active_session.Screen.Sendkeys(str(data))
        elif "<TAB>" in data:
            active_session.Screen.Sendkeys(str(data))
        else:
            active_session.Screen.Sendkeys(str(data) + "<ENTER>")

        while active_session.Screen.OIA.XStatus != 0:                   # TROYA CEVAP SURESINDE BEKLEMESI ICIN EKLENDI.
            self.counter += 1
            if self.counter > self.timeout:
                print("ekrandan data alınamadı")
                pass
        response = self.get_screen_tso()
        return response