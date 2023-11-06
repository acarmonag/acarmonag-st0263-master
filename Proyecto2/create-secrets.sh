#!/bin/bash
# Este script crea un secreto para la contraseña de la base de datos en Kubernetes.

# Cambiar 'tu-contraseña-de-db' por la contraseña real de tu base de datos
kubectl create secret generic db-password --from-literal=password='tu-contraseña-de-db'
