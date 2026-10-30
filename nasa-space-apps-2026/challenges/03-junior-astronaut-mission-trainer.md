# 03 — Build a Junior Astronaut Mission Trainer

> Cập nhật: 2026-10-30 · Đội hình: 6 người · Độ khó theo bản nguồn: Intermediate · Beginner/Youth.
> Căn cứ: bản người dùng cung cấp `docs/challenges.md`, mục 3/14, từ dòng 89; nguyên văn ở cuối file. Resources chưa được cung cấp/kiểm chứng đầy đủ.

Phân tích tiếng Việt bên dưới là **đề xuất NeuraX**. “Theo bản đề” chỉ xác nhận nội dung trong tài liệu đầu vào; không chứng minh đã tải dataset hay kiểm chứng khoa học. [Quy ước nguồn](../sources/challenge-intake.md) · [Shortlist hiện hành](../rankings/v4-data-qa-shortlist.md) · [Phân công chung](../planning/team-workstreams.md).

## Yêu cầu cốt lõi theo bản đề

Game/app tương tác cho trẻ 7–12 tuổi, dạy đánh đổi khi vận hành căn cứ: hỗ trợ sự sống, che chắn, năng lượng, thực phẩm và độ trễ liên lạc. Quyết định phải có hệ quả nhìn thấy.

## Gợi ý, lựa chọn và điều không nên hiểu thành bắt buộc

Đề khuyến khích dùng NASA data thật và cho phép dữ liệu lưu sẵn ghi nhãn. DONKI, OSDR, Artemis/Mars là ví dụ; không bắt buộc API live hoặc tái hiện tất cả hệ thống.

## DATA — đầu vào và những gì phải xác minh

Chọn sự kiện DONKI đã lưu và tài liệu OSDR/môi trường làm căn cứ. Không biến sự kiện Mặt Trời trực tiếp thành liều bức xạ của phi hành gia nếu thiếu mô hình vận chuyển và che chắn.

## AI — phân tích và baseline

Mô hình tài nguyên có quy tắc kiểm được là baseline. AI có thể giải thích hậu quả hoặc gợi ý nước đi từ trạng thái; tránh LLM tự phát minh số liệu vật lý.

## AI — prediction có phù hợp không?

Dự đoán trạng thái bước tiếp theo là mô phỏng theo luật trò chơi, không phải dự báo sức khỏe hoặc không gian thực tế.

## DEPLOY — demo, dashboard và hardware

Game trình duyệt một căn cứ, vài lượt và bàn điều khiển nút vật lý dùng chung logic.

## Concept NeuraX: Outpost Control — điều hành căn cứ với ba tài nguyên

### Đất diễn cho sáu thành viên — phân công đề xuất

| Thành viên | Đầu ra phụ trách |
| --- | --- |
| Hưng | Mô hình tài nguyên và trade-off |
| Việt — Technical Lead / DATA + AI | Sinh kịch bản và đánh giá luật; kiến trúc/contract và review kỹ thuật |
| Bích | Giải thích vòng tuần hoàn tài nguyên |
| Hiếu | Game UI và lưu trạng thái |
| Tiểu An | Bảng điều khiển nút/LED |
| Quang Luật | Thống kê lượt chơi, kiểm luật tài nguyên và biểu đồ học tập |

Quang Luật tự báo cáo thế mạnh phân tích thống kê, trực quan hóa bằng RStudio/MATLAB, AutoCAD và báo cáo LaTeX/Overleaf (người dùng chuyển lời ngày 2026-10-30). Vai trò chính là DATA QA, đánh giá và báo cáo; hỗ trợ An kiểm thiết bị. AutoCAD là năng lực bổ trợ, không mặc định giao chế tạo vỏ/cọc/gá; chuyên môn robotics/combustion chưa được xác nhận.

## MVP đề xuất cho sự kiện 14–15/11/2026

Ba tài nguyên: năng lượng, hỗ trợ sự sống, che chắn; một sự kiện có nguồn; mỗi lựa chọn phải tốn ít nhất một tài nguyên. Mỗi ván kết thúc bằng lý do thành/bại.

Lịch triển khai và thời gian dự phòng theo [kế hoạch sự kiện](../planning/event-timeline.md); giờ cụ thể của HCMC 2026 chưa xác nhận.

## Cách đánh giá và bằng chứng cần có

Không có lựa chọn thắng vô hạn; tài nguyên không tự sinh; người thử hiểu được một đánh đổi sau khi chơi; thử khả năng đọc và điều khiển.

## Rủi ro và phạm vi nên cắt

Cân bằng game và nội dung trẻ em tốn thời gian; không dùng dữ liệu NASA làm hình nền trang trí.

## Điều kiện chọn trước khi triển khai

Có luật đơn giản, nguồn cho giả định và cách kiểm người chơi học được gì.

## Đánh giá độ phù hợp

Có đất diễn hardware/cơ khí nhưng AI dự báo khoa học và môi trường không mạnh bằng Field Shift.

## Bản đề người dùng cung cấp — nguyên văn

<details>
<summary>Mở nội dung tiếng Anh để đối chiếu</summary>

### Build a Junior Astronaut Mission Trainer

Event
2026 NASA Space Apps Challenge
Difficulty
Intermediate
Beginner/Youth
Subjects
Games
Planets & Moons
Software
Space Exploration
Sun
Space-themed STEM content often oversimplifies the engineering trade-offs that define a real mission or presents them at a level too complex to hold a young learner's attention. Few tools make those trade-offs both tangible and fun. Your challenge is to design and build an interactive game or app that lets students run a lunar or Martian outpost, balancing competing demands like life support, radiation shielding, power, and food production, so they experience firsthand the decisions that determine whether a mission fails or succeeds.

Background
As NASA works to establish a sustained presence on the Moon and extend human exploration toward Mars, one of the most persistent challenges isn't just engineering hardware — it's building public understanding of what survival actually requires in these environments. Astronauts on a lunar or Martian outpost must balance competing demands: limited power has to be split between life support, communications, and science; radiation exposure has to be weighed against mission objectives; and every decision carries a resource cost that compounds over time. These are the same kinds of trade-offs NASA's own mission planners navigate daily, informed by real data — solar activity and radiation risk from the Space Weather Database (DONKI), astronaut radiation dosimetry and biological research from the Open Science Data Repository (OSDR), and environmental data from Artemis and Mars surface missions.

The gap is in translation. Space education content for kids often stays too abstract (e.g., posters and general facts) to convey real trade-offs or assumes a technical background too advanced for a young audience to engage with meaningfully. As a result, many students never encounter the actual decision-making logic behind a mission—only its outcomes. Content that leans purely educational often struggles to hold attention; content that leans purely toward entertainment can lose accuracy.

Participants might prioritize designing mechanics—not just visuals—that mirror real constraints: a choice that saves power today might cost oxygen tomorrow. Grounding gameplay in real NASA open data, rather than invented statistics, is encouraged. Possible approaches include survival-style resource management, narrative decision trees, or dashboard-style mission control simulators—but participants are encouraged to explore whatever format best teaches the underlying trade-off rather than conforming to any single template.

Objectives
Your challenge is to design and build an interactive game or app that lets kids ages 7–12 manage a lunar or Martian outpost, making real decisions about life support, radiation shielding, power budgeting, food production, and communication delay, and experiencing how those choices play out over the course of a simulated mission.

Think about how your tool can turn genuine mission constraints into gameplay: what does it feel like to trade oxygen reserves for an extra research opportunity, or to reinforce shielding against a radiation event at the cost of tonight's power supply? How will you represent competing resources so that no choice is free, and every decision teaches something true about what astronauts and mission planners actually navigate?

You're encouraged to ground your simulation in real NASA open data wherever possible — for example, using DONKI to reflect actual solar activity and radiation risk, the OSDR for real astronaut health and biological research findings, or Artemis and Mars surface mission data to inform environmental conditions at your chosen site. Incorporating live or archived NASA datasets, rather than fabricated numbers, will make the experience more authentic and give players a genuine window into how mission-critical decisions are made.

Format is open: you could build a resource-management survival game, a narrative-driven decision simulator, a mission-control-style dashboard experience, or something else entirely — browser-based, mobile, or desktop. The goal is a working prototype that demonstrates the trade-off mechanic clearly enough that a young player walks away understanding a real constraint of deep space survival, not just having played a fun game. Creative interpretations of "outpost," "site," or "mission" beyond the Moon and Mars are welcome, provided the underlying educational goal — teaching real engineering trade-offs through play — stays central.

Potential Considerations
You may (but are not required to) consider the following:

Audience and Accessibility

Your target audience is kids ages 7–12, but consider whether your tool can flex to engage older siblings, parents, or classroom settings too.
Favor plain language over jargon; where a scientific term is unavoidable — radiation dose, microgravity, sol — briefly explain it in-context rather than assuming prior knowledge.
Low barrier to entry matters — a browser-playable experience with no download or account required will reach more participants during judging and more students afterward.
Grounding in Real Data

Wherever possible, pull from NASA's public APIs and open datasets rather than inventing plausible-sounding numbers—even a small amount of real data—a real radiation reading, a real Mars photo, a real astronaut health finding—makes the experience meaningfully more credible than an entirely simulated one.
Clearly attribute your data sources within the tool itself, so players understand they're engaging with real NASA science, not just a themed game.
If live API calls aren't feasible during your build window, a curated real dataset embedded directly into your tool is a reasonable and honest alternative—just don't present static data as live.
Gameplay and Design Pitfalls to Avoid

Avoid designing a "safe" choice that has no cost—the educational value comes from every decision involving a genuine trade-off, mirroring real mission planning.
Don't let visual polish substitute for mechanical accuracy—a simple game that teaches a real constraint beats a beautiful one that doesn't.
Avoid overwhelming young players with too many simultaneous systems to track; two or three core resources—life support, power, shielding—are usually more effective than five or six.
What Would Make a Solution Stand Out

Tools that let players see the real-world consequences of their in-game choice—linking a radiation-shielding decision to actual current space weather data.
Replayability—mechanics or events that vary between playthroughs encourage kids to try different strategies and learn from failure without it feeling punitive.
Accompanying a working prototype with a short explanation of which NASA datasets were used and why, making the science traceable and verifiable by judges.
For data and resources related to this challenge, refer to the Resources tab at the top of the page. More resources may be added before the hackathon begins.

</details>
