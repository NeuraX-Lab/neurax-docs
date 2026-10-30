# 02 — Be An Earth System Trend Detective!

> Cập nhật: 2026-10-30 · Đội hình: 6 người · Độ khó theo bản nguồn: Advanced.
> Căn cứ: bản người dùng cung cấp `docs/challenges.md`, mục 2/14, từ dòng 37; nguyên văn ở cuối file. Resources chưa được cung cấp/kiểm chứng đầy đủ.

Phân tích tiếng Việt bên dưới là **đề xuất NeuraX**. “Theo bản đề” chỉ xác nhận nội dung trong tài liệu đầu vào; không chứng minh đã tải dataset hay kiểm chứng khoa học. [Quy ước nguồn](../sources/challenge-intake.md) · [Shortlist hiện hành](../rankings/v4-data-qa-shortlist.md) · [Phân công chung](../planning/team-workstreams.md).

## Yêu cầu cốt lõi theo bản đề

Chọn biến Earth science, vùng nghiên cứu và chuỗi đủ dài; trực quan hóa biến theo thời gian; tính tốc độ thay đổi và đánh giá ý nghĩa thống kê. Chỉ vẽ đường trend chưa đủ.

## Gợi ý, lựa chọn và điều không nên hiểu thành bắt buộc

t-test, Mann–Kendall hoặc khoảng tin cậy là các phương pháp được gợi ý; công cụ hỏi đáp tìm biến và phân tích phi tuyến không bắt buộc.

## DATA — đầu vào và những gì phải xác minh

Đề nêu MODIS, OMI, AIRS, GPM, MERRA-2 và GLDAS. Chọn 1–2 biến daily/monthly, ghi product/version, đơn vị, độ phân giải, QA, số kỳ thiếu và khoảng thời gian; tên mission chưa phải product đã tải được.

## AI — phân tích và baseline

Baseline tuyến tính + khoảng tin cậy; kiểm mùa vụ và tự tương quan trước diễn giải p-value. Nếu xem nhiều vùng, ghi rủi ro nhiều phép thử. Tương quan không chứng minh nguyên nhân; không có ý nghĩa thống kê vẫn là kết quả hợp lệ.

## AI — prediction có phù hợp không?

Ngoại suy chỉ là extension, không cần cho core. Nếu thử forecast, tách theo thời gian và so với seasonal-naive; trình bày ngoài biểu đồ xu hướng quan sát.

## DEPLOY — demo, dashboard và hardware

Dashboard chọn vùng/biến, chuỗi thời gian, slope, khoảng tin cậy và thẻ giải nghĩa. Thiết bị để bàn có thể điều khiển lựa chọn, nhưng không xác minh được xu hướng nhiều năm.

## Concept NeuraX: TrendLens — phòng điều tra xu hướng môi trường

### Đất diễn cho sáu thành viên — phân công đề xuất

| Thành viên | Đầu ra phụ trách |
| --- | --- |
| Hưng | Kiểm định thống kê và độ tin cậy |
| Việt — Technical Lead / DATA + AI | QA chuỗi và baseline dự báo tùy chọn; kiến trúc/contract và review kỹ thuật |
| Bích | Đơn vị, mùa vụ, giải thích biến và vùng |
| Hiếu | Dashboard và xuất báo cáo |
| Tiểu An | Bộ điều khiển hiển thị tùy chọn; kiểm dữ liệu đo |
| Quang Luật | EDA, kiểm missingness, đối chiếu slope/CI độc lập bằng R hoặc MATLAB |

Quang Luật tự báo cáo thế mạnh phân tích thống kê, trực quan hóa bằng RStudio/MATLAB, AutoCAD và báo cáo LaTeX/Overleaf (người dùng chuyển lời ngày 2026-10-30). Vai trò chính là DATA QA, đánh giá và báo cáo; hỗ trợ An kiểm thiết bị. AutoCAD là năng lực bổ trợ, không mặc định giao chế tạo vỏ/cọc/gá; chuyên môn robotics/combustion chưa được xác nhận.

## MVP đề xuất cho sự kiện 14–15/11/2026

Một vùng, 2 biến, một chu kỳ thời gian đủ dài và một phương pháp kiểm định có giả định công khai; 2 ví dụ điều tra có diễn giải.

Lịch triển khai và thời gian dự phòng theo [kế hoạch sự kiện](../planning/event-timeline.md); giờ cụ thể của HCMC 2026 chưa xác nhận.

## Cách đánh giá và bằng chứng cần có

So kết quả với phép tính tham chiếu độc lập; chuỗi tổng hợp có slope biết trước và chuỗi không trend; kiểm thiếu dữ liệu, mùa vụ, thay đổi cửa sổ.

## Rủi ro và phạm vi nên cắt

Dễ thành dashboard chung chung; hardware không có đóng góp cốt lõi, nhưng Quang Luật có vai trò QA/thống kê trực tiếp; significance bị hiểu thành tác động lớn hoặc quan hệ nhân quả.

## Điều kiện chọn trước khi triển khai

Có chuỗi đủ dài, metadata và cách xử lý mùa vụ phù hợp.

## Đánh giá độ phù hợp

Phương án dự phòng thiên về khoa học dữ liệu, khả thi hơn SAR khi nguồn khó xử lý.

## Bản đề người dùng cung cấp — nguyên văn

<details>
<summary>Mở nội dung tiếng Anh để đối chiếu</summary>

### Be An Earth System Trend Detective!

Event
2026 NASA Space Apps Challenge
Difficulty
Advanced
Subjects
Earth Science
Software
Change is always occurring in the Earth’s interconnected environmental system, and when it runs in a consistent direction – rising or falling, increasing or decreasing, thickening or thinning – measured variables reflect it. But a measured Earth science data variable can trend one way in one region and the opposite way in another, even when the same process drives both. The multitude of Earth science data variables makes it difficult to select variables that could indicate change, and to then perform an analysis on the selected variables. Your challenge is to create a tool that can select variables measured by Earth science missions or produced by Earth science models, visualize how they change over time, and determine what is changing, where it is changing, how much it is changing, and if these changes are what scientists call “significant.”

Background
Instruments on satellites observe many different aspects of the Earth system: on land, in the atmosphere, and in the oceans. Global models also use satellite instrument data and other kinds of data to examine and analyze the Earth system. One important reason for doing this is to observe and characterize changes in the Earth system. Changes, especially those moving in a particular direction over time – a trend – indicate both the processes causing such changes and the processes that will respond to them.

One complicating factor in this work is the wide variety of variables that can be studied. Another is that changes in a particular variable can move in one direction in one region and in the opposite direction in another, even when both trends are caused by the same process! So there are two important parts to this problem: finding variables that are trending, from simple ones like temperature and rainfall to more complex ones like evaporation or streamflow; and analyzing trends in particular regions of the land, ocean, or even levels of the atmosphere.

Instruments such as the Moderate Resolution Imaging Spectroradiometer (MODIS), the Ozone Monitoring Instrument (OMI), the Atmospheric Infrared Sounder (AIRS), and the Global Precipitation Measurement (GPM) provide analyzable variables. Global models – notably the Modern Era Retrospective analysis for Research and Applications, Version 2 (MERRA-2) and the Global Land Data Assimilation System (GLDAS) – provide many more. Finding, analyzing, and relating significant trends to the processes causing them is one of the most important uses of NASA Earth science data.

Objectives
A successful response to this challenge will bring together several important elements.

The first is to identify Earth science variables of interest that can be investigated for potential trends. As the Background notes, NASA and other space agencies offer numerous variables, some familiar and some more specialized for use by particular branches of science.

The second is to acquire the data variables for a particular region, since most trends in the data will not be global – though some trends can be!

The third is to generate and visualize a time series for the variable and region of interest over a long enough period of time to allow statistical analysis.

The final element of the challenge is to perform a basic statistical analysis of that time series, indicating the rate of change over time, and to test the trend’s significance using methods such as a t-test, the Mann-Kendall test, or confidence intervals.

Data sites offer tools that generate time series, and statistical analysis packages provide basic significance testing. A response that does both the visualization and the analysis meets the full scope of this challenge.

Potential Considerations
You may (but are not required to) consider the following:

Audience

This challenge involves science data and statistical analysis, so the likely audience is high school and college students, along with members of the public who have some scientific background.
Providing simple definitions of the variables would help these users considerably.
The concept is to help the users become data detectives – finding variables of interest, then determining whether those variables show a trend and whether that trend is significant.
Approach

Users could potentially respond to a short series of questions about what or where they would like to investigate, and then the answers to the questions would allow searching of related data variables. It would be highly useful to provide a couple of demonstration examples that the user could watch and would help them understand how the tool works.
While not required, SI could be useful here to identify data with the potential to show trends in particular areas, drawing on either news articles and research papers or the characteristics of a region such as a desert, rain forest, tidal estuary, or the atmosphere above a large city.
Working with the data

Earth science data are available at several different temporal resolutions – hourly, 3-hourly, daily, and monthly. For this challenge, daily and monthly data are likely the easiest to process.
Finding a trend is interesting even if it doesn’t reach the level of significance. Sometimes all a trend needs to become significant is a longer period for the data to be acquired.
Consider looking for publicly available tools for plotting hydrological data offered by outside organizations like the Consortium of Universities for the Advancement of Hydrologic Science, Inc. (CUAHSI).
Trend analysis with Earth science data can be complex. Trends can be non-linear, and some are not evident unless regular cycles, such as the seasonal cycle, are removed. More complex trend analyses are beyond the scope envisioned for this challenge; detecting and analyzing linear trends would be a great start.

For data and resources related to this challenge, refer to the Resources tab at the top of the page. More resources may be added before the hackathon begins.

</details>
