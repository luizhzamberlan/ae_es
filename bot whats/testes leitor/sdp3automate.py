import pyautogui
import clipboard
import mysql.connector
from time import sleep

def pesquisa_falha(system, module_number, fault_code):

    #DataBase Connect
    db = mysql.connector.connect(
        host = "localhost",
        user = "user",
        password = "senha")

    #lista para verificar se a falha pertence ao modulo e se o modulo pertence ao sistema
    

        
    pyautogui.hotkey('alt', 'tab')
    pyautogui.moveTo(637, 211)
    sleep(2)

    pyautogui.click(clicks=2)
    sleep(2)

    pyautogui.press('home')
    pyautogui.press('tab')
    pyautogui.press('home')


    match system:
        case 'ACS':
            match module_number:
                case '1785570':
                    pass
                case '1799955':
                    pyautogui.press('down')
                case '1849869':
                    for i in range(3):
                        pyautogui.press('down')
                case '1849871':
                    for i in range(4):
                        pyautogui.press('down')
                case '1878338':
                    for i in range(5):
                        pyautogui.press('down')
                case '1888382':
                    for i in range(6):
                        pyautogui.press('down')
                case '1902759':
                    for i in range(7):
                        pyautogui.press('down')
                case '1906040':
                    for i in range(8):
                        pyautogui.press('down')
                case '2010059':
                    for i in range(9):
                        pyautogui.press('down')
                case '2020682':
                    for i in range(10):
                        pyautogui.press('down')
                case '2054675':
                    for i in range(11):
                        pyautogui.press('down')
                case '2083206':
                    for i in range(12):
                        pyautogui.press('down')
                case '2083814':
                    for i in range(13):
                        pyautogui.press('down')
                case '2110665':
                    for i in range(14):
                        pyautogui.press('down')
                case '2294321':
                    for i in range(15):
                        pyautogui.press('down')
                case '2324708':
                    for i in range(16):
                        pyautogui.press('down')
                case '2392626':
                    for i in range(17):
                        pyautogui.press('down')
                case '2569763':
                    for i in range(18):
                        pyautogui.press('down')
                case '2582161':
                    for i in range(19):
                        pyautogui.press('down')
                case '2899938':
                    for i in range(20):
                        pyautogui.press('down')
                case '2899939':
                    for i in range(21):
                        pyautogui.press('down')
                case '2924832':
                    for i in range(22):
                        pyautogui.press('down')
                case '2949598':
                    for i in range(23):
                        pyautogui.press('down')
                case '2949603':
                    for i in range(24):
                        pyautogui.press('down')
                case '2949630':
                    for i in range(25):
                        pyautogui.press('down')
                case '3041326':
                    for i in range(26):
                        pyautogui.press('down')
                case _:
                    print('módulo n encontrado')
                    #Módulo não encontrado

        # case 'AHS':
            
        # case 'ALM':
            
        # case 'APS':
            
        # case 'AUS':
            
        # case 'AUTONOMOUS VEHICLE SYSTEM':
            
        # case 'AWD':
            
        # case 'AXI':
            
        # case 'BCS':
            
        # case 'BDC':
            
        # case 'BMS':
            
        # case 'BWE':
            
        # case 'BWS':
            
        # case 'CCC':
            
        # case 'CCS':
            
        # case 'CMD':
            
        # case 'COO':
            
        # case 'CTS':
            
        # case 'CUI':
            
        # case 'DAS':
            
        # case 'DCC':
            
        # case 'DCS':
            
        # case 'DIS':
            
        # case 'EACS':
            
        # case 'ELETRIC VEHICLE CONTROL SYSTEM':
            
        # case 'EEC':
            
        # case 'EHS':
            
        # case 'EMS':
            
        # case 'EQU':
            
        # case 'FLC':
            
        # case 'FSC':
            
        # case 'FSS':
            
        # case 'GMS':
            
        # case 'HLC':
            
        # case 'ICL':
            
        # case 'INL':
            
        # case 'LAS':
            
        # case 'LDW':
            
        # case 'MBS':
            
        # case 'MGS':
            
        # case 'PBC':
            
        # case 'RES':
            
        # case 'RTC':
            
        # case 'RTI':
            
        # case 'SMS':
            
        # case 'SRC':
            
        # case 'SRR':
            
        # case 'TCC':
            
        # case 'TCO':
            
        # case 'TPM':
            
        # case 'TSA':
            
        # case 'TSS':
            
        # case 'VIS':
            
        # case _:
        #     #System not found
        #     pass

    sleep(1)
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

    sleep(1)
    pyautogui.write(fault_code)

    sleep(1)
    pyautogui.moveTo(829,329)

    sleep(1)
    pyautogui.click()

    sleep(1)
    pyautogui.moveTo(867, 709)

    sleep(1)
    pyautogui.click(clicks=2)

    sleep(1)
    pyautogui.hotkey('ctrl'+'a')
    pyautogui.hotkey('ctrl'+'c')
    fault_text = clipboard.paste
    print(fault_text)


pesquisa_falha('ASC', '1785570', '1')
