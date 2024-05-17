import pyautogui
import clipboard
import db_connector
from time import sleep
from datetime import datetime

def pesquisa_falha(system, module_number, fault_code):

    log = open('log_failure.txt', 'a')
    time = datetime.now()

    sleep(3)

    verify_info = db_connector.search_fault(system, module_number, fault_code)
    if verify_info[0] == False:
        return 'Erro 500, entre em contato com o suporte'
    elif verify_info[1] == False:
        return 'System Error'
    elif verify_info[0] == True and verify_info[1] == False:
        return 'Module Error'
    elif verify_info[0] == True and verify_info[1] == True and verify_info[2] == False:
        return 'Fault Code Error'
    else:
        #Janela do SDP3
        pyautogui.hotkey('alt', 'tab')
        pyautogui.moveTo(637, 211)
        sleep(2)

        #Ajustando indicador na formulário
        pyautogui.click()
        sleep(1)
        pyautogui.click()
        sleep(2)
        pyautogui.press('home')
        sleep(2)



        match system:
            case 'ACS':
                pyautogui.press('tab')
                pyautogui.press('home')

                match module_number:
                    case '1785570':
                        pyautogui.press('tab')
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

            case 'AHS':
                match module_number:
                    case '1444640':
                        pyautogui.press('tab')
                    case '1501010':
                        for i in range(1):
                            pyautogui.press('down')
                    case '1512838':
                        for i in range(2):
                            pyautogui.press('down')
                    case '1544847':
                        for i in range(3):
                            pyautogui.press('down')
                    case '1544849':
                        for i in range(4):
                            pyautogui.press('down')
                    case '1545298':
                        for i in range(5):
                            pyautogui.press('down')
                    case '1722532':
                        for i in range(6):
                            pyautogui.press('down')
                    case '1724823':
                        for i in range(7):
                            pyautogui.press('down')
                    case '1724824':
                        for i in range(8):
                            pyautogui.press('down')
                    case '1728267':
                        for i in range(9):
                            pyautogui.press('down')
                    case '1728268':
                        for i in range(10):
                            pyautogui.press('down')
                    case '1768751':
                        for i in range(11):
                            pyautogui.press('down')
                    case '1851021':
                        for i in range(12):
                            pyautogui.press('down')
                    case '1851022':
                        for i in range(13):
                            pyautogui.press('down')
                    case '1857080':
                        for i in range(14):
                            pyautogui.press('down')
                    case '2160812':
                        for i in range(15):
                            pyautogui.press('down')
                    case '2197277':
                        for i in range(16):
                            pyautogui.press('down')
                    case '2197577':
                        for i in range(17):
                            pyautogui.press('down')
                    case '2288681':
                        for i in range(18):
                            pyautogui.press('down')
                    case '2488908':
                        for i in range(19):
                            pyautogui.press('down')
                    case '2607360':
                        for i in range(20):
                            pyautogui.press('down')
                    case '2607361':
                        for i in range(21):
                            pyautogui.press('down')
                    case '2640293':
                        for i in range(22):
                            pyautogui.press('down')
                    case '2640298':
                        for i in range(23):
                            pyautogui.press('down')
                    case '2724764':
                        for i in range(24):
                            pyautogui.press('down')
                    case '2735536':
                        for i in range(25):
                            pyautogui.press('down')
                    case '3034223':
                        for i in range(26):
                            pyautogui.press('down')
                    case '3034225':
                        for i in range(27):
                            pyautogui.press('down')
                
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


        #Formulário de pesquisa de falha por código
        sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        sleep(1)
        pyautogui.write(fault_code)

        #Click na primeira falha correspondente
        sleep(1)
        pyautogui.moveTo(829,329)
        sleep(1)
        pyautogui.click()
        sleep(1)

        #Texto da falha
        pyautogui.moveTo(547, 591)
        sleep(1)
        pyautogui.click()
        pyautogui.click()
        sleep(2)

        #Seleção e cópia do Texto
        pyautogui.keyDown('ctrl')
        sleep(1)
        pyautogui.press('a')
        sleep(1)
        pyautogui.press('c')
        sleep(1)
        pyautogui.keyUp('ctrl')
        sleep(1)

        #Armazenagem do Texto da Falha
        fault_text = clipboard.paste()
        log.write(f'{time}: Fault Text[V]'+ '\n')

        #Armazenar texto da falha no banco de dados
        db_fault_text = db_connector.arm_fault(system, module_number, fault_code, fault_text)



        return fault_text
