import pandas as pds

def logica(datos):
    #El formato de datos siempre inicia en esta fila, ignorando los encabezados
    fila_inicio = 4
    datos = datos.iloc[fila_inicio:]
    emision_padre = 0

    #Se pide el nivel de la consulta
    nivel_consulta = 2
    nivel_padre = nivel_consulta

    #Dentro del DataFrame de pandas, se ubica desde las filas donde inicia la consulta
    datos = datos.reset_index(drop=True)

    condicion_fila_cero = (
        datos.iloc[:, 0].notna() & 
        datos.iloc[:, 1:-1].isna().all(axis=1)
    )
    fila_cero = datos[condicion_fila_cero]

    emisiones_producto = datos.iloc[:, -1].dropna().iloc[0]

    # Procesamiento de cada fila
    def procesaFila(fila):
        #Se posiciona una fila antes del indice de carbono
        recorrido_componente = [c for c in fila.iloc[:-1] if pds.notnull(c)]
        # Se posiciona en la ultima fila
        emision = fila.iloc[-1]
        #Obtiene el nivel
        nivel = len(recorrido_componente) - 1
        if nivel == nivel_padre:
            global emision_padre
            emision_padre=emision
        if nivel == nivel_consulta + 1 and emision_padre != 0:
            porcentaje_padre = (emision / emision_padre) * 100
        else:
            porcentaje_padre = 0
        #Obtiene el porcentaje con respecto al total del producto
        porcentaje_total = (emision/emisiones_producto)*100
        #Obtiene la pieza a la que hace referencia
        ultimo_campo= recorrido_componente[-1] if recorrido_componente else None
        #Contiene indices, tipo de dato y los datos
        return pds.Series({
            "Nombre" : ultimo_campo,
            "Emision" : emision,
            "Porcentaje Total" : porcentaje_total,
            "Porcentaje Padre" : porcentaje_padre,
            "Nivel" : nivel
        })

    #Aplica la funcion procesaFila en eje de filas (1)
    datos_procesados = datos.apply(procesaFila, axis=1)
    datos_procesados = datos_procesados.reset_index(drop = True)

    #Obtiene los datos en el nivel consultado y el siguiente nivel inmediato
    filtro_niveles = datos_procesados[datos_procesados["Nivel"].isin([nivel_consulta, nivel_consulta+1])]

    print(filtro_niveles)