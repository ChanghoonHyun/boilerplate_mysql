#!/usr/bin/env python3
import json
import re
import subprocess
from subprocess import PIPE

from common import print_message
from common import print_session

with open('config.json') as ff:
    env = json.load(ff)['mysql']


def _manual_backup():
    print_session('dump mysql schema')

    print_message('get database address')

    database = env['database']
    host = env['host']
    password = env['password']
    user = env['user']

    _mysql_dump(host, user, password, database, './mysql_schema.sql')


def _mysql_dump(host, user, password, database, filename_path):
    ################################################################################
    print_message('dump schema')

    cmd = ['mysqldump']
    cmd += ['-h' + host]
    cmd += ['-u' + user]
    cmd += ['-p' + password]
    cmd += ['--column-statistics=0']
    cmd += ['--comments']
    cmd += ['--databases', database]
    cmd += ['--ignore-table=%s.django_migrations' % database]
    cmd += ['--no-data']

    print('\n>>> ' + ' '.join(cmd) + '\n')

    filename_path_raw = filename_path + '.raw'

    with open(filename_path_raw, 'w') as ff:
        subprocess.Popen(cmd, stdout=ff).communicate()

    with open(filename_path_raw, 'r') as ff_raw, open(filename_path, 'w') as ff:
        while True:
            line = ff_raw.readline()
            if not line:
                break

            if line.startswith('-- MySQL dump') or \
                    line.startswith('-- Host') or \
                    line.startswith('-- Server version') or \
                    line.startswith('-- Dump completed on'):
                ff.write('\n')
                continue

            line = re.sub(' AUTO_INCREMENT=[0-9]*', '', line)
            ff.write(line)

    cmd = ['rm', filename_path_raw]

    subprocess.Popen(cmd, stdout=PIPE).communicate()


################################################################################
#
# start
#
################################################################################
print_session('mysqldump data')

################################################################################
if __name__ == "__main__":
    _manual_backup()
