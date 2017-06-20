#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# Copyright (c) 2017 Tzutalin
# Create by TzuTaLin <tzu.ta.lin@gmail.com>

import argparse
import os
import schedule
import subprocess
import time
import yaml


# Color class
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Usage: colorPrint(str, Colors.HEADER or HEADER.BOLD)
def colorPrint(s, colors):
    print (colors + str(s) + Colors.ENDC)


def runCommands(arr_elems, ignore_errors=False, env_extra=None):
    # setup env
    env = os.environ
    env.update(env_extra)

    # run commands
    for elem in arr_elems:
        colorPrint(" * " + elem, Colors.BOLD)
        try:
            subprocess.check_call(elem, shell=True, env=env)
        except subprocess.CalledProcessError as e:
            if ignore_errors:
                pass
            else:
                colorPrint(" * " + elem, Colors.FAIL)
                # raise e


def doJob(ops):
    env = {}
    if 'envs' in ops:
        for key in ops['envs']:
            key = key
            value = os.path.expandvars(ops['envs'][key])
            env.update({key: value})

    if 'prepare' in ops:
        runCommands(ops['prepare'], ignore_errors=True, env_extra=env)

    if 'jobs' in ops:
        for job in ops['jobs']:
            env.update({'JOB_NAME': job})
            runCommands(ops['jobs'][job], env_extra=env)


def allowed_file(filename):
    allow_ext = set(['yaml', 'yml'])
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in allow_ext


def main():
    parser = argparse.ArgumentParser(description='task-scheduler will arrage the task according the YAML config')
    parser.add_argument('-f', '--file', type=str, help='YAML config file')
    args = parser.parse_args()

    root = None
    if args.file and allowed_file(args.file):
        stream = open(args.file, 'r')
        root = yaml.load(stream)
    else:
        colorPrint('Require [task].yaml or [task].yml file', Colors.WARNING)
        os.sys.exit(1)

    for taskname in root['task']:
        ops = root['task'][taskname]
        schedule_time_unit = ops['schedule_time_unit']
        schedule_time_every = ops['schedule_time_every']
        if schedule_time_every and schedule_time_unit:
            interval = int(schedule_time_every)
            colorPrint('Try to arrange ' + taskname + ' every ' + str(interval) + ' ' + schedule_time_unit, Colors.BOLD)
            if interval <= 1:
                eval("schedule.every().%s.do(doJob, ops)" % schedule_time_unit)
            else:
                eval("schedule.every(interval).%s.do(doJob, ops)" % schedule_time_unit)

            colorPrint('Arrange successfully: ' + taskname + ' every ' + str(interval) + ' ' + schedule_time_unit, Colors.OKBLUE)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
