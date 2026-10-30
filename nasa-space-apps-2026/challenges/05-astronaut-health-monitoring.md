# 05 — Create Health Monitoring Software for Astronauts on Space Missions

> Cập nhật: 2026-10-30 · Đội hình: 6 người · Độ khó theo bản nguồn: Intermediate.
> Căn cứ: bản người dùng cung cấp `docs/challenges.md`, mục 4/14, từ dòng 145; nguyên văn ở cuối file. Resources chưa được cung cấp/kiểm chứng đầy đủ.

Phân tích tiếng Việt bên dưới là **đề xuất NeuraX**. “Theo bản đề” chỉ xác nhận nội dung trong tài liệu đầu vào; không chứng minh đã tải dataset hay kiểm chứng khoa học. [Quy ước nguồn](../sources/challenge-intake.md) · [Shortlist hiện hành](../rankings/v4-data-qa-shortlist.md) · [Phân công chung](../planning/team-workstreams.md).

## Yêu cầu cốt lõi theo bản đề

Phần mềm thu nhận chỉ số sức khỏe, thể hiện trực quan và giúp phi hành gia tự đánh giá, nhận hướng dẫn chăm sóc/cải thiện sức khỏe. Bản đề đề cập hỗ trợ diễn giải và hành động, không chỉ lưu số đo.

## Gợi ý, lựa chọn và điều không nên hiểu thành bắt buộc

Nhập tay, camera, hình người tương tác, nhắc đo và gamification là gợi ý; không yêu cầu thiết bị y tế do team tự chế.

## DATA — đầu vào và những gì phải xác minh

NASA Human Research Program và tài liệu cơ quan khác để hiểu hazards/indicators. Dữ liệu theo thời gian có thể là fixture tổng hợp ghi nhãn; không giả định có dữ liệu sức khỏe phi hành gia thật hay nhãn chẩn đoán.

## AI — phân tích và baseline

Baseline theo dõi thay đổi so với cá nhân, cờ chất lượng và ghi nhận triệu chứng. Nội dung sức khỏe phải truy được nguồn và có người đủ chuyên môn rà; hiện team chưa xác nhận chuyên môn lâm sàng.

## AI — prediction có phù hợp không?

Không đủ cơ sở để dự báo bệnh từ vài chỉ số hoặc cảm biến hobby. Nếu thử phát hiện bất thường thì đánh giá trên fixture và gọi đúng là kiểm logic prototype.

## DEPLOY — demo, dashboard và hardware

Dashboard theo dõi có giải thích và chuyển vấn đề cho người chuyên môn; node cảm biến chỉ minh họa luồng đo, không là thiết bị chẩn đoán.

## Concept NeuraX: CrewHealth — theo dõi chỉ số và giải thích chất lượng đo

### Đất diễn cho sáu thành viên — phân công đề xuất

| Thành viên | Đầu ra phụ trách |
| --- | --- |
| Hưng | Đánh giá logic bất thường và giới hạn |
| Việt — Technical Lead / DATA + AI | Chuỗi theo thời gian, chất lượng đo; kiến trúc/contract và review kỹ thuật |
| Bích | Tổng hợp tài liệu hazards; không thay vai trò bác sĩ |
| Hiếu | Nhập liệu và dashboard riêng tư |
| Tiểu An | Cảm biến minh họa và kiểm nhiễu |
| Quang Luật | Kiểm đơn vị/chất lượng chuỗi chỉ số và báo cáo thử sensor cùng An; không chẩn đoán |

Quang Luật tự báo cáo thế mạnh phân tích thống kê, trực quan hóa bằng RStudio/MATLAB, AutoCAD và báo cáo LaTeX/Overleaf (người dùng chuyển lời ngày 2026-10-30). Vai trò chính là DATA QA, đánh giá và báo cáo; hỗ trợ An kiểm thiết bị. AutoCAD là năng lực bổ trợ, không mặc định giao chế tạo vỏ/cọc/gá; chuyên môn robotics/combustion chưa được xác nhận.

## MVP đề xuất cho sự kiện 14–15/11/2026

Một dashboard với nhịp tim/ngủ/tự báo cáo và chất lượng dữ liệu; tình huống thiếu dữ liệu và lịch sử; chỉ hướng dẫn có nguồn được rà.

Lịch triển khai và thời gian dự phòng theo [kế hoạch sự kiện](../planning/event-timeline.md); giờ cụ thể của HCMC 2026 chưa xác nhận.

## Cách đánh giá và bằng chứng cần có

Đơn vị và timestamp đúng; phân biệt thiếu dữ liệu với bình thường; giả lập nhiễu để đo cảnh báo sai; không gọi kết quả là validation lâm sàng.

## Rủi ro và phạm vi nên cắt

Thiếu chuyên gia y tế và dữ liệu có nhãn; AI có thể diễn giải quá mức. Ngưỡng và hướng dẫn chưa xác minh là chặn nội dung, không tự đặt.

## Điều kiện chọn trước khi triển khai

Có người rà chuyên môn, nguồn đáng tin cho nội dung và dữ liệu dùng được; nếu không thì không chọn.

## Đánh giá độ phù hợp

Hardware hợp nhưng rủi ro xác thực cao; không nằm trong shortlist ưu tiên.

## Bản đề người dùng cung cấp — nguyên văn

<details>
<summary>Mở nội dung tiếng Anh để đối chiếu</summary>

### Create Health Monitoring Software for Astronauts on Space Missions

Event
2026 NASA Space Apps Challenge
Difficulty
Intermediate
Subjects
Human Exploration
Software
Space Exploration
Long-duration missions expose astronauts to space radiation, isolation and confinement, altered gravity, and a hostile closed environment, which can bring immune changes, bone loss, cardiovascular events, and behavioral health problems. On long missions, astronauts carry much of the responsibility for spotting these changes in themselves. Your challenge is to build a health monitoring software that gathers health indicators and enables astronauts to evaluate and act on the status of their health.

Background
With rising investment in spacecraft technology and research, space missions have become more ambitious. NASA’s Artemis program recently accomplished a crewed lunar flyby, and NASA and others have plans to send humans to Mars in the future. With increasingly longer missions, astronauts will be more exposed to the hostile space environment, which brings both physical and mental health risks.

NASA’s Human Research Program has mapped the five hazards of human spaceflight, which are space radiation, isolation and confinement, distance from Earth, gravity fields, and hostile closed environments. These hazards can contribute to health problems such as immune system changes, bone density loss, cardiovascular events, inadequate nutrition, behavioral health conditions, and others. Astronauts must be capable of making health assessments on themselves during a mission, to prevent and treat health problems that may arise. Some useful health indicators are blood pressure, heart rate, blood sugar, body temperature, daily sleep hours, and mood.

Objectives
Your challenge is to create a visual tool that helps astronauts assess their own health during space missions and provides guidance on treatments and health improvements. You may consider gathering data from the user through any kind of input—keyboard text, mouse clicks, or camera images, for example. Any kind of data can be used, as long as it represents a health indicator, such as blood sugar levels in mg/dL or ultrasound images.

You can use NASA’s Human Research Program resources, along with the publicly available resources from other space agencies, to understand how spaceflight hazards affect human health, and to decide which indicators are useful and how they can support a quick assessment. Which measurements can be performed in space? Why is an exam needed? How do spaceflight hazards affect these health indicators? When might a result warrant attention from the crew or from flight surgeons on the ground? What actions can be taken to prevent a critical health condition? These are questions worth considering as you develop your solution.

User interface design plays an important role in presenting metrics and diagnosis clearly. You may consider taking advantage of animations and interactivity to present the information. For example, the software could display a human figure where each part of the body is clickable and displays information about its function and health status.

Potential Considerations
You may (but are not required to) consider the following:

Your tool could provide health insights for astronauts in different environments, such as a spacecraft, a space station, a rover, or a base on another planet or moon.
Your tool could prompt astronauts to take measurements or complete specific actions from time to time as a part of the mission routine.
Your tool could include the following features:
A gamification system to help astronauts engage with tasks that support their health
Dynamic charts that show how astronaut’s health indicators change over time
Color coding that helps the astronaut interpret the status of a health indicator at a glance
Do not assume that astronauts know everything about how to assess their health. Your tool could provide simple instructions and explanations covering measurements, health indicators, and risks.
For data and resources related to this challenge, refer to the Resources tab at the top of the page. More resources may be added before the hackathon begins.

</details>
