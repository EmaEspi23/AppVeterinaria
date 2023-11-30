import time
import os
import datetime as dt


def registroPaciente(
    nombre, sexo, edad, especie, rasgos, enfermedad, dueño, contacto, pacientes
):
    if len(pacientes) > 0:
        nroPaciente = list(pacientes.keys())
        ultimoNro = nroPaciente[len(nroPaciente) - 1]
        idPaciente = ultimoNro + 1
    else:
        idPaciente = 1

    fechaAlta = dt.datetime.now()
    formatoFecha = fechaAlta.strftime(
        "%d / %m / %Y - %H : %M"
    )
    pacientes[idPaciente] = {
        "fechaAlta": formatoFecha,
        "nombre": nombre,
        "sexo": sexo,
        "edad": edad,
        "especie": especie,
        "rasgos": rasgos,
        "enfermedad": enfermedad,
        "dueño": dueño,
        "contacto": contacto,
    }


def verRegistros(pacientes):
    if len(pacientes) > 0:
        for idPaciente, paciente in pacientes.items():
            print(
                f"""            
                --- Nro Paciente: {idPaciente} ---
                
                Fecha de Alta: {paciente["fechaAlta"]}
                Nombre: {paciente["nombre"]}
                Sexo: {paciente["sexo"]}
                Edad: {paciente["edad"]}
                Especie: {paciente["especie"]}
                Rasgos: {paciente["rasgos"]}
                Enfermedad: {paciente["enfermedad"]}
                Dueño: {paciente["dueño"]}
                Contacto: {paciente["contacto"]}
                  """
            )
    else:
        print("*" * 30)
        print(" ", "No hay Pacientes Registrados")
        print("*" * 30)


def modificarPaciente(pacientes, nroModificar, caractModificar, valorActualizar):
    pacientes[nroModificar][caractModificar] = valorActualizar
    print("¡El Paciente se modifico con Exito!")
    print("")
    tiempoClear()


def eliminarPaciente(pacientes, nroEliminar):
    if nroEliminar in pacientes.keys():
        pacientes.pop(nroEliminar)
        print("\n¡El Paciente se elimino con Exito!")
        print("")
        tiempoClear()


def tiempoClear():
    time.sleep(3)
    os.system("cls")
