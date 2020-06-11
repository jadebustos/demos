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

## Deployment

The deploy will:

+ Create a HTPasswd identity provider with two users:
  + **data_scientist** user with password **r3dh4t**.
  + **production** user with password **r3dh4t**.