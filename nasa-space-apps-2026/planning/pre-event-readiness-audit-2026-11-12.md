> Cập nhật phân công: [roles mới nhất](my-thanh-team-roles-2026-11-12.md), [điểm bắt đầu](START-HERE.md). Hưng-Việt cùng core; Bích Data; Hiếu backend remote; An demo ESP; Luật QA từng block.

# Audit chuẩn bị trước giờ G - 12/11/2026

**Kết luận:** ý tưởng vẫn đúng hướng Field Shift theo brief người dùng cung cấp; cách chuẩn bị đã phân tán quá nhiều vào tìm đất, polygon và PDF. Chưa thể gọi là sẵn sàng khuyến cáo luân canh hoặc đã có sản phẩm dùng NASA được kiểm end-to-end. Không cần đổi challenge hoặc tìm thêm địa bàn để sửa vấn đề này. Dừng mở rộng, giữ một case và ưu tiên điều kiện cây/nước, phạm vi bằng chứng, chuẩn bị theo đúng thời điểm BTC cho phép.

## 1. Fact check quyết định quan trọng nhất: làm gì trước thi?

Đã đọc câu trả lời **Paula-GO-Team ngày 05/11/2026**, có nhãn GO Team Answered, tại [nasa/spaceapps discussion #1813](https://github.com/nasa/spaceapps/discussions/1813). GO Team phân biệt nghiên cứu/chọn challenge/đọc resources/lập team trước thi với bắt đầu project khi hackathon mở **09:00 thứ Bảy theo giờ địa phương của Local Event**; làm project trước có thể dẫn đến loại. Không dùng tài liệu cũ hoặc lời khuyên “prototype ngay” của NeuraX thay quy định này.

Đây là nguồn sơ cấp mới đọc được; trang challenge, Participant FAQs và guide chính thức vẫn trả 502 trong lượt kiểm. Không suy từ lỗi truy cập rằng đã biết mọi rule hoặc Resources 2026. Quy định riêng, deadline/pitch HCMC và cách sử dụng các artifact nghiên cứu đã chuẩn bị vẫn cần Hưng xác nhận với BTC; không tự gửi liên hệ. Không tự kết luận artifact cụ thể đã vi phạm hay được miễn chỉ vì gọi nó là toolkit/research.

Ngày 14-15/11/2026 được [NASA Science](https://science.nasa.gov/universe/nasa-welcomes-all-ages-experience-levels-for-space-apps-challenge/) xác nhận. Địa điểm NOVAWORLD là thông tin người dùng, chưa xác minh địa chỉ/agenda HCMC. Không suy deadline pitch local từ deadline platform/global.

## 2. Đúng đề đến đâu, sẵn sàng đến đâu?

| Hạng mục | Bằng chứng kiểm được | Kết luận và việc cần giữ đúng |
| --- | --- | --- |
| Cốt lõi challenge | Nguyên văn brief đã lưu trong `challenges/07-field-shift.md`: NASA EO + đất + đặc tính cây + ưu tiên nông dân để khám phá luân canh | Ý tưởng align theo bản được cung cấp. Không đổi thành dự án chỉ cảnh báo độ ẩm/tưới hoặc giới thiệu chip. Live Resources chưa xác minh đủ |
| NASA và dữ liệu đất | Kiểm lại SHA của 16 raw files tại Mỹ Thành: 1 POWER và 15 WCS khớp retrieval; POWER 4.018 ngày, quality WARN | Có dữ liệu thật phục vụ nghiên cứu, không phải đã kiểm mô hình. Cờ mưa 488,17 mm ngày 14/06/2020 còn mở; không xóa/sửa |
| Địa bàn và polygon | Ranh xã có nguồn; MT-BLOCK-01 khoảng 2 ha số hóa theo ảnh 2025; trạng thái geometry ghi chưa kiểm cây/rotation/đồng nhất | Đủ định vị case minh họa, không đủ chứng minh ruộng/cây/đất phù hợp. Dừng tinh chỉnh polygon trừ lỗi thật hoặc thay hiện trạng có nguồn |
| Đất và hai phương án | SoilGrids là mô hình có khoảng dự đoán rộng; R1 bắp non/R2 đậu xanh dựa nghiên cứu lịch sử vùng | Chưa xác minh nước, giống, lịch mùa, R0 hiện tại tại block. Đây là khoảng trống quan trọng nhất, không giải quyết bằng bản đồ đẹp hơn |
| Hardware | HTTPSLAB đồng ý cho mượn theo team; datasheet/probe chưa có | Optional, không chặn core. “100% nội địa” là thông tin team cung cấp, chưa được kiểm độc lập. Đo giá thể HCM không là đo Mỹ Thành |
| ENSO | Có thể dùng outlook có ngày làm bối cảnh/kịch bản; chưa kiểm quan hệ tác động tại địa phương | Không gán hệ số giảm mưa, dự báo năng suất hoặc xác suất hạn ruộng. Không bắt buộc cho MVP |
| Toolkits và sản phẩm | README của `neurax-fieldshift-lab` và `neurax-readiness-kit` cùng nêu toolkit v0.2, tested on synthetic fixtures; không có thay đổi working tree trong lượt kiểm | Không cộng chúng thành hai bằng chứng model/dashboard NASA đã chạy. Không rerun training/test hoặc khảo sát product repo từ xa trong lượt này |
| Khác biệt và giải thưởng | Các nghiên cứu trước chưa chứng minh độc nhất hoặc có phiếu điểm giải thích vì sao winner thắng | NASA + sensor + dashboard tự nó chưa là bằng chứng mới. Giữ giá trị dự kiến là so lựa chọn có giải thích và unknown; không hứa local/global |

Hash khớp chứng minh snapshot không đổi so retrieval, không chứng minh dữ liệu đúng ngoài đồng. Không tái chạy toàn bộ QA/model hoặc coi README là kết quả chạy mới. Reference crop studies và metadata đã review trước giữ nguyên giới hạn; lượt này không tải lại tất cả nguồn.

## 3. Phạm vi khóa lại

Một địa bàn nghiên cứu Mỹ Thành; một nhóm người dùng nông dân; ba phương án **tham khảo** R0 lúa liên tục, R1 lúa-bắp non-lúa, R2 lúa-đậu xanh-lúa. R0 không được gọi là hiện trạng xác minh của block. So sánh điều kiện có nguồn, đánh đổi và thiếu thông tin; đưa ưu tiên nông dân vào tương tác. Không tự gán số tiết kiệm nước, lợi nhuận hoặc điểm phù hợp nếu thiếu cơ sở.

Hardware bàn, El Niño và farm ảo là phần bổ sung. Chúng không thay phần so luân canh có bằng chứng. Không tự thêm ML, nhiều sensor, 3D, địa bàn mới hoặc tìm winner mới để làm câu chuyện phức tạp hơn. Giữ PDF gửi Bích làm tài liệu nghiên cứu; không dùng số trang hoặc số artifact để chấm readiness.

## 4. Chỉ còn bốn gói chuẩn bị trước T0

| Owner | Đầu ra tối thiểu | Điều kiện dừng |
| --- | --- | --- |
| Hưng | Xác nhận giờ bắt đầu, deadline/pitch HCMC, yêu cầu nộp và việc dùng tài liệu/toolkit có trước; chốt một mô tả vấn đề | Có hướng dẫn BTC hoặc ghi rõ câu còn chờ; chưa làm submission project trước T0 |
| Bích - Data | Một bảng evidence cho R0/R1/R2: đúng cây, đất, mùa, nước, chống chỉ định, vị trí/năm/trang nguồn | Đủ nêu điều kiện áp dụng và unknown; không bắt xác minh đất ngoài đồng hoặc tìm vùng “hoàn hảo” |
| Hưng + Việt, Bích; Luật kiểm | Data dictionary và danh sách QA/cờ đã có; nguồn/unit/grid/time, dữ liệu dùng được và phần không dùng | Phân biệt NASA quan sát/model, SoilGrids, nguồn khác; không thêm training chỉ để có AI |
| Hiếu + An; Hưng-Việt hỗ trợ | Hiếu backend remote: khung online/handoff; An inventory/datasheet ESP/sensor; Hưng-Việt cùng output demo/UI | Không chờ phản hồi remote hoặc chip mới làm core; chưa triển khai submission trước T0 |

**Sau T0**, ưu tiên một luồng end-to-end hẹp: dữ liệu đã kiểm -> ba phương án -> điều kiện/giải thích -> thay ưu tiên/kịch bản -> kết quả nhất quán, unknown có lý do. Chỉ thêm hardware khi core ổn. Nếu domain thiếu, giữ comparison tham khảo và hiển thị chưa đủ thông tin; không biến nó thành khuyến cáo canh tác.

## 5. Quy tắc tiết kiệm quota

Mỗi lượt tiếp theo phải có một câu hỏi đóng và một artifact sửa được rủi ro thật. Tái dùng snapshot/hash và hồ sơ gửi Bích. Không tìm địa điểm, vẽ ranh, mở rộng winner research hoặc làm lại PDF khi không có bằng chứng mới ảnh hưởng quyết định. Không có tỷ lệ phần trăm “sẵn sàng” hoặc “cơ hội thắng” đáng tin để công bố. Lượt audit này không tạo PDF, build sản phẩm, cài dependency, push hoặc liên hệ ai.
