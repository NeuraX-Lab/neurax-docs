# SoilGrids: truy cập WCS được, chưa xác minh đất tiểu vùng

Ngày kiểm 12/11/2026. Đây là **probe tại điểm địa danh**, không phải đánh giá đất ruộng Đức Hạnh 1. [Hồ sơ địa phương](../../../../planning/cases/duc-lap/local-feasibility-study.md) giải thích phạm vi và cách sử dụng.

Đã tải 18 GeoTIFF: pH H2O, sand, clay × 0–5/5–15 cm × mean/Q0.05/Q0.95. Cửa sổ EPSG:4326 `[106.42,10.89,106.47,10.94]` do người nghiên cứu đặt quanh điểm GeoNames `(106.44351,10.91123)`, chưa intersect ranh ấp/thửa hoặc cropland mask. Điểm không là farm centroid. Không công bố trung bình đất của xã/ấp từ cửa sổ này.

- [retrieval.json](retrieval.json): URL, thời điểm UTC, MIME, bytes và SHA-256 cho từng file.
- [summary.json](summary.json): native/returned grid, phép đổi unit, các giá trị và giới hạn.
- [reference-values.csv](reference-values.csv): 18 giá trị integer/converted ở ô chứa điểm địa danh.
- Các `*-capabilities.xml` xác nhận coverage IDs; [phh2o-describe.xml](phh2o-describe.xml) xác nhận lưới gốc 250 m, EPSG:152160.

Lưới trả EPSG:4326, 22 × 21 ô, scale x=0,00227272727° / y=0,00238095238°; thuật toán resampling của dịch vụ chưa được đặt/kiểm. Cả 18 lớp có cùng extent/transform, không nhầm giá trị giữa các ô. Đây vẫn là mô hình dự đoán, chưa được đối chiếu đất tại ruộng. Khoảng Q05–Q95 là khoảng dự đoán của mô hình, không là khoảng quan trắc địa phương.

Unit theo [ISRIC layers](https://docs.isric.org/globaldata/soilgrids/SoilGrids_faqs_01.html): pH integer/10; cát và sét g/kg /10 ra %. WCS DescribeCoverage trả unit chung `W.m-2.Sr-1` không phải soil unit, nên không dùng field này để diễn giải. GeoTIFF không ghi đầy đủ nodata; có 0 trong một số ô, giữ raw nhưng loại khỏi diễn giải (không gọi là pH=0). Không nội suy lấp vùng thiếu hoặc gán texture class từ mean/quantile rộng.

Ở điểm địa danh, mean pH 5,5/5,6; cát 18,9/18,4%; sét 42,2/44,3% theo hai độ sâu. Khoảng dự đoán rộng, xem CSV. Không chuyển kết quả này thành mô tả ruộng cát pha hoặc ngưỡng canh tác. Chưa có SOC, tầng rễ đầy đủ, EC, drainage, nước tưới hay field sample.

Nguồn và credit: **ISRIC SoilGrids, CC-BY-4.0**, [access/status](https://docs.isric.org/globaldata/soilgrids/SoilGrids_faqs_02.html), [WCS](https://docs.isric.org/globaldata/soilgrids/wcs.html). REST tạm dừng theo thông báo nguồn, WCS thành công ở snapshot này. Dataset không phải NASA; không gọi là NASA soil measurement.

Chạy từ root repo với Windows Python 3.12.14 và Pillow 13.0.0 có sẵn:

```powershell
& $taskPython scripts/research/query_duc_lap_soilgrids.py
```

Mặc định cached replay kiểm SHA và geometry; `--refresh` mới gọi mạng. [Script](../../../../../scripts/research/query_duc_lap_soilgrids.py) là audit nhỏ phục vụ docs, không là pipeline GIS sản phẩm. QA tổng thể `warn_spatial_transfer_not_validated`; không cho phép rank/eligibility tại ruộng.
