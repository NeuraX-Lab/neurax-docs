# 14 — The Earth Information Jukebox

> Cập nhật: 2026-10-30 · Đội hình: 6 người · Độ khó theo bản nguồn: Intermediate · Beginner/Youth.
> Căn cứ: bản người dùng cung cấp `docs/challenges.md`, mục 14/14, từ dòng 692; nguyên văn ở cuối file. Resources chưa được cung cấp/kiểm chứng đầy đủ.

Phân tích tiếng Việt bên dưới là **đề xuất NeuraX**. “Theo bản đề” chỉ xác nhận nội dung trong tài liệu đầu vào; không chứng minh đã tải dataset hay kiểm chứng khoa học. [Quy ước nguồn](../sources/challenge-intake.md) · [Shortlist hiện hành](../rankings/v4-data-qa-shortlist.md) · [Phân công chung](../planning/team-workstreams.md).

## Yêu cầu cốt lõi theo bản đề

Sonification từ EIC visual frames, ghép hình với âm thanh có quan hệ giải thích được, hướng tới tiếp cận đa giác quan. Phần mở đầu nói real-time, nhưng Objectives chấp nhận cả bộ audio đã tạo kèm hình.

## Gợi ý, lựa chọn và điều không nên hiểu thành bắt buộc

ML, computer vision, API, desktop, playlist và tactile feedback là lựa chọn. Không cần vừa realtime vừa tất cả hình thức; NeuraX chọn một giao diện có điều khiển.

## DATA — đầu vào và những gì phải xác minh

EIC frames/animation với caption, legend, thời điểm và đơn vị nếu có. Không coi màu ảnh đã stylize là giá trị vật lý trực tiếp nếu chưa có mapping/legend.

## AI — phân tích và baseline

Baseline mapping nhất quán giữa đặc trưng hình và pitch/nhịp; dùng giới hạn âm lượng và quy tắc âm nhạc. AI chỉ cần nếu giúp tách đặc trưng; không thay bằng nhạc tạo ngẫu nhiên.

## AI — prediction có phù hợp không?

Prediction không tự nhiên với đề. Có thể phân tích pattern nhưng đừng làm forecast chỉ để đủ cấu trúc ba block.

## DEPLOY — demo, dashboard và hardware

Một visual sequence, audio đồng bộ, keyboard/screen-reader labels và điều khiển tactile. An làm nút/rung, Quang Luật kiểm mapping và thống kê đặc trưng, hỗ trợ thử điều khiển.

## Concept NeuraX: Earth Resonance — nghe mẫu biến đổi từ khung hình Earth data

### Đất diễn cho sáu thành viên — phân công đề xuất

| Thành viên | Đầu ra phụ trách |
| --- | --- |
| Hưng | Thiết kế mapping và kiểm độ trung thực |
| Việt — Technical Lead / DATA + AI | Đặc trưng hình và audio pipeline; kiến trúc/contract và review kỹ thuật |
| Bích | Diễn giải Earth science và legend |
| Hiếu | Player, đồng bộ và accessibility |
| Tiểu An | Nút vật lý hoặc rung có ý nghĩa |
| Quang Luật | Thống kê đặc trưng hình/âm thanh, trực quan mapping và cùng An test điều khiển |

Quang Luật tự báo cáo thế mạnh phân tích thống kê, trực quan hóa bằng RStudio/MATLAB, AutoCAD và báo cáo LaTeX/Overleaf (người dùng chuyển lời ngày 2026-10-30). Vai trò chính là DATA QA, đánh giá và báo cáo; hỗ trợ An kiểm thiết bị. AutoCAD là năng lực bổ trợ, không mặc định giao chế tạo vỏ/cọc/gá; chuyên môn robotics/combustion chưa được xác nhận.

## MVP đề xuất cho sự kiện 14–15/11/2026

Một bộ EIC frames và 2 preset mapping giải thích rõ; playback có pause/volume; thuyết minh bằng chữ; dùng được chỉ bằng bàn phím.

Lịch triển khai và thời gian dự phòng theo [kế hoạch sự kiện](../planning/event-timeline.md); giờ cụ thể của HCMC 2026 chưa xác nhận.

## Cách đánh giá và bằng chứng cần có

Cùng input cho mapping nhất quán; người thử phân biệt được pattern mục tiêu; kiểm không chỉ dựa vào màu, độ lệch audio/frame và thao tác không nhìn màn hình.

## Rủi ro và phạm vi nên cắt

Nhạc hay nhưng sai dữ liệu hoặc không tiếp cận được; chưa xác nhận kỹ năng audio của team.

## Điều kiện chọn trước khi triển khai

Có EIC frames đủ metadata, mapping và cách thử accessibility.

## Đánh giá độ phù hợp

Hardware và kiểm mapping có đóng góp rõ, nhưng không phù hợp ưu tiên prediction bằng shortlist chính.

## Bản đề người dùng cung cấp — nguyên văn

<details>
<summary>Mở nội dung tiếng Anh để đối chiếu</summary>

### The Earth Information Jukebox

Event
2026 NASA Space Apps Challenge
Difficulty
Intermediate
Beginner/Youth
Subjects
Arts & Multimedia
Earth Science
Software
NASA’s Earth Information Center (EIC) produces stunning visualizations of our changing planet, but presenting Earth science through visualization alone limits who can reach it. We invite you to make this complex Earth science accessible, engaging, and multi-sensory by translating sight into sound. Your challenge is to build an "Earth Jukebox"—an interface, script, or application that pairs EIC visual frames with dynamic sonifications generated in real time.

Background
NASA’s EIC provides extraordinary visualizations that track how our planet is changing, from shifting global temperatures to evolving oceanic currents. However, this vital information is predominantly presented in a visual format. This current landscape presents a significant gap: relying exclusively on sight limits accessibility for blind and low-vision users and constrains how the public can interact with complex Earth science.

Sonification—the process of translating data into sound—offers a powerful way to bridge this gap. Converting visual elements into audio unlocks multi-sensory ways to experience Earth data. Auditory processing can reveal subtle data patterns that might be missed by the naked eye and can foster a deeper emotional connection to our home planet. Participants might prioritize creating an interactive environment where the translation from sight to sound is exploratory, blending scientific data with artistic expression.

To do this, participants need a way to connect visual imagery with audio generation. You may consider building a "jukebox" interface or algorithm that analyzes EIC visual frames and plays a corresponding soundscape. Potential solutions could involve using computer vision to map color spectrums to musical chords, applying algorithms to translate pixel density into rhythm, or writing artistic rulesets that drive synthesizer parameters based on visual shapes. These are just examples, and we encourage you to develop your own creative alternatives that blend software development, data processing, and audio engineering.

Objectives
Your challenge is to create an "Earth Jukebox" experience that generates dynamic sonifications from NASA's EIC visual frames. The desired outcome is a project where individuals can select or experience a specific EIC visualization alongside its corresponding soundscape. You may consider developing an interactive tool that actively translates the visual data into sound, or you may choose to submit a curated collection of original, generated audio files that tell the auditory story of the data.

As you build your project, you may consider exploring a variety of methods and technologies to process the visual data. You might use computer vision techniques to analyze color palettes, shapes, or pixel densities in the EIC imagery, and map those elements to audio parameters like pitch, tempo, or instrumentation. You are welcome to employ machine learning algorithms, open-source audio synthesis frameworks, or custom data-driven artistic rulesets to generate the soundscapes. The exact method of translation is entirely up to you — we encourage you to aim for soundscapes that balance data interpretation with artistic, musically pleasing outputs.

The final deliverable can take many forms to suit your team's skills. You may consider developing an interactive web-based jukebox, a standalone desktop application, a backend API endpoint, or an engaging playlist of original, generated audio files accompanied by an explanation of the creative process used to make them. Think about how your audience will experience the visual data and how your approach can best convey the complexity of our changing planet through sound. By blending software development, audio engineering, and artistic creativity, you can create a unique multi-sensory experience.

Potential Considerations
You may (but are not required to) consider the following:

Understanding the Concepts

Sonification: the use of non-speech audio to convey information or perceptualize data.
Visual Frames: many EIC visualizations are animated sequences or images. You might explore extracting individual images (frames) from these sequences to serve as the foundation for your audio generation.
Designing Your "Jukebox" Experience

Your final submission can take many forms, from a coded, interactive user interface (UI) to a thoughtfully curated digital gallery or playlist of your original, generated audio files paired with the imagery.
If you choose to build an interactive tool, you might consider the user experience (UX) and how intuitively someone can select a visualization and initiate the audio.
Accessibility is a core theme of this challenge. You could explore adding features that support blind and low-vision users, such as screen-reader compatibility, tactile feedback, or rich descriptive text accompanying your audio.
Approaches to Data Translation

You might explore mapping visual elements—color spectrums, brightness, geometric shapes, or spatial pixel density—to audio parameters such as pitch, rhythm, tempo, volume, or instrumentation.
Consider the balance between strict data translation and musicality. A direct pixel-to-sound translation might result in chaotic noise; you may want to apply artistic rulesets, musical scales, or harmonies to make the audio engaging and pleasant to listen to.
You may explore using a variety of disciplines, from writing custom computer vision algorithms and machine learning models to utilizing audio synthesizers and digital audio workstations.
Telling the Story

Documenting your process can help others understand your vision. You might consider sharing the "why" behind your artistic choices or explaining the algorithms and scripts you used to generate the sounds.
Think about the emotional impact of the Earth science data. You might consider how your soundscapes can reflect the urgency of climate change or the beauty of our planet's interconnected systems.
For data and resources related to this challenge, refer to the Resources tab at the top of the page. More resources may be added before the hackathon begins.

</details>
