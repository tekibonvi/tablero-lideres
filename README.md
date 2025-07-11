# Proyecto: Tablero Lideres 0810.
# Data
Se usan 6 archivos 3 generados en CISCO, los dos de pausas salen de qlikview y 1 de casos de salesforce
# CISCO
1.  `informe_entrantes` : -Contact Service Queue Activity Report by Interval
2.  `informe_detalle_agentes` : -Agent Detail Report
3.  `detalle_sistema` : -Detailed Call CSQ Agent Report
# QlikView
 Salen del tablero: estados en construccion - estados agente.
 **IMPORTANTE** Sale de una tabla de cisco el reporte que lo trae es : -Agent State Detail Report
 - `informe_pausas` 
 - `informe_estados`
# Salesforce
 Informe: Casos Reporte Customizado . Objeto de SF : Caso
 - `informe_casos`

Se compone de 5 scripts.py : todos se ejecutan desde la terminal, pasando la ruta de los archivos
como argumento:
```bash
python3 script.py "archivo1" "archivo2" "archivo3"
```
1. llamadas.py
2. tiempos.py
3. llamadas_agente.py
4. estados.py
5. cases.py

# llamadas.py 
- archivos que usa:
1.  `informe_entrantes`
2.  `informe_detalle_agentes`
3.  `detalle_sistema`

**Importante:** El script tiene dos pausas (`input()`). Después de generar y mostrar la primera tabla, el programa esperará a que presiones **Enter** para continuar y generar la segunda tabla. Esto se hizo para dar tiempo a copiar los datos del portapapeles

El script ejecuta dos funciones principales en secuencia:

### llamadas_total()
 . Organiza los kpis y el resumen del dia.
 **Importante** Los datos de llamadas_total() van en la hoja *LLAMADAS* , de la hoja de calculo usada como bdd. 

### tablero_llamadas()
. Generar una tabla detallada por hora con las principales métricas de llamadas entrantes.
**Importante** Los datos de llamadas_total() van en la hoja *RECIBIDAS-ATENDIDAS-ABANDONADAS* , de la hoja de calculo usada como bdd. 
- Los datos tienen esa distribución para poder armar el primer gráfico combinado que se vé en Looker.
![alt text](image.png)


# tiempos.py
- archivos que usa:
1.  `informe_detalle_agentes`
2.  `informe_pausas`

### tiempos()
* **Propósito:** Generar un resumen con los **tiempos promedio generales** del día para todo el equipo seleccionado.
* **Importante** Los datos van en la hoja *TIEMPOS*
- Los datos proporcionan el kpi diario de TMO y TML.
### tiempos_por_agente()

* **Propósito:** Generar una tabla detallada con el **TMO y TML individual para cada agente**.
* **Importante** Los datos van en la hoja *TIEMPOS_POR_AGENTE*


- Los datos se usan para generar estos dos gráficos.
![alt text](image-1.png)

