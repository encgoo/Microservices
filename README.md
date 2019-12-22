# Microservices

This is a followup project of the [Kubernetes](../Kubernetes) POC. In the Kubernetes POC, Kubernetes (minikube), Docker,
and Flask are used to build a (_single_) web/API service. In some sense, it is a [monolithic](https://articles.microservices.com/monolithic-vs-microservices-architecture-5c4848858f59) 
architecture. 

Microservices architecture on the other hand recommends splitting a monolithic application into a set of
services.

This is a POC for microservices, following 
this [post](https://www.freecodecamp.org/news/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882/). It
demos how to use Kubernetes to manage/connect microservices. 

_Note_: instead of using node.js as in that post above, we will use python for all microservices in this POC.

## Architecture

This POC contains these three services:
* Presentation: A python flask server (WebServer) that returns a _static_ HTML file. The [HTML file](WebServer/templates/sentiment.html) contains
javascript code that uses AJAX to communicate with the ApiServer below.
* Application integration: A python flask server (ApiServer) that manages the RESTful API.
* Business Logic: A python flask server (LogicServer) that do the following logics:
    * Given a sentence, use python textbloc to find its polarity (same as the post above)
    * Given a polarity, find the emoji that has the closest polarity (something new/interesting we add)
    

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