# POWER Long Khánh–Cai Lậy: sample sẵn cho case nghiên cứu

Đã tải 12/11/2026 qua HTTPS từ NASA. [Manifest](manifest.json) lưu request, raw hash, API header, unit và QA. [Raw JSON](power_daily_2015_2025.json), [daily.csv](daily.csv). [Khuyến nghị chọn case](../../../planning/cases/site-choice-2026-11-12.md).

Điểm 10.38333 N,106.11667 E là **địa danh Long Khánh** theo [Mapcarta/GeoNames](https://mapcarta.com/15497128), không phải tọa độ các thí nghiệm công bố. Không ghép đất thí nghiệm với ô này như quan trắc đồng vị trí. POWER meteorology support 0,5° × 0,625°, [nguồn resolution](https://power.larc.nasa.gov/docs/tutorials/service-data-request/api/).

Daily UTC 01/01/2015–31/12/2025: 4.018 ngày, 16.072 giá trị T2M/T2M_MAX/T2M_MIN (C), PRECTOTCORR (mm/day). Kiểm đủ keys/năm nhuận, không duplicate JSON keys/fill/nonfinite, thứ tự nhiệt độ, mưa không âm và unit/time đạt. **QA=WARN:** 14/06/2020 có 488,17 mm, vượt ngưỡng review khám phá 200; chưa chứng minh sai, raw giữ nguyên. Không áp cross-check ERA5 của điểm Đức Lập sang đây.

Period này khác kỳ thí nghiệm đất lịch sử; không là tái lập thí nghiệm, forecast hay local weather validation. Không có ET, tưới, Kc hoặc soil water balance. Không dùng để hứa yield/water saving. Credit NASA Langley Research Center POWER Project, [Daily API](https://power.larc.nasa.gov/docs/services/api/temporal/daily/).

Chạy lại cached checks/CSV, standard library Windows Python 3.12.14, không mạng:

```powershell
& $taskPython scripts/research/audit_long_khanh_power.py
```

Script: [audit_long_khanh_power.py](../../../../scripts/research/audit_long_khanh_power.py). URL đầy đủ trong manifest cho phép tải lại có chủ đích; không tự refresh snapshot khi chạy audit. Không cài dependency mới.
