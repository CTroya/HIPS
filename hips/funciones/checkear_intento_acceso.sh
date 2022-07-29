#!/bin/bash
# cambiar el /var/log/auth.log por /var/log/secure
grep "Failed password for" /var/log/auth.log | grep -v grep > /intento_acceso.txt