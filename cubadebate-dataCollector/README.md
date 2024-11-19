# Proyecto sobre recopilación de informacion acerca del Sistema Electrico Nacional (SEN).

### Información sobre el scrapper:

*1. Función principal*

— Este scraper extrae información estructurada y relevante sobre el Sistema Eléctrico Nacional (SEN) desde cualquier página web especificada por el usuario.

— Genera un archivo .json con los datos procesados, listo para su uso en análisis o almacenamiento.

*2.	Cómo Funciona:*

— Utiliza la biblioteca Requests para realizar solicitudes HTTP y descargar el contenido HTML de las páginas web.

— Procesa el contenido HTML mediante BeautifulSoup, una herramienta de scraping que facilita encontrar, navegar y extraer elementos específicos del HTML.

### Ventajas del Scraper

	1.	Personalización: Permite al usuario especificar cualquier URL, adaptándose a diferentes sitios web relacionados con el SEN.
	2.	Formato Estructurado: Produce un archivo JSON organizado, ideal para su uso en proyectos de Ciencia de Datos o para integrarse con APIs o dashboards.
	3.	Facilidad de Uso: El código es modular y fácil de ajustar según las necesidades de scraping de cada página.
	4.	Compatibilidad: Utiliza bibliotecas populares y bien documentadas como Flask, Requests, y BeautifulSoup.

Ejecuta `python dataCollector.py` para ejecutar el scrapper.

> Los archivos ".json" se guardan en el directorio [data](./data/)

### Datos recopilador por el scrapper:

- Informacion principal:
    - Fecha.
    - Día.
    - URL.

- Estimación:
    - Horario.
    - Disponibilidad.
    - Demanda Máxima.
    - Déficit.
    - Pronostico:
        - Afectación.

- Info de los horarios:
    - Mañana:
        - Cantidad de MW para la disponibilidad.
        - Demanda prevista para ese horario.
        - Totalidad del funcionamiento del SEN
    - Mediodia:
        - Pronóstico:
            - Afectación.

- Termoeléctricas:
    - Límite en la Generación Térmica.
    - Fuera de servicio:
        - Por averias:
            - Nombre de la Unidad.
            - Nombre de la CTE.
        - Por Mantenimiento:
            - Nombre de la Unidad.
            - Nombre de la CTE.

- Centrales de Generacion Distribuida:
    - Sin servicio:
            - Cantidad de Centrales de Generación Distribuida.
            - Razon por la que se encuentra sin servicio.
            - Cantidad de MW afectados.

- Pico:
    - Estimación.
        - Descripcion de la estimación.
        - Razón por la que estuvieron fuera.
        - Cantidad de MW totales.

- Maxima afectacion del dia:
    - Cantidad de MW afectados.
    - Hora en la que ocurrió.
    - Descripción.

- Dia anterior:
    - Descripción.
    - Total de horas en las que se estuvo sin servicio.
    - Hora en la que se restableció.

### La anterior información se guardará en un archivo .json con la siguiente estructura:

```json
{
    "sen_info": {
        "main_info": {
            "_comentario": "Las fechas deben expresarse con guiones",
            "fecha": "",
            "dia": "",
            "url": ""
        },
        "_comentario": "Toda esta informacion se expresa en MW",
        "estimacion": {
            "horario": "",
            "disponibilidad": 0,
            "demanda_max": 0,
            "deficit": 0,
            "pronostico": {
                "afectacion": 0
            }
        },
        "info_horarios": {
            "mañana": {
                "disponibilidad": 0,
                "demanda": 0,
                "totalidad": true
            },
            "mediodia": {
                "pronostico": {
                    "afectacion": 0
                }
            }
        },
        "termoelectricas": {
            "_comentario": "Esto quiere decir: Limitaciones en la generacion termica",
            "lim_gen_term": 0,
            "fuera": {
                "averias": [
                    {
                        "nombre": "Unidad",
                        "CTE": ""
                    }
                ],
                "mantenimiento":[
                    {
                        "nombre": "Unidad",
                        "CTE": ""
                    }
               ]
            }
        },
        "centr_gen_distr": {
            "no_servicio": [
                {
                    "cantidad": 0,
                    "razon": "",
                    "mw_afectados": 0
                }
            ]
        },
        "pico": {
            "estimacion": [
                {
                    "desc": "",
                    "razon": "",
                    "cantidad_mw": 0
                }
            ]
        },
        "max_afect_dia": {
            "cantidad_mw": 0,
            "hora": "",
            "desc": ""
        },
        "dia_anterior": {
            "desc": "",
            "horas": 0,
            "hora_rest": ""
        }
    }
}
```
