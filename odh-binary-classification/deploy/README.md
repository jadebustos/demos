# Deployment

To deploy you will need:

+ A OpenShift cluster with OCS enabled.
+ A bastion host with OpenShift client installed.
+ A OpenShift cluster admin user.
+ A bastion user with public key configured.

## Configuration

Configure the folowing files to fit your environment:

+ **inventory** configure the bastion host ip and the ansible user.
+ **group_vars/general.yaml**

## OCS deployment

Create the OCS namespace:

```
ansible-playbook -i inventory deploy-ocs.yaml
```

Deploy OCS as usual.

> Not yet automated.

## Configure authentication

First you have con create two users. Check if HTPasswd provider is already created in your deployment. 

If it is created then you can create the two user as shown:

If HTPasswd provider is already configured you will need to add two users:

+ **data_scientist** user with password **temporal2020**.
+ **production** user with password **temporal2020**.

```
[user@bastion ocp]$ oc get identities
NAME                            IDP NAME            IDP USER NAME   USER NAME     USER UID
htpasswd_provider:opentlc-mgr   htpasswd_provider   opentlc-mgr     opentlc-mgr   db6d9da9-99fb-459b-a6da-2cc900722896
[user@bastion ocp]$ oc get secrets -n openshift-config | grep htt
[user@bastion ocp]$ oc get secrets -n openshift-config | grep ht
htpasswd-secret                       Opaque                                1      133m
[user@bastion ocp]$ oc describe secrets htpasswd-secret -n openshift-config
Name:         htpasswd-secret
Namespace:    openshift-config
Labels:       <none>
Annotations:  <none>

Type:  Opaque

Data
====
htpasswd:  9229 bytes
[user@bastion ocp]$ oc get secret htpasswd-secret -ojsonpath={.data.htpasswd} -n openshift-config | base64 -d > users.htpasswd
[user@bastion ocp]$ htpasswd -bB users.htpasswd data_scientist temporal2020
Adding password for user data_scientist
[user@bastion ocp]$ htpasswd -bB users.htpasswd production temporal2020
Adding password for user production
[user@bastion ocp]$ oc create secret generic htpasswd-secret --from-file=htpasswd=users.htpasswd --dry-run -o yaml -n openshift-config | oc replace -f -
secret/htpasswd-secret replaced
[user@bastion ocp]$
```

If there is no HTPasswd provided you can create:

```
[user@yourhost ansible]$ ansible-playbook -i inventory create-idp.yaml
```

## Install Opendatahub operator

Using the GUI or CLI install the opendatahub operator as cluster admin.

> Not yet automated.

## Create project to work on

Create a project for **data_scientist** user to work on:

```
[user@yourhost ansible]$ ansible-playbook -i inventory create-lab.yaml
```

This will create the **binary-classification** project for **data_scientist** user and will assign project admin role to that user.

After that you will have to deploy, default configuration, opendatahub in that project.

When all is deployed you will have to increase the limits to be able to create jupyter notebooks with medium and large resource configuration:

```
[user@bastion ocp]$ oc whoami
opentlc-mgr
[user@bastion ocp]$ oc project
Using project "binary-classification" on server "https://api.cluster-syone-a5ce.syone-a5ce.example.opentlc.com:6443".
[user@bastion ocp]$ oc get limits
NAME                                         CREATED AT
binary-classification-core-resource-limits   2020-06-22T08:23:22Z
[user@bastion ocp]$
```

You can use **oc edit limits binary-classification-core-resource-limits** and you can configure something like that:

```
# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file will be
# reopened with the relevant failures.
#
apiVersion: v1
kind: LimitRange
metadata:
  creationTimestamp: "2020-06-22T08:23:22Z"
  name: binary-classification-core-resource-limits
  namespace: binary-classification
  resourceVersion: "1658716"
  selfLink: /api/v1/namespaces/binary-classification/limitranges/binary-classification-core-resource-limits
  uid: 85cdc5df-e6c7-4e10-affd-98b1356210f4
spec:
  limits:
  - default:
      cpu: 500m
      memory: 1536Mi
    defaultRequest:
      cpu: 50m
      memory: 256Mi
    max:
      cpu: "8"
      memory: 24Gi
    type: Container
  - max:
      cpu: "16"
      memory: 48Gi
    type: Pod
```

After configure:

```
[user@bastion ocp]$ oc describe limits binary-classification-core-resource-limits
Name:       binary-classification-core-resource-limits
Namespace:  binary-classification
Type        Resource  Min  Max   Default Request  Default Limit  Max Limit/Request Ratio
----        --------  ---  ---   ---------------  -------------  -----------------------
Container   cpu       -    8     50m              500m           -
Container   memory    -    24Gi  256Mi            1536Mi         -
Pod         memory    -    48Gi  -                -              -
Pod         cpu       -    16    -               
[user@bastion ocp]$
```

## Create S3 buckets

