import mysql.connector
from mysql.connector.errors import Error
from datetime import datetime



def search_fault(system, module_number, fault_code):
    
    #log de erros
    log = open('log_failure.txt', 'a')
    time = datetime.now()



    #Verifica Conexão com Servidor
    try:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "user",
        password = "senha",
        database = "fault_code"
        )

        connection_status = f'{time}: {mydb}'
        connection_status = repr(connection_status)
        log.write(connection_status + '\n')
        connection_bool = True

    except mysql.connector.Error as err:
        connection_status = f'{time}: Connection Error: {err}'
        connection_status = repr(connection_status)
        log.write(connection_status + '\n')
        log.close
        connection_bool = False
        retorno = [connection_bool, connection_status]

        return retorno
    

    cursor = mydb.cursor()




    #Verifica se o Sistema foi digitado corretamente
    try:
        sys_search = f'SELECT * FROM SYSTEMS WHERE name_system="{system}"'

        cursor.execute(sys_search)
        db_result_sys = cursor.fetchone()
        if type(db_result_sys) == type(None):
           sys_status = f'{time}: System [X]: Not found'
           sys_status = repr(sys_status)
           log.write(sys_status + '\n')

           sys_bool = False
        else:
           sys_status = f'{time}: System [V]'
           sys_status = repr(sys_status)
           log.write(sys_status + '\n')

           sys_bool = True

        mydb.commit()

    except:
        sys_status = f'{time}: System [X]'
        sys_status = repr(sys_status)
        log.write(sys_status + '\n')

        sys_bool = False



    #Verifica se o Modulo da falha foi digitado corretamente
    try:
        module_search = f'SELECT * FROM MODULOS_{system} WHERE modulo_number="{module_number}"'
    
        cursor.execute(module_search)
        db_result_module = cursor.fetchone()
        if type(db_result_module) == type(None):
            module_status = f'{time}: Module [X]: Not found'
            module_status = repr(module_status)
            log.write(module_status + '\n')

            module_bool = False
        else:    
            module_status = f'{time}: Module [V]'
            module_status = repr(module_status)
            log.write(module_status + '\n')

            module_bool = True
        
        mydb.commit()
    except:
        module_status = f'{time}: Module [X]'
        module_status = repr(module_status)
        log.write(module_status + '\n')

        module_bool = False
    


    #Verifica se o código de falha foi digitado corretamente
    try:
        fault_search = f'SELECT * FROM FAULTS_{system} WHERE fault="{fault_code}" AND modulo_id="{db_result_module[0]}"'

        cursor.execute(fault_search)
        db_result_fault = cursor.fetchone()
        if type(db_result_fault) == type(None):
            fault_status = f'{time}: Fault Code [X]: Not found'
            fault_status = repr(fault_status)
            log.write(fault_status + '\n')

            fault_bool = False
        else:
            fault_status = f'{time}: Fault Code [V]'
            fault_status = repr(fault_status)
            log.write(fault_status + '\n')

            fault_bool = True
        
        mydb.commit()
    except:
        fault_status = f'{time}: Fault Code [X]'
        fault_status = repr(fault_status)
        log.write(fault_status + '\n')

        fault_bool = False
    
    retorno = [connection_bool, sys_bool, module_bool, fault_bool]
    
    return retorno

def arm_fault(system, module_number, fault_code, fault_text):
     
    #log de erros
    log = open('log_failure.txt', 'a')
    time = datetime.now()




    #Verifica Conexão com Servidor
    try:
        mydb = mysql.connector.connect(
        host = "localhost",
        user = "user",
        password = "senha",
        database = "fault_code"
        )

        log.write(f'{time}: {mydb}' + '\n')
        connection_bool = True

    except mysql.connector.Error as err:
        log.write(f'{time}: Connection Error: {err}' + '\n')
        log.close
        connection_bool = False

        return connection_bool
    

    cursor = mydb.cursor()
    
    #Get modulo_id
    search_modulo_id = f'SELECT * from modulos_{system} WHERE modulo_number="{module_number}"'
    modulo = []
   
    cursor.execute(search_modulo_id)
    result = cursor.fetchone()
    for i in result:
        modulo.append(i)
    
    fault_text_verf = f'SELECT * from FAULTS_{system} WHERE fault="{fault_code}" AND modulo_id="{modulo[0]}"'
    cursor.execute(fault_text_verf)
    verf = cursor.fetchone()

    #Verify if fault_text already exist
    if type(verf[1]) == type(None):
        
        log.write(f'{time}: Fault Text Register Complete [V]'+'\n')

        #Write the fault_text in the DataBase
        db_arm_text = f'UPDATE FAULTS_{system} SET fault_text="{fault_text}" WHERE fault="{fault_code}" AND modulo_id="{modulo[0]}"'

        cursor.execute(db_arm_text)
        result = cursor.fetchone()
        mydb.commit()

        log.close
        mydb.close()

    else:
        log.write(f'{time}: Fault Text Already Registered [V]'+'\n')
        log.close
