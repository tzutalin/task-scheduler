#!/bin/sh
# Packaging
sudo rm -rf py_task_scheduler.egg-info/ build/ dist
sudo python setup.py sdist;sudo python setup.py install
# Test : pip -v install --no-index --find-links dist/ py-task-scheduler
# Release please check your ~/.pypirc
# python setup.py register
# python setup.py sdist upload
