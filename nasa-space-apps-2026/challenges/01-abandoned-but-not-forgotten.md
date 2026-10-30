# 01 — Abandoned but not Forgotten: Storytelling about NASA's Discarded Equipment on the Moon and Mars

> Cập nhật: 2026-10-30 · Đội hình: 6 người · Độ khó theo bản nguồn: Intermediate · Beginner/Youth.
> Căn cứ: bản người dùng cung cấp `docs/challenges.md`, mục 1/14, từ dòng 1; nguyên văn ở cuối file. Resources chưa được cung cấp/kiểm chứng đầy đủ.

Phân tích tiếng Việt bên dưới là **đề xuất NeuraX**. “Theo bản đề” chỉ xác nhận nội dung trong tài liệu đầu vào; không chứng minh đã tải dataset hay kiểm chứng khoa học. [Quy ước nguồn](../sources/challenge-intake.md) · [Shortlist hiện hành](../rankings/v4-data-qa-shortlist.md) · [Phân công chung](../planning/team-workstreams.md).

## Yêu cầu cốt lõi theo bản đề

Kể chuyện có căn cứ về thiết bị NASA để lại trên Moon, Mars hoặc nơi khác, giúp trẻ đi học và người xem phổ thông hiểu thiết bị đã làm gì và đóng góp khoa học nào. Không mặc định mọi thiết bị đều ngừng hoạt động.

## Gợi ý, lựa chọn và điều không nên hiểu thành bắt buộc

Bản đồ, truyện tranh, podcast, game, sách số hoặc video đều là lựa chọn; không bắt buộc web, AI, dự báo hay phần cứng.

## DATA — đầu vào và những gì phải xác minh

Lịch sử nhiệm vụ, ảnh, mô tả thiết bị và phát hiện khoa học. Bản đề chưa có URL Resources; phải chọn nguồn NASA cụ thể cho từng mốc và kiểm tra quyền dùng ảnh.

## AI — phân tích và baseline

Tra cứu có dẫn nguồn, nối thiết kế thiết bị với kết quả khoa học. AI chỉ hỗ trợ tìm và diễn đạt từ hồ sơ đã kiểm chứng; baseline là nội dung biên tập thủ công.

## AI — prediction có phù hợp không?

Không có bài toán dự báo tự nhiên. Mô phỏng giả định thiết bị còn hoạt động dễ làm sai lịch sử; không dùng chỉ để đủ block AI.

## DEPLOY — demo, dashboard và hardware

Một truyện tương tác 5 phút, 3 hiện vật và bản đồ/timeline. Nếu có mô hình vật lý, nút bấm mở đúng chương chuyện.

## Concept NeuraX: Silent Explorers — câu chuyện từ một thiết bị đã hoàn thành sứ mệnh

### Đất diễn cho sáu thành viên — phân công đề xuất

| Thành viên | Đầu ra phụ trách |
| --- | --- |
| Hưng | Kiểm soát độ chính xác câu trả lời |
| Việt — Technical Lead / DATA + AI | Trích xuất sự kiện và nguồn; kiến trúc/contract và review kỹ thuật |
| Bích | Giải thích bối cảnh khoa học, kiểm nội dung |
| Hiếu | Trải nghiệm kể chuyện tương tác |
| Tiểu An | Nút bấm hoặc âm thanh của mô hình |
| Quang Luật | Kiểm bảng sự kiện/nguồn, trực quan timeline và báo cáo khoa học |

Quang Luật tự báo cáo thế mạnh phân tích thống kê, trực quan hóa bằng RStudio/MATLAB, AutoCAD và báo cáo LaTeX/Overleaf (người dùng chuyển lời ngày 2026-10-30). Vai trò chính là DATA QA, đánh giá và báo cáo; hỗ trợ An kiểm thiết bị. AutoCAD là năng lực bổ trợ, không mặc định giao chế tạo vỏ/cọc/gá; chuyên môn robotics/combustion chưa được xác nhận.

## MVP đề xuất cho sự kiện 14–15/11/2026

Chọn một nhóm tuổi và 3 thiết bị; mỗi thiết bị có nhiệm vụ, cơ chế, khám phá và trạng thái kèm nguồn. Làm một đường đi hoàn chỉnh trước khi thêm chatbot.

Lịch triển khai và thời gian dự phòng theo [kế hoạch sự kiện](../planning/event-timeline.md); giờ cụ thể của HCMC 2026 chưa xác nhận.

## Cách đánh giá và bằng chứng cần có

Rà 100% phát biểu thực tế bằng nguồn; người xem thử trả lời được thiết bị làm gì và vì sao khám phá quan trọng. Không chấm chất lượng bằng số lần chatbot trả lời.

## Rủi ro và phạm vi nên cắt

Thế mạnh môi trường và prediction ít được dùng; nguồn lịch sử có thể bị AI trộn với chi tiết hư cấu.

## Điều kiện chọn trước khi triển khai

Có đủ 3 hồ sơ nguồn và người viết chuyện phù hợp lứa tuổi.

## Đánh giá độ phù hợp

Ưu tiên thấp với định hướng DATA → AI → DEPLOY của team; tốt nếu team chủ động chuyển trọng tâm sang giáo dục.

## Bản đề người dùng cung cấp — nguyên văn

<details>
<summary>Mở nội dung tiếng Anh để đối chiếu</summary>

### Abandoned but not Forgotten: Storytelling about NASA's Discarded Equipment on the Moon and Mars

Event
2026 NASA Space Apps Challenge
Difficulty
Intermediate
Beginner/Youth
Subjects
Astrophysics
Planets & Moons
Space Exploration
Since the 1960s, NASA has left hardware across the solar system–on the Moon, on Mars, and in deep space. From rovers and instruments that completed their science missions to probes still traveling away from Earth this hardware varies widely in both its purpose and current level of functionality. Your challenge is to tell the story of some or all of this equipment that introduces school-age space enthusiasts to the hardware and the science it made possible.

Background
For over half a century, humanity has sent incredible machines to the Moon, Mars, and other celestial bodies. When their missions end, probes, rovers, landers, descent stages, and scientific instruments are left behind, standing—or flying—silently as monuments to human exploration. While space agencies know the histories of these machines, school-age space enthusiasts often hear only about active, ongoing missions. There is a real opportunity here to inspire the next generation using the rich, untold histories of these off-world artifacts and the groundbreaking science that paved the way for today's achievements and tomorrow’s exploration.

To respond to this challenge, participants will want to know what types of equipment currently reside on the Moon, on Mars, and elsewhere—old rovers, descent stages, scientific payloads—and the specific missions they facilitated. The priority is to translate complex historical and scientific data into an engaging narrative.

People looking to learn about past space missions often work through dense technical websites or historical textbooks that lack the spark of imagination and storytelling needed to capture a younger or more casual audience's attention. Potential projects could include an interactive map of the Moon with clickable "ghost rovers," a digital graphic novel told from the perspective of a dormant Mars lander, or an audio podcast series chronicling the final days of a deep space instrument. We encourage you to think outside the box and develop your own creative alternatives!

Objectives
The goal of this challenge is to create an engaging, story-driven educational tool or narrative that teaches school-age and casual space enthusiasts about the hardware left on the Moon, Mars, and elsewhere. Your project might bring these silent or active artifacts (back) to life, explaining what they are, why they were originally sent into space, and the scientific discoveries they made and continue to make.

Your final project can take many forms, and we welcome a variety of formats and technologies. For example, you might develop an interactive web-based experience using HTML, CSS, or JavaScript; prototype an educational video game using a game engine of your choice; write and illustrate a digital children's book; produce a short animated video; design an interactive 3D timeline; or take another approach entirely!

Potential Considerations
Regardless of the medium or technology you choose, a strong narrative focus will serve your project well. Consider weaving real historical facts and mission data into your story, and showing your audience how these missions operated rather than listing facts about them. The aim is to draw a clear, exciting connection between the engineering of the hardware and the scientific knowledge humanity gained from it. By the end of your story, your audience might walk away feeling a personal connection to these forgotten robotic explorers and inspired by the science they conducted. Accuracy is important throughout!

You may (but are not required to) consider the following:

What age group is your story designed for?
How accessible is the format you chose to use?
Do you want to focus on specific missions and pieces of equipment, or tell a broader story about NASA’s exploration?
What perspective(s) do you want to highlight?
For data and resources related to this challenge, refer to the Resources tab at the top of the page. More resources may be added before the hackathon begins.

</details>
