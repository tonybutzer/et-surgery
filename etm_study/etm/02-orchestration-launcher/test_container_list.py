#!/usr/bin/env python
# coding: utf-8
import time
import docker
import os
import subprocess
import re

client = docker.from_env()

try:
    running_containers = client.containers.list()
except:
    running_containers=[]
for c in running_containers:
    print(c.name)

