#!/bin/bash
# cambiar el /var/log/auth.log por /var/log/secure
grep "Failed password for" /var/log/secure | grep -v grep > /var/log/hips/intento_acceso.log