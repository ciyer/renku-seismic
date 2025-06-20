# renku-seismic

A project for plaing with public data sets on on AWS:

* https://registry.opendata.aws/northern-california-earthquakes/
* https://registry.opendata.aws/southern-california-earthquakes/


# Data Connectors

When creating data connectors, it is not necessary to mount the full datasets, which are large. You can just mount the `earthquake_catalog` folders.

Data connector 1: Northern California Earthquake Data

| Field        | Value                                         |
|--------------|-----------------------------------------------|
| Source path  | `ncedc-pds/earthquake_catalogs/NCEDC/`        |
| Name         | Northern California Earthquake Data           |
| Mount point  | `ncedc`                                       |

Data connector 2: Southern California Earthquake Data

| Field        | Value                                         |
|--------------|-----------------------------------------------|
| Source path  | `scedc-pds/earthquake_catalogs/SCEC_DC/`      |
| Name         | Southern California Earthquake Data           |
| Mount point  | `scedc`                                       |
