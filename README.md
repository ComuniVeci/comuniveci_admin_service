# 🛠️ ComuniVeci – Admin Service

Este microservicio actúa como agregador administrativo en el ecosistema de ComuniVeci. Su propósito principal es reunir, resumir y exponer datos desde otros servicios (como post-service y auth-service) para alimentar el panel de administración del frontend.

Forma parte de una arquitectura de microservicios y fue construido con FastAPI y principios de desacoplamiento.

---

## 🚀 Funcionalidades principales

Este servicio expone los siguientes endpoints:

| Método | Endpoint                         | Descripción                                                       |
|--------|----------------------------------|-------------------------------------------------------------------|
| GET    | /api/admin/posts/statistics      | Devuelve resumen de publicaciones (aprobadas, pendientes, total) |
| GET    | /api/admin/users                 | Devuelve lista de usuarios registrados (vía auth-service)         |
| GET    | /api/admin/metrics               | Devuelve métricas procesadas desde los servicios monitoreados     |monitoreados     |

---

## ⚙️ Tecnologías utilizadas

- Python 3.13
- FastAPI
- Uvicorn
- requests
- python-dotenv
- Prometheus metrics parsing
- Arquitectura modular inspirada en puertos y adaptadores

---

## 🧪 Requisitos

- Python ≥ 3.11
- MongoDB (para los otros servicios)
- Tener corriendo los siguientes servicios:
  - auth-service (http://localhost:8002)
  - post-service (http://localhost:8000)

---

## 🛠️ Instalación y ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/ComuniVeci/comuniveci_admin_service
cd comuniveci_admin_service
```

2. Instala dependencias con poetry:

```bash
poetry install
```

3. Crea un archivo .env y configura las variables:

```bash
AUTH_SERVICE_URL=http://localhost:8002
POST_SERVICE_URL=http://localhost:8000/api/posts/summary/
```

4. Ejecuta el servidor:

```bash
poetry run uvicorn src.main:app --reload --port 8003
```

La API estará disponible en http://localhost:8003

---

## 🧪 Endpoints detallados

- GET /api/admin/posts/statistics
    → Realiza una petición al post-service para obtener un resumen con número de publicaciones aprobadas, pendientes y totales.

- GET /api/admin/users
    → Consulta el auth-service para obtener una lista de usuarios registrados. El auth-service debe tener un endpoint público GET /api/auth/users implementado.

- GET /api/admin/metrics
    → Consulta el endpoint /metrics del auth-service (Prometheus format), parsea los datos y los expone en JSON. Incluye métricas personalizadas como:

        - auth_login_success_total

        - auth_register_failure_total

        - http_request_duration_seconds, etc.

---

## 🔐 Seguridad

Este servicio no expone endpoints públicos ni autenticación propia. Se espera que el frontend valide el rol de usuario antes de acceder a estos endpoints.

---

## 📦 Estructura del proyecto

```bash
src/
├── domain/
│   ├── entities.py           
│   ├── repositories.py           
│   ├── schemas.py          
├── infrastructure/
│   ├── api/          
│       ├── admin_views.py
│       ├── routes.py      
├── usecases/
│   ├── get_all_users.py         
│   ├── get_auth_metrics.py         
│   └── get_post_statistics.py       
├── config.py
├── main.py
```

---

## 📊 Ejemplo de respuesta

GET /api/admin/metrics

```json
{
  "requests_total": {
    "GET /api/auth/me": 2
  },
  "request_duration_seconds": {
    "GET /api/auth/me": 0.043
  },
  "custom_metrics": {
    "auth_login_success_total": 4,
    "auth_login_failure_total": 1,
    "auth_register_success_total": 3,
    "auth_register_failure_total": 0
  }
}
```

---

## 🛡️ Notas

- Este servicio no persiste datos. Solo agrega y transforma respuestas de otros servicios.

- Para usarlo correctamente, se requiere que los servicios a consultar estén activos.