print("""      apreta 1 para agregar un equipo al torneo, 
      apreta 2 para registrar un resultado
      apreta 3 para mostrar la tabla de posiciones
      apreta 4 para eliminar un equipo del torneo
      apreta 5 para salir del programa""")
equipos=[]
seleccion=int(input("selecciona la opcion: "))
esta=False
while seleccion != 5:
      if seleccion == 1:
            esta=False
            nuevo={"equipo":input("pon el nombre del equipo "),"puntos":0}
            for aux in equipos:
                  if aux.get("equipo") == nuevo["equipo"]:
                        print("este equipo ya esta en el torneo")
                        esta=True
                        break
            if(esta==False):
                  equipos.append(nuevo)
      elif seleccion == 4:
            eliminar = input("equipo a eliminar: ")
            for aux in equipos:
                  if aux.get("equipo") == eliminar:
                        equipos.remove(aux)
                        break
      elif seleccion == 3:
            equipos.sort(key=lambda x: x["puntos"])
            equipos.reverse()
            print(equipos)
      else:
            esta1=False
            esta2=False
            equipo1=input("ingrese equipo 1: ")
            equipo2=input("ingrese equipo 2: ")
            marcador=input("ingrese el marcador: ")
            marcador=marcador.split("-")
            for i in equipos:
                  if i.get("equipo")==equipo1:
                        esta1=True
                  if i.get("equipo")==equipo2:
                        esta2=True
            if esta1==True and esta2==True:
                  if int(marcador[0])>int(marcador[1]):
                        for i in equipos:
                              if i.get("equipo") == equipo1:
                                    i["puntos"] +=3
                  elif int(marcador[0])<int(marcador[1]):
                        for i in equipos:
                              if i.get("equipo") == equipo2:
                                    i["puntos"]+=3
                  else:
                        for i in equipos:
                              if i.get("equipo")==equipo1 or i.get("equipo")==equipo2:
                                    i["puntos"] +=1
            else:
                  print("falta uno o mas equipos")
      seleccion=int(input("selecciona la opcion: "))

      