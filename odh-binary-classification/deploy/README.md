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