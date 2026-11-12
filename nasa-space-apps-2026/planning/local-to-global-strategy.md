> **TRẠNG THÁI 12/11 - THAM KHẢO/SNAPSHOT:** phần thiết kế, địa bàn, phân công và phase bên dưới có nội dung trước correction. Không dùng làm quyết định hiện hành. Đọc [Bắt đầu ở đây](START-HERE.md), [roles hiện hành](my-thanh-team-roles-2026-11-12.md) và [bảng R0/R1/R2 Mỹ Thành](cases/my-thanh-cai-lay/rotation-evidence-for-bich.md). Hưng-Việt cùng core/UI khi cần; Hiếu backend remote gián đoạn; Bích Data/review nguồn-feature; An ESP demo; Luật QA/thống kê/đánh giá từng block. Không lấy Đức Lập/bắp hạt/đậu phộng hoặc lời “prototype ngay” ở snapshot thay case và quy định hiện tại.

# AgroTwin: phương án nâng chất lượng cho local và global

> 12/11/2026. Kế hoạch đề xuất theo yêu cầu người dùng; mục tiêu là bài thi đủ mạnh để cạnh tranh local và được đề cử global. Chưa là cam kết giải thưởng, quyết định toàn đội hay kết quả đã triển khai. Khung năm tiêu chí dùng để review nội bộ; chưa xác nhận đầy đủ guide 2026/HCMC.

## Phương án được khuyến nghị

Giữ Field Shift, chọn một case nghiên cứu tại Đức Lập Hạ cũ (nay thuộc xã Đức Lập, Tây Ninh), người dùng là nông dân. AgroTwin là farm 2D tương tác để so kế hoạch luân canh, mở căn cứ và tìm điều kiện làm kết luận thay đổi. Sensor thật tạo một ô thử nghiệm live riêng; chip HTTPSLAB đang chờ model/datasheet. Không chờ chip để hoàn thành core NASA/K1.

Định vị làm việc: **Hiểu lựa chọn trước mùa vụ: vì sao chọn, vì sao loại, khi nào cần đổi ý.** Khác biệt hữu ích cần được chứng minh qua case địa phương, phương pháp và trải nghiệm; không tự gọi độc nhất. [Audit đối thủ](../competitor-research/field-shift-novelty-audit-2026-11-12.md) cho thấy NASA/ranking/ENSO/explanation và farm game đều có tiền lệ.

## Ba tương tác phải làm tốt

| Tương tác | Giá trị cho quyết định | Bằng chứng cần có |
| --- | --- | --- |
| Vì sao loại? | Một kế hoạch vi phạm ràng buộc được nêu lý do và nguồn, không chỉ điểm thấp | constraint_id, scope, source, trạng thái; rule được review |
| Khi nào đổi ý? | Chỉ ra thay đổi ưu tiên hoặc giả định khiến kết quả đổi, hòa hoặc chưa chắc chắn | Sweep hữu hạn trong miền cho phép, contributions; không bịa ngưỡng chính xác |
| Còn thiếu gì? | Hướng người dùng tới dữ liệu/câu hỏi cần kiểm trước khi quyết định | Danh sách thiếu gắn rule; unknown không thành pass |

Chỉ gọi ngưỡng đổi kết luận khi phương pháp thực sự tìm được: ghi rõ lưới bước, miền quét và các biến giữ cố định. Nếu không tìm thấy thì hiện “chưa thấy đổi hạng trong miền đã thử”; nếu thiếu dữ liệu thì needs_review. Cận ngưỡng số học không phải xác suất đúng nông học. Không điều chỉnh trọng số để ép một màn đảo hạng đẹp.

## Case và phương án

Nguồn khuyến nông xác nhận mô hình đậu phộng lịch sử tại Đức Lập Hạ, không đủ chứng minh hiện trạng 2026 hoặc loại đất của một thửa. Bích lập case sheet đất/nước/mùa/giống/hiện trạng/nguồn và khoảng trống. Nhóm cây nghiên cứu lúa–bắp–đậu phộng chưa là ba chuỗi đã hợp lệ. Hưng/Bích chốt hiện trạng và hai phương án sau review; nếu chỉ hai phương án đủ bằng chứng thì ghi rõ giới hạn, không bịa phương án thứ ba.

Chốt AOI nghiên cứu trước khi lấy NASA sample; tọa độ có thể là điểm nghiên cứu công khai có nhãn, không giả một ruộng đã khảo sát. Độ phân giải NASA không đủ để tách các ruộng nhỏ chỉ vì UI cho zoom gần. Nếu không có nguồn đất, giữ unknown hoặc đổi case có nguồn tốt hơn. [Dossier địa phương](local-case-scope-and-simulation.md) ghi nguồn và mapping địa danh.

## Luồng sản phẩm

NASA history → feature/quality → constraint/score → farm 2D → evidence packet. ENSO có ngày phát hành/horizon là input bối cảnh; muốn dùng thay ranking cần quan hệ địa phương hoặc forecast khu vực được dẫn nguồn. Chưa có thì dùng kịch bản giả định riêng và không gọi là dự báo El Niño tại ruộng. Sensor H1 → quality → ô live; sandbox cần bật riêng, không ghi đè dữ liệu vùng.

Farm hiển thị chuỗi cây theo mùa và các khoảng đất trống nếu lịch có căn cứ; lợi ích đất không được suy trực tiếp từ một probe ẩm. Giữ score định tính khi nguồn chỉ hỗ trợ định tính; không quy đổi thành % tăng sức khỏe đất/năng suất.

## Chuẩn bị local và gói review global

Đây là hai góc trình bày của cùng sản phẩm và cùng bằng chứng, không phải hai hệ thống. Local judges cũng cần validity; global judges cũng cần hiểu câu chuyện nhanh. Việc đạt giải local không tự bảo đảm global nomination; xác nhận quy trình đúng năm với BTC.

| Góc chuẩn bị | Local: trình bày trực tiếp theo thời lượng BTC | Global: reviewer tự xem artifact |
| --- | --- | --- |
| Hiểu bài toán | Một case Việt Nam và quyết định cụ thể | Tóm tắt tiếng Anh đủ context địa phương |
| Demo | Một đường so kế hoạch hoàn chỉnh, chuyển sensor có nhãn | Demo truy cập được, snapshot và hướng dẫn ngắn |
| Khoa học | Mở một rule/source và phép tính kiểm lại | Method/data card, manifest, E1 cùng version |
| Tính mới | Thừa nhận overlap, nêu đóng góp cần chứng minh | So dự án public theo commit/nguồn; không claim đầu tiên |
| Độ tin cậy | Thử missing/stale/mất mạng và backup | Limitations, data_as_of, cách chạy lại và phụ thuộc |
| Bài nộp | Q&A và format/deadline địa phương đã xác nhận | Guide global đúng năm, nguồn/license/AI disclosure |

Các hạng mục chỉ là lăng kính: Validity/Relevance làm nền; Presentation/Impact phải có case và artifact. Không tăng feature để cố gắn nhãn Best Technology hoặc Local Impact.

## Protocol đánh giá nhỏ nhưng có ý nghĩa

Quang Luật kiểm độc lập bảng tính/rule trong một case bằng công cụ quen thuộc; giữ input và expected output tách khỏi code sản phẩm. DATA kiểm grain/unit/time/nodata; method kiểm ràng buộc, tie, missing và sensitivity; UI kiểm hiển thị đúng trạng thái.

Đề xuất thử khám phá với 3–5 người nếu tiếp cận được, phân biệt nông dân/người tư vấn với thành viên team hoặc sinh viên. Đây là số mục tiêu tuyển, chưa là người đã tham gia. Cho cùng thông tin vào bảng tĩnh và AgroTwin, đổi thứ tự giữa người tham gia để giảm hiệu ứng học. Không cho feedback ở lượt đầu trước khi hoàn thành lượt sau. Ghi familiarity và mức hỗ trợ.

Ba tác vụ: tìm phương án bị loại và lý do; nêu điều kiện có thể đổi lựa chọn; nhận ra thông tin chưa đủ và nguồn cần kiểm. Ghi hoàn thành/thời gian/lỗi hiểu/nguyên văn feedback nếu được đồng ý; không bịa quote. Dữ liệu cá nhân không cần cho demo. Mẫu nhỏ dùng phát hiện vấn đề và cải tiến, không khẳng định statistical significance hay hiệu quả toàn bộ nông dân. Nếu chỉ test với bạn học thì gọi usability smoke test.

Gate nội bộ đề xuất: không vi phạm known hard constraints trong eligible set; phép tính khớp review độc lập; mọi lý do demo mở được source; người review phân biệt history/scenario/live; không có lỗi khiến sensor tại bàn bị hiểu thành dữ liệu ruộng. Các gate này không thay xác nhận khoa học ngoài phạm vi.

## Trình tự và cắt scope

| Mốc | Đầu ra ưu tiên | Owner dẫn / điều kiện dừng |
| --- | --- | --- |
| Chuẩn bị 12–13/11 | Case sheet, data/rule candidates, guide check, storyboard, thông số chip khi có | Hưng/Bích; Việt/Quang Luật; An. Chỉ triển khai theo thời gian BTC cho phép |
| Khối đầu của thời gian build được phép | Một case D1/Q1/K1/A1 chạy end-to-end | Việt/Hưng/Hiếu; thiếu domain thì needs_review |
| Sau core | Ba tương tác, review độc lập và fault cases | Hưng/Quang Luật/Hiếu |
| Sau khi nhận board | Adapter/log thật, live tile và stale | An/Quang Luật; không chặn core |
| Trước khóa nộp | Rehearsal, brief Anh, snapshot, hướng dẫn, link/format/credits | Cả team, Hưng tổng hợp |

Nếu phải cắt: bỏ 3D, chatbot, nguồn EO phụ, forecast học máy, cloud realtime, actuator và animation phụ trước. Giữ decision flow, NASA thực chất, K1/limits, evidence và bài nộp. Nếu thiếu chip: replay có nhãn hoặc bỏ live, không giả truyền số đo. Nếu thiếu K1: giữ case nghiên cứu minh bạch hoặc đổi case có nguồn, không dùng synthetic làm tư vấn thật.

## Storyboard và thông điệp

Mở bằng câu hỏi nông dân cần quyết, không mở bằng danh sách công nghệ. Dùng case nghiên cứu công khai, chưa đặt tên người thật nếu chưa phỏng vấn. Một kế hoạch có thể tốt về nước nhưng bị loại bởi lịch/đất; một kế hoạch có thể đổi hạng khi ưu tiên đổi; một kết quả có thể cần review khi thiếu nguồn. Sau đó minh họa phép đo live và giới hạn quy mô. Kết bằng pilot hẹp và việc sẽ đo để chứng minh ích lợi.

Draft English: “AgroTwin helps farmers explore crop-rotation choices before the next season. For a local study case, it shows why a plan is eligible, what could change the ranking, and what still needs local review. NASA climate history informs the comparison; a separate live sensor tile demonstrates point measurements.”

Đây là nháp thông điệp, không mô tả các chức năng đã triển khai. Thời lượng rehearsal nội bộ không thay thời lượng BTC. Không hứa bảo đảm an ninh lương thực, tăng năng suất hoặc chip nội địa tự bảo đảm an ninh dữ liệu.

## Gói bàn giao và tiêu chí xong

Proposal/PDF đồng bộ; paper An có trạng thái thiết bị mới và backup; case sheet/K1; sample NASA/manifest/Q1; A1/E1; storyboard; method/data card; credits; instructions/snapshot. Năm gói sản phẩm sau docs chỉ được ghi hoàn tất khi có artifact thật ở repo sản phẩm. Với mỗi claim pitch, ghi source hoặc phép thử, version, owner và giới hạn.

Không cần chờ sau local mới chuẩn bị gói review độc lập; chuẩn bị cùng core. Không tự ý sửa sản phẩm sau deadline; mọi cập nhật bài nộp theo BTC. Mục tiêu là giảm lý do bị loại và tăng chất lượng bằng chứng, không đưa xác suất thắng thiếu cơ sở.
