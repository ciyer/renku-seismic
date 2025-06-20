import geopandas as gpd
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


def read_northern_path(file_path):
    """
    Read a EHP CSV file from the Northern California Seismic System (NCEDC).
    See: https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php
    """

    # E.g.: ncedc/earthquake_catalogs/NCEDC/2025.ehpcsv
    df = pd.read_csv(file_path, encoding="cp1252")
    return df


def read_raw_southern_path(file_path):
    """
    Read a catalog file from the Southern California Seismic Network (SCSN).
    See: https://scedc.caltech.edu/eq-catalogs/
    """
    df = pd.read_csv(file_path, sep="\s+", skiprows=9)
    df = df.drop(index=[df.index[-1]])
    df["MAG"] = df["MAG"].astype(float)
    return df


def read_southern_path(file_path):
    """
    Read a catalog file from the Southern California Seismic Network (SCSN).
    See: https://scedc.caltech.edu/eq-catalogs/
    """
    df = read_raw_southern_path(file_path)
    # TODO: rename columns
    tdf = df.rename(
        columns={"LAT": "latitude", "LON": "longitude", "DEPTH": "depth", "MAG": "mag"}
    )
    return tdf


def to_gdf(df, crs="EPSG:4326"):
    """
    Convert a DataFrame with latitude and longitude to a GeoDataFrame.
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with 'latitude' and 'longitude' columns.
    crs : str, optional
        Coordinate reference system (CRS) to use for the GeoDataFrame.
        Default is "EPSG:4326" (WGS 84).
    """
    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs=crs
    )
    return gdf
