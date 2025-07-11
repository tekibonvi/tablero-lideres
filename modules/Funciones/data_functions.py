import pandas as pd


def limpiar_excel(excel):
    df = pd.read_excel(excel , header=1)
    if df.iloc[-1].isnull().all() or df.iloc[-1].dtype == object:
        df = df.iloc[:-2]
    return df

def formatear_decimales(numero):
    decimal = numero - int(numero)
    if decimal >= 0.5:
        return round(numero)
    return int(numero)

def formatear_tiempo(tiempo):
    if pd.isna(tiempo):
        return "0:00:00" 
    segundos_totales = int(tiempo.total_seconds())
    horas, rem =divmod(segundos_totales, 3600)
    minutos, segundos = divmod(rem, 60)
    return f"{horas:0}:{minutos:02d}:{segundos:02d}"
