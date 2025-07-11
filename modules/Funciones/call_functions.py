import pandas as pd
from  data_functions import limpiar_excel



def tasa_rellamado(informe_detalle_sistema):
    excel = limpiar_excel(informe_detalle_sistema)
    excel = excel[excel["Tiempo en cola"] != "00:00:00"]
    excel = excel[excel['Número del autor (número que llama)'] != "Anonymous"]
    print(len(excel))
    total_llamadas = len(excel)
    excel = excel[excel['Disposición de contacto'] != 1]
    #Disposición de contacto filtra no contestadas


    total_registros = excel["Número del autor (número que llama)"].count()
    print(total_registros)
    if total_registros > 0:
        duplicados = excel["Número del autor (número que llama)"].duplicated(keep="first").sum()
        tasa = (duplicados / total_llamadas)
        tasa = format(tasa, ".2f").replace('.', ',')

        return tasa
    else:
        return 0  

def tiempo_med_espera(agents):
    df_agents = limpiar_excel(agents)
    df_filtrado = df_agents[df_agents["Tiempo en cola"] != "00:00:00"]

    if not df_filtrado.empty:
        df_filtrado["Tiempo en cola"] = pd.to_timedelta(df_filtrado["Tiempo en cola"])
        promedio_segundos = (df_filtrado["Tiempo en cola"].sum() / len(df_filtrado)).total_seconds()
        return round(promedio_segundos)
    else:
        return 0
