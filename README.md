# renku-seismic

A project for plaing with public data sets on on AWS:

* https://registry.opendata.aws/northern-california-earthquakes/
* https://registry.opendata.aws/southern-california-earthquakes/


# Data Connectors

When creating data connectors, it is not necessary to mount the full datasets, which are large. You can just mount the `earthquate_catalog` folders.

* Name: Northern California Earthquake Data
* Source path: ncedc-pds/earthquake_catalogs/NCEDC/
* Mount point: ncedc

* Name: Southern California Earthquake Data
* Source path: scedc-pds/earthquake_catalogs/SCEC_DC/
* Mount point: scedc
