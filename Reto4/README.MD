# Equipo:

- Daniel Jaramillo Valencia
- Jacobo Rave Londoño
- Kevin Alejandro Sossa Chavarria
- Antonio Carmona Gaviria

# Despliegue de WordPress con MySQL en MicroK8s

Este README describe los pasos para desplegar una aplicación WordPress junto con una base de datos MySQL en un clúster de Kubernetes gestionado por MicroK8s. El despliegue también incluye la configuración de un Ingress Controller usando NGINX para gestionar el tráfico hacia la aplicación.

## Pre-requisitos

- Un clúster de MicroK8s configurado y en funcionamiento.
- Tres nodos en el clúster: un nodo maestro y dos nodos trabajadores.
- Acceso a la línea de comandos de `kubectl` o `microk8s.kubectl` en el nodo maestro.

## Pasos del Despliegue

### 1. Despliegue de MySQL

1. Crear un archivo `mysql-deployment.yaml` con el siguiente contenido:


# (contenido del archivo mysql-deployment.yaml)


2. Aplicar la configuración con el siguiente comando:

```bash
microk8s.kubectl apply -f mysql-deployment.yaml
```

### 2. Despliegue de WordPress

1. Crear un archivo `wordpress-deployment.yaml` con el siguiente contenido:

```yaml
# (contenido del archivo wordpress-deployment.yaml)
```

2. Aplicar la configuración con el siguiente comando:

```bash
microk8s.kubectl apply -f wordpress-deployment.yaml
```

### 3. Configuración del NGINX Ingress Controller

1. Crear un archivo `nginx-ingress.yaml` con el siguiente contenido:

```yaml
# (contenido del archivo nginx-ingress.yaml )
```

2. Aplicar la configuración con el siguiente comando:

```bash
microk8s.kubectl apply -f nginx-ingress.yaml
```

### 4. Configuración del Ingress para WordPress

1. Crear un archivo `wordpress-ingress.yaml` con el siguiente contenido:

```yaml
# (contenido del archivo wordpress-ingress.yaml )
```

2. Aplicar la configuración con el siguiente comando:

```bash
microk8s.kubectl apply -f wordpress-ingress.yaml
```

### 5. Acceso a WordPress

Después de completar estos pasos, deberías poder acceder a WordPress a través de la IP proporcionada por el servicio LoadBalancer de NGINX. Puedes obtener la IP externa con el siguiente comando:

```bash
microk8s.kubectl get svc ingress-nginx
```

Si la IP externa está en estado `<pending>`, puede que necesites esperar un poco más o revisar la configuración de tu clúster y la documentación del proveedor de servicios en la nube.

## Comprobaciones Finales

Verifica que todos los servicios, despliegues, y pods estén funcionando correctamente con los siguientes comandos:

```bash
microk8s.kubectl get services
microk8s.kubectl get deployments
microk8s.kubectl get pods
```

Estos comandos te mostrarán el estado actual de los recursos en tu clúster, y te ayudarán a identificar cualquier problema o configuración incorrecta.

---

Este README proporciona una guía básica para desplegar WordPress y MySQL en un clúster de MicroK8s con un NGINX Ingress Controller. Para una configuración más avanzada o personalizada, se recomienda revisar la documentación oficial de Kubernetes, MicroK8s, y NGINX Ingress Controller.