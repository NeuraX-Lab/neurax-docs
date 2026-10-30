# Tiểu An phụ trách hardware; Quang Luật kiểm dữ liệu đo

> 2026-10-30 · BOM đề xuất cho Field Shift. Chưa biết team đã có thiết bị nào; chưa mua, chưa có báo giá, chưa kiểm pinout/module thực tế.
> Mục tiêu: node đo tại chỗ có log và hiển thị kết quả. An sở hữu thiết bị; Quang Luật hỗ trợ thống kê/kiểm log. Gá/vỏ dùng đồ sẵn có nếu cần, không là deliverable chính của Quang Luật.

## Bộ tối thiểu nên kiểm tra hoặc mượn trước

| Hạng mục | Số lượng dự kiến | Chức năng / lựa chọn | Người phụ trách |
| --- | ---: | --- | --- |
| ESP32 dev board, ưu tiên board sẵn có; ứng viên ESP32-S3-DevKitC-1 | 1, thêm 1 dự phòng nếu có | Thu sensor, truyền dữ liệu, nhận kết quả hiển thị; chọn exact SKU trước wiring | An |
| Cảm biến độ ẩm đất điện dung, ứng viên DFRobot SEN0193 | 1–2 | Chỉ số độ ẩm tương đối sau hiệu chuẩn; 2 chiếc giúp thử khác biệt cảm biến | An |
| Module nhiệt/ẩm SHT31 với breakout phù hợp | 1 | Context không khí tại điểm đo, không phải soil health | An |
| OLED I2C nhỏ hoặc LED trạng thái | 1 | Hiện giá trị, dữ liệu cũ/mất kết nối; nếu chưa có, dùng Serial Monitor | An |
| USB data cable đúng cổng board + cáp dự phòng | 2 | Nguồn và dữ liệu; tránh cáp chỉ sạc | An |
| Breadboard, jumper, header, điện trở phù hợp mạch | 1 bộ | Lắp prototype; xác nhận pull-up/điện áp module thực | An |
| Nguồn USB ổn định; power bank sẵn có nếu phù hợp | 1 | Demo bàn; không cần tự thiết kế bộ pin | An |
| Đồng hồ vạn năng | Mượn 1 | Kiểm nguồn, continuity và điện áp ngõ ra trước nối ADC | An |
| Hộp, standoff, vít, kẹp dây và cọc/gá | 1 bộ | Giữ board khô, chống kéo dây, giữ độ sâu đầu dò nhất quán | An; Quang Luật hỗ trợ bản vẽ khi cần |
| Hai chậu/khay có nhãn, mẫu đất, cốc đong, thước | 1 bộ | Quy trình khô/ẩm có ghi điều kiện và lặp đo | An chuẩn bị; Quang Luật + Bích thiết kế phép thử |
| Laptop hiện có | 1 | Chạy inference/dashboard và lưu log | Hiếu + Việt |

Đây là danh sách chuẩn bị theo chức năng, không khẳng định tính tương thích của mọi module mang cùng tên. An kiểm revision, sơ đồ board, mức điện áp nguồn/tín hiệu, ADC range và pin bị chiếm trước khi chốt BOM. Không nối tín hiệu 5 V trực tiếp vào GPIO/ADC 3.3 V.

## Căn cứ chọn linh kiện

- ESP32-S3-DevKitC-1 là board phát triển có Wi-Fi/Bluetooth LE theo [tài liệu Espressif](https://documentation.espressif.com/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html). Có nhiều cấu hình/revision; board sẵn có đáp ứng I/O thường hợp lý hơn mua board mạnh.
- SEN0193 là cảm biến điện dung có ngõ ra analog theo [DFRobot](https://wiki.dfrobot.com/sen0193/). [Hướng dẫn calibration](https://wiki.dfrobot.com/sen0193/docs/18037) mô tả mốc khô/ướt; mốc này không tự biến tín hiệu thành volumetric water content chuẩn.
- SHT31 đo nhiệt độ/độ ẩm theo [nhà sản xuất Sensirion](https://sensirion.com/products/catalog/SHT31-DIS-B). Chọn breakout hỗ trợ mức điện áp của board và kiểm datasheet của module mua thực tế.

Đã xem nguồn kỹ thuật ngày 2026-10-30; chưa kiểm tồn kho/giá/nhà cung cấp địa phương. Trước mua: An điền exact SKU, số lượng có sẵn, giá báo thực, thời gian giao; Hưng tổng hợp ngân sách do team chốt. Không dùng giá ước đoán làm báo giá.

## Đất diễn thật của An

1. Thiết kế measurement chain: sensor → đọc/QA → timestamp → truyền log → hiển thị.
2. Ghi quy trình hiệu chuẩn, noise/drift và nhãn đơn vị.
3. Chốt contract H1 với Việt/Hiếu và Quang Luật; cùng chạy tình huống rút sensor/mất mạng/stale.
4. Trình diễn một kết quả analysis từ hệ thống xuất xuống màn hình/LED, có thời gian và nhãn dữ liệu.
5. Bàn giao wiring, BOM, test log và những giới hạn đo.

Chưa cần thiết kế chip hoặc PCB riêng. “Có chip” ở đây là làm chủ node embedded hữu ích. TinyML chỉ cân nhắc sau khi có model đủ nhỏ, target rõ và bằng chứng nó cần chạy trên thiết bị.

## Quang Luật hỗ trợ An bằng thống kê và kiểm dữ liệu

- Thống nhất test plan với An: điều kiện đo, số lần lặp, thời gian, cột log, trường hợp rút sensor/mất mạng.
- Nhận H1 CSV theo [contract](architecture.md); dùng RStudio hoặc MATLAB để vẽ time series, phân bố, missingness và kiểm duplicate/timestamp.
- Báo độ lặp/độ phân tán; chỉ báo bias/accuracy khi có thiết bị hoặc phương pháp tham chiếu đủ căn cứ.
- Đối chiếu kết quả thiết bị đang hiển thị với run_id/value/unit/data_as_of của A1; ghi stale/replay đúng nhãn.
- Bàn giao một trang kết quả thử và biểu đồ để An sửa thiết bị, Hiếu sửa trạng thái UI, team dùng trong báo cáo.
- AutoCAD dùng bổ trợ nếu An cần bản vẽ đơn giản. Không tự phát sinh task chế tạo vỏ/cọc/gá; Quang Luật ưu tiên D1/Q1/E1 và báo cáo khoa học.

Một phiên test chung khoảng 60–90 phút, không chặn đường DATA. Lịch và gate theo [event-timeline](event-timeline.md). Khi Quang Luật bận QC, An vẫn tự chạy test điện/firmware và lưu log để review sau.

## Kiểm thử bàn đề xuất

| Bài thử | Owner | Bằng chứng đạt |
| --- | --- | --- |
| Board nhận sensor, màn hình | An | Log có đơn vị và timestamp, không reset trong buổi rehearsal |
| Khô/ẩm có điều kiện ghi lại | Quang Luật thực hiện, An hướng dẫn | Các lần lặp có log; phân biệt mức tương đối; không quảng cáo độ chính xác chưa đo |
| Rút cảm biến | An + Hiếu | Missing/invalid hiện rõ; không biến thành đất khô 0% |
| Ngắt Wi-Fi/USB dữ liệu | An + Hiếu | Trạng thái cũ/mất kết nối có thể thấy; reconnect không nhân bản bản ghi |
| Tháo/lắp phần giữ thiết bị nếu có | An | Không kéo đứt dây, board không chạm nước, độ sâu đo tái lập |
| Hiển thị kết quả từ AI | An + Hiếu; Quang Luật đối chiếu log | Khớp run_id, timestamp, loại analysis/forecast/scenario |
| Replay | Cả nhóm | Ghi rõ phát lại, nguồn log và ngày, không giả live |

Mục tiêu demo: chứng minh tích hợp và phương pháp đo, không chứng minh node rẻ đo được năng suất, dinh dưỡng, pH hoặc “sức khỏe đất”. Không nhúng phần điện của sensor; chỉ vùng đầu dò được nhà sản xuất cho phép tiếp xúc môi trường.

## Thiết bị chỉ cân nhắc khi đổi bài hoặc vượt MVP

| Nhánh | Bổ sung có lý do | Giới hạn |
| --- | --- | --- |
| Earth Analog / Martian Map | IMU/module nghiêng + fixture dốc | Đo trên Earth; không chứng nhận vận hành ở Moon/Mars |
| Lunar Navigator | Panel nhỏ, bộ gá chỉnh góc, phép đo dòng/áp | Mô hình bàn về góc chiếu; không tái tạo chân không/bức xạ |
| Jukebox | Loa/tai nghe, nút tactile hoặc motor rung có driver | Cần mapping và kiểm accessibility |
| MODIS/VIIRS | Màn hình/LED calendar/anomaly | Không coi cảm biến khói bàn là ground truth vệ tinh |

Raspberry Pi/Jetson, LoRa, camera, pH/EC, bơm/van, rover và PCB riêng đều chưa cần cho Field Shift MVP. Chỉ bổ sung khi có đầu ra không thể đáp ứng bằng bộ tối thiểu và lịch/ngân sách cho phép.

