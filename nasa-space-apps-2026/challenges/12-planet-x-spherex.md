# 12 — Planet X and SPHEREx

> Cập nhật: 2026-10-30 · Đội hình: 6 người · Độ khó theo bản nguồn: Advanced.
> Căn cứ: bản người dùng cung cấp `docs/challenges.md`, mục 12/14, từ dòng 561; nguyên văn ở cuối file. Resources chưa được cung cấp/kiểm chứng đầy đủ.

Phân tích tiếng Việt bên dưới là **đề xuất NeuraX**. “Theo bản đề” chỉ xác nhận nội dung trong tài liệu đầu vào; không chứng minh đã tải dataset hay kiểm chứng khoa học. [Quy ước nguồn](../sources/challenge-intake.md) · [Shortlist hiện hành](../rankings/v4-data-qa-shortlist.md) · [Phân công chung](../planning/team-workstreams.md).

## Yêu cầu cốt lõi theo bản đề

Web công khai nhận Right Ascension/declination, hiển thị chuỗi ảnh cùng vùng như video để thấy biến đổi. Bản đề yêu cầu thử Barnard’s Star, Epsilon Indi B, WISE 0855, RW Aurigae và R Draconis.

## Gợi ý, lựa chọn và điều không nên hiểu thành bắt buộc

Gộp 102 bands theo detector, spectra, cộng/trừ ảnh, field of view, overlay Gaia/WISE, query trong URL và cờ contamination là gợi ý. Không yêu cầu tìm ra Planet X.

## DATA — đầu vào và những gì phải xác minh

Ảnh SPHEREx nhiều epoch, WCS/coordinates, band, PSF và quality flags. Dữ liệu đủ epoch ở cả 5 đối tượng là gate; không thay SPHEREx hoàn toàn bằng survey khác.

## AI — phân tích và baseline

Baseline blink ảnh đã căn chỉnh; AI đề xuất candidate thay đổi khi có phép kiểm độc lập. Cân nhắc chuyển động riêng/parallax, nhiễu và PSF trước gắn nhãn object.

## AI — prediction có phù hợp không?

Dự đoán quỹ đạo hoặc phát hiện hành tinh không thuộc MVP; từ vài chấm khác biệt chưa thể tuyên bố khám phá.

## DEPLOY — demo, dashboard và hardware

RA/Dec → cutout → playback → metadata; cập nhật release bằng manifest. Hardware là nút điều khiển blink, đóng góp cơ khí nhỏ.

## Concept NeuraX: SPHEREx Blink — quan sát chuyển động qua nhiều thời điểm

### Đất diễn cho sáu thành viên — phân công đề xuất

| Thành viên | Đầu ra phụ trách |
| --- | --- |
| Hưng | Candidate detection và false positives |
| Việt — Technical Lead / DATA + AI | WCS, epoch alignment và kiểm ảnh; kiến trúc/contract và review kỹ thuật |
| Bích | Tổng hợp bằng chứng và giới hạn, cần hỗ trợ thiên văn |
| Hiếu | Viewer, cache và query |
| Tiểu An | Điều khiển playback tùy chọn |
| Quang Luật | QC epoch/missingness, biểu đồ kiểm alignment và báo cáo targets |

Quang Luật tự báo cáo thế mạnh phân tích thống kê, trực quan hóa bằng RStudio/MATLAB, AutoCAD và báo cáo LaTeX/Overleaf (người dùng chuyển lời ngày 2026-10-30). Vai trò chính là DATA QA, đánh giá và báo cáo; hỗ trợ An kiểm thiết bị. AutoCAD là năng lực bổ trợ, không mặc định giao chế tạo vỏ/cọc/gá; chuyên môn robotics/combustion chưa được xác nhận.

## MVP đề xuất cho sự kiện 14–15/11/2026

Cutout nhỏ, vài bands/epochs và checklist đủ 5 mục tiêu được nêu; thiếu đối tượng nào phải ghi partial, không tuyên bố đáp ứng toàn bộ.

Lịch triển khai và thời gian dự phòng theo [kế hoạch sự kiện](../planning/event-timeline.md); giờ cụ thể của HCMC 2026 chưa xác nhận.

## Cách đánh giá và bằng chứng cần có

Ngôi sao cố định căn khớp; playback đúng thứ tự; quan sát trên 5 targets; không nhầm background/PSF/contamination thành chuyển động.

## Rủi ro và phạm vi nên cắt

Astronomy domain gap, tải nhiều bands, WCS sai và quá ít epochs.

## Điều kiện chọn trước khi triển khai

Có cutout SPHEREx multi-epoch và hướng kiểm chuẩn ở targets.

## Đánh giá độ phù hợp

Ưu tiên thấp; có chiều sâu AI nhưng ít tận dụng môi trường/hardware; Quang Luật vẫn có vai trò QC và báo cáo.

## Bản đề người dùng cung cấp — nguyên văn

<details>
<summary>Mở nội dung tiếng Anh để đối chiếu</summary>

### Planet X and SPHEREx

Event
2026 NASA Space Apps Challenge
Difficulty
Advanced
Subjects
Astrophysics
Planets & Moons
Software
Since 2025, NASA’s SPHEREx mission has been mapping the entire sky every six months in 102 bands of near-infrared light, returning images of more than a billion objects. Comets, asteroids, stars, brown dwarfs, and even new planets reveal themselves by shifting position between images, but no one person can sift through all that data alone. Your challenge is to create a public-facing web tool to display images of the sky from SPHEREx mission, making it easy for anyone to quickly see how they change over time.

Background
Asteroids and comets orbit around the Sun. Nearby stars march across the sky as they orbit around the Galaxy. The Earth orbits the Sun too, causing objects near us to change their apparent positions. Watching for these motions help us discover new astronomical objects and also help measure the distances to these objects. For example, the dwarf planet Pluto was discovered when an astronomer compared two images of the sky taken at different times and recognized that one point of light had shifted between images.

More recently, astronomers have mounted massive searches for nearby objects using this process with help from the public. Hundreds of thousands of volunteers have used this technique to discover asteroids, comets, stars and brown dwarfs—balls of gas too massive to be considered planets yet without enough mass to burn like stars. In fact, most of the known comets and brown dwarfs were discovered by volunteers in this manner through projects like backyardworlds.org.

Since May 2025, NASA’s new SPHEREx mission has been returning unique data that could yield new discoveries. SPHEREx is mapping the whole sky once every six months in 102 bands of near-infrared light, making it uniquely sensitive to objects that are rich in hydrogen, water, carbon dioxide, carbon monoxide, and many other molecules. There will be too much data for any one person or even computer code to completely comprehend. There will be images of more than a billion objects - including brown dwarfs, quasars, comets, asteroids, stars, supernovae and galaxies - which often overlap or vary in brightness. We need your creative new tools to make the most of this treasure trove and help as many people as possible pitch in to make discoveries.

Objectives
Your challenge is to create a public-facing web tool to display images of the sky from the SPHEREx mission, making it easy for anyone to quickly see how they change over time. Users will enter the coordinates of a patch of sky (Right Ascension and declination). Your tool will display a series of images of that patch like a little video, making it easy to spot moving objects.

Test your tool on Barnard’s Star, Epsilon Indi B (a pair of brown dwarfs orbiting a star), WISE 0855, (a fast-moving brown dwarf Right Ascension 08h55m10.831s, declination -7d14m42.53s), and variable stars RW Aurigae and R Draconis.

Potential Considerations
You may (but are not required to) consider the following:

New SPHEREx data is arriving fast! Make sure to design a tool that’s easy to update with the latest data releases.
Think creatively about how to display those 102 infrared bands so users can take advantage of them to make new discoveries! For example, it may make sense to separately add together all the data taken by each of the six detector arrays to improve the signal-to-noise in the images you display. Extra kudos if your tool can generate spectra on the fly.
It may help users discover moving objects if they have the options to add together or subtract images taken at different times.
Let users choose the field of view! Larger fields of view can make it possible to track faster-moving sources, at the cost of longer data transfer times.
Users could benefit from having the option to overlay astronomical data from other telescopes, such as the Gaia mission or the WISE mission.
If you make it possible to query your tool by including coordinates in the URL, users will be able to easily embed it in other websites and projects.
It can be useful to display metadata, like contamination flags.
Consider looking for publicly available tools that may help in handling astronomical data, like the Astrophy tools, and in displaying astronomical data, like the Aladin tool developed by the Strasbourg Astronomical Data Center (CDS).
For data and resources related to this challenge, refer to the Resources tab at the top of the page. More resources may be added before the hackathon begins.

</details>
