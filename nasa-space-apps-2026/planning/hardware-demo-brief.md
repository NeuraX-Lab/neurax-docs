# Brief gửi chị An — node đo và demo AgroTwin

> Sau review 06/11: bản này và PDF sáu trang chỉ là tóm tắt phụ trợ. Tài liệu thuyết minh chính là [paper đầy đủ](hardware-design-paper.md) / [PDF kỹ thuật A4](../../output/pdf/NeuraX-AgroTwin-Technical-Paper-An.pdf), có lý do chọn, phương án thay thế, hiệu chuẩn, kiểm thử và backup.

> 2026-11-06 · Nội dung nguồn cho PDF cùng tên. Thiết kế đề xuất, chưa xác nhận thiết bị sẵn có, chưa wiring/test hay báo giá. Logo do người dùng cung cấp; ảnh linh kiện là mẫu tham khảo từ hãng, không phải inventory của team.

## Trả lời ngắn cho An

Chị làm một node đo ẩm đất, gửi số đo lên laptop và có thể nhận kết quả AgroTwin để hiển thị. Bộ tối thiểu chỉ cần **một probe ẩm đất điện dung**, **ESP32**, USB data, breadboard/jumper và laptop. **SHT31 là tùy chọn** để thêm nhiệt/ẩm không khí; **OLED cũng tùy chọn**, có thể thay bằng Serial Monitor/dashboard.

NASA + bảng cây/đất dùng so luân canh; sensor đo context tại chỗ. Hai chậu đất phục vụ minh họa phép đo, không xác nhận cây nào tốt hay làm ranking của vùng tự đổi.

## Linh kiện đề xuất

| Mức | Hạng mục | Số lượng | Công dụng |
| --- | --- | ---: | --- |
| Tối thiểu | Probe ẩm đất điện dung; ứng viên DFRobot SEN0193 | 1 | Chỉ số ẩm tương đối sau hiệu chuẩn, không phải soil health hoặc %VWC đã kiểm |
| Tối thiểu | ESP32 dev board có sẵn; minh họa ESP32-S3-DevKitC-1 v1.1 | 1 | Đọc analog, đóng gói H1, truyền và nhận summary |
| Tối thiểu | USB data đúng đầu cổng; jumper/breadboard | 1 bộ | Cấp nguồn USB từ laptop và nối module |
| Tối thiểu | Laptop + hai chậu/khay cùng loại đất có nhãn | 1 + 2 | Dashboard/log, thử hai điều kiện đo có ghi quy trình |
| Bổ sung | SHT31 breakout, hình minh họa Adafruit #2857 | 1 | Nhiệt độ và độ ẩm không khí qua I2C |
| Bổ sung | OLED I2C hoặc LED | 1 | Hiện trạng thái, data age và tóm tắt A1; dùng Serial nếu thiếu |
| Mượn/kiểm | Đồng hồ vạn năng, cáp dự phòng, hộp/kẹp | 1 bộ | Kiểm mức điện áp, giữ board khô và dây chắc |

Một probe đo hai chậu tuần tự. Đặt cùng độ sâu, chờ ổn định theo thử thực, ghi điều kiện và lặp đo. Không hứa số lần lấy mẫu, độ chính xác hoặc ngưỡng cảnh báo khi chưa thử thiết bị. Không cần mua đủ mọi linh kiện ngay.

## Kết nối sơ bộ — chưa là pinout

Probe analog → ADC phù hợp ESP32. SHT31/OLED → I2C nếu có. ESP32 ↔ laptop qua USB Serial ở lượt đầu; Wi-Fi là mở rộng. USB laptop cấp board, GND chung; kiểm nguồn/module và ADC attenuation/range trước nối. SEN0193 theo hãng có supply 3.3–5.5 V và output 0–3.0 V; phải kiểm đầu ra thực và dải ADC của cấu hình board. Không đưa 5 V vào GPIO. Đầu điện tử probe và board giữ khô.

Không chọn GPIO cụ thể trước khi biết SKU/revision và pin đã dùng. Không trộn firmware ESP32 thường và S3. SHT31 breakout minh họa không đại diện mọi module bán cùng tên.

## Demo nội bộ khoảng 90 giây — storyboard, không phải giới hạn BTC

1. 0–15s: giới thiệu câu hỏi luân canh; mở vùng, dữ liệu NASA và ba phương án nếu có đủ nguồn.
2. 15–35s: đo hai chậu tuần tự, cho thấy tín hiệu và timestamp đổi; nhãn 'đo tại bàn'.
3. 35–60s: đổi ưu tiên trên dashboard, xem lý do xếp hạng; thao tác này tách khỏi đổi chậu sensor.
4. 60–75s: gửi summary A1 xuống OLED/Serial, đối chiếu run_id và status.
5. 75–90s: rút sensor/ngắt link; trạng thái invalid/stale hiện đúng, luồng NASA vẫn hoạt động với snapshot hợp lệ.

Mốc chỉ là phân bổ rehearsal đề xuất. Nếu chưa có data/model thật, fixture có nhãn synthetic; replay không được gọi live. Video/slides nộp theo quy định 2026, không dùng 90 giây này làm độ dài mặc định.

## H1 và bàn giao

H1 dùng contract architecture.md: event_id, device_id, timestamp UTC, event_type, value nullable, unit, quality, calibration_id, source_context và delivery_mode. Giữ raw ADC riêng khi cần; nếu chưa hiệu chuẩn, hiển thị raw hoặc normalized index có nhãn, không tự ghi % ẩm tuyệt đối. A1 summary có run_id, label/value/unit, status, data_as_of và warning.

An giao wiring theo board thật, BOM exact SKU, firmware về sau và log. Quang Luật kiểm độ lặp/missing/timestamp và so display với A1; Việt–Hiếu chốt interface. Bích rà diễn giải. Cần An xác nhận board, probe, cáp, OLED hiện có; Hưng tổng hợp ngân sách nếu cần mua.

## Acceptance

- Đọc được probe, lưu timestamp và quality; hai điều kiện được thử lặp với quy trình rõ, không gọi repeatability là accuracy.
- Rút sensor có policy phát hiện/kiểm tra; nếu chưa phân biệt được open-circuit, ghi unknown thay vì hứa tự phát hiện. Không biến missing thành 0%.
- Mất link quá timeout đã chốt hiện stale; reconnect không nhân đôi record; dashboard NASA vẫn đọc được snapshot.
- Summary display khớp run/version/unit của A1; replay có nhãn và ngày log. Không dùng node xác nhận độ đúng của NASA pixel xa.

## Nguồn kỹ thuật và ảnh — truy cập 2026-11-06

1. [DFRobot SEN0193: chức năng và thông số](https://wiki.dfrobot.com/sen0193). [Calibration](https://wiki.dfrobot.com/sen0193/docs/18037). [Ảnh hãng](https://dfimg.dfrobot.com/enshop/SEN0193/SEN0193_Main_01_1200x630.jpg.webp).
2. [Espressif ESP32-S3-DevKitC-1 v1.1](https://documentation.espressif.com/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html). [Ảnh từ repo hãng](https://raw.githubusercontent.com/espressif/esp-dev-kits/master/docs/_static/esp32-s3-devkitc-1/esp32-s3-devkitc-1-v1.1-isometric.png).
3. [Adafruit SHT31-D breakout #2857](https://www.adafruit.com/product/2857). [Ảnh hãng](https://cdn-shop.adafruit.com/970x728/2857-03.jpg).

Ảnh dùng nhận diện linh kiện trong brief nội bộ, giữ credit; không đại diện endorsement hay linh kiện đã mua. Không có báo giá địa phương trong tài liệu. Phần thiết kế luồng, BOM tối thiểu và storyboard là đề xuất NeuraX.

[PDF để gửi](../../output/pdf/NeuraX-AgroTwin-Hardware-Brief-An.pdf) · [Phân tích dự án](project-brief.md) · [BOM chi tiết](hardware-preparation.md).
