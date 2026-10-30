# 10 — Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars

> Cập nhật: 2026-10-30 · Đội hình: 6 người · Độ khó theo bản nguồn: Advanced · Intermediate · Beginner/Youth.
> Căn cứ: bản người dùng cung cấp `docs/challenges.md`, mục 9/14, từ dòng 408; nguyên văn ở cuối file. Resources chưa được cung cấp/kiểm chứng đầy đủ.

Phân tích tiếng Việt bên dưới là **đề xuất NeuraX**. “Theo bản đề” chỉ xác nhận nội dung trong tài liệu đầu vào; không chứng minh đã tải dataset hay kiểm chứng khoa học. [Quy ước nguồn](../sources/challenge-intake.md) · [Shortlist hiện hành](../rankings/v4-data-qa-shortlist.md) · [Phân công chung](../planning/team-workstreams.md).

Workflow hiện hành có schema, baseline và handoff: [earth-analog](../planning/workflows/earth-analog.md).

## Yêu cầu cốt lõi theo bản đề

Dùng dữ liệu mở Earth kết hợp Moon/Mars để tìm và mô tả một hay nhiều địa điểm analog; giải thích tương đồng, khác biệt và giá trị cho khoa học/khám phá. Không chỉ tìm ảnh giống nhau hoặc liệt kê địa điểm nổi tiếng.

## Gợi ý, lựa chọn và điều không nên hiểu thành bắt buộc

Báo cáo, bản đồ, ranking, ML, một địa điểm hoặc tìm kiếm toàn cầu đều có thể phù hợp. Một analog không cần giống mọi thuộc tính; địa điểm ít được chú ý là hướng được khuyến khích.

## DATA — đầu vào và những gì phải xác minh

Địa hình, slope, roughness, vật liệu, nhiệt và môi trường Earth/Moon/Mars theo khả năng lấy dữ liệu. Candidate: Earth DEM, LOLA/Mars DEM và dữ liệu planetary có nguồn; chưa có danh mục Resources để chốt product.

## AI — phân tích và baseline

Baseline khoảng cách đã chuẩn hóa theo từng đại lượng và trọng số từ mục tiêu thử. Tách tương đồng địa hình khỏi nhiệt/địa chất; lưu phần thiếu dữ liệu. Chọn ít ứng viên và một target planetary có đủ metadata.

## AI — prediction có phù hợp không?

Ranking/similarity là analysis, không phải forecast. Có thể dự đoán khả năng vượt dốc của thiết bị Earth chỉ sau thử bàn có kiểm soát; không ngoại suy sang trọng lực hay bụi Moon/Mars.

## DEPLOY — demo, dashboard và hardware

Bản đồ và hồ sơ analog 'giống ở đâu/không giống ở đâu'. An làm IMU/log đo độ nghiêng; Quang Luật kiểm feature/scale, sensitivity và độ lặp của log thiết bị.

## Concept NeuraX: NeuraX TerraTwin — tìm analog theo nhu cầu thử thiết bị

### Đất diễn cho sáu thành viên — phân công đề xuất

| Thành viên | Đầu ra phụ trách |
| --- | --- |
| Hưng | Mục tiêu test, dimensions/weights, review similarity và tiêu chí ranking |
| Việt — Technical Lead / DATA + AI | Feature pipeline + triển khai distance/similarity, metadata so sánh liên hành tinh; kiến trúc/contract và review kỹ thuật |
| Bích | Địa hình, môi trường và giới hạn analog |
| Hiếu | Map, so site và evidence cards |
| Tiểu An | Node đo độ nghiêng/ghi log thử thiết bị |
| Quang Luật | QC đặc trưng, kiểm normalization/sensitivity, cùng An kiểm log độ nghiêng |

Quang Luật tự báo cáo thế mạnh phân tích thống kê, trực quan hóa bằng RStudio/MATLAB, AutoCAD và báo cáo LaTeX/Overleaf (người dùng chuyển lời ngày 2026-10-30). Vai trò chính là DATA QA, đánh giá và báo cáo; hỗ trợ An kiểm thiết bị. AutoCAD là năng lực bổ trợ, không mặc định giao chế tạo vỏ/cọc/gá; chuyên môn robotics/combustion chưa được xác nhận.

## MVP đề xuất cho sự kiện 14–15/11/2026

Một mục tiêu thử mobility, một target Moon hoặc Mars, 3–5 vùng Earth có dữ liệu; ít nhất một ứng viên ngoài bộ địa điểm kinh điển, kèm lý do còn là candidate.

Lịch triển khai và thời gian dự phòng theo [kế hoạch sự kiện](../planning/event-timeline.md); giờ cụ thể của HCMC 2026 chưa xác nhận.

## Cách đánh giá và bằng chứng cần có

Thứ hạng thay đổi hợp lý theo trọng số; đối chiếu analog đã biết chỉ là sanity check; người rà độc lập kiểm đặc trưng, dữ liệu và giới hạn của candidate mới.

## Rủi ro và phạm vi nên cắt

Trọng số tùy tiện; khác resolution/projection giữa hành tinh; chưa có bằng chứng địa chất để xác nhận địa điểm mới. Earth không tái hiện gravity/vacuum/radiation ngoài hành tinh.

## Điều kiện chọn trước khi triển khai

Có cặp dữ liệu Earth–planetary so được cùng đại lượng, mục tiêu test và lập luận khoa học rõ.

## Đánh giá độ phù hợp

Khuyến nghị #2; có việc thiết bị cho An và QC/sensitivity cho Quang Luật, cùng câu chuyện không gian. Có thể lên #1 nếu Field Shift thiếu dữ liệu nông học.

## Bản đề người dùng cung cấp — nguyên văn

<details>
<summary>Mở nội dung tiếng Anh để đối chiếu</summary>

### Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars

Event
2026 NASA Space Apps Challenge
Difficulty
Advanced
Intermediate
Beginner/Youth
Subjects
Earth Science
Planets & Moons
Software
Space Exploration
Selecting future landing sites and lunar base locations depends on many factors, including topography, geology, environment, and available resources, to name a few. Places on Earth that have analogous characteristics to the Moon or Mars – the Atacama Desert, Haughton Crater, Death Valley – allow mission teams to test equipment and methods before they fly; however, such terrestrial analog sites are not entirely well characterized. Your challenge is to use open Earth, Moon, and Mars data from NASA and other space agencies to identify and characterize new terrestrial analogs for future bases or landing sites, drawing on deserts, polar regions, volcanic and arid terrains, caves, and other environments that share conditions with the lunar or Martian surface, then present your findings as a map, visualization, or other tool.

Background
Earth is our most accessible laboratory for preparing to explore the Moon and Mars. Scientists and engineers already use terrestrial “analog” environments — deserts, polar regions, volcanic landscapes, impact craters, and caves — to study planetary processes and test instruments, technologies, and exploration concepts. However, no location on Earth perfectly reproduces another planetary environment, and different locations may provide useful analogs for different characteristics.

As humanity prepares for sustained exploration of the Moon and future human exploration of Mars, we could use open Earth, Moon, and Mars data to search globally and systematically for terrestrial environments that may provide useful — and perhaps previously unrecognized — analogs. Participants might consider dimensions such as geology and surface materials, terrain type and topography, atmospheric and aeolian processes such as dust storms, temperature and other environmental extremes, water or ice, biological and habitability characteristics, subsurface environments, and conditions relevant to robotic or human operations.

The goal is not simply to rediscover well-known analog sites, or to find one place that simply looks like the Moon or Mars. Participants are encouraged to combine datasets creatively to identify and characterize locations anywhere on Earth, explain what makes them analogous and what does not, and show how these environments could help conduct lunar or Mars science and exploration. Solutions might range from identifying a compelling individual site, environment, or geophysical process to developing maps, similarity metrics, machine learning approaches, or other innovative methods for discovering and comparing planetary analogs. You might consider Earth, Moon, Mars data obtained from various NASA and other space agencies missions, as well as data and images obtained locally.

Objectives
Your challenge is to search our own planet Earth for places, environments and processes that could serve as analogs and can help us explore the Moon and Mars. Using open NASA Earth data together with available Moon and Mars data from other space agencies and open sources, identify and characterize one or more locations on Earth that could serve as useful analogs for candidate permanent Moon-base locations or future Mars landing and exploration sites. Explore what makes your Earth location analogous to the Moon or Mars. You might compare data and images of geology and surface materials, terrain and topography, temperature and environmental extremes, water or ice, dust and atmospheric processes, biology and habitability, caves or subsurface environments, or conditions relevant to robotic and human exploration. Your analog does not need to match the Moon or Mars in every way. Explain which characteristics or processes provide a strong analogy, where the analogy breaks down, and how studying or using your Earth analog could help prepare for the exploration of the Moon or Mars.

Be creative in how you search for, analyze, and communicate your analog. You could develop a written report, an interactive map, visualization, app, story, similarity-ranking system, ML tool, or another innovative approach. You might investigate a single compelling location, compare several locations around the world, or develop a method for systematically searching Earth for previously unrecognized analogs. Use open data from NASA and other space agencies as your window into Earth, the Moon, and Mars—and show us what our home planet can teach us about exploring the next ones. You might consider documenting your findings in a written format to share with other enthusiasts interested in the topic and to educate the public.

Potential Considerations
You may (but are not required to) consider the following:

Think beyond visual similarity. Two places may look alike but differ substantially in geology, environment, or physical processes. Use data to explain why your proposed Earth location is a meaningful analog.
Consider different dimensions of analogy, including:
Geology, mineralogy, and surface materials
Terrain, elevation, slope, roughness, craters, and other topographic features
Temperature, illumination, and environmental extremes
Water, ice, permafrost, and other potential resources
Dust, wind, erosion, and other atmospheric or surface processes
Biology, extremophiles, habitability, and biosignatures
Caves, lava tubes, underground environments, and other subsurface features
Conditions relevant to landing, mobility, navigation, robotic operations, human exploration, or construction
An analog does not have to match everything. An Earth location might be an excellent geological analog but a poor temperature analog, for example. Identify what is similar, how similar it is, and what is different.
Think about processes as well as places. Earth processes such as sedimentation, dust storms, volcanic activity, erosion, ice dynamics, or water-driven alteration may provide insights into processes occurring today — or that occurred in the past — on the Moon or Mars.
Look beyond well-known analog sites. Locations such as Antarctica, the Atacama Desert, Iceland, Hawaii are already widely studied. For example, NASA's global Earth-observation datasets may allow you to discover compelling analogs in places that have received much less attention.
Explore the whole Earth, including below its surface. Polar regions, deserts, mountains, volcanoes, impact craters, salt flats, glaciers, caves, lava tubes, mines, and other environments could all offer interesting possibilities.
Use multiple datasets when useful. Combining observations of terrain, temperature, geology, vegetation, water, ice, aerosols, or other characteristics may reveal relationships that are difficult to recognize using a single dataset.
Consider scale. A continent or desert does not need to be treated as a single analog. A particular crater, valley, volcanic field, cave system, or even a small area within a much larger region could provide a much stronger match.
Connect your analog to exploration. Explain how the location or process you identify could help scientists and engineers understand Moon, Mars, or both; test instruments or technologies, prepare robotic or human operations; search for resources or signs of habitability; or reduce exploration risks.
Be creative with your approach. Maps and visualizations are welcome, but solutions could also use geographic information systems (GIS), statistical analysis, similarity metrics, machine learning, interactive applications, games, or other innovative methods.
Remember Earth's limits as an analog. Earth cannot reproduce important lunar and Martian conditions such as reduced gravity, the lunar vacuum, the thin Martian atmosphere, or their radiation environments. Recognizing these differences is part of good scientific analysis.
Surprise us. A strong solution may identify an unexpected Earth location, reveal an unexpected connection between Earth and Moon or Mars, or introduce a new way of using Earth data to help enable future exploration.
For data and resources related to this challenge, refer to the Resources tab at the top of the page. More resources may be added before the hackathon begins.

</details>
