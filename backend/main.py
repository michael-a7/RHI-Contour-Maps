from fastapi import FastAPI, Query
from fastapi.responses import FileResponse,StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import pandas as pd
import netCDF4 as nc
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import BoundaryNorm, ListedColormap
import os
import io


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)


@app.get("/image")
async def get_image(t: str = Query(..., description = "Date in format YYYY_MM_DD")):
    date = t.replace("_", "-")
    filename = f"wbgt_{date}.nc"
    data_path = Path(__file__).parent/ "data"/ filename
    ds = nc.Dataset(data_path)
    lat = np.array(ds.variables['lat'])
    lon = np.array(ds.variables['lon'])
    time = np.array(ds.variables['time'])
    wbgt = np.array(ds.variables['wbgt'])

    lat_min = np.min(lat)
    lat_max = np.max(lat)
    lon_min = np.min(lon)
    lon_max = np.max(lon)
    lat_mask = (lat >= lat_min) & (lat <= lat_max)
    lon_mask = (lon >= lon_min) & (lon <= lon_max)
    filtered_lat = lat[lat_mask]
    filtered_lon = lon[lon_mask]
    filtered_wbgt = np.squeeze(wbgt[:, lat_mask, :][:, :, lon_mask])

    bounds = np.linspace(26, 88, 11)
    colors = ["#08306b","#2171b5","#6baed6","#bdd7e7","#31a354","#78c679","#d9ef8b","#fee08b","#fc8d59","#d73027","#a50026"]
    cmap = ListedColormap(colors)
    norm = BoundaryNorm(bounds, cmap.N)

    fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, figsize = (10,8))
    ax.plot
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.add_feature(cfeature.COASTLINE)
    ax.set_extent([lon_min,lon_max,lat_min,lat_max])

    lon_grid, lat_grid = np.meshgrid(filtered_lon, filtered_lat)
    plt.contourf(lon_grid, lat_grid, filtered_wbgt,levels = bounds, transform=ccrs.PlateCarree(), cmap=cmap, norm = norm,)
    contours = plt.contour(lon_grid, lat_grid, filtered_wbgt,levels = bounds, colors = 'black', linewidths=1 )
    labels = ax.clabel(contours, inline=True,inline_spacing=10, fontsize=10, fmt='%d', colors='black')
    for txt in labels:
        txt.set_rotation(0)
    buf = io.BytesIO()
    ax.set_axis_off()
    plt.savefig(buf, format = 'png', bbox_inches='tight', pad_inches=0)
    buf.seek(0)
    plt.close(fig)

    return StreamingResponse(buf, media_type = "image/png", headers = {
        "Access-Control-Allow-Origin": "*"
    })