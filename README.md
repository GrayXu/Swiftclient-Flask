# Swiftclient-Flask （华中科技大学 物联网存储实验2019春）

## Intro

An Openstack Swift's client built on flask.

## Funcion

- CURD
- Get temporary downlaod URL by your key (*edit "mykey.txt"*).

## how to use

`python3 my.py`

## Dependence

### Server

Openstack-swift  
how to install by docker? [view docker info&doc here](https://github.com/cs-course/openstack-swift-docker)


### Client 

python-swiftclient: provide swift's high level python api. [view doc here](https://docs.openstack.org/python-swiftclient/3.2.0/index.html)  
install by pip: `pip install python-swiftclient`

## Todo List

- upload&download big files by multi-threads
- operation on container level
- file list filter
- directory support
- resume from break-point