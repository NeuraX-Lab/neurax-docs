# 07 — Field Shift: Adapting Farms with NASA Data

> Cập nhật: 2026-10-30 · Đội hình: 6 người · Độ khó theo bản nguồn: Advanced · Intermediate.
> Căn cứ: bản người dùng cung cấp `docs/challenges.md`, mục 6/14, từ dòng 216; nguyên văn ở cuối file. Resources chưa được cung cấp/kiểm chứng đầy đủ.

Phân tích tiếng Việt bên dưới là **đề xuất NeuraX**. “Theo bản đề” chỉ xác nhận nội dung trong tài liệu đầu vào; không chứng minh đã tải dataset hay kiểm chứng khoa học. [Quy ước nguồn](../sources/challenge-intake.md) · [Shortlist hiện hành](../rankings/v4-data-qa-shortlist.md) · [Phân công chung](../planning/team-workstreams.md).

Workflow hiện hành có schema, baseline và handoff: [field-shift](../planning/workflows/field-shift.md).

## Yêu cầu cốt lõi theo bản đề

Công cụ hỗ trợ nông dân khám phá luân canh thích nghi với điều kiện thay đổi, kết hợp NASA EO, đất địa phương, đặc tính cây và ưu tiên người dùng. Không thay thế quyết định nông dân hay chuyên môn nông học.

## Gợi ý, lựa chọn và điều không nên hiểu thành bắt buộc

Đề gợi ý ít nhất 3 chiến lược gồm luân canh hiện tại, giải thích bằng chứng/lợi ích/rủi ro và khoảng trống. Đây là gợi ý bằng 'may', được NeuraX chọn thành tiêu chí MVP; không bắt dùng toàn bộ dataset hoặc có hardware.

## DATA — đầu vào và những gì phải xác minh

Đề nêu SMAP, ECOSTRESS, GPM, Landsat, MODIS, NASA POWER, GRACE/GRACE-FO, SRTM và GEDI trong phần data fusion. MVP chỉ chọn 1–2 nguồn khí hậu/EO có metadata + bảng đất/cây có trích dẫn. Cảm biến điểm không thể đại diện cả pixel vệ tinh hay tự xác nhận dữ liệu lịch sử.

## AI — phân tích và baseline

Phân tích mùa khô, nóng, độ trống đất và chất lượng dữ liệu; tạo bảng đặc trưng, ràng buộc nông học và xếp hạng luân canh giải thích được. Baseline weighted/rule-based; ML chỉ được thêm khi có mục tiêu và cách kiểm tốt hơn baseline.

## AI — prediction có phù hợp không?

Việt có thể dự báo chỉ số stress khí hậu cho mùa kế tiếp bằng lịch sử, so seasonal-naive trên rolling holdout. Đó là mục tiêu đề xuất chưa được chứng minh; không suy thành dự báo năng suất hay % tiết kiệm nước. Slider mưa/nhiệt là scenario, hiển thị tách forecast.

## DEPLOY — demo, dashboard và hardware

Dashboard so luân canh + node ESP32 thu độ ẩm tương đối/nhiệt độ, hiển thị tình trạng đo và kết quả phân tích được gửi xuống. Quang Luật sở hữu QA/thống kê và cùng An kiểm log, độ lặp của phép đo. Gá/vỏ chỉ chuẩn bị nếu An cần.

## Concept NeuraX: NeuraX AgroTwin — so sánh luân canh có bằng chứng và bối cảnh đo tại chỗ

### Đất diễn cho sáu thành viên — phân công đề xuất

| Thành viên | Đầu ra phụ trách |
| --- | --- |
| Hưng | Ràng buộc, baseline ranking, model và quyết định scope |
| Việt — Technical Lead / DATA + AI | EO features + baseline/candidate forecast có gate dữ liệu; phối hợp ranking với Hưng; kiến trúc/contract và review kỹ thuật |
| Bích | Bảng cây/đất, mùa vụ và rà bằng chứng nông học |
| Hiếu | Luồng DATA–AI–dashboard, contract và demo |
| Tiểu An | Node cảm biến, firmware về sau, QA và hiển thị kết quả |
| Quang Luật | QA/EDA, kiểm feature và metric bằng R/MATLAB; cùng An kiểm log đo; báo cáo khoa học |

Quang Luật tự báo cáo thế mạnh phân tích thống kê, trực quan hóa bằng RStudio/MATLAB, AutoCAD và báo cáo LaTeX/Overleaf (người dùng chuyển lời ngày 2026-10-30). Vai trò chính là DATA QA, đánh giá và báo cáo; hỗ trợ An kiểm thiết bị. AutoCAD là năng lực bổ trợ, không mặc định giao chế tạo vỏ/cọc/gá; chuyên môn robotics/combustion chưa được xác nhận.

## MVP đề xuất cho sự kiện 14–15/11/2026

Một vùng, một loại đất có nguồn, 3 chiến lược gồm hiện trạng, 2–3 mùa; bản đồ/context, giải thích và sensitivity; một node bàn optional cho nguồn dữ liệu, nhưng là deliverable riêng của An–Quang Luật. Chưa chọn cây cụ thể khi thiếu nguồn địa phương.

Lịch triển khai và thời gian dự phòng theo [kế hoạch sự kiện](../planning/event-timeline.md); giờ cụ thể của HCMC 2026 chưa xác nhận.

## Cách đánh giá và bằng chứng cần có

Nguồn/đơn vị/grid/thời gian truy được; không có rotation vi phạm ràng buộc; đổi ưu tiên làm đổi ranking có lý do. Forecast so baseline và ghi lỗi ngoài mẫu; hardware có log, kiểm thiếu sensor, timestamp và độ lặp lại. Chưa chứng minh tăng năng suất.

## Rủi ro và phạm vi nên cắt

Thiếu dữ liệu nông học là rủi ro số 1. Dễ dùng pixel thô như đo tại ruộng, dùng soil-moisture sensor để khẳng định soil health, hoặc gọi scenario là prediction.

## Điều kiện chọn trước khi triển khai

Bích có bảng đất/cây đủ căn cứ và Việt có một mẫu NASA dùng được; An–Quang Luật xác nhận module và cách thử; nếu nông học thiếu, so gate với Earth Analog.

## Đánh giá độ phù hợp

Khuyến nghị #1. Sáu người có đầu ra riêng và cùng tham gia một vòng dữ liệu → phân tích/dự báo có kiểm chứng → quyết định/thiết bị.

## Bản đề người dùng cung cấp — nguyên văn

<details>
<summary>Mở nội dung tiếng Anh để đối chiếu</summary>

### Field Shift: Adapting Farms with NASA Data

Event
2026 NASA Space Apps Challenge
Difficulty
Advanced
Intermediate
Subjects
Arts & Multimedia
Earth Science
Software
Farmers around the world navigate shifting temperatures, changing rainfall patterns, water shortages, extreme weather, and declining soil health. These pressures make it difficult to choose crop rotations that protect fields, conserve water, and support long‑term resilience. Your challenge is to create a decision‑support tool that uses NASA Earth observations along with local soil information, crop characteristics, and farmer priorities to help farmers explore rotation strategies that could strengthen soil health and adapt their farms to changing conditions.

Background
Farmers face increasingly complex decisions as temperatures shift, rainfall becomes less predictable, and soil health declines across many regions. Water shortages, erosion, nutrient depletion, and extreme weather events add further uncertainty. Selecting new crops to add to a rotation can be difficult, because a crop that improves soil health in one place may consume too much water, introduce disease, conflict with local markets, or fall outside expected growing seasons somewhere else.

This challenge is inspired in part by multigenerational farming experience — many families have lived through seasons where better tools for tracking changing conditions could have helped identify healthier, more resilient rotation choices. Today, NASA’s long‑term environmental datasets offer new ways to understand local growing conditions, and SI techniques open opportunities to translate that data into practical, farmer‑friendly insights.

Objectives
You may consider combining NASA Earth observations with local agricultural information to create an app, model, interactive map, or other decision‑support tool. The goal is to help farmers explore crop‑rotation options that may improve soil health and strengthen resilience to changing weather and water conditions.

You may explore NASA datasets such as SMAP, ECOSTRESS, GPM, Landsat, MODIS, NASA POWER, GRACE and GRACE‑FO, and SRTM or other NASA elevation products. Using these datasets, you may analyze patterns in temperature, heat stress, rainfall, soil moisture, evaporation, frost risk, extreme precipitation, vegetation stress, and long‑term water trends. You may also consider local soil information, crop characteristics, and farmer priorities—such as water use, forage value, nitrogen‑fixing potential, erosion reduction, organic matter improvement, or market suitability.

Your tool may highlight times when fields are typically bare, seasons when current crops appear more vulnerable, or opportunities for rotations that could interrupt pest cycles, reduce water demand, improve infiltration, or add supplemental income. You may compare at least three rotation strategies, including the existing rotation. For each strategy, you may explain why it was suggested, what evidence supports it, what benefits it may offer, where information gaps exist, and any risks that would need local review by farmers or agricultural experts.

The intended outcome is a supportive tool — one that helps identify patterns and possibilities, but does not replace farmer judgment or local agricultural expertise.

Potential Considerations
You may (but are not required to) consider the following:

Understanding Conditions & Data

Explore how changes in temperature, soil moisture, rainfall, evaporation, and vegetation stress relate to crop vulnerability and soil health.
Consider explaining scientific terms such as evapotranspiration, soil moisture anomalies, vegetation indices (e.g., NDVI), frost risk, and water‑balance indicators.
Clarify how satellite observations differ from ground‑based measurements, and how combining both may improve accuracy.
SI, Modeling, and Data Fusion

You may compare different SI or statistical approaches for identifying patterns in historical climate and soil conditions.
Consider how SI could highlight seasonal transitions, bare‑field periods, or times when current crops show increased stress.
Explain how the model interprets uncertainty and where local expertise would be needed to validate results.
You may consider harmonizing datasets with different spatial and temporal resolutions by downsampling, aggregating, or resampling them to a common analysis grid. Harmonizing resolution can help the SI combine SMAP soil moisture, ECOSTRESS land‑surface temperature, GPM precipitation, Landsat/MODIS vegetation indices, GEDI biomass, and soil datasets into coherent features that support clear, explainable rotation‑strategy comparisons.
Rotation Strategy Exploration

Compare rotation scenarios by examining nutrient cycling, erosion risk, organic matter contributions, pest‑cycle disruption, water use, forage potential, or market considerations.
You may consider mapping which rotation ideas best align with farmer priorities—such as conserving water, generating supplemental income, or improving soil structure.
Include brief explanations of how nitrogen‑fixing crops, cover crops, deep‑rooting crops, or drought‑tolerant crops contribute to long‑term soil health.
Geospatial Mapping & Visualization

Consider whether interactive maps could help users explore trends over time such as long‑term soil moisture, heat waves, or water‑storage declines.
Explore ways to visualize field‑level vulnerabilities (e.g., zones of erosion risk, water stress hotspots, frost‑prone areas).
You may include optional add‑ons such as timelines, overlays comparing datasets, or scenario sliders that adjust rainfall or temperature patterns.
Farmer‑Centered Design

Consider how to make the tool easily interpretable for farmers who may have limited technical or geospatial experience.
Think about ways to allow farmers to input their own priorities or constraints, such as water availability, equipment limitations, or market preferences.
Share reminders that the tool is intended to support—not replace—local expertise, and highlight where human judgment is particularly important.
For data and resources related to this challenge, refer to the Resources tab at the top of the page. More resources may be added before the hackathon begins.

</details>
