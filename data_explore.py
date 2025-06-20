# %%
import pandas as pd
import geopandas as gpd
from geodatasets import get_path
import seismic_reader

# %%
nc_df = seismic_reader.read_northern_path(
    # If you have the full dataset, use:
    # "../ncedc/earthquake_catalogs/NCEDC/2025.ehpcsv"
    "../ncedc/2025.ehpcsv"
)
nc_df.head()

# %%
sc_df = seismic_reader.read_southern_path(
    # If you have the full dataset, use:
    # "../scedc/earthquake_catalogs/SCEC_DC/2025.catalog"
    "../scedc/2025.catalog"
)
sc_df.head()

# %%
nc_gdf = seismic_reader.to_gdf(nc_df)

# %%
world = gpd.read_file(get_path("naturalearth.land"))
ax = world.plot(color="white", edgecolor="black")
nc_gdf.plot(ax=ax, color="red", alpha=0.1)

# %%
sc_gdf = seismic_reader.to_gdf(sc_df)

# %%
ax = world.plot(color="white", edgecolor="black")
sc_gdf.plot(ax=ax, color="red", alpha=0.1)
