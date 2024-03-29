# Boilerplate for mysql

## How to setup

This server uses Vagrant on VirtualBox

1. Download and install Vagrant and VirtualBox on your machine

    1. VirtualBox: https://www.virtualbox.org/wiki/Downloads
    
    1. Vagrant: https://www.vagrantup.com/downloads.html

1. Clone repository using `$ git clone git@github.com:ChanghoonHyun/boilerplate_mysql.git`

1. Move to boilerplate_mysql folder using `$ cd boilerplate_mysql`

1. Copy public key using `boilerplate_mysql $ cp ~/.ssh/id_rsa.pub _provisioning/ansible/roles/ssh/rsa/` or generate public key at _provisioning/ansible/roles/ssh/rsa/

1. Copy rc.local using `boilerplate_mysql $ cp _provisioning/ansible/roles/common_tasks/rc.local.sample _provisioning/ansible/roles/common_tasks/rc.local`  

1. Copy config.json.sample to config.json using `boilerplate_mysql $ cp config.json.sample config.json` 

1. Open `config.json` and edit values

1. Move to provisioning folder using `$ cd _provisioning`

1. Create vagrant using  `boilerplate_mysql/_provisioning $ vagrant up`

## How to load schema and data

1. Run `boilerplate_mysql/ $ ./reset_database.py`

## How to dump schema

1. Run `boilerplate_mysql/ $ ./mysqldump_schema.py`

## How to dump data

1. Run `boilerplate_mysql/ $ ./mysqldump_data.py`

## How to alter schema and data

1. Create a folder under history folder in the format YYYYMMDD for your patch date

1. Write alter query for schema and data

1. Run `boilerplate_mysql/ $ ./alter_database.py`

1. Input your patch date
