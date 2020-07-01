# for presenters

## Deploy Open Data Hub

You will show the audience how easy is to deploy **Open Data Hub**.

Log as **production** user:

+ Create a project.

+ Go to **Operators -> Installed Operators**. The **Open Data Hub Operator** will appear in a few seconds:

![odh-operator](imgs/production-odh-operator.png)

+ Deploy OpenDataHub in that proyect. Click on **Open Data Hub Operator** and scroll down to show what projects and versions includes the Open Data Hub. After that click in **Create Instance**:

![odh-create-instance](imgs/production-odh-create-instance.png)

+ Scroll down the yaml file showing it. Do not modify anything we will use the default configuration:

![odh-yaml](imgs/production-odh-yaml.png)

+ Click on **Create** to start deploying **Open Data Hub** on the project.

![odh-creation](imgs/production-odh-create.png)

+ Go to **Workloads -> Pods** to show how pods are being deployed:

![odh-pods](imgs/production-pods-deploying.png)

Deployment could take from 2 to 5 minutes. 

## Jupyter Notebook Demo

Close the session and log with the **data_scientist** user.

Go to **binary-classification** project and go to **Networking -> Routes** to show the routers to access all the deployed software.

Browse the following to show how easy is to deploy and use them:

+ **Argo**:

![dashboard-argo](imgs/dashboard-argo.png)

+ **Grafana**:

![dashboard-argo](imgs/dashboard-grafana.png)

+ **Prometheus**:

![dashboard-argo](imgs/dashboard-prometheus.png)

+ **Apache Superset** (log with credentials **admin/admin**):

![dashboard-argo](imgs/dashboard-superset.png)

