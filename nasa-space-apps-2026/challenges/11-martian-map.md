# 11 — Interplanetary Survival Guide: Martian Map

> Cập nhật: 2026-10-30 · Đội hình: 6 người · Độ khó theo bản nguồn: Intermediate.
> Căn cứ: bản người dùng cung cấp `docs/challenges.md`, mục 10/14, từ dòng 460; nguyên văn ở cuối file. Resources chưa được cung cấp/kiểm chứng đầy đủ.

Phân tích tiếng Việt bên dưới là **đề xuất NeuraX**. “Theo bản đề” chỉ xác nhận nội dung trong tài liệu đầu vào; không chứng minh đã tải dataset hay kiểm chứng khoa học. [Quy ước nguồn](../sources/challenge-intake.md) · [Shortlist hiện hành](../rankings/v4-data-qa-shortlist.md) · [Phân công chung](../planning/team-workstreams.md).

## Yêu cầu cốt lõi theo bản đề

Tích hợp dữ liệu nhiều NASA missions tại một địa điểm/tuyến Mars để hỗ trợ Marswalk vừa có mục tiêu khoa học vừa hiểu nguy cơ và khả năng di chuyển.

## Gợi ý, lựa chọn và điều không nên hiểu thành bắt buộc

Ít nhất 3 loại dữ liệu, route map, HUD/tablet và điều kiện dự báo là gợi ý. Bản đồ tĩnh cũng được đề cho phép; NeuraX chọn tương tác để thể hiện trade-off.

## DATA — đầu vào và những gì phải xác minh

Đề nêu Mars Trek, USGS-NASA mapping và ảnh rover. Chọn AOI có lớp quang học, địa hình và địa chất/thermal phù hợp; kiểm CRS, scale, thời gian và gap.

## AI — phân tích và baseline

Baseline route theo chiều dài/độ dốc + điểm khoa học; đồ thị có cạnh cấm đi khi không đủ dữ liệu hoặc vượt ngưỡng minh họa. Không suy chướng ngại nhỏ hơn pixel DEM.

## AI — prediction có phù hợp không?

Ước tính thời gian/năng lượng dưới tải giả định là mô phỏng; thiếu mô hình sinh lý nên không khẳng định oxygen/survival budget thật.

## DEPLOY — demo, dashboard và hardware

Hai tuyến nhanh hơn/ưu tiên khoa học hơn, lớp hazard và góc nhìn rover. Thiết bị cầm tay/nút chọn hướng minh họa; Quang Luật kiểm terrain/route metrics và trực quan kết quả.

## Concept NeuraX: Marswalk Planner — bản đồ nhiều lớp cho một chuyến khảo sát

### Đất diễn cho sáu thành viên — phân công đề xuất

| Thành viên | Đầu ra phụ trách |
| --- | --- |
| Hưng | Route optimization và giới hạn |
| Việt — Technical Lead / DATA + AI | Raster features và đánh giá route; kiến trúc/contract và review kỹ thuật |
| Bích | Địa hình, bối cảnh khoa học và nguồn |
| Hiếu | Layered map, route compare |
| Tiểu An | Thiết bị hiển thị/cảm biến nghiêng minh họa |
| Quang Luật | Thống kê slope/coverage, kiểm route metrics và trực quan kết quả |

Quang Luật tự báo cáo thế mạnh phân tích thống kê, trực quan hóa bằng RStudio/MATLAB, AutoCAD và báo cáo LaTeX/Overleaf (người dùng chuyển lời ngày 2026-10-30). Vai trò chính là DATA QA, đánh giá và báo cáo; hỗ trợ An kiểm thiết bị. AutoCAD là năng lực bổ trợ, không mặc định giao chế tạo vỏ/cọc/gá; chuyên môn robotics/combustion chưa được xác nhận.

## MVP đề xuất cho sự kiện 14–15/11/2026

Một AOI, 3 lớp khả dụng, 2 điểm khoa học và 2 tuyến; ghi rõ phần dữ liệu tĩnh và giả định chuyển động.

Lịch triển khai và thời gian dự phòng theo [kế hoạch sự kiện](../planning/event-timeline.md); giờ cụ thể của HCMC 2026 chưa xác nhận.

## Cách đánh giá và bằng chứng cần có

Route không xuyên vùng cấm; kiểm slope theo DEM; so shortest-path baseline; sensitivity với ngưỡng dốc và vùng thiếu dữ liệu.

## Rủi ro và phạm vi nên cắt

Bản đồ toàn cầu không đủ chi tiết Marswalk; có thể hứa an toàn từ dữ liệu độ phân giải thấp; hardware chỉ là mô phỏng Earth.

## Điều kiện chọn trước khi triển khai

Lớp dữ liệu cùng vùng, độ phân giải đủ cho câu hỏi và đường đi có thể kiểm.

## Đánh giá độ phù hợp

Ứng viên #4 giàu demo và hợp QA địa hình và kiểm thiết bị, nhưng cần giảm phạm vi địa hình và tránh hứa công cụ bay thật.

## Bản đề người dùng cung cấp — nguyên văn

<details>
<summary>Mở nội dung tiếng Anh để đối chiếu</summary>

### Interplanetary Survival Guide: Martian Map

Event
2026 NASA Space Apps Challenge
Difficulty
Intermediate
Subjects
Human Exploration
Mars
Planets & Moons
Software
Space Exploration
NASA has explored Mars robotically for decades, studying its extreme environment, mapping its surface, and collecting many types of data. Far from home, the first astronauts to set foot on Mars will want the best map possible, with information on the details of their routes and destinations, updates on current conditions, and the data needed to complete their mission quickly and safely. Your challenge is to create a layered, integrated view of a location or route on the Martian surface that pulls together data from multiple NASA science missions and could help a human explorer plan and carry out a successful Marswalk while conducting new and exciting science along the way.

Background
Human explorers are able to conduct science and do other activities that robotic systems cannot. As seen during the recent Artemis II mission’s lunar flyby, astronauts use their critical thinking skills to make connections, solve problems quickly, and apply context to observations and scientific measurements in real time. This is why NASA sends humans into the extreme environments of space, where we can learn more about our solar system and how it formed, and do science we can’t on Earth. Today, human exploration is focused on the lunar surface, with more Artemis missions upcoming and planning for the phased buildup of a Moon Base underway. Part of the role of science missions at NASA is to pave the way for humans to visit new destinations in the future. Each new robotic Mars mission has represented a hugely complex engineering challenge. Sending humans will be the biggest challenge, and the biggest achievement, yet, and becoming an interplanetary species will take all of our knowledge, imagination, and hard work.

Data from NASA’s current and past Mars missions paints a detailed picture of the planet, but it isn’t yet layered together in the combinations needed to plan specific human missions. Tools like the Jet Propulsion Laboratory’s (JPL) Mars Trek and the USGS-NASA Planetary Geologic Mapping Program allow you to layer different data over a global map of Mars, but they are built for regional and global views rather than the hyperlocalized areas astronauts will target on individual spacewalks or surface excursions.

Objectives
Your challenge is to create a map, tool, or interface a Mars astronaut could use during a surface exploration mission, using NASA data and tools. You might start by identifying some scientific goals for your mission and the location the astronaut will explore. For example, if you chose a science objective of learning more about boxwork formations, a geologic phenomenon the Curiosity rover studied in 2025, you would want to pick a location where the formations are abundant, like the Mount Sharp region where Curiosity observed them.

You might start with a location one of NASA’s Mars Rovers or another mission has explored extensively, so you have a lot of data and imagery to work with, or you might challenge yourself by focusing on an area that hasn’t been studied as closely.

You may consider including at least three kinds of data—optical, thermal, spectral, topographic, geophysical, atmospheric, radiation, and chemical are a few examples—layered or combined in a way that provides helpful context for navigating the chosen location.

NASA’s first priority is always astronaut safety, so consider what information might help a crew move safely through a new environment. For example, the radiation environment on Mars differs from those of Earth, Earth-orbit, and the Moon, so you might include space weather data. Astronauts will conduct Mars surface science wearing spacesuits and possibly carrying scientific equipment and other supplies. Consider how this might impact their mobility and, if possible, include a route map that shows where the astronaut will travel to accomplish their scientific objectives while avoiding significant obstacles such as large rock formations.

Potential Considerations
You may (but are not required to) consider the following:

You might visualize your map as a display used inside the crew’s spacecraft or habitat to plan their route, as a tablet application they carry with them, as a heads-up-display (HUD) projected on the spacesuit’s helmet visor, or in another format you imagine.
Your map can be a static snapshot, an interactive digital product, or a tool or system that generates maps of different locations or with different types of data.
Look at how NASA missions to destinations other than Mars—Earth, the Moon, other planets in our solar system, and exoplanets in other systems—have created this type of map, for inspiration.
You may choose to use data from a specific time frame in the past, predicted data and conditions for a future time frame, or no specified time frame at all, for example if you are focusing on more stable information like topography and geology.
Try looking at imagery taken by NASA’s Mars surface missions to help visualize what it would feel like to execute your mission using your map. Consider how you might include these point-of-view images as part of your map, so the astronaut knows what to expect when they arrive at their destination.
Think about whether your mission might use rovers or other robotic systems to help transport the crew and their tools, or whether the astronauts might work in pairs to accomplish more science.
For data and resources related to this challenge, refer to the Resources tab at the top of the page. More resources may be added before the hackathon begins.

</details>
