from rsc.modules import pacientesVet
import time


def app():
    pacientes = {}
    registros = 0
    registrosE = 0

    while True:
        time.sleep(1)

        print("-" * 40)
        print(" " * 7, "Veterinaria Huellitas", " " * 5)
        print("-" * 40)

        time.sleep(1)

        op = int(
            input(
                """                                                                 
            ---- Menu de Opciones ----
            
            1- Registrar paciente
            2- Ver Registros
            3- Modificar Registro
            4- Eliminar Registro
            5- Salir
            
            Elija una opción: """
            )
        )

        match op:
            case 1:
                print("")
                print(" " * 5, "*" * 29)
                print(" " * 7, "01 - Registro de Paciente")
                print(" " * 5, "*" * 29)

                print("")
                print("Completa el Formulario")
                print("")

                nombre = input("Nombre: ")
                sexo = input("Sexo: ")
                edad = int(input("Edad: "))
                especie = input("Especie: ")
                rasgos = input("Rasgos: ")
                enfermedad = input("Enfermedad: ")
                dueño = input("Nombre del Dueño/a: ")
                contacto = int(input("Telefono de Contacto: "))

                pacientesVet.registroPaciente(
                    nombre,
                    sexo,
                    edad,
                    especie,
                    rasgos,
                    enfermedad,
                    dueño,
                    contacto,
                    pacientes,
                )
                registros += 1

                print("")
                print(" " * 5, "*" * 20)
                print(" " * 7, "Registro Exitoso")
                print(" " * 5, "*" * 20)

                print("")

                pacientesVet.tiempoClear()

            case 2:
                print("")
                print(" " * 5, "*" * 20)
                print(" " * 7, "02 - Registro/s")
                print(" " * 5, "*" * 20)
                pacientesVet.verRegistros(pacientes)

                pacientesVet.tiempoClear()

            case 3:
                if registros >= 1:
                    pacientesVet.verRegistros(pacientes)
                    print("")
                    nroModificar = int(
                        input("Ingrese el Número del Paciente que desea modificar: ")
                    )
                    if nroModificar in pacientes:
                        caractModificar = input(
                            """
                            Items Cargados

                            - nombre
                            - sexo
                            - edad
                            - especie
                            - rasgos
                            - enfermedad
                            - dueño
                            - contacto

                            Ingrese Item: 
                            """
                        ).lower()

                        match caractModificar:
                            case "nombre":
                                valorActualizar = input("Nuevo Nombre: ")
                                pacientesVet.modificarPaciente(
                                    pacientes,
                                    nroModificar,
                                    caractModificar,
                                    valorActualizar,
                                )
                            case "sexo":
                                valorActualizar = input("Nuevo Sexo: ")
                                pacientesVet.modificarPaciente(
                                    pacientes,
                                    nroModificar,
                                    caractModificar,
                                    valorActualizar,
                                )
                            case "edad":
                                valorActualizar = input("Nueva Edad: ")
                                pacientesVet.modificarPaciente(
                                    pacientes,
                                    nroModificar,
                                    caractModificar,
                                    valorActualizar,
                                )
                            case "especie":
                                valorActualizar = input("Nueva Especie: ")
                                pacientesVet.modificarPaciente(
                                    pacientes,
                                    nroModificar,
                                    caractModificar,
                                    valorActualizar,
                                )
                            case "rasgos":
                                valorActualizar = input("Nuevos Rasgos: ")
                                pacientesVet.modificarPaciente(
                                    pacientes,
                                    nroModificar,
                                    caractModificar,
                                    valorActualizar,
                                )
                            case "enfermedad":
                                valorActualizar = input("Nueva Enfermedad: ")
                                pacientesVet.modificarPaciente(
                                    pacientes,
                                    nroModificar,
                                    caractModificar,
                                    valorActualizar,
                                )
                            case "dueño":
                                valorActualizar = input("Nuevo Dueño/a: ")
                                pacientesVet.modificarPaciente(
                                    pacientes,
                                    nroModificar,
                                    caractModificar,
                                    valorActualizar,
                                )
                            case "contacto":
                                valorActualizar = input("Nuevo Tel. de Contacto: ")
                                pacientesVet.modificarPaciente(
                                    pacientes,
                                    nroModificar,
                                    caractModificar,
                                    valorActualizar,
                                )
                            case _:
                                print("¡Item Invalido!")

                                pacientesVet.tiempoClear()
                    else:
                        print("¡Nro de Paciente Inexistente!")

                        pacientesVet.tiempoClear()

                else:
                    print("*" * 30)
                    print(" " , "No hay Pacientes Registrados")
                    print("*" * 30)

                    pacientesVet.tiempoClear

            case 4:
                if registros >= 1:
                    pacientesVet.verRegistros(pacientes)
                    print("")
                    nroPaciente = int(
                        input("Ingrese el Número de Paciente que desea eliminar: ")
                    )
                    if nroPaciente in pacientes:
                        pacientesVet.eliminarPaciente(pacientes, nroPaciente)
                        registrosE += 1
                    else:
                        print("¡ID Inexistente!")
                else:
                    print("*" * 30)
                    print(" " , "No hay Pacientes Registrados")
                    print("*" * 30)

            case 5:
                print("")
                print(" " * 5, "*" * 20)
                print(" " * 6, "05 - Reporte Final")
                print(" " * 5, "*" * 20)

                print(f"\nSe registraron {registros} Pacientes.")
                print(f"\nSe Eliminaron {registrosE} Pacientes.")
                print("\n--- FIN DEL PROGRAMA ---")
                break

            case _:
                print(
                    """
                      ¡Opción Invalida!
                      
                      Regresando al menu principal...                      
                      """
                )


if __name__ == "__main__":
    app()
