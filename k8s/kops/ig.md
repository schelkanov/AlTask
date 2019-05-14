apiVersion: kops/v1alpha2
kind: InstanceGroup
metadata:
  creationTimestamp: 2019-05-14T14:04:05Z
  labels:
    kops.k8s.io/cluster: alex-csv-demo.k8s.local
  name: master-us-west-2a
spec:
  image: kope.io/k8s-1.11-debian-stretch-amd64-hvm-ebs-2018-08-17
  machineType: t2.micro
  maxSize: 1
  minSize: 1
  nodeLabels:
    kops.k8s.io/instancegroup: master-us-west-2a
  role: Master
  subnets:
  - us-west-2a

---

apiVersion: kops/v1alpha2
kind: InstanceGroup
metadata:
  creationTimestamp: 2019-05-14T14:04:06Z
  labels:
    kops.k8s.io/cluster: alex-csv-demo.k8s.local
  name: nodes
spec:
  image: kope.io/k8s-1.11-debian-stretch-amd64-hvm-ebs-2018-08-17
  machineType: t2.small
  maxSize: 1
  minSize: 1
  nodeLabels:
    kops.k8s.io/instancegroup: nodes
  role: Node
  subnets:
  - us-west-2a

---

apiVersion: kops/v1alpha2
kind: InstanceGroup
metadata:
  creationTimestamp: 2019-05-14T14:14:01Z
  labels:
    kops.k8s.io/cluster: alex-csv-demo.k8s.local
  name: spotnodes
spec:
  image: kope.io/k8s-1.11-debian-stretch-amd64-hvm-ebs-2018-08-17
  machineType: t2.medium
  maxPrice: "0.07"
  maxSize: 1
  minSize: 1
  nodeLabels:
    kops.k8s.io/instancegroup: spotnodes
  role: Node
  subnets:
  - us-west-2a
