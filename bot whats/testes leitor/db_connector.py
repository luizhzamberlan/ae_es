import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "user",
    password = "senha",
    database = "fault_code"
)
print(mydb)

cursor = mydb.cursor()

def search_fault(system, module_number, fault_code):
    #Verifica se o Sistema da falha foi digitado corretamente
    db_sys_list = []
    sys_search = f'SELECT * FROM SYSTEMS WHERE name_system="{system}"'
    cursor.execute(sys_search)
    db_result = cursor.fetchall()
    for x in db_result:
        for c in x:
            db_sys_list.append(c)
    
    if db_sys_list[1] != system:
        return 'System [ ]: System not found'
    else:
        return 'System [X]'
    
    #Verifica se o Modulo da falha foi digitado corretamente
    db_module_list = []
    module_search = f'SELECT * FROM MODULOS_{system} WHERE modulo_number="{module_number}"'
    cursor.execute(module_search)
    db_result = cursor.fetchall()
    for x in db_result:
        for c in x:
            db_module_list.append(c)
    
    if db_module_list[1] != module_number:
        return 'Module Number [ ]: Module not found'
    else: 
        return 'Module Number [x]'
    


print(search_fault('ACS', 1234, 1))
