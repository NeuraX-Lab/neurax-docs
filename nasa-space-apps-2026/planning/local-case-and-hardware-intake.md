> **TRẠNG THÁI 12/11 - THAM KHẢO/SNAPSHOT:** phần thiết kế, địa bàn, phân công và phase bên dưới có nội dung trước correction. Không dùng làm quyết định hiện hành. Đọc [Bắt đầu ở đây](START-HERE.md), [roles hiện hành](my-thanh-team-roles-2026-11-12.md) và [bảng R0/R1/R2 Mỹ Thành](cases/my-thanh-cai-lay/rotation-evidence-for-bich.md). Hưng-Việt cùng core/UI khi cần; Hiếu backend remote gián đoạn; Bích Data/review nguồn-feature; An ESP demo; Luật QA/thống kê/đánh giá từng block. Không lấy Đức Lập/bắp hạt/đậu phộng hoặc lời “prototype ngay” ở snapshot thay case và quy định hiện tại.

# Case địa phương, ENSO và thiết bị mượn

> Sau intake: [audit case Đức Lập và NASA 12/11](cases/duc-lap/README.md) đã có sample POWER thật/WARN. Chưa đủ khóa hiện trạng và hai rotation; chip tiếp tục chờ thông số. Phần chưa tải sample bên dưới ghi trạng thái ở thời điểm intake trước audit.

> Review cụ thể hơn: [Đức Lập và farm mô phỏng](local-case-scope-and-simulation.md), 12/11. Ưu tiên nghiên cứu Đức Lập Hạ cũ, nay thuộc xã Đức Lập; chưa có thửa/hộ được xác minh.

> Cập nhật 12/11/2026. Bổ sung cho proposal; các lựa chọn địa phương dưới đây là khuyến nghị nghiên cứu, chưa là quyết định team hay kết quả thử nghiệm.

## Thông tin mới từ người dùng

- Người dùng mục tiêu là nông dân. Câu chuyện hướng tới đóng góp giải quyết vấn đề tại Việt Nam và an ninh lương thực dài hạn.
- Team ở TP.HCM, có thành viên học môi trường; cần chọn địa điểm để bắt đầu tìm dữ liệu đất/cây/mùa.
- Team muốn ENSO/El Niño trở thành đầu vào hỗ trợ chuẩn bị mùa vụ, không chỉ làm bối cảnh pitch.
- Theo người dùng, HTTPSLAB có chip nội địa và đã đồng ý cho mượn. Chưa có model, datasheet, SDK, giao tiếp, inventory cảm biến, ngày bàn giao hoặc bằng chứng về phạm vi “100% nội địa”. Không coi thông tin này là xác nhận toàn bộ sensor/board được chế tạo trong nước hay chứng minh bảo mật.

## Khuyến nghị case nghiên cứu đầu tiên

Ưu tiên khảo sát khu vực Đức Hòa (địa danh huyện cũ trong tài liệu), tìm một điểm canh tác thực sự còn hoạt động, có tọa độ và người liên hệ. Đây là vùng nghiên cứu đề xuất, không chọn chính thửa đất trong bài báo: bài đó có bối cảnh thu hồi đất.

Báo địa phương ngày 22/04/2025 ghi nhận một hộ tại địa bàn Đức Lập Thượng cũ luân canh đậu phộng Đông Xuân, bắp Hè Thu và lúa vụ còn lại. Bằng chứng này cho thấy có câu hỏi luân canh thực tế để nghiên cứu, không xác nhận lịch đó thích hợp cho mọi thửa đất hoặc năm 2026. Nguồn: https://baotayninh.vn/tien-phong-ban-giao-mat-bang-cho-du-an-khu-do-thi-130839.html

Đầu việc cho Bích: xác minh tên địa bàn hiện hành và điểm cụ thể; nhóm đất/pH/thoát nước; nước tưới; lịch và giống cây; hiện trạng luân canh; sâu bệnh; nguồn kỹ thuật và người review. Bắt đầu từ nhóm lúa–bắp–đậu phộng nhưng chưa cố định ba phương án trước khi có nguồn. Thành viên môi trường rà bối cảnh và nguồn, không mặc nhiên thay vai chuyên gia nông học.

Củ Chi là phương án tiếp cận thực địa thay thế nếu team có người liên hệ thuận lợi hơn; chưa có đủ evidence cây–mùa để đặt cao hơn Đức Hòa trong lượt nghiên cứu này. Chọn nơi có nguồn và người review, không chọn chỉ vì NASA có pixel phủ lên khu vực.

## Ba luồng dữ liệu cần tách

| Luồng | Vai trò | Cách thử trước |
| --- | --- | --- |
| NASA POWER Daily | Nhiệt độ và mưa lịch sử tại khu vực nghiên cứu | Lấy sample sau khi chốt tọa độ; kiểm unit, fill value, coverage, time standard và grid |
| NOAA CPC ENSO | Trạng thái/outlook khí hậu quy mô lớn | Lưu ngày phát hành, horizon, xác suất và nguồn; không coi ENSO là dự báo mưa tại ruộng |
| Sensor/board HTTPSLAB | Quan sát tại điểm nếu có cảm biến và giao tiếp phù hợp | Yêu cầu một payload thật và tài liệu; dùng fixture có nhãn để thử parser trước khi nhận thiết bị |

NASA POWER cung cấp dữ liệu mở toàn cầu qua API, không cần chờ BTC giao riêng một dataset. Docs: https://power.larc.nasa.gov/docs/services/api/temporal/daily/

Trong lượt đọc ngày 12/11, trang NOAA CPC hiển thị bản phát hành 08/10/2026, El Niño Advisory, và lịch bản kế tiếp 12/11. Không ghi đây là bản phát hành tháng 11. Nguồn: https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml

ENSO được nhận làm đầu vào bối cảnh có ngày/horizon. Muốn dùng nó thay đổi xếp hạng cần có quan hệ địa phương được kiểm định hoặc outlook khu vực có nguồn; nếu chưa có, chỉ trình bày outlook và cho chạy kịch bản nóng/khô được gắn nhãn giả định. Không nhân xác suất El Niño thành xác suất thiếu nước tại ruộng. Không dùng forecast hiện tại để đánh giá ngược các năm lịch sử.

## Câu hỏi gửi người cho mượn thiết bị

1. Tên/model chip và board, datasheet, SDK/example và công cụ nạp/debug là gì?
2. Board đang kết nối cảm biến nào, đo đại lượng gì, đơn vị/range và yêu cầu hiệu chuẩn ra sao? Chip riêng không đồng nghĩa có sẵn cảm biến.
3. Có gửi được một file log/payload thật, format, timestamp, chu kỳ lấy mẫu và hướng dẫn đọc qua USB/UART/I2C/SPI hoặc giao tiếp khác không?
4. Chip được kỳ vọng thu thập số đo, xử lý tại chỗ hay chạy model? Có demo chạy sẵn và giới hạn bộ nhớ/tính toán nào?
5. Khi nào nhận được board và phụ kiện? Ai hỗ trợ kỹ thuật? Phạm vi nào của chip/board/sensor được thiết kế, chế tạo hoặc lắp ráp trong nước và được phép mô tả công khai thế nào?

## Thử trước và backup

Thử phần mềm bằng historical open data NASA và fixture H1 có nhãn synthetic; fixture chỉ chứng minh parser/UI. Test thiết bị bằng log thật sau bàn giao; số đo live/replay phải phân biệt. Giữ adapter riêng để đổi board không đổi logic NASA/K1/ranking. Có thể giữ ESP32 trong paper cũ như backup đề xuất nếu inventory xác nhận có; không tiếp tục gọi nó là hardware chính đã chốt.

Thay dataset không chỉ đổi đường dẫn: kiểm schema, unit, grain, thời gian, resolution, QA, license và tính lại feature/score. Giữ một snapshot đã audit cho demo dự phòng. Chưa có sample NASA tải/kiểm hay firmware chạy trong lượt bổ sung tài liệu này.

## Phần đã tích hợp vào PDF 12/11

Proposal 0.4: người dùng nông dân, case Đức Lập, ba luồng dữ liệu, gate ENSO và câu chuyện đóng góp Việt Nam. Paper hardware 0.3: HTTPSLAB là nhánh ưu tiên có điều kiện thông số, intake và test plan; sơ đồ ESP32 là cấu hình tham chiếu backup. Chưa vẽ wiring board mượn khi chưa biết model. Mốc tiếp theo: case sheet/tọa độ nghiên cứu, sample NASA và datasheet/log thiết bị để thay giả định bằng evidence.
