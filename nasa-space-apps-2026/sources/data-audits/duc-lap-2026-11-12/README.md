# Sample NASA POWER — Đức Lập, audit 12/11/2026

Nghiên cứu địa phương mới: [SoilGrids WCS](soilgrids-context/README.md) là nguồn ISRIC riêng, không phải NASA soil observation; [kiểm 44 cửa sổ bắp/đậu phộng](rotation-window-screen/README.md) dùng raw NASA có sẵn. [Hồ sơ tiểu vùng](../../../planning/cases/duc-lap/local-feasibility-study.md) giữ kết luận có điều kiện; chưa sửa proposal/PDF hoặc push.

Bổ sung: [đối chiếu event ERA5](event-crosscheck/README.md) đã thực hiện, bất đồng còn mở; [exposure một cửa sổ tham chiếu](reference-exposure/README.md) đã tính từ raw. Không thay raw NASA hoặc nâng WARN thành pass.

**Có dữ liệu thật; QA = WARN, chưa dùng làm khuyến nghị nông học.** Xem [case review](../../../planning/cases/duc-lap/README.md).

| File | Vai trò |
| --- | --- |
| [power_daily_2015_2025.json](power_daily_2015_2025.json) | Raw response, giữ nguyên bytes NASA |
| [retrieval.json](retrieval.json) | URL, timestamp UTC, HTTP status, bytes |
| [manifest.json](manifest.json) | Điểm địa danh, query, header/version/source, resolution, hash và giới hạn |
| [qa.json](qa.json) | Completeness, unit/time/physical checks và review flags |
| [data_dictionary.json](data_dictionary.json) | Định nghĩa field gốc/derived và giới hạn |
| [daily.csv](daily.csv) | Bốn biến theo ngày UTC, 4.018 dòng dữ liệu |
| [monthly.csv](monthly.csv) | 132 tháng, tổng mưa và thống kê nhiệt |
| [monthly_reference_2015_2025.csv](monthly_reference_2015_2025.csv) | Mean/median/min/max theo tháng, 11 năm, không là normal 30 năm |
| [annual.csv](annual.csv) | Tổng hợp 11 năm |
| [summary.json](summary.json) | Kết quả mô tả và sensitivity có nhãn |

Điểm API 10.91123 N / 106.44351 E là tham chiếu địa danh GeoNames, không là ruộng thật hoặc điểm lấy mẫu đất. Dữ liệu nguồn lưới khí tượng 0,5° × 0,625° theo docs NASA; không nâng độ chính xác bằng zoom hoặc số lẻ tọa độ. T2M/T2M_MAX/T2M_MIN đơn vị C; PRECTOTCORR mm/day; cộng chuỗi ngày đầy đủ thành tổng mm. Header API v2.10.3, MERRA2/POWER; fill -999.0.

Không thiếu ngày/giá trị hoặc lỗi thứ tự nhiệt độ trong sample. **14/06/2020: 494,17 mm/day** vượt threshold review nội bộ 200; giữ raw và gắn cờ, chưa kết luận lỗi. Phép bỏ đóng góp ngày đó trong summary là sensitivity trên period thiếu một ngày, không phải dữ liệu đã sửa hoặc giá trị dùng cho ranking. Các diagnostic >=35 C và mưa <1 mm/day cũng chưa là ngưỡng hại cây/khô hạn đất được xác thực.

Credit: NASA Langley Research Center POWER Project; source header và [Daily API docs](https://power.larc.nasa.gov/docs/services/api/temporal/daily/) / [resolution](https://power.larc.nasa.gov/docs/tutorials/service-data-request/api/). Không suy quyền sử dụng các PDF đất/nông học khác từ quyền dùng NASA. Không kèm thông tin nông hộ.

Chạy lại từ root repo bằng Python native Windows đã xác minh; script chỉ dùng standard library, không có dependency cần cài:

```powershell
& $taskPython scripts/research/audit_duc_lap_power.py
```

Mặc định dùng raw đã lưu, không gọi API lại. `--refresh` mới tải lại; việc đó thay retrieval/raw/hash và kết quả, nên cần review trước ghi đè. Interpreter audit lần này: bundled Windows Python 3.12.14, không là runtime AI/model-training. Source script: [audit_duc_lap_power.py](../../../../scripts/research/audit_duc_lap_power.py).
