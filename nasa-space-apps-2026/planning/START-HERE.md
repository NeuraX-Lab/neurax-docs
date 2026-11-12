# Bắt đầu ở đây - trạng thái hiện hành

> **Cho phép tiếp tục theo xác nhận mới của người dùng:** ngày 12/11, người dùng báo đã confirm BTC và chỉ thị làm tiếp. Không yêu cầu lại cùng quyền. [Repo thực tế / phần đã chạy / bước tiếp theo](repository-inventory-and-next-step-2026-11-12.md) và [nội dung gửi Bích](bich-review-message.md). Các ghi chú T0 trước đó là bối cảnh quy định chung, không phải lý do chặn công việc vừa được cho phép. Chưa giả là có văn bản thay đổi global rules hoặc khung online remote.

> **Kiểm định tổng thể mới nhất:** [kết luận từng phần, flow ví dụ và việc còn thiếu](full-readiness-verification-2026-11-12.md). Tài liệu/data integrity đạt với warning upstream; readiness khoa học/core còn partial.

> 12/11/2026. Trang điều hướng và trạng thái thống nhất, không phải proposal mới. Dùng để tránh ghép phân công/địa bàn từ các snapshot khác ngày.

## 1. Chúng ta đang làm gì?

**AgroTwin / Field Shift:** hỗ trợ nông dân khám phá ba phương án luân canh với dữ liệu NASA, thông tin đất/cây/mùa có nguồn và ưu tiên của họ. **Giữ Mỹ Thành** làm địa bàn nghiên cứu từ xa. R0 lúa-lúa-lúa, R1 lúa-bắp non-lúa, R2 lúa-đậu xanh-lúa là phương án tham khảo từ nghiên cứu vùng, chưa là lịch thực tế hoặc khuyến cáo cho block.

Ranh xã có nguồn; block khoảng 2 ha là khối canh tác số hóa theo cạnh nhìn thấy trên ảnh, không chứng minh đất đồng nhất. SoilGrids là mô hình; đất demo HCM là mẫu lab riêng. Không cần lấy đất Mỹ Thành cho demo. HTTPSLAB đã đồng ý cho mượn theo team, chưa có datasheet đủ để chốt tích hợp. Chưa chứng minh năng suất, lợi nhuận, tiết kiệm nước hoặc mô hình đã kiểm ngoài đồng.

## 2. Đọc đúng ba tài liệu

| Việc cần hiểu | Tài liệu hiện hành |
| --- | --- |
| Ai làm gì, Hưng-Việt cùng core, Hiếu remote và cách bàn giao | [Vai trò và job](my-thanh-team-roles-2026-11-12.md) |
| Bích/Data cần review bằng chứng nào cho R0/R1/R2 | [Bảng đất-nước-cây-mùa](cases/my-thanh-cai-lay/rotation-evidence-for-bich.md), [CSV 12 hàng review](cases/my-thanh-cai-lay/rotation-evidence-review.csv) |
| Bản đồ, cảm biến/demo, nguồn, giới hạn và vai trò trong một bản để gửi | [Hồ sơ Markdown](cases/my-thanh-cai-lay/bich-site-and-demo-dossier.md), [PDF hiện hành 1.3](../../output/pdf/NeuraX-AgroTwin-Site-and-Demo-Dossier-Bich.pdf), [ZIP bàn giao](../../output/handoff/NeuraX-MyThanh-Bich-Research-Pack-2026-11-12.zip) |

Vai trò nguồn là file roles; bảng bằng chứng nguồn là file rotation-evidence. PDF xuất từ các file này bằng include, không sửa vai trò riêng trong PDF. Nếu mâu thuẫn với snapshot proposal/workflow cũ, dùng các tài liệu hiện hành ở bảng trên và chỉ dẫn mới nhất của người dùng.

## 3. Phân công đã chốt theo người dùng

- **Hưng:** workflow chính, scope Data -> AI; cùng Việt đóng góp chính.
- **Việt:** technical AI, Data Analysis; cùng Hưng features, pipeline data, kiến trúc, output demo; cả hai có thể làm dashboard UI/UX và backend support.
- **Bích:** Data theo chuyên ngành, review nguồn/src, features và bảng đất-nước-cây-mùa.
- **Hiếu:** Backend từ xa, có lúc offline; chưa có khung giờ cụ thể. Hưng-Việt hỗ trợ khi cần; không chờ phản hồi ngay mới tích hợp được.
- **Tiểu An:** demo ESP/sensor, firmware/giao tiếp/log lab và backup có nhãn.
- **Quang Luật:** thống kê và đánh giá từng block chức năng, QA, hỏi owner để nắm workflow/trạng thái/blocker. Không chỉ đánh giá cuối hoặc sensor.

## 4. Bước kế tiếp duy nhất để gỡ rối

Trước giờ G: mỗi người review phần của mình trong hồ sơ, ghi **đầu ra đang có / thiếu gì / ai nhận**. Bích ưu tiên nguồn nước/thoát nước và cửa sổ chuyển vụ của R1/R2; thiếu thì unknown. Hiếu báo khung online khả thi và cách bàn giao, không mặc định trực liên tục. Luật tổng hợp trạng thái từng block để Hưng-Việt chốt luồng hẹp nhất.

[Audit trước giờ G](pre-event-readiness-audit-2026-11-12.md) và [timeline](event-timeline.md) giữ điều kiện: nghiên cứu/chuẩn bị trước T0, triển khai submission sau giờ BTC cho phép. Remote eligibility/deadline HCMC cần xác nhận, không suy từ lời báo có thể remote. Chưa mở thêm địa bàn, model, sensor, winner research hoặc proposal mới.

## 5. Các bản chỉ đọc tham khảo

| Snapshot | Vì sao không dùng làm quyết định hiện hành? |
| --- | --- |
| [Proposal tổng thể 0.4](project-brief.md) / PDF Preliminary Proposal | Có thiết kế rộng, địa bàn/phân công/phase trước các correction; không thay roles và case hiện hành |
| [Đề xuất team 1.0](team-proposal-2026-11-12.md) / PDF Team Decision Proposal | Còn Đức Lập và bắp/đậu phộng; không dùng khóa cây hoặc cho phép làm project trước T0 |
| [Hardware paper](hardware-design-paper.md) / PDF Technical Paper An | Dùng nguyên lý đo/backup có giới hạn; phân công, inventory và pinout phải theo thông tin mới, không coi là thiết bị đã kiểm |
| Case Đức Lập, Long Khánh lịch sử, hình thoi 17 ha và workflow Earth Analog/MODIS | Giữ provenance/nghiên cứu cũ hoặc phương án không chọn; không phải địa bàn/luồng đang triển khai |

PDF snapshot có trang cảnh báo trạng thái được thêm vào, nội dung gốc giữ để truy vết. Không cần đọc chúng trước ba tài liệu hiện hành ở mục 2.
