
<div align="center">
	<h1>🔐 Authentication & RBAC</h1>
	<img src="https://img.icons8.com/color/96/lock--v1.png" alt="Auth"/>
</div>

Corelia uses JWT authentication and role-based access control (RBAC).

## Roles
- `Admin`: Full access
- `Employee`: Limited access

## Endpoints
- `/auth/token`: Get JWT token
- Protected endpoints require `Authorization: Bearer <token>`

See `auth.py` for implementation.