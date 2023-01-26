# [Python入門]例外と例外処理の基礎 atmarkit.itmedia.com
"""
# color on command line
## color
RED = "\033[31m"
ORANGE = "\033[38;2;253;126;0m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
DEEPPINK = "\033[38;2;255;20;147m"
## style
BACKGROUND = "\033[7m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
## program process status
FAIL = "\033[91m"
SUCCEED = "\033[92m"
WARNING = "\033[93m"
"""

RED = "\033[31m"
RANGE = "\033[38;2;253;126;0m"
GREEN = "\033[32m"
END = "\033[0m"

def msg_txt(txt:str, msgtype:str) -> str:
    try:
        if msgtype == "info":
            msg = f"[{GREEN}info{END}]: {txt}"
        elif msgtype == "warning":
            msg = f"[{ORANGE}WARNING{END}]: {ORANGE}{txt}{END}"
        elif msgtype == "error":
            msg = f"[{RED}ERROR{END}]: {RED}{txt}{END}"
        else:
            raise ValueError("Do NOT support this msgtype") 
    except Exception as e:
        print(e)

        


def msg_print(txt:str, msgtype:str) -> None:
    try:
        if msgtype == "info":
            print(f"[{GREEN}info{END}]: {txt}")
        elif msgtype == "warning":
            print(f"[{ORANGE}WARNING{END}]: {ORANGE}{txt}{END}")
        elif msgtype == "error":
            print(f"[{RED}ERROR{END}]: {RED}{txt}{END}")
        else:
            raise ValueError("Do NOT support this msgtype") 
    except Exception as e:
        print(e)



