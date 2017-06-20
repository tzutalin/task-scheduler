#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'schedule',
    'pyyaml'
]

test_requirements = [
    'schedule',
    'pyyaml'
]

setup(
    name='py-task-scheduler',
    version='0.0.3',
    description="A tool to help you schedule your task according to your config file",
    long_description=readme + '\n\n' + "Usage: py-task-scheduler -f task.yaml",
    author="TzuTa Lin",
    author_email='tzu.ta.lin@gmail.com',
    url='https://github.com/tzutalin/task-scheduler',
    packages=[
        'taskscheduler'
    ],
    package_dir={'taskscheduler': 'taskscheduler'},
    entry_points={
        'console_scripts': [
            'py-task-scheduler=taskscheduler.taskscheduler:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='taskscheduler',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
