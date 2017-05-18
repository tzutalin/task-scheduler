==============
task-scheduler
==============

task-scheduler is an in-process scheduler to arrange and run the task periodically according to YAML config file

Inspired by `schedule <https://schedule.readthedocs.io/en/stable>`_

Usage
-----

.. code-block:: bash

    $ git clone https://github.com/tzutalin/labelImg
    $ cd task-scheduler
    $ python task-scheduler.py -f tasks.yml


This is a tasks.yml example file::

  task:
     <First task name>
       schedule_time_unit: [seconds/minutes/hours/day/monday/Thusday]
       schedule_time_every: 1
       prepare:
          - <shell command>
          - <shell command>
       jobs:
         <jobname>:
           - <shell command>
         <jobname>:
           - <shell command>

In the example below, we have two jobs, a `prepare` job is used to install the additional package::

  task:
     schedule_task1:
       schedule_time_unit: seconds
       schedule_time_every: 2

       jobs:
         test1:
           - echo 'Hi, this is task-scheduler'

     schedule_task2:
       schedule_time_unit: minutes
       schedule_time_every: 2

       prepare:
         - pip install pyyaml

       jobs:
         test1:
           - echo 'Hello world'
