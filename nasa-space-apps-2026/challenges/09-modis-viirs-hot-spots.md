# 09 — Harmonization of MODIS and VIIRS Hot Spots

> Cập nhật: 2026-10-30 · Đội hình: 6 người · Độ khó theo bản nguồn: Advanced · Intermediate.
> Căn cứ: bản người dùng cung cấp `docs/challenges.md`, mục 8/14, từ dòng 339; nguyên văn ở cuối file. Resources chưa được cung cấp/kiểm chứng đầy đủ.

Phân tích tiếng Việt bên dưới là **đề xuất NeuraX**. “Theo bản đề” chỉ xác nhận nội dung trong tài liệu đầu vào; không chứng minh đã tải dataset hay kiểm chứng khoa học. [Quy ước nguồn](../sources/challenge-intake.md) · [Shortlist hiện hành](../rankings/v4-data-qa-shortlist.md) · [Phân công chung](../planning/team-workstreams.md).

Workflow hiện hành có schema, baseline và handoff: [modis-viirs](../planning/workflows/modis-viirs.md).

## Yêu cầu cốt lõi theo bản đề

Hài hòa chuỗi MODIS/VIIRS và xây web calendar để xem hoạt động hotspot lịch sử theo vùng và thời gian. Cốt lõi gồm cả harmonization lẫn trình bày chuỗi nhất quán.

## Gợi ý, lựa chọn và điều không nên hiểu thành bắt buộc

AOI vẽ trên bản đồ, CSV, so tháng hiện tại với lịch sử và màu dễ tiếp cận là gợi ý. Forecast không phải yêu cầu cốt lõi; không đổi bài thành chỉ cảnh báo cháy thời gian thực.

## DATA — đầu vào và những gì phải xác minh

Đề nêu FIRMS. Cần MODIS và VIIRS có giai đoạn overlap, sensor/platform, confidence/QA, acquisition time, vị trí; chọn product và xử lý nguồn nhiệt cố định khi có cơ sở.

## AI — phân tích và baseline

Baseline gộp theo ô/tháng và hiệu chỉnh trong overlap; so với chuỗi raw. Không đếm một hotspot thành một vụ cháy hoặc diện tích cháy; một sensor không là ground truth tuyệt đối cho sensor kia.

## AI — prediction có phù hợp không?

Dự báo mức hoạt động hotspot theo tháng chỉ là extension; chia thời gian và vùng giữ lại, so lịch sử mùa vụ. Không gọi đó là xác suất cháy một khu nhà hoặc cảnh báo tác nghiệp.

## DEPLOY — demo, dashboard và hardware

Calendar, AOI, chuỗi raw/harmonized, anomaly và export. An làm thiết bị hiển thị chỉ số có nhãn thời gian; Quang Luật kiểm thống kê raw/harmonized và cùng An đối chiếu display với kết quả; không dùng sensor bàn để xác minh vệ tinh.

## Concept NeuraX: NeuraX FireSense — lịch hoạt động cháy có kiểm soát khác biệt sensor

### Đất diễn cho sáu thành viên — phân công đề xuất

| Thành viên | Đầu ra phụ trách |
| --- | --- |
| Hưng | Harmonization và đánh giá ngoài mẫu |
| Việt — Technical Lead / DATA + AI | Ingestion/cell-month-sensor, anomaly baseline và forecast extension có điều kiện; kiến trúc/contract và review kỹ thuật |
| Bích | Giải thích nguồn nhiệt, mùa đốt và vùng |
| Hiếu | Web calendar, AOI và export |
| Tiểu An | Bảng hiển thị lịch sử/anomaly và trạng thái cũ |
| Quang Luật | QC chuỗi, so raw/harmonized trên holdout, thống kê sai lệch và báo cáo |

Quang Luật tự báo cáo thế mạnh phân tích thống kê, trực quan hóa bằng RStudio/MATLAB, AutoCAD và báo cáo LaTeX/Overleaf (người dùng chuyển lời ngày 2026-10-30). Vai trò chính là DATA QA, đánh giá và báo cáo; hỗ trợ An kiểm thiết bị. AutoCAD là năng lực bổ trợ, không mặc định giao chế tạo vỏ/cọc/gá; chuyên môn robotics/combustion chưa được xác nhận.

## MVP đề xuất cho sự kiện 14–15/11/2026

Một AOI, chuỗi dài nhất lấy được gồm overlap và thời kỳ VIIRS; calendar tháng, raw vs corrected, uncertainty, CSV. Nếu chỉ có mẫu ngắn phải ghi chưa bao phủ mục tiêu dài hạn đầu 2000s đến nay.

Lịch triển khai và thời gian dự phòng theo [kế hoạch sự kiện](../planning/event-timeline.md); giờ cụ thể của HCMC 2026 chưa xác nhận.

## Cách đánh giá và bằng chứng cần có

Giữ lại năm/vùng trong overlap; báo bias/MAE và ổn định seasonality; so với no-adjustment baseline; phân tích ngày ít quan sát và khoảng trống.

## Rủi ro và phạm vi nên cắt

Harmonization xóa mất biến động thật; viễn thám khác cảm biến khói tại chỗ. Nhận định đối thủ ở v2 chưa có nguồn từng dự án nên không dùng để trừ điểm v3.

## Điều kiện chọn trước khi triển khai

Có dữ liệu overlap đủ dùng và phép đối chiếu ngoài mẫu; nếu không thì không tuyên bố harmonized.

## Đánh giá độ phù hợp

Khuyến nghị #3, mạnh nhất về kiểm chứng dữ liệu trong shortlist; thế mạnh thống kê của Quang Luật tăng độ phù hợp; hardware là output hiển thị, không cần chế tạo riêng.

## Bản đề người dùng cung cấp — nguyên văn

<details>
<summary>Mở nội dung tiếng Anh để đối chiếu</summary>

### Harmonization of MODIS and VIIRS Hot Spots

Event
2026 NASA Space Apps Challenge
Difficulty
Advanced
Intermediate
Subjects
Earth Science
Software
Understanding how burning activity is distributed across our planet over time, including wildfires and agricultural burns intense enough to be detected by satellite sensors, enables us to anticipate critical periods, guide monitoring efforts, and improve fire response. Satellites have tracked active fire hotspots for more than two decades, but the record is split across sensors whose data cannot be compared directly, leaving fire managers without a consistent picture of when and where burning has occurred. Your challenge is to build a web application that harmonizes these records into a burning activity calendar based on active fire hotspots, enabling early warning and emergency responders, scientists, and land managers to examine historical fire patterns, unusual conditions, and critical periods within a selected area of interest.

Background

Fire regimes

Some ecosystems need periodic fires to maintain their function and their structure. However, changes in fire intensity, extent, and frequency can have negative impacts on climate, society, and biodiversity, along with the ecosystem services they provide. Fires can also cause loss of life and properties, degradation of health, and acute risk to fire managers.

Because humans have modified global patterns of vegetation, ignition, and climate over millennia, fires on both local and global scales are increasingly human-related.

Burning activity involves wildfires in natural vegetation and forested areas, as well as anthropogenic fires associated with agriculture, land-clearing, waste disposal, and industrial activities. It is one of the many dynamic phenomena that can be detected with remote sensing.

Satellite fire detection and monitoring

Climate models project that fire weather will become more common and more intense. Earth Observation (EO) satellites provide technological solutions for early detection, rapid response, and postfire assessment, measuring thermal radiation and smoke across regional to global scales.

Detecting hotspots on Earth's surface

EO satellites provide information on fire location, intensity, and temporal evolution. Satellite sensors operating in the thermal infrared (TIR) range can detect hotspots on the Earth's surface generated by urban and wildfires, volcanic eruptions, and industrial processes such as gas flares in oil and gas operations.

For active fires, detection and monitoring rely mainly on mid-infrared (MIR) and TIR measurements, where active combustion produces its stronger signal. Sensors such as MODIS and VIIRS provide real-time thermal anomaly detection, enabling early hotspot identification and the assessment of burned areas.

Burn activity calendars

Using satellite-detected hotspots, fire activity calendars can be developed by integrating historical information with recent data, allowing for the rapid visual identification of seasonal patterns, anomalies, and trends in each region.

MODIS sensors on board Terra and Aqua satellites provide more than two decades of observations, but they are approaching the end of their operational life and are being replaced by VIIRS sensors. Their records cannot be directly compared without harmonization, since MODIS and VIIRS have different spatial resolutions, sensitivities, and observation schedules.

Therein lies the root of the challenge. As fire frequency and intensity increase, emergency managers benefit from an updated and consistent hotspot calendar that enables them to rapidly visualize, for example, which month and years had the highest fire activity, and compare the burning activity of the current month against the historical median for a selected area.

You may consider harmonizing NASA Earthdata FIRMS hotspots, combining the extensive historical series of MODIS with the continuity and greater detail of VIIRS.

Emergency managers could then use the web application to monitor sensitive regions, recognize changes relative to historical patterns, and strengthen fire forecasting and response.

Objectives
Your challenge is to develop a harmonized burning activity calendar based on active fire hotspots in a web application, combining the extensive historical series of MODIS with the continuity and greater detail of VIIRS to provide a consistent time series of hotspot activity.

This challenge could be approached in two parts. The first is MODIS and VIIRS hotspot harmonization, so that by the end of that phase the sensor of origin no longer matters and the patterns, trends, and anomalies become the focus.

The second involves developing a web application that takes harmonized hotspot data as input. Through this visual tool, a user could select a region and a specific date range, then download analytics and visualizations of fire activity.

A calendar of burning activity showing the number of hotspots detected from the early 2000s to the present, built on the harmonized hotspots dataset and integrated into the web application, would give emergency managers a view of the fire history of an area: which periods of the year see more fires, which years had more burning activity, and how a current fire compares with previous ones.

In addition to numerical information, you could consider how color ramps might represent similarities and differences in the number of detected hotspots across months, providing an accessible and intuitive way to visualize fire activity. A downloadable CSV File of hot spots detected during a search would be another useful output.

Potential Considerations
You may (but are not required to) consider the following:

Your target audience can include early warning and emergency responders, scientists, land managers, and firefighters.
Consider making your web application interactive – for example, a map where users can draw the area of interest, or an option to enter latitude and longitude.
Consider using accessible color ramps.
Your tool could depict a burning calendar
Your tool could focus on a few key indices and figures and present them through data visualizations, such as:
Historical comparisons, including anomalies against multi-year averages
Number of fires detected and reported
For data and resources related to this challenge, refer to the Resources tab at the top of the page. More resources may be added before the hackathon begins.

Photo credit: The National Commission on Space Activities of Argentina (CONAE)

</details>
