# Việt — lời thoại slide 4 và 5

Phân công đã chốt: **Ngọc Bích: 1–3; Việt: 4–5; Hưng: 6–7.** Video 30 giây phát riêng. Việt có khoảng 75 giây: slide 4 khoảng 25 giây; slide 5 khoảng 50 giây gồm kiến trúc và ví dụ. Phần Anh khoảng 140 từ, nên có thời gian chỉ vào visual và chuyển người nói.

## Slide 4 — NASA DATA

### English

Thank you, Bích. NASA POWER provides our climate backbone: rainfall, temperature and humidity across 514 months, from 1984 through October 2026. We check units and missing days before building monthly estimates. The chart shows regional climate history, not measurements from one farm. Our seasonal baseline also displays an uncertainty range, so farmers can see the limits of the estimate.

### Tiếng Việt

Cảm ơn Bích. NASA POWER là trục dữ liệu khí hậu của chúng tôi: mưa, nhiệt độ và độ ẩm trong 514 tháng, từ năm 1984 đến tháng 10/2026. Chúng tôi kiểm đơn vị và ngày thiếu dữ liệu trước khi tạo ước tính theo tháng. Biểu đồ thể hiện lịch sử khí hậu vùng, không phải phép đo của một ruộng. Baseline theo mùa cũng hiển thị khoảng bất định để người dùng nhìn thấy giới hạn của ước tính.

## Slide 5 — Method và demo tĩnh

### English

ArgoTwin has two blocks. The climate block uses seasonal mean climatology. The evidence block searches seventeen bilingual cards using BM25 and character TF-IDF, then checks question support and source integrity. It returns a cited answer or declines when evidence is insufficient.

Here, poor drainage is a declared input. The mungbean guideline warns against waterlogged sites, so the system blocks that option. This shows how evidence becomes a decision check. Hưng will now explain our validation and next steps.

### Tiếng Việt

ArgoTwin có hai khối. Khối khí hậu dùng trung bình lịch sử theo mùa. Khối bằng chứng tìm trong 17 thẻ song ngữ bằng BM25 và character TF-IDF, sau đó kiểm mức hỗ trợ câu hỏi và tính toàn vẹn nguồn. Hệ thống trả câu trả lời có trích dẫn hoặc từ chối khi thiếu bằng chứng.

Trong ví dụ này, thoát nước kém là thông tin khai báo. Quy trình đậu xanh cảnh báo tránh nơi bị úng, nên hệ thống chặn phương án đó. Đây là cách bằng chứng được chuyển thành một bước kiểm quyết định. Hưng sẽ trình bày tiếp phần kiểm chứng và các bước tiếp theo.

## Điểm chỉ trên slide

- Slide 4: chỉ 514 tháng, rồi chart mưa và dải bất định. Không đọc từng nhãn trong flow.
- Slide 5: chỉ nhánh trên khi nói climate, nhánh dưới khi nói evidence; xuống ba ô ví dụ khi nói poor drainage. Không có thao tác bấm hoặc nội dung ẩn.
- Đọc một ngôn ngữ trong slot; bản Việt phục vụ hiểu nghĩa và luyện nói. Không đọc cả hai nối tiếp.
- Không gọi khoảng 80% là accuracy, hoặc nói hệ thống đã chọn được cây tốt nhất. Climatology là baseline thống kê; phần evidence không fine-tune LLM.
