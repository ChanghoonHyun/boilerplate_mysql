#!/usr/bin/env python3
import datetime
import json
import os.path
import subprocess
import sys

from common import print_message
from common import print_session

print_session('alter database')

print_message('get database address')

with open('config.json') as ff:
    env = json.load(ff)['mysql']

print('/* YYYYMMDD list */')
list_dir = os.listdir('./history')
list_dir.sort()
print('\n'.join(list_dir))
yyyymmdd = str(input('\nplease input YYYYMMDD: '))
yyyymmdd_today = datetime.datetime.today().strftime('%Y%m%d')

if yyyymmdd < yyyymmdd_today:
    print('Not allow to alter with script older than today (%s).' % yyyymmdd_today)
    sys.exit(0)

print('*' * 80)
print('alter data\n')

cmd_common = ['mysql']
cmd_common += ['-h' + env['host']]
cmd_common += ['-u' + env['user']]
cmd_common += ['-p' + env['password']]

cmd = cmd_common + ['--comments']

filename = './history/%s/mysql_schema_alter.sql' % yyyymmdd
if not os.path.exists(filename):
    print('file \'%s\' does not exists.' % filename)
    sys.exit(0)

with open(filename, 'r') as f:
    subprocess.Popen(cmd, stdin=f).communicate()
