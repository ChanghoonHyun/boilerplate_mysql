# Boilerplate for mysql

## How to setup

This server uses Vagrant on VirtualBox

1. Download and install Vagrant and VirtualBox on your machine

    1. VirtualBox: https://www.virtualbox.org/wiki/Downloads
    
    1. Vagrant: https://www.vagrantup.com/downloads.html

1. Clone repository using `$ git clone git@github.com:ChanghoonHyun/boilerplate_mysql.git`

1. Copy config.json.sample to config.json using `boilerplate_mysql $ cp config.json.sample config.json` 

1. Open `config.json` and edit values

1. Move to provisioning folder using `$ cd boilerplate_mysql/_provisioning`

1. Create vagrant using  `boilerplate_mysql/_provisioning $ vagrant up`

## How to load schema and data

1. Run `./reset_database.py` to load schema and data to database

## How to alter schema and data

1. Create a folder under history folder in the format YYYYMMDD

2. Write alter query for schema and data  
