# Nguồn đầu vào và quy ước bằng chứng

> Ngày tiếp nhận/phân tích: 2026-10-30 (Asia/Saigon).

## Bản đề được sử dụng

- Người dùng cung cấp `C:/INDIVIDUALS/NeuraX/docs/challenges.md`, gồm đúng **14** heading `###`.
- SHA-256 của file đầu vào: `C45F36DF0FAF4D5F9A60FE02E9BE37D7AA4308AF4D6E26135FCD61D8E364FF84`.
- Bản này có Background, Objectives và Potential Considerations; không chứa nội dung tab Resources hay danh sách URL dataset đầy đủ.
- Từng mục đã được giữ nguyên văn ở cuối [14 hồ sơ](../challenges/README.md), nên người clone riêng neurax-docs vẫn có thể đối chiếu mà không cần file nằm ngoài repo.
- Mục 11 trong nguồn là Lunar Landing Site Navigator, tiếp tục dùng file ID 04 của repo. Đây là mapping nội dung, không là một challenge thứ 15.
- Baseline repo trước đợt cập nhật: commit `0c53a9659947c23279e22fbd2891623c32e77dda`; v1/v2 giữ lịch sử. Dossier hiện hành thay các phân tích trước khi có brief chi tiết.

## Đã xác nhận đến đâu?

| Nhãn | Ý nghĩa |
| --- | --- |
| Theo bản đề người dùng cung cấp | Nội dung xuất hiện trong file đầu vào; chưa hàm ý đã đối chiếu từng câu với website live |
| Nguồn web đã đọc | Đọc trang được liên kết, ghi ngày và phạm vi; không suy ra đã tải dataset |
| Candidate / cần kiểm | Product, phương pháp, thời gian, quyền dùng, kỹ năng hoặc phần cứng chưa đủ bằng chứng |
| Đề xuất NeuraX | Idea, phân công, xếp hạng, MVP và kiến trúc do team/trợ lý đề xuất |
| Đã thử/đo | Chỉ dùng khi có artifact/log/metric thực tế; hiện chưa có data/model/hardware spike |

Các câu “you may”, “could”, “encouraged”, “Potential Considerations” không tự thành yêu cầu bắt buộc. Có thể chọn chúng làm acceptance criteria nội bộ, nhưng phải ghi đó là quyết định của NeuraX.

Tài liệu đính kèm là nguồn nội dung để phân tích; các chỉ dẫn hướng tới người dự thi trong bản đề không phải quyền cho trợ lý tự build, đăng ký, mua đồ hoặc công bố kết quả.

## Đối chiếu web ngày 2026-10-30

| Nguồn | Kết quả/phạm vi |
| --- | --- |
| [NASA Space Apps challenges 2026](https://www.spaceappschallenge.org/2026/challenges/) | Công cụ truy cập trả 502; chưa đối chiếu được toàn bộ bản live |
| [Field Shift challenge](https://www.spaceappschallenge.org/2026/challenges/field-shift-adapting-farms-with-nasa-data/) | Công cụ truy cập trả 502; không đánh dấu Resources verified |
| [NASA POWER API overview](https://power.larc.nasa.gov/docs/services/api/) | Đọc được tài liệu API; chưa gọi API lấy dữ liệu vùng hay kiểm product/parameter cụ thể |
| [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/) | Đọc được mô tả nguồn MODIS/VIIRS và truy cập dữ liệu; chưa tải chuỗi overlap |
| [Espressif board guide](https://documentation.espressif.com/esp-dev-kits/en/latest/esp32s3/esp32-s3-devkitc-1/user_guide_v1.1.html) | Căn cứ lựa chọn board ứng viên; phải kiểm revision thực |
| [DFRobot SEN0193](https://wiki.dfrobot.com/sen0193/) và [calibration](https://wiki.dfrobot.com/sen0193/docs/18037) | Căn cứ loại sensor và phép hiệu chuẩn tương đối |
| [Sensirion SHT31](https://sensirion.com/products/catalog/SHT31-DIS-B) | Căn cứ chức năng sensor; chưa kiểm breakout được mua |

Tên mission/dataset được đề nhắc đến không có nghĩa dữ liệu chưa tồn tại. Điều chưa có trong đợt làm việc này là gói Resources đầy đủ và sample đã audit cho phạm vi NeuraX.

## Audit data tiếp theo

Mỗi nguồn cần provider, URL, product/version, biến/đơn vị, resolution, time coverage, AOI, định dạng, quyền truy cập, license/citation, QA/missingness, cách aggregate và hạn chế. Ghi riêng “đã đọc docs”, “đã tải sample”, “đã kiểm sample”.

Không tự gán product level, license, số năm coverage hoặc khả năng truy cập từ tên mission. Lịch/địa điểm/quy định dự thi và phạm vi chuẩn bị trước cần xác nhận từ ban tổ chức; các mốc 2026-10-28 trong tài liệu v1/v2 là lịch kỳ vọng cũ, không còn là việc đang chờ trong trạng thái hiện hành.


## Bổ sung sau khi cập nhật workflow

Ngày 2026-10-30, đã kiểm ngày thi 14–15/11/2026 qua NASA/CSA. Người dùng xác nhận local event HCMC tại NOVAWORLD; giờ local chưa công bố. [Event timeline](../planning/event-timeline.md) lưu nguồn 2025/2026 và phân biệt lịch thật với baseline nội bộ. Điều này cập nhật phần lịch còn thiếu ở lượt intake đầu, không thay đổi trạng thái Resources/sample chưa audit.
