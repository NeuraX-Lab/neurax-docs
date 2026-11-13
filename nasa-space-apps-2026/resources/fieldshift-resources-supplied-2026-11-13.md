# Field Shift — Resources do người dùng cung cấp ngày 2026-11-13

Nguồn tiếp nhận: nguyên văn nội dung Resources người dùng dán vào chat ngày 2026-11-13 (Asia/Saigon), được người dùng mô tả là NASA Space Apps vừa công bố. Đã bỏ ký tự escape và chuẩn hóa định dạng liên kết; giữ nội dung tiếng Anh bên dưới. Đây là snapshot của bản cung cấp, không phải chứng nhận đã đối chiếu toàn bộ tab Resources live. Trang challenge vẫn trả HTTP 502 khi kiểm qua công cụ web ngày tiếp nhận.

Các mô tả dưới đây là **source statements**. Độ phân giải, phiên bản, quyền truy cập và các diễn giải như “ground truth”, “soil health”, crop labels phải kiểm theo từng product. Xem [audit và Q&A](fieldshift-source-audit.md). Chưa chốt dataset cho AI.

## NASA Data & Resources

### R01 — Soil Moisture Active Passive (SMAP)

[SMAP](https://www.earthdata.nasa.gov/data/platforms/space-based-platforms/smap): SMAP provides global measurements of surface soil moisture and freeze/thaw state, collected every 2–3 days. Soil-moisture information helps identify drought stress, water availability, infiltration potential, and early crop-stress signals. These data are valuable for evaluating rotation crops that could improve water efficiency, soil conditions, or drought resilience.

### R02 — Global Precipitation Measurement (GPM) & IMERG

[GPM data](https://gpm.nasa.gov/data): The GPM mission and its IMERG product provide global precipitation rate and accumulation estimates. These help assess rainfall reliability, extreme-storm frequency, erosion risk, water input to soils, and long-term trends in field moisture. IMERG is valuable for comparing rotation strategies under different precipitation scenarios. (Worldview IMERG layers can be downloaded directly as high-resolution images.)

### R03 — Landsat and MODIS/VIIRS: Reflectance, NDVI, Vegetation Indices

[Landsat](https://earthexplorer.usgs.gov/), [MODIS](https://lpdaac.usgs.gov/products/), [VIIRS](https://search.earthdata.nasa.gov/search?q=VIIRS): Landsat (30-meter resolution) and MODIS/VIIRS (250–1000 m) provide corrected reflectance, NDVI, vegetation indices, and indicators of plant stress, bare ground, and seasonal change. These datasets allow participants to map crop vigor, track seasonal transitions, detect high-stress periods, and compare rotation options visually.

### R04 — NASA POWER: Agroclimatology & Meteorological Data

[NASA POWER](https://power.larc.nasa.gov/): NASA POWER provides accessible solar, meteorological, and climatology datasets used widely in agriculture. The datasets include temperature, humidity, radiation, and derived indicators that help estimate crop water use, growing-season conditions, frost risk, and climate suitability for potential rotation crops.

### R05 — Shuttle Radar Topography Mission (SRTM): Elevation & Terrain Models

[SRTM](https://www.earthdata.nasa.gov/data/instruments/srtm): The Shuttle Radar Topography Mission (SRTM) provides global elevation data suitable for analyzing slope, runoff, erosion risk, water flow, and terrain-driven stress conditions. Terrain patterns help determine which rotation crops may improve infiltration, reduce erosion, or stabilize soil on slopes.

### R06 — ECOSTRESS

[ECOSTRESS data](https://ecostress.jpl.nasa.gov/data): ECOSTRESS measures land-surface temperature (LST) and evapotranspiration (ET) at high spatial resolution. This helps detect hotspots of plant stress, heat exposure, shallow-root vulnerability, and crop-water demand. It is particularly useful for identifying when current crops may be becoming more vulnerable and for mapping field-level microclimate differences.

### R07 — USDA Ag Data Commons: Open Access Agricultural Datasets

[USDA Ag Data Commons](https://www.nal.usda.gov/services/agdatacommons): USDA’s Ag Data Commons provides open-access agricultural datasets covering soils, crops, climate, land management, phenology, water quality, and ecological conditions. These datasets offer valuable ground-based and agricultural context that can complement NASA’s satellite observations. Participants may use Ag Data Commons to incorporate local crop information, soil-property measurements, management practices, and field-level agricultural research into their models. These data can help SI tools align NASA’s environmental indicators with practical farm-level constraints and crop-rotation realities.

### R08 — Web Soil Survey (WSS)

[WSS](https://websoilsurvey.nrcs.usda.gov/app/): The WSS, maintained by USDA’s Natural Resources Conservation Service (NRCS), provides official U.S. soil data, including detailed soil maps, soil properties, drainage classifications, erosion risk, hydrologic ratings, and suitability for different land uses. Participants may use WSS to identify field-specific soil characteristics—such as organic matter, texture, infiltration, and compaction risk—which can improve SI-driven rotation recommendations. Integrating NASA Earth observations with WSS data may help teams build stronger, locally accurate interpretations of soil health and crop suitability.

### R09 — Cropland Data Layer (CDL): CropScape

[CropScape](https://nassgeodata.gmu.edu/CropScape/): The USDA CDL provides annual, high-resolution (30-meter) cropland classifications for the United States, identifying specific crop types such as corn, soybeans, cotton, wheat, alfalfa, and more. These data can help participants examine existing crop rotations, track changes across seasons, identify bare fields, evaluate crop suitability, and compare local cropping patterns with NASA-observed environmental conditions. The CDL can also support SI models by supplying labeled land-cover inputs tied to real agricultural production.

### R10 — PRISM Climate Data: Oregon State University

[PRISM](https://prism.oregonstate.edu/): PRISM provides high-quality climate datasets for the United States, including daily, monthly, and 30-year climate normals for precipitation, temperature, dewpoint, frost/freeze dates, and more. Because PRISM incorporates topographic effects, it offers highly accurate climate context for local farms. Participants may use PRISM to assess long-term climate trends, align rotation strategies with local temperature and rainfall history, and validate environmental stress indicators derived from NASA satellites.

### R11 — USDA NRCS SSURGO/STATSGO2: Soil Data

[NRCS soils](https://www.nrcs.usda.gov/resources/data-and-reports/soils): SSURGO (field-scale) and STATSGO2 (regional-scale) provide detailed soil attributes such as texture, organic matter, drainage class, hydrologic soil group, erosion-risk factors, restrictive layers, and water-holding capacity. These data complement NASA observations by enabling accurate, location-specific assessments of soil health, erosion potential, infiltration dynamics, and crop suitability. Integrating SSURGO with NASA datasets can help SI models produce more grounded and agronomically meaningful rotation suggestions.

### R12 — National Agriculture Imagery Program (NAIP)

[NAIP](https://naip-usdaonline.hub.arcgis.com/): NAIP provides high-resolution (typically 1-meter) aerial imagery captured during the U.S. growing season. These images allow participants to map field boundaries, detect bare soil periods, observe crop development, monitor land-management changes, and assess vegetation cover at fine spatial scales. NAIP imagery can serve as a powerful input for training SI models that require closer-than-satellite detail or for validating crop and soil-condition patterns detected from NASA Earth observations.

### R13 — USGS National Land Cover Database (NLCD)

[NLCD](https://www.usgs.gov/centers/eros/science/national-land-cover-database): NLCD offers land-cover and land-use classifications at 30-meter resolution across multiple decades. This dataset helps identify farmland, pasture, forested areas, water bodies, wetlands, and development zones near agricultural fields. Participants may use NLCD to contextualize landscape features that influence microclimates, water availability, erosion risk, and pest dynamics. NLCD also supports long-term analysis of land-cover change and its relationship to farm vulnerability.

### R14 — NLDAS/GLDAS: Land Data Assimilation Systems

[Earthdata](https://www.earthdata.nasa.gov/): NLDAS and GLDAS combine satellite and ground-based meteorological observations to generate gridded datasets of temperature, precipitation, soil moisture, evapotranspiration proxies, radiation, and other surface variables at sub-daily resolution. These datasets help participants study drought onset, moisture deficits, growing-season transitions, and environmental stress conditions. When combined with NASA’s mission-based datasets, NLDAS/GLDAS can enhance SI models by providing continuous time-series climate features. (search “NLDAS” or “GLDAS” within Earthdata Search.)

### R15 — FAO Global Agro-Ecological Zones (GAEZ)

[GAEZ](https://gaez.fao.org/): GAEZ provides global agro-climatic suitability layers for dozens of crops, along with soil constraints, water availability indicators, yield potentials, and land-productivity assessments. These resources can help participants evaluate whether proposed rotation crops align with local climate and soil conditions, and compare multiple rotation scenarios from a global agronomic perspective.

### R16 — CoCoRaHS: Community Rain/Snow Observations

[CoCoRaHS maps](https://www.cocorahs.org/Maps): CoCoRaHS offers crowd-sourced daily precipitation measurements across North America. Participants may use this dataset to validate satellite rainfall estimates (such as IMERG), detect hyper-local extreme rain events affecting specific fields, and refine model accuracy for water-stress or irrigation-timing predictions.

### R17 — USGS National Water Information Systems (NWIS)

[NWIS](https://waterdata.usgs.gov/nwis): NWIS provides long-term records of groundwater levels, streamflow, river stages, and water-quality measurements. These data can help participants assess water availability for irrigation, identify hydrologic stress, understand downstream erosion risks, and compare NASA-observed moisture conditions with in-situ observations.

### R18 — USDA AMS Market News

[Market News](https://www.ams.usda.gov/market-news): USDA Market News publishes commodity prices, demand trends, and market conditions for crops and livestock. Participants may use these data to help determine whether proposed rotation crops have viable markets locally or regionally—an important farmer-driven constraint when evaluating rotation strategies.

### R19 — USDA NASS QuickStats

[QuickStats](https://quickstats.nass.usda.gov/): QuickStats provides county-level and state-level agricultural statistics, including yields, planted acreage, production history, and crop frequency. These data can help participants calibrate their models against historical performance, compare rotation possibilities, and explore long-term agricultural trends.

### R20 — OpenET: Evapotranspiration for Water Management

[OpenET](https://openetdata.org/): OpenET delivers field-scale evapotranspiration estimates using satellite-driven models for western U.S. states. Participants may use this dataset to evaluate crop water demand, irrigation timing, water-use efficiency, and identify fields under thermal or moisture stress. OpenET offers valuable ground-truth ET information that complements ECOSTRESS and NASA POWER.

### R21 — USFS LANDFIRE: Vegetation & Fuel Layers

[LANDFIRE](https://www.landfire.gov/): LANDFIRE provides vegetation type, vegetation condition, fuel models, and landscape characteristics across the United States. These data may be used to understand local ecosystems, perennial cover, tree-crop interactions, and landscape features that affect microclimates, water flow, erosion, and biodiversity relevant to rotational planning.

### R22 — Global Ecosystem Dynamics Investigation (GEDI)

[GEDI data](https://gedi.umd.edu/data): GEDI provides high-resolution laser-based measurements of forest structure, including canopy height, leaf area index, and above-ground biomass. Participants may use GEDI Level-4 biomass products to understand vegetation density, canopy stress, and long-term ecosystem changes around agricultural landscapes. While GEDI is most effective in areas with taller vegetation, its biomass and canopy metrics can help identify shifts in surrounding land cover, detect environmental stress impacts, and complement rotation-crop analysis by providing structural context that pairs well with SMAP, Landsat, and MODIS vegetation indicators.

## Space Agency Partner Resources

### R23 — Copernicus Sentinel-2: ESA

[Copernicus Data Space](https://dataspace.copernicus.eu/): Sentinel-2 provides freely accessible 10–20-meter multispectral imagery at high revisit frequency. With bands specifically designed for vegetation analysis (red-edge, NIR, SWIR), participants may use Sentinel-2 for NDVI/EVI, bare-soil mapping, crop stress detection, and fine-scale monitoring during growing seasons. Its higher spatial resolution complements Landsat and MODIS for field-level assessments.

### R24 — ERA5: ECMWF Reanalysis

[ERA5 single levels](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview): ERA5 is a global reanalysis dataset that provides hourly climate variables such as temperature, precipitation, wind, humidity, soil temperature, and radiation. Participants may use ERA5 to fill gaps where local weather stations are sparse, analyze long-term climate trends, build temporal features for SI models, and contextualize NASA Earth observations with continuous climate time series.
