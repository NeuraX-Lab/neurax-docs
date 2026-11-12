> Sửa phạm vi 12/11: AOI chính là xã Mỹ Thành (AOI-MT-ADMIN-v1). POWER/SoilGrids dưới đây vẫn là query điểm, không phải trung bình cả xã; SCL 419 pixel chỉ áp cho mẫu 17 ha thủ công cũ. Ranh chính nguồn nằm ở `imagery/official-my-thanh-geometry.json`; ảnh xã ở `imagery/admin-satellite-raw.png` và extent ở `admin-map-export.json`. Xem hồ sơ case để phân biệt chính/illustrative.

# Snapshot dữ liệu AOI-MT-01, Mỹ Thành–Cai Lậy

Mục tiêu: sẵn dữ liệu công khai cho AOI cố định, không cần khảo sát thực địa để bắt đầu prototype. [Hồ sơ và bản đồ](../../../planning/cases/my-thanh-cai-lay/README.md). Đã tải 12/11/2026, chưa push.

| Thành phần | Artifact / phạm vi |
| --- | --- |
| NASA POWER | [raw JSON](power_daily_2015_2025.json), [daily.csv](daily.csv), 4.018 ngày UTC 2015–2025, bốn biến; sample tại tâm AOI |
| SoilGrids | `soilgrids/*.tif`, 15 WCS coverage; pH ba tầng tới 30 cm, cát/sét tầng 0–5 cm; mean/Q05/Q95 |
| Retrieval | [retrieval.json](retrieval.json): request URLs, UTC, status, MIME, bytes/SHA của POWER/WCS |
| Tổng hợp/QA | [summary.json](summary.json): unit, support, flags, soil model values và giới hạn |
| Ảnh nền | `imagery/my-thanh-detail.png`, `my-thanh-close.png` và JSON export có **extent thực trả về**, EPSG:4326 |
| Citation ảnh | [imagery/aoi-imagery-citation.json](imagery/aoi-imagery-citation.json): metadata layer12 Esri, source date 2025-08-07; không là ngày chụp 2026 |
| Sentinel-2 | `imagery/sentinel-2026-11-05.png`, `sentinel-2026-03-25.png`: TCI/visual, không dùng làm reflectance |
| QA SCL | `imagery/scl-*.tif`: categorical nearest, output EPSG:4326; lấy pixel centers trong AOI, không tính trên cả tile |
| STAC và render URL | [imagery/pc-scenes.json](imagery/pc-scenes.json), `imagery/render-*.json`: item IDs, time, processing baseline, assets; các asset reflectance đầy đủ chưa tải |
| Ranh xã tham khảo | [imagery/my-thanh-boundary.geojson](imagery/my-thanh-boundary.geojson), commit pin trong `boundary-source-commit.txt`; không phải AOI hoặc ranh địa chính |

**POWER QA=WARN:** 14/06/2020 có 488,17 mm/day vượt threshold khám phá 200. Không xóa/sửa. Các mảng biến giống probe Long Khánh vì support nguồn thô, không tăng độ phân giải hoặc coi là hai chuỗi đo độc lập. Chưa đối chiếu ERA5 tại điểm này; không chuyển kiểm chứng từ Đức Lập sang đây. Không tính water deficit/forecast/yield.

**SoilGrids là mô hình**, native 250 m/Homolosine, WCS trả EPSG:4326 và resample chưa xác minh; sample ở ô chứa tâm không phải trung bình đo cả AOI. Integer /10 theo [unit chính thức ISRIC](https://docs.isric.org/globaldata/soilgrids/SoilGrids_faqs_01.html); 0 không diễn giải thành giá trị đất hợp lệ. Q05/Q95 là khoảng dự đoán mô hình. Không có EC/drainage/đế cày hoặc mẫu đất tại ruộng.

Credit/nguồn: [NASA POWER](https://power.larc.nasa.gov/docs/services/api/temporal/daily/); [ISRIC SoilGrids WCS, CC-BY-4.0](https://docs.isric.org/globaldata/soilgrids/wcs.html); Contains modified Copernicus Sentinel data (2026), qua [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/dataset/sentinel-2-l2a); Esri, Vantor, Earthstar Geographics, and the GIS User Community. Ranh tham khảo từ [Vietnamese Provinces Database](https://github.com/ThangLeQuoc/vietnamese-provinces-database), dẫn nguồn bản đồ hành chính của NXB Tài nguyên–Môi trường và Bản đồ Việt Nam; README gốc/citation/commit được lưu. Không gộp quyền sử dụng Esri imagery với license SoilGrids hoặc Sentinel.

Chạy cached audit: `scripts/research/prepare_my_thanh_sources.py`; dựng bản đồ/QA: `scripts/research/build_my_thanh_aoi.py`, từ root repo. Python Windows 3.12.14/Pillow 13.0.0, không cài dependency mới. Chỉ dùng `--refresh` với script nguồn khi muốn thay snapshot. Các URL export ảnh gốc có thể hết hạn; bbox, CRS, size và API nguồn được lưu để tạo lại export.
