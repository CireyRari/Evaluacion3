def menu():
    print('-'*28)
    print('\t¡Bienvenid@ a Aerolineas Flash!')
    print('-'*28)
    print('[1] Compra de pasajes')
    print('[2] Ubicaciones disponibles')
    print('[3] Listado de pasajeros')
    print('[4] Buscar pasajero')
    print('[5] Re-asignar asiento')
    print('[6] Mostrar ganancias totales')
    print('[7] Salir')
    return validarNum(int,'-> Seleccione opción: ','Opción',1,7)

def validarNum(type,txt,entidad,min,max): #validaciones con numeros
    while True:
        try:
            num = type(input(txt))
            if min <= num <= max:
                break
            else: 
                print(f'ERROR ¡{entidad} incorrect@!')
        except:
            print('ERROR ¡Se esperan números!')
    return num

def validarLen(txt,large,strict): #validar lago de la informacion entrante
    while True:
        entry = input(txt)
        if strict: #si es True quiere decir que en estricto rigor el largo es de x caracteres
            if len(entry) == large:
                break
            else: 
                print(f'ERROR ¡Se necesit un largo de {large} caracteres!')
        else: #si es False quiere decir que el largo debe ser de minimo x caracteres
            if len(entry) >= large:
                break
            else:
                print(f'¡Se necesita como minimo un largo de {large} caracteres!')
    return entry

def asientos(): #reutilizar para venta de pasajes y listar los vendidos en op3
    asientosComun = []
    asientosEspacio = []
    asientosNorecli = []
    comun = ['A1','A2','A3','A4','A5','A18','B1','B2','B3','B4','B18',
             'C1','C2','C3','C4','C18','D1','D2','D3','D4','D5','D18',
             'E1','E2','E3','E4','E5','E18','F1','F2','F3','F4','F5','F18']
    espacio = ['A6','A7','A8','A9','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33'
               'B6','B7','B8','B9','B19','B20','B21','B22','B23','B24','B25','B26','B27','B28','B29','B30','B31','B32','B33'
               'C6','C7','C8','C9','C19','C20','C21','C22','C23','C24','C25','C26','C27','C28','C29','C30','C31','C32','C33'
               'D6','D7','D8','D9','D19','D20','D21','D22','D23','D24','D25','D26','D27','D28','D29','D30','D31','D32','D33'
               'E6','E7','E8','E9','E19','E20','E21','E22','E23','E24','E25','E26','E27','E28','E29','E30','E31','E32','E33'
               'F6','F7','F8','F9','F19','F20','F21','F22','F23','F24','F25','F26','F27','F28','F29','F30','F31','F32','F33']
    norecli = ['A10','A17','B10','B17','C10','C17','D10','D17','E10','E17','F10','F17']
    return asientosComun,asientosEspacio,asientosNorecli,comun,espacio,norecli

def compraPasajes(comun,espacio,norecli):
    dni = validarNum(int,'-> Ingrese su rut: ','Rut',4000000,90000000)
    buy = validarNum(int,'Pasajes disponibles: \n[1]Asiento común   -> $60.000\n[2]Espacio piernas -> $80.000\n[3]No reclina      -> $50.000\n-> Seleccione opción:','Opción',1,3)
    if buy == 1:
        print(f'Los asientos son: {comun}')
        cant_comun = validarNum(int,'-> ¿Cuántos pasajes desea comprar?: ',1,11)
        venta_comun =+ (60000*cant_comun)
    elif buy == 2:
        print(f'Los asientos son: {espacio}')
        cant_espacio = validarNum(int,'-> ¿Cuántos pasajes desea comprar?: ',1,175)
        venta_espacio =+ (80000*cant_espacio)
    else: 
        print(f'Los asientos son: {norecli}')
        cant_norecli = validarNum(int,'-> ¿Cuántos pasajes desea comprar?: ',1,12)
        venta_norecli =+ (50000*cant_norecli)
    print('¡Registro y compra realizada exitosamente!')
    print('Volviendo al menú principal...\n')
    return dni,buy,cant_comun,cant_espacio,cant_norecli,venta_comun,venta_espacio,venta_norecli

def registrarPasajero():
    pasajeros = []
    acomun,asientosEspacio,asientosNorecli,comun,espacio,norecli = compraPasajes()
    rut,buy,cant_comun,cant_espacio,cant_norecli,venta_comun,venta_espacio,venta_norecli = compraPasajes()
    pasajeros.append(asientoscomun)
    pasajeros.append()
    pasajeros.append()
    pasajeros.append()
    pasajeros.append()
    pasajeros.append()
    pasajeros.append()
    pasajeros.append()
    pasajeros.append()
    pasajeros.append()





def listarxRut(pasajeros):
    dnii = validarNum(int,'-> Ingrese su rut: ','Rut',4000000,90000000)
    no_encontrado = True
    for i in range(len(pasajeros)):
        if dnii == pasajeros [i][0]:
            print('¡Rut registrado!')
            no_encontrado = False
            break

    if no_encontrado:
        print('¡Pasajero NO registrado!')

def ventaPasajes():
    print('')
    