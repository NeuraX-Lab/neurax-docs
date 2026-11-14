# Yêu cầu dữ liệu gửi Ngọc Bích — AgroTwin / Mỹ Thành

> Ngày 14/11/2026, Asia/Saigon (UTC+7). Người giao: Việt theo yêu cầu hiện tại; người tìm/review Data: Ngọc Bích; phối hợp Hưng và Quang Luật. Đây là tài liệu để người dùng gửi Bích, chưa gửi tin hay xác nhận Bích đã nhận việc.

## Tin nhắn có thể gửi nguyên đoạn

Bích ơi, team cần dữ liệu public, truy cập miễn phí về đất–nước–cây–mùa vụ tại Việt Nam để bổ sung NASA cho AgroTwin. Ưu tiên Mỹ Thành/khối MT-BLOCK-01, sau đó Cai Lậy–Tiền Giang theo địa danh lịch sử và vùng tương đồng ở ĐBSCL; dữ liệu vùng khác phải ghi giới hạn, chưa chuyển thành số của ruộng.

NASA đã có POWER mưa/nhiệt/độ ẩm không khí 01/2015–10/2026, MODIS NDVI/EVI 2023–2025 và metadata SMAP/IMERG. Pack đã có pH/cát/sét SoilGrids dạng mô hình, chưa phải mẫu đất địa phương. Bích ưu tiên tìm phần NASA chưa có: đất đo/bản đồ đất, tưới–thoát nước/mặn, lịch và yêu cầu đúng lúa–bắp non–đậu xanh, cùng nghiên cứu đối chứng để validation. Nếu có chuỗi trạm mưa/nhiệt ở Việt Nam thì tìm thêm để đối chiếu NASA.

Dữ liệu thời tiết ưu tiên 2015–2025, tối thiểu 2019–2025; phần 2026 tới tháng 10 là bổ sung cho bối cảnh hiện tại. Đất ưu tiên khảo sát/bản mới 2020–2026; tài liệu cũ vẫn dùng làm reference có năm và phạm vi. Lịch vụ/hiện trạng ưu tiên 2024–2026. Nghiên cứu luân canh có thể từ 2000–2026 nếu có phương pháp/đối chứng, không bỏ bài CTU cũ chỉ vì năm xuất bản.

Mỗi nguồn gửi kèm link/file, địa điểm, năm đo và năm công bố, biến/đơn vị/phương pháp, độ sâu nếu là đất, nguồn miễn phí/quyền dùng và nguồn đó chứng minh được điều gì. CSV/Excel tốt; PDF có bảng số cũng được, chỉ giúp trích bảng và ghi trang. Không cần tự scale, nội suy, ghép NASA hoặc train. Tiếp tục 12 hàng review sẵn có trong pack; chỗ chưa tìm được ghi unknown và việc đã thử.

Mục tiêu team là có baseline để kiểm chứng chiều–tối thứ Bảy 14/11. Đề xuất gửi nguồn tìm được theo từng đợt, ưu tiên crop rules + nước/đất + reference đối chứng trước; chuỗi trạm dài có thể bổ sung sau. Không cần chờ đủ tất cả mới bàn giao.

## 1. Đầu ra sản phẩm đang được định hướng

Hưng đang làm lại dashboard; layout và toàn bộ tính năng chưa chốt. Ba đầu ra đã được người dùng nêu: (a) thông tin thổ nhưỡng/đất, (b) dự báo mưa, (c) hỗ trợ so sánh/recommend luân canh. Dữ liệu Bích tìm cần giúp kiểm tính đúng của những đầu ra này; không mặc định phải có số cho mọi chỉ số.

Phạm vi nghiên cứu: **MT-BLOCK-01**, 1,996 ha, tâm 10.4790980766 N / 106.0216210397 E, Mỹ Thành, Đồng Tháp theo pack v1.3. Ranh số hóa trên ảnh, chưa là ranh pháp lý hoặc ruộng/crop/soil đồng nhất đã xác minh. Geometry nguồn ở `NeuraX-MyThanh-Bich-Research-Pack/gis/study-block.geojson`. Ranh xã 52,3 km² là context khác. Giữ địa danh và mã đơn vị theo năm; không ghép tỉnh/huyện cũ/mới chỉ theo tên.

## 2. NASA/toàn cầu hiện có gì và Việt Nam cần bổ sung gì?

| Output | Đã có trong EDA | Cần dữ liệu Việt Nam / tại Việt Nam | Mức ưu tiên |
| --- | --- | --- | --- |
| Mưa/nhiệt lịch sử | POWER 4.322 ngày, 142 tháng 2015-01 → 2026-10; PRECTOTCORR/T2M/T2M_MIN/T2M_MAX/RH2M | Trạm quan trắc mưa/nhiệt có tọa độ, thời gian, QA, đơn vị và quy ước ngày để so chéo | P1; không chặn baseline thuật toán nếu chưa có |
| Soil panel | SoilGrids pH/clay/sand tại 1 ô model, mean + Q05/Q95, tới 30 cm cho pH | Soil samples/map có địa bàn/phương pháp, EC/mặn/phèn, khả năng giữ/thoát nước; SOC/OM hoặc N/P/K chỉ nếu thật sự có | P0 cho căn cứ/rủi ro; chỉ số chưa có giữ unknown |
| Lịch luân canh | R0 lúa–lúa–lúa, R1 lúa–bắp non–lúa, R2 lúa–đậu xanh–lúa là reference scenarios | Giống/sản phẩm, thời gian sinh trưởng, lịch gieo/thu/chuyển vụ, đất/nước phù hợp và không phù hợp | P0 |
| Điều kiện tưới/tiêu | Mưa NASA, chưa có water management | Nguồn/lịch tưới, ngập/thoát, EC nước nếu có, điều kiện đổi ruộng lúa sang cây cạn | P0; thiếu sẽ chặn kết luận phù hợp ngoài đồng |
| Reference/validation | Bài CTU lịch sử trong pack, 12 hàng review chưa ký | Nghiên cứu có đối chứng, outcome/đơn vị/method/n rõ; nguồn kiểm chứng riêng theo từng block | P0 |
| Vùng nông nghiệp/hiện trạng | Block minh họa; MODIS 69 kỳ, strict giữ 26, chưa xác nhận cây | Bản đồ sử dụng đất thực tế/cropland và lịch/cây có ngày; phân biệt hiện trạng với quy hoạch | P1; hiện trạng cây tối thiểu ghi được có/không có nguồn |

SMAP vẫn chưa có numeric values ở route ORNL tại điểm này; IMERG mới có catalog/granule metadata, chưa scientific subset. Không giao Bích “tìm lại tất cả NASA”; Việt phụ trách nguồn NASA và adapter. SoilGrids là **ISRIC, không phải NASA**, và đã có trong pack. Dữ liệu của cơ quan quốc tế đo tại trạm Việt Nam có thể đáp ứng mục tiêu địa lý, nhưng ghi đúng nhà cung cấp.

## 3. Yêu cầu thời gian, địa lý và mức chấp nhận

| Nhóm | Khoảng ưu tiên | Tối thiểu / nếu không đủ | Độ chi tiết / metadata cần |
| --- | --- | --- | --- |
| Trạm thời tiết lịch sử | 01/01/2015–31/12/2025 | 01/01/2019–31/12/2025; ngắn hơn vẫn ghi nhận là partial, không bịa phần thiếu | Daily ưu tiên; monthly chấp nhận để so tháng. Trạm ID, lat/lon, elevation nếu có, timestamp/timezone, tích lũy ngày nào, QA/missing code |
| Thời tiết hiện tại | 01/01/2026–31/10/2026 | Tới tháng hoàn chỉnh mới nhất có thật; không yêu cầu nửa tháng 11 thành tổng tháng | Giữ provisional/final và as-of. Không coi dữ liệu 2026 là forecast đã đánh giá |
| Đất | Khảo sát/bản phiên bản 2020–2026; ưu tiên gần block và mới | 2000–2019 dùng reference lịch sử nếu phương pháp/phạm vi rõ; model tĩnh ghi release/version, không đòi chuỗi năm giả | pH(H2O/KCl), EC với cách chiết, texture %mass, soil depth; OM/SOC, N/P/K optional. Tọa độ/polygon hoặc địa danh có scope |
| Cây/lịch vụ/hiện trạng | 2024–2026, hướng dẫn vụ 2026–2027 nếu công bố | Nguồn cũ được dùng tham khảo; không tự nhận là hiện trạng 2026 | Đúng giống hoặc nhóm giống, bắp non khác bắp hạt, đậu xanh khác đậu phộng/đậu nành; ngày gieo/thu và thời gian chuyển vụ |
| Luân canh đối chứng | 2000–2026; ưu tiên nghiên cứu gần đây và cùng điều kiện | Không áp cứng năm cắt để loại reference cũ có ích; luôn giữ năm thí nghiệm khác năm xuất bản | Địa bàn, đất, mùa, treatments/control, phương pháp, n/độ phân tán nếu có, outcome/units |
| Cropland/land use/thống kê | Bản mới nhất có thật trong 2020–2026; thống kê 2015–2025 để context | Giữ năm/ranh hành chính thật, không đổi bản 2021 thành hiện trạng 2026 | Land use khác crop species; annual thống kê không xác nhận tất cả vụ của block |

Bán kính trạm không tự là tiêu chuẩn đúng. Ưu tiên gần và điều kiện tương đồng; ghi khoảng cách nếu tính được, chênh cao và ảnh hưởng biển/đê/tưới nếu có. Không lấy một địa điểm xa chỉ vì đủ năm rồi gọi là ground truth Mỹ Thành.

## 4. Public và free nghĩa là gì trong đầu việc này?

- Có URL gốc công khai, người nhận mở được và không phải mua data. Tài khoản miễn phí chấp nhận nhưng ghi cần đăng ký; không gửi password/token.
- Phân biệt **free access** và **quyền dùng lại/phân phối**. Ghi license/terms URL khi có; nếu chưa rõ thì evidence citation được giữ riêng, chưa tự đưa raw vào repo public/training.
- CSV/XLSX/JSON/GeoTIFF/NetCDF phù hợp đều được; PDF bảng số là evidence có thể trích. Ảnh chụp/map screenshot thiếu units/georeference chỉ làm context, chưa là raw dataset.
- Giữ nguyên raw. Không tự nội suy missing, clip outlier, standardize, đổi tên biến mất nguồn hoặc combine các site. Việc đó được bàn sau EDA.
- Chưa có thì báo **not_found / access_blocked / scope_mismatch** với nguồn đã thử; không điền 0 hoặc một giá trị trung bình từ tỉnh khác.

## 5. Bích tìm những trường cụ thể nào?

### P0-A: đất và nước cho 3 reference scenarios

pH và cách đo; clay/sand/silt với đơn vị; độ sâu; EC/độ mặn và phương pháp (ECe khác EC 1:5); mô tả phèn nếu có; drainage/waterlogging; nguồn tưới và thời điểm cấp/tiêu. SOC/OM, CEC, bulk density và dinh dưỡng là mở rộng khi có nguồn. pH/texture từ model không đủ gọi là “độ phì/thổ dưỡng đã đo”.

### P0-B: crop/season rules

Mỗi rule cần cây/sản phẩm, giống nếu biết, factor, điều kiện/range/đơn vị, hard/soft/unknown, phương pháp/địa bàn/năm, nguồn và trang. Cần hiểu thời gian chuẩn bị đất, thu hoạch và gieo vụ kế tiếp, không chỉ tổng số ngày sinh trưởng. Có thể đọc giấy khuyến nông và nghiên cứu để điền bảng evidence; không phải bắt buộc tìm được một CSV hoàn chỉnh.

### P0-C: reference để đối chiếu

Ít nhất cố gắng có nguồn cho bắp non và đậu xanh cùng 1 reference so với lúa liên tục; có thể tái dùng S4/S5 trong pack nếu đúng câu hỏi. Một nghiên cứu có thể hỗ trợ nhiều hàng; không yêu cầu đủ số nguồn bằng cách dùng bài yếu. Giữ các kết quả không có ý nghĩa thống kê hoặc trái kỳ vọng. So cùng outcome/method/units; không so tấn bắp non với tấn lúa rồi gọi hiệu quả cao hơn.

### P1-D: trạm thời tiết độc lập / hỗ trợ khu vực

PRCP, TMIN/TMAX/TAVG nếu có, station metadata, QC và source flags; ghi date windows thực có. Catalogue ghi first/last year chưa chứng minh không thiếu ngày. Check lineage: cùng một dataset được tải qua hai website chưa là hai nguồn độc lập; reanalysis khác model chỉ là model cross-check nếu chưa có quan trắc riêng.

## 6. Đối chiếu theo từng block

| Block | Baseline/reference cần | Validation làm được | Không được suy |
| --- | --- | --- | --- |
| Đất | Mẫu đất/local map có method/depth tương thích; nếu thiếu giữ SoilGrids model context | So cùng thuộc tính/depth/method; chỉ tính sai số khi có mẫu phù hợp, n rõ | 1 cell model = ground truth block; pH = soil health tổng thể |
| Mưa | Seasonal-naive cùng tháng năm trước, có thể thêm climatology lịch sử; trạm là đối chiếu ngoài mẫu riêng | MAE/RMSE/bias mm trên time split cho model; so station khi alignment/lineage hợp lệ | Backtest POWER estimate = accuracy ngoài ruộng, hoặc số model chưa chạy |
| Luân canh | R0/R1/R2 research references + reviewed constraints | Vi phạm rule, traceability, case review và sensitivity; unknown phải hiện rõ | Accuracy cây tốt nhất khi thiếu labels; % tiết kiệm nước/yield chưa đo |
| Ingestion/EDA | Raw vs aggregate sample, missing code và time/unit checks | Q1 sample recomputation và lỗi tái lập | Test code = human/domain approval |

## 7. File bàn giao và cách điền

Trong `neurax-fieldshift-lab/handoffs/bich-2026-11-14/templates/` có các CSV header: `source-register.csv`, `soil-water.csv`, `crop-season-rules.csv`, `reference-cases.csv`, `station-reference.csv`, `search-log.csv`. Raw có thể để riêng trong thư mục `raw/` không commit. Nếu dùng Excel vẫn giữ tên cột và export CSV UTF-8.

Bắt đầu từ `NeuraX-MyThanh-Bich-Research-Pack/research/rotation-evidence-review.csv` (12 hàng): giữ evidence cũ, bổ sung nguồn/reviewer_note; chỉ ký reviewer_decision/date khi thực sự review. Không đổi REFERENCE_ONLY thành verified chỉ vì có link. Không bắt Bích làm lại research pack từ đầu.

Mỗi batch kèm tóm tắt 5 dòng: **đã có gì / thuộc vùng-năm nào / hỗ trợ output nào / thiếu gì / cần Việt-Hưng-Luật quyết định gì**. Có thể gửi file/link đã tìm được trước khi hoàn thiện toàn bộ form.

## 8. Thời hạn phục vụ baseline thứ Bảy

**Mốc đích do người dùng yêu cầu: chiều–tối thứ Bảy 14/11/2026 có baseline để cả team kiểm chứng.** Các giờ sau là nhịp đề xuất, chưa là cam kết cá nhân hoặc agenda BTC:

- 12:30: batch nguồn đầu tiên và search blockers.
- 14:00: chốt phần evidence P0 hiện có, bảng unknown và reference dùng được.
- 16:00: mục tiêu baseline mưa đơn giản + data/soil context sau review EDA và thống nhất bước xử lý tối thiểu.
- 18:00: mục tiêu comparison baseline R0/R1/R2 bằng rules đã review, hoặc REFERENCE_ONLY/UNKNOWN nếu chưa đủ.
- 20:00: mục tiêu cả team kiểm nguồn, QA, baseline và giới hạn; dừng mở thêm nguồn gây chặn demo.

Bích ưu tiên P0 và bàn giao cuốn chiếu. Chuỗi trạm dài/extra layers là P1 khi việc tìm vượt thời gian. Thiếu trạm không được bịa validation; thiếu K1 không ép rank 3 cây. Hưng đang thiết kế dashboard, Việt làm NASA/external data, preprocessing và AI architecture sau buổi bàn EDA; Luật kiểm từng block; Hiếu backend theo thời gian online, An hardware context riêng.

## 9. Nguồn bắt đầu, không phải tất cả đã có dataset phù hợp

| Nguồn | Đã xác minh ở lượt này | Bích nên tìm gì / giới hạn |
| --- | --- | --- |
| [CTU S4](https://ctujsvn.ctu.edu.vn/index.php/ctujsvn/article/download/605/3214/3214) | PDF nghiên cứu 2009 đọc được, có phương pháp và nghiệm thức Long Khánh/Cai Lậy | Tables/method/outcome cho R0/R1/R2; historic reference, chưa là hiện trạng block |
| [CTU S5 trong pack](https://ctujsvn.ctu.edu.vn/index.php/ctujsvn/article/download/597/3222/3222) | Có source/evidence record của pack; web tool chưa mở được ở lần này | Dùng bản đã có trong pack hoặc đọc link khi truy cập được, ghi bảng/trang; không ghi mới downloaded nếu chưa tải |
| [PXWeb Cục Thống kê](https://pxweb.nso.gov.vn/pxweb/vi/) | Trang chọn database công khai mở được | Crop area/yield/production theo địa bàn/năm thực có; context thống kê, không labels cho block |
| [Trung tâm Dự báo KTTV quốc gia](https://www.nchmf.gov.vn/kttv/) | Có mục dự báo tháng/mùa và thủy văn/mặn công khai | Bản tin có ngày/kỳ dự báo/phạm vi; chưa xác minh có raw station time series free 2015–2025 |
| [NOAA GHCN-Daily](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily) | Catalogue trạm toàn cầu và country code VM=Vietnam công khai | Trạm tại Việt Nam, biến/record spans/QC; publisher quốc tế. Chưa coi catalogue là measured dataset đã EDA |
| [SoilGrids / ISRIC](https://isric.org/explore/soilgrids/) | Global model grid 250m, uncertainty và CC-BY-4.0 được nguồn chính thức nêu | Pack đã có subset statistics. Tìm local soil để support, không tải lặp chỉ để tăng số nguồn |
| Cơ quan nông nghiệp/khuyến nông địa phương, trường/viện | Hướng tìm có mục đích, chưa xác minh bộ raw đầy đủ | Lịch vụ, tưới–tiêu, đất và crop rules đúng vùng; ghi free access/license và phạm vi rõ |

Không bắt buộc mọi nguồn do Việt Nam xuất bản; bắt buộc dữ liệu dùng cho khu vực Việt Nam và rõ scope. Không tìm WSS/SSURGO/CDL/PRISM của Hoa Kỳ để gán cho Mỹ Thành.
## Bổ sung kiểm catalogue trạm ngày 14/11

Đã đọc catalogue NOAA GHCN-Daily có 56 station metadata entries tại Việt Nam và inventory theo biến/năm. Trong 10 trạm gần tâm block nhất ở catalogue này, chưa có PRCP span phù hợp 2015–2025. Vĩnh Long khoảng 26,65 km có PRCP metadata 1963–1967; Tân Sơn Hòa khoảng 80,36 km có PRCP 1951–2013 và TAVG 1951–2025. Chỉ là catalogue, chưa tải measurement values hoặc xác minh coverage liên tục. Không kết luận các hệ thống/trạm khác ở Việt Nam không có dữ liệu.

Bích nên kiểm actual variable/date overlap trước tải. NOAA ISD/GHCNh hoặc nguồn KTTV khác là hướng tìm P1 nếu có quyền/free access và năm phù hợp; không hứa sẵn dữ liệu. Forecast bulletin hoặc reanalysis khác có thể so context/model nhưng chưa là quan trắc ground truth.
