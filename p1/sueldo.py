def sueldoTrabajadores(horas_trab,sueldo):
    sueldo_base=sueldo*horas_trab   
    return sueldo_base


print("\033c")
trabajadores=0
acum_sueldo_neto=0
opc="S"
while opc=="S":
    nombre=input("Nombre: ")
    horas_trab=int(input("Horas trabajadas: "))
    sueldo=float(input("Sueldo por Horas trabajadas: "))
    aumento=0
    sueldo_base=sueldoTrabajadores(horas_trab,sueldo)

    if horas_trab==10:
        aumento=0.20
    elif horas_trab==15:
        aumento=0.30
    elif horas_trab==20:
        aumento=0.15
    elif horas_trab>25:
        aumento=0.08
        
    aumento_pagar=aumento*sueldo_base
    suel_neto=sueldo_base+aumento_pagar
    
    trabajadores+=1
    acum_sueldo_neto+=suel_neto
    
    print(f"El aumento es: {aumento_pagar}\n Y el sueldo neto cobrado es: {suel_neto}")
    
    opc=input("¿Desea ingresar mas trabajadores (S/N)").upper().strip()
print(f"El total de trabajadores es: {trabajadores}\nY monto total del sueldo neto cobrado es: {acum_sueldo_neto}")