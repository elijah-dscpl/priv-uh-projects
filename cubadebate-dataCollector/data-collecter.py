from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)

@app.route('/extract', methods=['GET'])
def extract_sen_info():
    # Solicitar al usuario la URL personalizada
    print("Introduce la URL de la página que deseas procesar:")
    custom_url = input("URL: ").strip()

    # Validar si se ingresó una URL
    if not custom_url:
        return jsonify({"error": "No se proporcionó una URL válida"}), 400
    
    try:
        # Realizar el request a la URL ingresada
        response = requests.get(custom_url)
        if response.status_code != 200:
            return jsonify({"error": f"No se pudo acceder a la URL: {custom_url}"}), 500
        
        # Parsear el HTML de la URL ingresada
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer datos básicos (ejemplo simulado)
        fecha = "2024-11-18"  # Ejemplo de fecha fija, ajusta según lo que scrapees
        dia = "Lunes"
        url = custom_url

        # Datos ficticios para ilustrar el formato del JSON
        data = {
            "sen_info": {
                "main_info": {
                    "fecha": fecha,
                    "dia": dia,
                    "url": url
                },
                "estimacion": {
                    "horario": "20:00",
                    "disponibilidad": 500,
                    "demanda_max": 600,
                    "deficit": 100,
                    "pronostico": {
                        "afectacion": 50
                    }
                },
                "info_horarios": {
                    "mañana": {
                        "disponibilidad": 450,
                        "demanda": 500,
                        "totalidad": True
                    },
                    "mediodia": {
                        "pronostico": {
                            "afectacion": 20
                        }
                    }
                },
                "termoelectricas": {
                    "lim_gen_term": 300,
                    "fuera": {
                        "averias": [
                            {
                                "nombre": "Unidad 1",
                                "CTE": "CTE Guiteras"
                            }
                        ],
                        "mantenimiento": [
                            {
                                "nombre": "Unidad 2",
                                "CTE": "CTE Renté"
                            }
                        ]
                    }
                },
                "centr_gen_distr": {
                    "no_servicio": [
                        {
                            "cantidad": 5,
                            "razon": "Averías técnicas",
                            "mw_afectados": 50
                        }
                    ]
                },
                "pico": {
                    "estimacion": [
                        {
                            "desc": "Alta demanda en horario pico",
                            "razon": "Consumo elevado",
                            "cantidad_mw": 200
                        }
                    ]
                },
                "max_afect_dia": {
                    "cantidad_mw": 150,
                    "hora": "22:00",
                    "desc": "Corte por sobrecarga"
                },
                "dia_anterior": {
                    "desc": "Afectaciones moderadas",
                    "horas": 4,
                    "hora_rest": "02:00"
                }
            }
        }

        # Guardar los datos en un archivo .json
        with open('sen_info.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print("Datos extraídos correctamente. Archivo 'sen_info.json' generado.")
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
