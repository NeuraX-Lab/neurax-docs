# 13 — Space Mission Design Game

> Cập nhật: 2026-10-30 · Đội hình: 6 người · Độ khó theo bản nguồn: Intermediate · Beginner/Youth.
> Căn cứ: bản người dùng cung cấp `docs/challenges.md`, mục 13/14, từ dòng 598; nguyên văn ở cuối file. Resources chưa được cung cấp/kiểm chứng đầy đủ.

Phân tích tiếng Việt bên dưới là **đề xuất NeuraX**. “Theo bản đề” chỉ xác nhận nội dung trong tài liệu đầu vào; không chứng minh đã tải dataset hay kiểm chứng khoa học. [Quy ước nguồn](../sources/challenge-intake.md) · [Shortlist hiện hành](../rankings/v4-data-qa-shortlist.md) · [Phân công chung](../planning/team-workstreams.md).

## Yêu cầu cốt lõi theo bản đề

Game tương tác cho người chơi thiết kế, quản lý và mô phỏng toàn nhiệm vụ, nhìn thấy trade-off giữa mục tiêu khoa học, tàu, payload, launch/orbit và tài nguyên.

## Gợi ý, lựa chọn và điều không nên hiểu thành bắt buộc

Chơi một người hoặc nhóm tối đa 4 người, multiplayer, leaderboard, random events và nhiều nhiệm vụ là gợi ý. Con số 4 nói về người chơi trong game, không giới hạn đội thi NeuraX 6 người.

## DATA — đầu vào và những gì phải xác minh

Cần bảng tham số spacecraft/instrument/launch có nguồn và ghi giả định giản lược. Bản đề không chốt dataset cụ thể; tài liệu NASA chỉ dùng sau kiểm nguồn, không tự coi mọi hằng số là dữ liệu đo.

## AI — phân tích và baseline

Constraint engine + tối ưu tổ hợp là baseline; AI mentor giải thích vì sao thiết kế không hợp lệ bằng các số đã tính.

## AI — prediction có phù hợp không?

Dự báo thành/bại là kết quả simulator theo luật; không gọi là flight certification. Simulation phải công khai giả định orbit, duty cycle và link.

## DEPLOY — demo, dashboard và hardware

Một mission và nhiều lựa chọn payload; mass/power/cost/data hiện đồng thời. An có thể làm controller; Quang Luật kiểm thống kê tài nguyên và scoring, AutoCAD chỉ khi cần.

## Concept NeuraX: Mission Architect — thiết kế nhiệm vụ với budget hữu hạn

### Đất diễn cho sáu thành viên — phân công đề xuất

| Thành viên | Đầu ra phụ trách |
| --- | --- |
| Hưng | Constraint engine và scoring |
| Việt — Technical Lead / DATA + AI | Simulation/sensitivity, mentor tùy chọn; kiến trúc/contract và review kỹ thuật |
| Bích | Mục tiêu Earth-observation và giá trị khoa học |
| Hiếu | Game UI và phản hồi thiết kế |
| Tiểu An | Giao tiếp module/bảng điều khiển |
| Quang Luật | Thống kê tài nguyên/scoring, kiểm hệ quả thay payload, AutoCAD tùy nhu cầu |

Quang Luật tự báo cáo thế mạnh phân tích thống kê, trực quan hóa bằng RStudio/MATLAB, AutoCAD và báo cáo LaTeX/Overleaf (người dùng chuyển lời ngày 2026-10-30). Vai trò chính là DATA QA, đánh giá và báo cáo; hỗ trợ An kiểm thiết bị. AutoCAD là năng lực bổ trợ, không mặc định giao chế tạo vỏ/cọc/gá; chuyên môn robotics/combustion chưa được xác nhận.

## MVP đề xuất cho sự kiện 14–15/11/2026

Một nhiệm vụ, 3–5 payload, ngân sách mass/power/cost/data; ít nhất hai thiết kế khả thi có trade-off; chơi đơn trước.

Lịch triển khai và thời gian dự phòng theo [kế hoạch sự kiện](../planning/event-timeline.md); giờ cụ thể của HCMC 2026 chưa xác nhận.

## Cách đánh giá và bằng chứng cần có

Không có cấu hình tối đa mọi thứ mà không mất chi phí; thay payload làm cập nhật đủ ràng buộc; người thử giải thích vì sao nhiệm vụ thất bại.

## Rủi ro và phạm vi nên cắt

Cơ khí có chỗ nhưng dễ tốn thời gian dựng mô hình/game thay vì khoa học; multiplayer tăng rủi ro tích hợp.

## Điều kiện chọn trước khi triển khai

Có bảng giả định nhất quán và một vòng chơi có thể kiểm.

## Đánh giá độ phù hợp

Quang Luật hỗ trợ kiểm resource/scoring nhưng vẫn sau bài dữ liệu môi trường cho mục tiêu hiện tại.

## Bản đề người dùng cung cấp — nguyên văn

<details>
<summary>Mở nội dung tiếng Anh để đối chiếu</summary>

### Space Mission Design Game

Event
2026 NASA Space Apps Challenge
Difficulty
Intermediate
Beginner/Youth
Subjects
Games
Designing a space mission requires careful consideration of competing demands, including mission objectives, spacecraft design, scientific instruments, launch vehicles, budgets, power, mass, communications, and orbital constraints. For students who rarely get to experiment with an entire mission from concept to operation, these trade-offs often remain abstract. Your challenge is to create an interactive game that allows participants to design, manage, and simulate a complete space mission while making engineering decisions, managing limited resources, and evaluating how each choice shapes the success of their mission.

Background
Space missions are complex systems in which scientific objectives, engineering requirements, available resources, and operational constraints must work together. Designing a mission involves decisions about the spacecraft, scientific instruments, launch vehicle, orbit, power, mass, communications, budget, and mission lifetime. A decision that improves one aspect of a mission can create limitations in another. For example, adding a more capable instrument may increase scientific value while also increasing mass, power consumption, data volume, and cost. Understanding these trade-offs is essential to developing successful space missions.

However, learning space mission design is often limited to theoretical exercises because students and aspiring engineers rarely have access to an environment where they can experiment with an entire mission from concept to operation. Existing tools often focus on individual topics such as orbital mechanics, spacecraft design, or rocket launches without demonstrating how these elements interact as a complete system. This leaves a gap between learning individual space concepts and understanding how mission teams make integrated engineering decisions.

An interactive game can help address this gap by allowing participants to experiment, make decisions, encounter constraints, and learn from both successful and unsuccessful missions. Players could design missions individually or collaborate in teams of up to four people, with each participant contributing to the mission strategy and working together to achieve the best possible result. Potential approaches could include mission planning, spacecraft configuration, instrument selection, resource management, orbital selection, launch planning, communications, and mission simulation. You are encouraged to develop creative alternatives that make the experience engaging while preserving the fundamental trade-offs of real-world space mission design.

Objectives
Your challenge is to create an interactive Space Mission Design Game that allows participants to experience the process of designing and managing a complete space mission. You may consider enabling a player to participate individually or collaborate with a team of up to four people, with participants working together to make strategic decisions and achieve the highest possible mission performance.

The game could allow participants to define a mission objective, establish mission requirements, design a spacecraft, select scientific instruments, choose a launch vehicle and orbit, and manage key constraints such as budget, mass, power, communications, data, and mission lifetime. Players benefit from seeing how their decisions affect other parts of the mission, and from understanding the trade-offs involved in real-world space mission design.

A strong solution might include a functional interactive game or simulation with a clear user interface, mission configuration system, resource management mechanisms, collaboration or multiplayer functionality for up to four participants, and a mission simulation and evaluation system. The game could provide feedback on mission performance and reward effective engineering decisions, efficient resource management, successful collaboration, and achievement of mission objectives. Participants are encouraged to develop creative game mechanics, visualizations, scoring systems, and mission scenarios that make the experience engaging while requiring players to solve problems, make trade-offs, and collaborate to achieve mission success.

Potential Considerations
You may (but are not required to) consider the following:

Game design and experience

The game could be accessible to participants with different levels of knowledge about space science and engineering.
The game could support both single-player and team play, allowing up to four participants to collaborate on the same mission.
Team members could have different responsibilities, such as mission planning, spacecraft design, science, communications, or resource management.
Clear objectives and feedback help participants understand why a mission succeeds or fails.
Consider making the game interactive, allowing participants to modify their mission design and simulate it multiple times.
A scoring system could reward mission success, scientific value, efficient use of resources, and effective decision making.
The game could include different difficulty levels, mission types, or scenarios.
Mission design

Participants could begin by defining a mission objective before making spacecraft and engineering decisions.
Consider giving every major design decision a consequence. For example, increasing the number of instruments could increase scientific capabilities but also increase mass, power consumption, cost, and data generation.
Consider demonstrating that there is rarely a single perfect solution. Different combinations of spacecraft, instruments, orbits, and launch vehicles could achieve the same mission objective.
Consider including realistic constraints such as limited budget, spacecraft mass, available power, communications capacity, and mission lifetime.
Spacecraft and payload

The spacecraft could include components such as structure, power systems, batteries, communications, onboard computers, attitude control, and scientific instruments.
Scientific instruments could have different characteristics, including mass, power consumption, cost, data generation, and scientific value.
Consider allowing participants to choose between simple and advanced spacecraft components depending on the difficulty level.
Orbit and launch

The game could provide several orbital options and explain their basic characteristics.
Participants could consider how the selected orbit affects coverage, observation opportunities, communications, mission lifetime, and other mission requirements.
Launch vehicles could have different payload capacities, costs, and orbital capabilities.
Consider building in a check that the spacecraft mass and selected orbit are compatible with the chosen launch vehicle.
Resource Management

The game should clearly display the main resources available to the mission team.
Important resources could include:
Mass: the total mass of the spacecraft and payload.
Power: the energy available to operate spacecraft systems and instruments.
Budget: the financial resources available to develop and operate the mission.
Data: the amount of information generated by scientific instruments.
Communications: the spacecraft's ability to transmit data to ground stations.
Time: The planned development and operational lifetime of the mission.
You may consider identifying which resources are most critical to your specific mission.
Collaboration

In team mode, up to four participants could work together on the same mission.
Consider giving team members different roles or responsibilities while asking them to make decisions collectively.
The game could include situations where team members must negotiate between competing priorities.
The final mission result could depend on how effectively the team coordinates its decisions.
Educational value

Scientific and engineering concepts work best when explained in simple terms rather than assuming advanced knowledge.
Complex concepts such as orbital altitude, payload capacity, power consumption, data rate, and communications could be introduced through the game itself.
Consider including short explanations, tutorials, visual indicators, or optional learning resources.
Consider teaching participants why a particular decision affects mission performance, rather than simply indicating whether the decision is correct or incorrect.
You may consider adding features such as:

Multiple mission scenarios with different objectives
Random events or unexpected mission constraints
Different difficulty levels
Realistic or simplified spacecraft models
Interactive spacecraft visualizations
Mission dashboards showing real-time resource consumption
Leaderboards or mission rankings
Mission reports generated at the end of each simulation
The ability to save, share, and compare mission designs
Cooperative missions for teams of up to four participants
Competitive scenarios where different teams design missions to solve the same objective
A sandbox mode that allows participants to experiment without predefined constraints
A post-mission analysis explaining why the mission succeeded or failed
For data and resources related to this challenge, refer to the Resources tab at the top of the page. More resources may be added before the hackathon begins.

</details>
