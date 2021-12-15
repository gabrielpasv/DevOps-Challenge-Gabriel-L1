
# PlanA DevOps Challenge 1 - Resolution

This is the resolution of the Plan A challenge 1 located [here](https://github.com/Plan-A-Technologies/DevOps-Challenge-Level-1)

If you want to build the application yourself, then you will need to have a docker hub account and update *k8s/deployment.yaml* file with the correct docker image name.

## Requirements

1. Docker - [how do install docker](https://docs.docker.com/engine/install/)
2. A docker Hub account - [create it here](https://hub.docker.com/signup)
3. Minikube - [how to install minikube](https://minikube.sigs.k8s.io/docs/start/)
4. kubectl - [how to install kubectl](https://kubernetes.io/docs/tasks/tools/)

## To build

In the **src/** folder you can find the app and the dockerfile.

To build, navigate to the **src/** and run:

```docker build -t devops-challenge-gabriel-l1 .```


To push to docker hub. First run *docker login* to authenticate, then:

``` docker tag devops-challenge-gabriel-l1 <your_dockerhub_account>/devops-challenge-gabriel-l1```

and

```docker push <your_dockerhub_account>/devops-challenge-gabriel-l1```

## To Deploy

To deploy it on kubernetes, first make sure you have access to a k8s cluster or minikube, then navigate to *k8s/* folder and run:

```kubectl apply -f deployment.yaml,service.yaml```

Note that I am using my own docker hub account.

You can run the command below to make sure pod is in running state

```
gabriel@gabriel-Inspiron:~/challenges/DevOps-Challenge-Gabriel-L1/k8s$ kubectl get pod
NAME                         READY   STATUS    RESTARTS   AGE
challenge1-c94944d59-2xdnj   1/1     Running   0          73s
```



## To Access

To access the application, you can run the following to get the port and IP address. Since I am using NodePort for this demo.

```
gabriel@gabriel-Inspiron:/tmp$ kubectl get svc
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
challenge1   NodePort    10.111.77.96   <none>        80:32107/TCP   39m
```

Then get the minikube IP

```
gabriel@gabriel-Inspiron:/tmp$ minikube ip
192.168.99.101
```

And finally try to access it
```
gabriel@gabriel-Inspiron:/tmp$ curl -s http://192.168.99.101:32107 |jq
{
  "engine": "3.8.12",
  "hostname": "challenge1-c94944d59-s9br6",
  "timestamp": "Tue, 14 Dec 2021 23:01:20 GMT",
  "visitor ip": "172.17.0.1"
}
```
