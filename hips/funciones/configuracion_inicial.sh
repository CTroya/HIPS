#!/bin/bash
# Creo el directorio y los .log para las alarmas y los modulos de prevencion
if [ ! -d '/var/log/hips' ]
then
    mkdir /var/log/hips
    if [ ! -f '/var/log/hips/alarmas.log' ]
    then
        touch /var/log/hips/alarmas.log
    fi
    if [ ! -f '/var/log/hips/prevencion.log' ] 
    then
        touch /var/log/hips/prevencion.log
    fi
fi
# Creo los directorios para los backups que usamos de comparacion
if [ ! -d '/backup' ]
then 
    mkdir /backup
    if [ ! -d '/backup/hashes' ]
    then
        mkdir /backup/hashes
        if [ ! -d '/backup/hashes/bin' ]
        then 
            mkdir /backup/hashes/bin
        fi
        if [ ! -d '/backup/hashes/etc' ]
        then
            mkdir /backup/hashes/etc
        fi
    fi
fi
# Creo el directorio de cuarentena
if [ ! -d '/cuarentena' ]
then
    mkdir /cuarentena
fi
# Creo el directorio de ejemplos de ataques
if [ ! -d '/ataques' ]
then
    mkdir /ataques
fi