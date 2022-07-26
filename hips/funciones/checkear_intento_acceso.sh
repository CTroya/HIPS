#!/bin/bash
# cambiar el /var/log/auth.log por /var/log/secure
exec `grep "Failed password for" /var/log/auth.log > intento_acceso.txt`