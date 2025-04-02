# Data Pipeline de Accidentes para Análisis de Riesgo en Seguros

Este proyecto implementa un pipeline completo de Ingeniería de Datos para analizar datos reales de accidentes de tránsito con el objetivo de identificar zonas de alto riesgo, patrones temporales y tipos de vehículos más afectados. Es ideal para su uso por parte de aseguradoras en el ajuste dinámico de pólizas o políticas de prevención.

---

## 📌 Objetivo

Construir una solución que:
- Ingesta datos de accidentes de tránsito desde una API pública.
- Limpia, transforma y almacena los datos en una base de datos.
- Visualiza la información en un dashboard de Power BI.
- Automatiza todo el flujo con Apache Airflow.

---

## 🧠 Problema a Resolver

Las aseguradoras necesitan conocer en tiempo casi real:
- ¿Dónde ocurren más accidentes?
- ¿A qué horas hay más siniestros?
- ¿Qué tipo de vehículos están más involucrados?

Este proyecto resuelve eso con datos actualizados, centralizados y listos para análisis.

---

## 🌍 Fuente de Datos

API pública del Gobierno de Nueva York:  
**NYC Motor Vehicle Collisions**  
[https://data.cityofnewyork.us/resource/h9gi-nx95.json](https://data.cityofnewyork.us/resource/h9gi-nx95.json)

---

## ⚙️ Stack Tecnológico
```
| Componente        | Tecnología                             |
|-------------------|----------------------------------------|
| Lenguaje          | Python, SQL                            |
| Ingesta API       | requests, pandas                       |
| ETL               | pandas                                 |
| Orquestación      | Apache Airflow                         |
| Almacenamiento    | PostgreSQL                             |
| Visualización     | Power BI                               |
| Infraestructura   | Docker, Git                            |
```
---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/trismald/NYC-Accident-Insights
cd NYC-Accident-Insights
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Levantar Airflow con Docker

```bash
cd docker/
docker-compose up -d
```

### 4. Visualizar los datos

- Cargar el archivo `.pbix` en Power BI Desktop.
- Configurar la conexión a la base de datos PostgreSQL.
- Actualizar visualizaciones.

---

## 📈 Métricas del Proyecto
```
| Métrica                                | Resultado estimado                     |
|----------------------------------------|----------------------------------------|
| Datos procesados diarios               | +1,000,000 registros                   |
| Tiempo de ingesta y carga              | < 1 hora por ejecución                 |
| Reducción de tiempo de reportes        | 80% menos vs. carga manual             |
| KPI disponibles                     | +6 métricas clave para análisis de riesgo |
| Automatización                         | 100% orquestado con Airflow           |
```
---

## 🔐 Seguridad y Gobernanza

- Versionado de código con **Git**.
- Enmascaramiento y validación de campos PII.
- Roles y accesos mínimos (IAM / PostgreSQL).
- Datos respaldados diariamente.

---

## 🧪 Pruebas

Puedes ejecutar pruebas unitarias sobre las transformaciones con PyTest:

```bash
pytest tests/
```

---

## 🤝 Créditos

Desarrollado por trismald como parte de un proyecto personal para portafolio profesional.

Inspirado por el uso de datos abiertos del Gobierno de NYC.

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.

---

## 📬 Contacto

¿Comentarios, sugerencias o colaboración?

📧 triss.maldonado@outlook.com  
🐙 [github.com/trismald](https://github.com/trismald)

---
