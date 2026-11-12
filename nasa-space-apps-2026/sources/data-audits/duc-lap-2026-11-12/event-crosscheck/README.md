# Kiểm chéo event mưa 12–17/06/2020

Đã lấy một response thật ERA5 qua Open-Meteo ngày audit 12/11. Đây là sản phẩm độc lập với MERRA2/POWER, **không phải ground truth hoặc xác nhận NASA sai**. Xem [raw](era5_open_meteo_raw.json), [retrieval](retrieval.json), [comparison CSV](comparison.csv), [summary/hash](summary.json).

| Daily UTC | NASA POWER, mm trong một ngày | ERA5 qua Open-Meteo, mm |
| --- | ---: | ---: |
| 14/06/2020 | 494,17 | 17,3 |
| Tổng 12–17/06/2020 | 651,17 | 65,2 |

Request models=era5 tường minh, không dùng best_match. ERA5 trả lon/lat 106,5 / 11,0; grid 0,25°. POWER trả point làm tròn 106,444 / 10,911, source grid khí tượng 0,5° × 0,625°. Cả hai daily UTC; PRECTOTCORR mm/day được tích phân một ngày để so với daily precipitation_sum mm. Chênh support/model vẫn tồn tại, không resample rồi gọi cùng phép đo.

Kết quả: `warn_model_disagreement_unresolved`. Bất đồng lớn cả trong cửa sổ sáu ngày, không được dùng để chọn một giá trị “đúng”, xóa raw, sửa series hoặc tính % sai số khi chưa có tham chiếu phù hợp. Bản raw NASA/hash giữ nguyên. Một event không đủ ước lượng bias hoặc chất lượng toàn period.

Credit: NASA Langley Research Center POWER Project; ECMWF/Copernicus ERA5 phân phối qua Open-Meteo. [Docs Open-Meteo](https://open-meteo.com/en/docs/historical-weather-api) / [docs NASA](https://power.larc.nasa.gov/docs/tutorials/service-data-request/api/). Không mở tài khoản, dùng API key hay dịch vụ trả phí.

Chạy lại từ root bằng bundled Python native Windows đã xác minh, chỉ standard library:

```powershell
& $taskPython scripts/research/crosscheck_duc_lap_rain.py
```

Mặc định đọc raw đã lưu; `--refresh` thay snapshot và phải review lại. [Script](../../../../../scripts/research/crosscheck_duc_lap_rain.py) đọc NASA raw đã có, kiểm unit/UTC/keys và lưu comparison; không thay script/raw NASA.
