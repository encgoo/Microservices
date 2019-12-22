# Microservices

This is a followup project of the [Kubernetes](../Kubernetes) POC. In the Kubernetes POC, Kubernetes (minikube), Docker,
and Flask are used to build a web/API service.

Now we go further to build a POC for microservice, following 
this [post](https://www.freecodecamp.org/news/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882/).

Instead of using node.js as in that post, we will use python here.

## Minikube
Minikube is used to create local Kubernetes cluster. This POC runs on Debian 9 VM. Refer to [Minikube](../Kubernetes/README.md) for
instruction on installing minikube on Debian 9 VM. 

Run this to make sure everything is working first.

* Start minicube

    ```sudo -E minikube start --vm-driver=none```
* check kube system services

    ```kubectl get services -n kube-systemn```
    
## Steps
These are the steps to use