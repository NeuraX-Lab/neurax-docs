# 06 — Dancing with the SARs

> Cập nhật: 2026-10-30 · Đội hình: 6 người · Độ khó theo bản nguồn: Advanced · Intermediate.
> Căn cứ: bản người dùng cung cấp `docs/challenges.md`, mục 5/14, từ dòng 181; nguyên văn ở cuối file. Resources chưa được cung cấp/kiểm chứng đầy đủ.

Phân tích tiếng Việt bên dưới là **đề xuất NeuraX**. “Theo bản đề” chỉ xác nhận nội dung trong tài liệu đầu vào; không chứng minh đã tải dataset hay kiểm chứng khoa học. [Quy ước nguồn](../sources/challenge-intake.md) · [Shortlist hiện hành](../rankings/v4-data-qa-shortlist.md) · [Phân công chung](../planning/team-workstreams.md).

## Yêu cầu cốt lõi theo bản đề

Dùng NISAR để theo dõi và trực quan hóa biến đổi bề mặt qua thời gian, giúp người dùng hiểu quan sát radar. Objectives nhấn mạnh giải pháp tương tác, dễ dùng, open-source.

## Gợi ý, lựa chọn và điều không nên hiểu thành bắt buộc

Đề cũng mở hình thức báo cáo/video/story map ở phần hướng dẫn. NeuraX ưu tiên app tương tác để bám mục tiêu chính; ảnh quang học bổ sung không thay thế NISAR.

## DATA — đầu vào và những gì phải xác minh

NISAR là nguồn trung tâm theo đề. Cần ít nhất 2 acquisitions phù hợp vùng/thời gian, product level, polarization, geometry, QA và quyền truy cập; chưa kiểm chứng được gói Resources.

## AI — phân tích và baseline

Baseline change detection sau đồng nhất lưới và geometry; phân biệt backscatter với thay đổi mặt đất. Speckle, góc tới và mưa có thể gây biến đổi tín hiệu. Không suy ra độ lún cm từ ảnh cường độ.

## AI — prediction có phù hợp không?

Forecast mặt đất là extension chỉ làm khi đủ chuỗi/nhãn; MVP chỉ phân tích biến đổi đã quan sát, kèm giả thuyết nguyên nhân.

## DEPLOY — demo, dashboard và hardware

Bản đồ trước/sau, biểu đồ chuỗi, ghi chú độ tin cậy. Node nước/ẩm tại bàn là minh họa bổ sung, không ground truth cho vùng vệ tinh xa.

## Concept NeuraX: Wetland Pulse — diễn giải biến đổi một vùng ngập nước

### Đất diễn cho sáu thành viên — phân công đề xuất

| Thành viên | Đầu ra phụ trách |
| --- | --- |
| Hưng | Phát hiện thay đổi và đánh giá |
| Việt — Technical Lead / DATA + AI | Tiền xử lý SAR và QA; kiến trúc/contract và review kỹ thuật |
| Bích | Chọn vùng và kiểm giải thích môi trường |
| Hiếu | Bản đồ tương tác và provenance |
| Tiểu An | Quy trình cảm biến nước/ẩm bổ trợ |
| Quang Luật | EDA, mask/coverage, biểu đồ phân bố biến đổi và rà thống kê độc lập |

Quang Luật tự báo cáo thế mạnh phân tích thống kê, trực quan hóa bằng RStudio/MATLAB, AutoCAD và báo cáo LaTeX/Overleaf (người dùng chuyển lời ngày 2026-10-30). Vai trò chính là DATA QA, đánh giá và báo cáo; hỗ trợ An kiểm thiết bị. AutoCAD là năng lực bổ trợ, không mặc định giao chế tạo vỏ/cọc/gá; chuyên môn robotics/combustion chưa được xác nhận.

## MVP đề xuất cho sự kiện 14–15/11/2026

Một AOI, một loại thay đổi, 2–3 thời điểm NISAR; một lớp bối cảnh; báo cáo vùng có tín hiệu thay đổi và chỗ chưa chắc.

Lịch triển khai và thời gian dự phòng theo [kế hoạch sự kiện](../planning/event-timeline.md); giờ cụ thể của HCMC 2026 chưa xác nhận.

## Cách đánh giá và bằng chứng cần có

Đồng đăng ký, mask chất lượng và vùng ổn định; đối chiếu ảnh/tài liệu độc lập phù hợp thời gian; precision/recall chỉ khi có nhãn độc lập.

## Rủi ro và phạm vi nên cắt

Tải và xử lý SAR có thể tiêu hết thời gian; đổi sang Sentinel-1 hoàn toàn sẽ lệch nguồn trung tâm của đề.

## Điều kiện chọn trước khi triển khai

Có cặp NISAR dùng được và quy trình preprocessing nhỏ; không có thì chuyển bài.

## Đánh giá độ phù hợp

Mạnh về môi trường và AI, nhưng xếp sau phương án ít rủi ro dữ liệu; hardware bổ trợ; Quang Luật ưu tiên QC và đánh giá dữ liệu.

## Bản đề người dùng cung cấp — nguyên văn

<details>
<summary>Mở nội dung tiếng Anh để đối chiếu</summary>

### Dancing with the SARs

Event
2026 NASA Space Apps Challenge
Difficulty
Advanced
Intermediate
Subjects
Earth Science
Earth's surface is an endless dance of natural processes and human activities, but these changes are often difficult to visualize, understand, and communicate. From wetland loss to forest wildfires, earthquakes, farming activities, glacier movement, and more, Earth is in a constant waltz of surface changes. Your challenge is to build an interactive application that uses radar remote sensing data from the NASA-ISRO Synthetic Aperture Radar (NISAR) mission to track and visualize one or more types of surface change at locations around the world.

Background
Earth remote sensing helps us acquire information from a bird’s eye view. Space-borne and airborne instruments image the planet and contribute to Earth observations that help decision makers in lieu of or supplement their field surveys. The most common source of energy that these instruments use is from the Sun, which reflects from objects and surfaces on the ground back to the instrument. The amount of this energy varies by the wavelength within the electromagnetic spectrum, and we can use this spectral fingerprint to identify water, rocks/minerals, vegetation, etc. These instruments that utilize the Sun’s energy conduct passive remote sensing while radar instruments, such as those we’ll use in this challenge, conduct active remote sensing.

Active instruments emit and receive their own source of energy, and in the case of radar, operate in the microwave band of the electromagnetic spectrum. Radar instruments can be used to study forest structure, soil moisture, wetlands, ocean topography, sea ice, and more. In this challenge, we will download data from SAR (synthetic aperture radar) satellites. SAR “synthesizes” a long antenna by combining a sequence of acquisitions from its actual, shorter antenna to provide higher spatial resolution data. SAR instruments send out a pulse of energy which reacts with the Earth’s surface and is reflected back to the instrument. This collection can be done day or night and even in cloudy weather, which allows for critical data collection during disaster events like oil spills, wildfires, hurricanes, etc.

Radar data is most sensitive to two things: roughness and the dielectric constant. In other words, the radar images are more than just typical satellite images that you may see with your GPS app. This roughness information characterizes the backscatter from Earth’s surface and different polarizations and can tell us something about structure, geometry, and material properties. Since water has a high dielectric constant, SAR data also highlights water bodies, flood inundation, and soil moisture. SAR can also measure fine surface movement on the centimeter scale, such as for earthquakes and land subsidence.

Objectives
On Earth's surface there is an endless dance of natural processes and human activities in constant motion, but these changes are often difficult to visualize, understand and communicate. Wetlands and floodplains are constantly extending and retracting; forest footprints are shrinking from deforestation and wildfires; agricultural lands transform their crop types and health, moisture is swelling and shrinking in soils; glaciers and sea ice are in a constant waltz; and land surfaces are deforming from earthquakes and coastal subsidence. All of these changes have important implications for ecosystems, water resources, agriculture and infrastructures, ultimately impacting local communities.

In this challenge, participants will build an interactive application that leverages radar remote sensing data from NISAR to track and visualize one or more types of surface changes, at locations around the world. Participants are encouraged to design intuitive tools and innovative visualizations, such as interactive change-detection maps, time-series animations, or dashboards, that make NISAR data accessible to a broad audience. The desired outcome is an open-source, user-friendly solution that translates complex radar observations into actionable insights, helping scientists, resource managers, educators, decision-makers, and the public better understand the patterns and rhythms of Earth’s surface at different time steps.

First, pick an interesting study area – this can be your hometown, a tropical wetland, ice sheet, forest wildfire, flooded neighborhood, volcano eruption, etc. - wherever the music calls you! Second, download freely available NISAR data using the list of resources provided. You may want to download supplemental data such as optical images or GIS (geographic information systems) layers to contextualize the SAR imagery. And lastly, present your findings in an interactive digital medium you prefer: a final report, video, presentation slides, story map - even an interpretive dance? Hypothesize the physical drivers behind what you see (or don’t see) in the SAR data. For example, if you are looking at the Amazon Rainforest, why might the vegetation change over time? Which polarizations highlight these changes on land and ice? What future applications of NISAR are possible?

Potential Considerations
You may (but are not required to) consider the following:

Analyze NISAR data with different polarizations and/or different frequencies (from other sensors). Download data from different dates to show a time series and ancillary datasets (population, vegetation type, etc.) to contextualize the study area.
Show how human drivers (agriculture, industry, etc.) are impacting Earth’s natural resources.
Focus on compelling storytelling through data visualizations. Your project summary can be in any digital medium you prefer: a final report, video, presentation slides, story map, etc.
If you are familiar with your study area (e.g., it’s your hometown), you can provide personal context and stories for the SAR imagery.
Consider making your summary interactive (e.g., image sliders, web maps, etc.).
For data and resources related to this challenge, refer to the Resources tab at the top of the page. More resources may be added before the hackathon begins.

</details>
