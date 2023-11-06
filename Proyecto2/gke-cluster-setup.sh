#!/bin/bash
# Este script crea un clúster regional en Google Kubernetes Engine (GKE).

# Configurar variables
PROJECT_ID="inlaid-goods-380214"
CLUSTER_NAME="wordpress-ha-cluster"
REGION="us-central1"

# Crear el clúster de GKE
gcloud container clusters create $CLUSTER_NAME \
    --project $PROJECT_ID \
    --region $REGION \
    --num-nodes 1 \
    --enable-autorepair \
    --enable-autoupgrade \
    --enable-autoscaling --min-nodes 3 --max-nodes 5 \
    --machine-type e2-medium

# Obtener credenciales para kubectl
gcloud container clusters get-credentials $CLUSTER_NAME --region $REGION --project $PROJECT_ID

