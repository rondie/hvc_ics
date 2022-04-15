## Description
Flask web app which generates an ics file, using input from the request:<br>
 `/hvc-<postalcode>-<housenumber>.ics`
only works if you're in an HVC region where they collect (https://www.hvcgroep.nl/)

## Container
uid:gid set to 1000:1000

Environment variables that can be set:
| Name | default |
| ---- | ------- |
| HVC_ICS_HOST | 0.0.0.0 |
| HVC_ICS_PORT | 80 |
| HVC_ICS_WORKERS | 4 |
| HVC_ICS_THREADS | 4 |
| HVC_ICS_TIMEOUT | 120 |
