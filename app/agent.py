from openai import OpenAI
from dotenv import load_dotenv
import json
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "solicitar_caso_negocio",
            "description": "Recopila y estructura la informacion del caso de negocio del cliente: problema, sector, publico objetivo, presupuesto estimado y objetivos.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre_proyecto": {"type": "string", "description": "Nombre del proyecto o producto de IA"},
                    "sector": {"type": "string", "description": "Sector o industria del cliente (fintech, salud, retail, etc.)"},
                    "problema": {"type": "string", "description": "Problema de negocio que se busca resolver"},
                    "publico_objetivo": {"type": "string", "description": "Publico objetivo del producto"},
                    "presupuesto_estimado_usd": {"type": "number", "description": "Presupuesto estimado en USD"},
                    "plazo_meses": {"type": "integer", "description": "Plazo estimado del proyecto en meses"}
                },
                "required": ["nombre_proyecto", "sector", "problema", "publico_objetivo", "presupuesto_estimado_usd", "plazo_meses"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "preparar_ficha_producto",
            "description": "Genera la ficha tecnica del producto de IA con descripcion, features, stack tecnologico y diferenciadores.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre_proyecto": {"type": "string"},
                    "sector": {"type": "string"},
                    "problema": {"type": "string"}
                },
                "required": ["nombre_proyecto", "sector", "problema"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calcular_capex",
            "description": "Calcula el CapEx (gastos de capital) para un producto de IA: infraestructura, licencias, desarrollo inicial, hardware.",
            "parameters": {
                "type": "object",
                "properties": {
                    "presupuesto_total_usd": {"type": "number"},
                    "plazo_meses": {"type": "integer"},
                    "complejidad": {"type": "string", "enum": ["baja", "media", "alta"], "description": "Complejidad tecnica del proyecto"}
                },
                "required": ["presupuesto_total_usd", "plazo_meses", "complejidad"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calcular_opex",
            "description": "Calcula el OpEx (gastos operativos) para un producto de IA: APIs, cloud, mantenimiento, soporte, equipo.",
            "parameters": {
                "type": "object",
                "properties": {
                    "presupuesto_total_usd": {"type": "number"},
                    "plazo_meses": {"type": "integer"},
                    "complejidad": {"type": "string", "enum": ["baja", "media", "alta"]}
                },
                "required": ["presupuesto_total_usd", "plazo_meses", "complejidad"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "crear_roadmap",
            "description": "Crea un roadmap del producto con fases, hitos y entregables.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre_proyecto": {"type": "string"},
                    "plazo_meses": {"type": "integer"},
                    "complejidad": {"type": "string", "enum": ["baja", "media", "alta"]}
                },
                "required": ["nombre_proyecto", "plazo_meses", "complejidad"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "crear_metas",
            "description": "Define KPIs, OKRs y metricas de exito para el producto de IA.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre_proyecto": {"type": "string"},
                    "sector": {"type": "string"},
                    "problema": {"type": "string"}
                },
                "required": ["nombre_proyecto", "sector", "problema"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "generar_caso_negocio",
            "description": "Genera el documento final del caso de negocio consolidando toda la informacion recopilada.",
            "parameters": {
                "type": "object",
                "properties": {
                    "nombre_proyecto": {"type": "string"},
                    "sector": {"type": "string"},
                    "ficha_producto": {"type": "string"},
                    "capex": {"type": "string"},
                    "opex": {"type": "string"},
                    "roadmap": {"type": "string"},
                    "metas": {"type": "string"}
                },
                "required": ["nombre_proyecto", "sector", "ficha_producto", "capex", "opex", "roadmap", "metas"]
            }
        }
    }
]


def solicitar_caso_negocio(nombre_proyecto, sector, problema, publico_objetivo, presupuesto_estimado_usd, plazo_meses):
    return json.dumps({
        "status": "capturado",
        "caso": {
            "nombre_proyecto": nombre_proyecto,
            "sector": sector,
            "problema": problema,
            "publico_objetivo": publico_objetivo,
            "presupuesto_estimado_usd": presupuesto_estimado_usd,
            "plazo_meses": plazo_meses
        }
    }, ensure_ascii=False)


def preparar_ficha_producto(nombre_proyecto, sector, problema):
    return json.dumps({
        "ficha": {
            "nombre": nombre_proyecto,
            "sector": sector,
            "problema_que_resuelve": problema,
            "tipo_ia": "Por determinar segun analisis",
            "stack_sugerido": ["Python", "FastAPI", "OpenAI API", "PostgreSQL", "Docker", "AWS/GCP"],
            "features_core": [
                "Motor de IA principal",
                "API REST para integraciones",
                "Dashboard de monitoreo",
                "Sistema de reportes"
            ],
            "diferenciadores": [
                "Automatizacion inteligente con IA generativa",
                "Integracion nativa con sistemas existentes",
                "Escalabilidad cloud-native"
            ]
        }
    }, ensure_ascii=False)


def calcular_capex(presupuesto_total_usd, plazo_meses, complejidad):
    multiplicadores = {"baja": 0.30, "media": 0.40, "alta": 0.50}
    mult = multiplicadores.get(complejidad, 0.40)
    capex_total = presupuesto_total_usd * mult

    return json.dumps({
        "capex": {
            "total_usd": round(capex_total, 2),
            "porcentaje_del_presupuesto": f"{mult * 100}%",
            "desglose": {
                "infraestructura_cloud_inicial": round(capex_total * 0.25, 2),
                "licencias_software": round(capex_total * 0.15, 2),
                "desarrollo_inicial": round(capex_total * 0.40, 2),
                "hardware_equipos": round(capex_total * 0.10, 2),
                "capacitacion_equipo": round(capex_total * 0.10, 2)
            },
            "nota": f"CapEx estimado para proyecto de complejidad {complejidad} a {plazo_meses} meses"
        }
    }, ensure_ascii=False)


def calcular_opex(presupuesto_total_usd, plazo_meses, complejidad):
    multiplicadores = {"baja": 0.15, "media": 0.20, "alta": 0.25}
    mult = multiplicadores.get(complejidad, 0.20)
    opex_mensual = (presupuesto_total_usd * mult) / plazo_meses

    return json.dumps({
        "opex": {
            "mensual_usd": round(opex_mensual, 2),
            "anual_estimado_usd": round(opex_mensual * 12, 2),
            "desglose_mensual": {
                "apis_ia_openai_etc": round(opex_mensual * 0.30, 2),
                "cloud_hosting": round(opex_mensual * 0.25, 2),
                "mantenimiento_software": round(opex_mensual * 0.20, 2),
                "soporte_tecnico": round(opex_mensual * 0.15, 2),
                "monitoreo_seguridad": round(opex_mensual * 0.10, 2)
            },
            "nota": f"OpEx mensual estimado para complejidad {complejidad}"
        }
    }, ensure_ascii=False)


def crear_roadmap(nombre_proyecto, plazo_meses, complejidad):
    fases = []
    if plazo_meses <= 3:
        fases = [
            {"fase": "MVP", "duracion": f"Mes 1-{plazo_meses}", "entregables": ["Prototipo funcional", "Validacion con usuarios", "Deploy inicial"]}
        ]
    elif plazo_meses <= 6:
        fases = [
            {"fase": "Descubrimiento", "duracion": "Mes 1", "entregables": ["Investigacion de mercado", "Definicion de requerimientos", "Arquitectura tecnica"]},
            {"fase": "MVP", "duracion": "Mes 2-3", "entregables": ["Desarrollo core", "Integracion IA", "Testing basico"]},
            {"fase": "Beta", "duracion": "Mes 4-5", "entregables": ["Beta cerrada", "Iteracion por feedback", "Optimizacion de modelos"]},
            {"fase": "Lanzamiento", "duracion": f"Mes 6", "entregables": ["Go-to-market", "Onboarding clientes", "Monitoreo post-launch"]}
        ]
    else:
        fases = [
            {"fase": "Descubrimiento", "duracion": "Mes 1-2", "entregables": ["Research", "Product discovery", "Definicion de arquitectura"]},
            {"fase": "Fundacion", "duracion": "Mes 3-4", "entregables": ["Infraestructura base", "Pipeline de datos", "Modelo IA v1"]},
            {"fase": "MVP", "duracion": f"Mes 5-{min(plazo_meses, 7)}", "entregables": ["Producto minimo viable", "Integraciones clave", "QA"]},
            {"fase": "Escalamiento", "duracion": f"Mes {min(plazo_meses, 8)}-{min(plazo_meses, 10)}", "entregables": ["Optimizacion", "Nuevas features", "Escalabilidad"]},
            {"fase": "Maduracion", "duracion": f"Mes {min(plazo_meses, 11)}-{plazo_meses}", "entregables": ["Estabilizacion", "Documentacion", "Transferencia de conocimiento"]}
        ]

    return json.dumps({
        "roadmap": {
            "proyecto": nombre_proyecto,
            "duracion_total": f"{plazo_meses} meses",
            "complejidad": complejidad,
            "fases": fases
        }
    }, ensure_ascii=False)


def crear_metas(nombre_proyecto, sector, problema):
    return json.dumps({
        "metas": {
            "okrs": [
                {
                    "objetivo": f"Lanzar {nombre_proyecto} como solucion lider en {sector}",
                    "resultados_clave": [
                        "Alcanzar 100 usuarios activos en los primeros 3 meses",
                        "Lograr un NPS mayor a 40",
                        "Reducir el tiempo de resolucion del problema en un 50%"
                    ]
                },
                {
                    "objetivo": "Validar el product-market fit",
                    "resultados_clave": [
                        "Tasa de retencion mensual mayor al 70%",
                        "Al menos 3 clientes pagando en el Q1",
                        "Feedback positivo en 80% de entrevistas"
                    ]
                }
            ],
            "kpis": [
                {"kpi": "Usuarios activos mensuales (MAU)", "meta": "100+ en Q1", "frecuencia": "Mensual"},
                {"kpi": "Tasa de conversion", "meta": ">5%", "frecuencia": "Semanal"},
                {"kpi": "Costo por adquisicion (CAC)", "meta": "<$50 USD", "frecuencia": "Mensual"},
                {"kpi": "Tiempo de respuesta IA", "meta": "<2 segundos", "frecuencia": "Diario"},
                {"kpi": "Precision del modelo", "meta": ">85%", "frecuencia": "Semanal"},
                {"kpi": "Uptime del servicio", "meta": "99.5%", "frecuencia": "Diario"}
            ],
            "mediciones": [
                "Encuestas NPS trimestrales",
                "A/B testing continuo",
                "Analisis de cohortes mensual",
                "Reviews de modelo IA quincenal"
            ]
        }
    }, ensure_ascii=False)


def generar_caso_negocio(nombre_proyecto, sector, ficha_producto, capex, opex, roadmap, metas):
    return json.dumps({
        "caso_de_negocio": {
            "proyecto": nombre_proyecto,
            "sector": sector,
            "estado": "Documento generado exitosamente",
            "secciones": [
                "Ficha de Producto",
                "Analisis CapEx",
                "Analisis OpEx",
                "Roadmap",
                "KPIs y OKRs"
            ],
            "ficha_producto": ficha_producto,
            "capex": capex,
            "opex": opex,
            "roadmap": roadmap,
            "metas": metas,
            "recomendacion": "Proceder con fase de descubrimiento para validar supuestos antes de comprometer el presupuesto completo."
        }
    }, ensure_ascii=False)


FUNCTION_MAP = {
    "solicitar_caso_negocio": solicitar_caso_negocio,
    "preparar_ficha_producto": preparar_ficha_producto,
    "calcular_capex": calcular_capex,
    "calcular_opex": calcular_opex,
    "crear_roadmap": crear_roadmap,
    "crear_metas": crear_metas,
    "generar_caso_negocio": generar_caso_negocio,
}

SYSTEM_PROMPT = """Eres un agente financiero experto en productos de IA. Tu rol es ayudar a los clientes a construir su caso de negocio completo para productos basados en inteligencia artificial.

Tienes acceso a las siguientes herramientas:
1. solicitar_caso_negocio - Para capturar la informacion inicial del proyecto
2. preparar_ficha_producto - Para generar la ficha tecnica del producto
3. calcular_capex - Para calcular gastos de capital
4. calcular_opex - Para calcular gastos operativos
5. crear_roadmap - Para crear el plan de ejecucion
6. crear_metas - Para definir KPIs, OKRs y metricas
7. generar_caso_negocio - Para consolidar todo en un documento final

FLUJO DE TRABAJO:
- Primero, saluda al cliente y pregunta sobre su proyecto de IA.
- Recopila la informacion necesaria conversando de forma natural.
- Cuando tengas suficiente informacion, usa las herramientas en este orden:
  1. solicitar_caso_negocio
  2. preparar_ficha_producto
  3. calcular_capex y calcular_opex
  4. crear_roadmap
  5. crear_metas
  6. generar_caso_negocio (consolidacion final)
- Presenta los resultados de forma clara y profesional.
- Responde consultas adicionales sobre el caso.

REGLAS:
- Se profesional pero amigable.
- Usa formato markdown para presentar resultados.
- Si falta informacion, pregunta antes de asumir.
- Para la complejidad, evaluala tu mismo basandote en la descripcion del proyecto.
- Siempre muestra montos en USD.
- Responde en espanol."""


class FinancialAgent:
    def __init__(self):
        self.conversation_history = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]

    def chat(self, user_message: str) -> str:
        self.conversation_history.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.conversation_history,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0.7
        )

        message = response.choices[0].message

        while message.tool_calls:
            self.conversation_history.append(message)

            for tool_call in message.tool_calls:
                fn_name = tool_call.function.name
                fn_args = json.loads(tool_call.function.arguments)
                fn = FUNCTION_MAP.get(fn_name)

                if fn:
                    result = fn(**fn_args)
                else:
                    result = json.dumps({"error": f"Funcion {fn_name} no encontrada"})

                self.conversation_history.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.conversation_history,
                tools=TOOLS,
                tool_choice="auto",
                temperature=0.7
            )
            message = response.choices[0].message

        assistant_content = message.content or ""
        self.conversation_history.append({"role": "assistant", "content": assistant_content})
        return assistant_content

    def reset(self):
        self.conversation_history = [
            {"role": "system", "content": SYSTEM_PROMPT}
        ]
