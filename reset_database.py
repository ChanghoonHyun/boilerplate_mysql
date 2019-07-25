#!/usr/bin/env python3
import json
import re
import subprocess
from datetime import datetime

from common import print_session

print_session('reset database')

with open('config.json') as ff:
    env = json.load(ff)['mysql']

if re.match(r'^op-', env['host']):
    print('\'OP\' phase does not allow this operation.')
    raise Exception()

cmd_common = ['mysql']
cmd_common += ['-h' + env['host']]
cmd_common += ['-u' + env['user']]
cmd_common += ['-p' + env['password']]

start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(' '.join(['Started at:', start_time]))

cmd = cmd_common + ['-e', 'DROP DATABASE IF EXISTS `%s`;' % env['database']]
subprocess.Popen(cmd).communicate()

cmd = cmd_common + ['-e', 'CREATE DATABASE `%s` CHARACTER SET utf8;' % env['database']]
subprocess.Popen(cmd).communicate()

cmd = cmd_common + ['--comments']

filename = './mysql_schema.sql'
with open(filename, 'r') as f:
    subprocess.Popen(cmd, stdin=f).communicate()

filename = './mysql_data.sql'
with open(filename, 'r') as f:
    subprocess.Popen(cmd, stdin=f).communicate()

finish_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(' '.join(['Finished at:', finish_time]))
