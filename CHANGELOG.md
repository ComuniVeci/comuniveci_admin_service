# 📜 CHANGELOG – ComuniVeci Admin Service

Historial de versiones y cambios del servicio de administración y agregación de ComuniVeci.

---

## [1.0.0] – 2025-07-13

🎉 Versión inicial del servicio admin-service.

### ✨ Funcionalidades implementadas

- 📊 GET /api/admin/posts/statistics:
  - Consulta post-service para obtener estadísticas agregadas de publicaciones (aprobadas, pendientes, totales).

- 👥 GET /api/admin/users:
  - Consulta auth-service para obtener una lista de usuarios registrados.
  - Requiere que auth-service tenga un endpoint GET /api/auth/users.

- 📈 GET /api/admin/metrics:
  - Realiza parsing del formato Prometheus desde /metrics de auth-service.
  - Expone métricas en formato JSON limpio para el frontend.
  - Se identifican métricas personalizadas como:
    - auth_login_success_total
    - auth_register_failure_total
    - http_request_duration_seconds, etc.

### ⚙️ Arquitectura

- Uso de FastAPI modularizado con rutas separadas.
- Lógica de parsing y requests externos desacoplada en carpeta services/.

---

## 🧭 Próximas versiones

- [ ] Agregar tests automáticos para los endpoints.
- [ ] Incluir reintentos y manejo de errores en caso de fallo de otros servicios.
- [ ] Permitir consultar métricas de múltiples servicios (post, map, etc.).
- [ ] Autenticación opcional para proteger los endpoints.
- [ ] Documentación OpenAPI automática.
