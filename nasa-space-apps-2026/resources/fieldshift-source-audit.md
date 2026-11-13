# Field Shift — lựa nguồn cho EDA tại Mỹ Thành

> 2026-11-13 · Trạng thái **khảo sát ứng viên**, chưa chọn dataset cho AI. Bản tiếp nhận: [24 nhóm Resources](fieldshift-resources-supplied-2026-11-13.md). Kết quả chi tiết và notebook ở nhánh `research/resources-eda-2026-11-13` của `neurax-fieldshift-lab`.

## Phạm vi có căn cứ

Người dùng chỉ định `NeuraX-MyThanh-Bich-Research-Pack`, bản 1.3 ngày 12/11. Kiểm đủ **24/24 hash** trong manifest. Địa bàn theo pack: **Mỹ Thành, Đồng Tháp**; khối minh họa **MT-BLOCK-01**, 1,996 ha, tâm **10.4790980766 N, 106.0216210397 E**, EPSG:4326. Ranh được số hóa theo cạnh canh tác trên ảnh, chưa là ranh pháp lý, mẫu đất, vùng đất đồng nhất hoặc ruộng có crop/rotation được xác minh. Ranh xã 52,3 km² và khối ~2 ha là hai đối tượng khác nhau.

Nguồn pack trong workspace: `../NeuraX-MyThanh-Bich-Research-Pack`. Pack không chứa toàn bộ raw NASA/SoilGrids. Không gọi ảnh Esri/Vantor là ảnh NASA. Chưa thay lựa chọn challenge hoặc tự duyệt bằng chứng của Bích.

## Kết quả shortlist để KHẢO SÁT

| Nguồn / product | Vì sao đáng EDA | Mức phù hợp workflow | Đã làm thực tế | Chưa đủ / quyết định mở |
| --- | --- | --- | --- | --- |
| **NASA POWER Daily Point** | Có mưa và nhiệt đúng hai biến D1 đã định nghĩa | Direct adapter `PRECTOTCORR -> precip_sum_mm`, `T2M -> air_temp_mean_c`; UTC, vùng × tháng | Tải 2.557 ngày 2019–2025, 5 biến; 84 tháng đầy đủ theo kiểm tự động | Chỉ climate context ở ô thô; Q1/K1 chưa có chữ ký; không có irrigation/yield labels |
| **MODIS MOD13Q1 qua NASA ORNL TESViS** | Bổ sung NDVI/EVI và QA để xem biến động thảm thực vật | Cần **extension** D1; giữ composite native và QA; không đổi core schema tự động | Tải 69 kỳ trong 2023–2025, một ô chứa tâm; strict QA giữ 26/69 | 43 kỳ bị loại bởi policy bảo thủ, không phải raw null; pixel lớn hơn block; cần xem sensitivity, product version và footprint |
| **SMAP SPL3SMP_E** | Biến độ ẩm đất bề mặt khác với lượng mưa | Extension D1, cần QA, units, native support, retrieval coverage | Đọc band metadata/CMR; ORNL dates trả 400 “No data available” tại tâm | Chưa có số liệu để EDA measurement; thử đường Earthdata/subset có đăng nhập. Không kết luận mission không bao phủ Mỹ Thành |
| **GPM IMERG Final daily V07** | Ứng viên mưa thay thế/bổ sung cho POWER, có spatial support khác | Adapter mới: đọc đúng rate/accumulation, time bounds, QA và mask trước tổng tháng | CMR có collection V07 và tìm được granule giao điểm, chưa tải pixel | Chưa có authenticated subset/export; thiếu sample QA/units. Cần audit nguồn gốc chung trước coi POWER/IMERG là validation độc lập |
| **ISRIC SoilGrids từ pack** (bổ sung, không phải NASA) | Đã có context pH/cát/sét tại đúng tâm và bất định | **K1-context tĩnh**, không nhét thành climate time series | EDA 15 thống kê cho 5 cặp property-depth tại một ô mô hình | Raw rasters không nằm trong pack; EC, nước tưới, thoát nước, mẫu đất và rule cây chưa đủ; không phải crop label |

Mẫu POWER được lấy mới tại tâm block, không tự nhận là chuỗi 2015–2025 ở điểm cũ được pack nhắc đến. Header nhận được: POWER Daily API **v2.10.3**, sources `MERRA2`, `POWER`; version API không thay cho version toàn bộ underlying products. MODIS CMR cho lead collection 061, nhưng version của subset TESViS chưa được xác minh chỉ từ CMR hiện hành.

## Tự Q&A: vì sao lựa những nguồn này?

**Q: Có phải NASA bắt dùng hết danh sách không?** A: Không có căn cứ để biến danh sách gợi ý thành yêu cầu tích hợp tất cả. Chọn một nguồn phục vụ một câu hỏi rõ; việc shortlist ở đây không là quyết định chọn dataset.

**Q: Vì sao POWER trước?** A: Repo đã có normalizer daily JSON/CSV và contract vùng × tháng cho mưa/nhiệt. Giao dịch API thử thành công, metadata trả units `mm/day`, `C`, `%` và UTC. Đây là cách ít thay adapter nhất để kiểm D1. Dữ liệu vẫn là gridded estimates, chưa là quan trắc ruộng. [Daily API](https://power.larc.nasa.gov/docs/services/api/temporal/daily/), [native resolution](https://power.larc.nasa.gov/docs/tutorials/service-data-request/api/).

**Q: Vì sao không chỉ dùng POWER?** A: Mưa/nhiệt không cho biết loại cây hiện tại, pH/EC, nguồn tưới hoặc điều kiện thoát nước. MODIS thêm vegetation context; SoilGrids thêm soil-model context. Chúng bổ sung thông tin, chưa tự tạo quy tắc luân canh hoặc ground truth.

**Q: Vì sao MODIS thay vì tải Landsat toàn cảnh ngay?** A: [ORNL TESViS API](https://modis.ornl.gov/data/modis_webservice.html) trả số liệu cùng QA ở một điểm/ô, nhẹ và tái lập được. Lý do chọn là khả năng khảo sát nhanh. Khối 2 ha nhỏ hơn một ô danh nghĩa 250 × 250 m (6,25 ha), nên không dùng MODIS để kết luận cây trên block. Sentinel-2/Landsat là bước tiếp nếu câu hỏi cần field-scale; vẫn phải cloud-mask và xử lý mixed pixels.

**Q: 62,3% MODIS missing nghĩa là gì?** A: Raw NDVI/EVI có 69 giá trị; policy bảo thủ chỉ giữ pixel reliability=0 và MODLAND bits=0, kèm fill/range mask, nên 43/69 không được dùng. Notebook so với một policy nới lỏng để thảo luận, không tự thông qua. Missing do source fill, thiếu record, QA và range được ghi riêng; không tự nội suy cho đẹp.

**Q: Vì sao giữ SMAP trong danh sách khi chưa tải được?** A: Độ ẩm đất bề mặt có ý nghĩa cho câu hỏi nước, nhưng đường ORNL chưa có subset tại điểm chọn. Notebook là **audit truy cập/metadata**, không giả phân bố hoặc tỷ lệ missing. Cần data bytes + quality flags trước đánh giá; grid spacing 9 km cũng không đồng nghĩa độ chính xác/độ phân giải hiệu dụng 9 km ở ruộng.

**Q: Vì sao IMERG Final?** A: [NASA](https://gpm.nasa.gov/data/imerg) khuyên Final cho nghiên cứu không cần độ trễ thấp; metadata CMR xác nhận candidate `GPM_3IMERGDF` V07. Chưa tải values nên chưa xếp chất lượng hơn POWER ở Mỹ Thành. PNG Worldview là visualization; cần scientific variable, scale và time support. [GIS documentation](https://gpm.nasa.gov/resources/documents/imerg-gis-geotiff-documentation).

**Q: SoilGrids có xác nhận đất phù hợp cho đậu xanh/bắp non không?** A: Không. Pack cho pH mean 6,3, Q05–Q95 4,5–8,3 ở ba lớp; cát/sét cũng có khoảng rộng. Một ô mô hình không chứng minh đất đồng nhất, EC hay đế cày. Mean/quantile/depth không phải các mẫu huấn luyện độc lập; giữ thành context có uncertainty.

**Q: Có đủ nhãn để train “cây tốt nhất” chưa?** A: Chưa. Ba chuỗi R0 lúa–lúa–lúa, R1 lúa–bắp non–lúa, R2 lúa–đậu xanh–lúa là **reference scenarios** theo pack, chưa phải crop labels của block. Cả 12 hàng review vẫn chưa có quyết định reviewer. Không tự điền “approved”, “current rotation” hoặc score để có kết quả.

**Q: Có tự train vì POWER đủ 84 tháng không?** A: Không. Độ dài chỉ là điều kiện kỹ thuật ban đầu. Task/horizon, availability, split theo thời gian, baseline, sai số và independent QA phải review riêng. Nhánh này chỉ EDA và proposal.

## Audit toàn bộ danh sách: dùng ở đâu, hoãn gì?

Những dòng ngoài shortlist dưới đây mới ở mức mô tả Resources/định hướng, chưa khẳng định đã tải hoặc kiểm product cho AOI.

| ID | Nhóm nguồn | Xử lý cho Mỹ Thành |
| --- | --- | --- |
| R01 | SMAP | Shortlist có điều kiện truy cập/QA/scale |
| R02 | GPM/IMERG | Shortlist có điều kiện sample/units/lineage |
| R03 | Landsat, MODIS, VIIRS | EDA MOD13Q1 trước; Landsat để khảo sát field-scale tiếp; chưa cần cả MODIS và VIIRS trùng vai trò |
| R04 | POWER | EDA climate/D1 trước, chưa chọn chính thức |
| R05 | SRTM | Ưu tiên sau nếu slope/runoff thực sự ảnh hưởng câu hỏi; cần DEM product/vertical datum/độ phân giải. Không dùng DEM thô suy vi địa hình ruộng bằng phẳng |
| R06 | ECOSTRESS | Sau khi có ET/LST product, QA và số kỳ đủ; LST không phải T2M, ET không tự thành nhu cầu tưới |
| R07 | Ag Data Commons | Search từng study theo geography/license; kho chứa nhiều loại nghiên cứu, không mặc định dataset nào cũng đại diện Việt Nam |
| R08 | WSS | Soil data Hoa Kỳ, không dùng làm đất Mỹ Thành; liên quan SSURGO, không là nguồn độc lập thứ hai |
| R09 | CDL | Crop classification Hoa Kỳ; không mang crop labels sang Mỹ Thành, annual class cũng không xác nhận toàn bộ vụ trong năm |
| R10 | PRISM | Phạm vi Hoa Kỳ theo Resources, không là chuỗi khí hậu local Việt Nam |
| R11 | SSURGO/STATSGO2 | Hoa Kỳ; không thay local soil evidence |
| R12 | NAIP | Imagery Hoa Kỳ; một ảnh một thời điểm không tự phát hiện toàn bộ bare-soil periods |
| R13 | NLCD | Phạm vi Hoa Kỳ theo Resources; hoãn cho AOI Việt Nam |
| R14 | NLDAS/GLDAS | Phân biệt hai hệ thống; đánh giá **GLDAS** global nếu thực sự thiếu water-state context; không gán phạm vi NLDAS thành global; chưa tải |
| R15 | GAEZ | Reference suitability có điều kiện crop/management/scenario; cần pin version (link cũ v4, FAO có v5). Không là current yield/rotation label của block |
| R16 | CoCoRaHS | Theo Resources là North America; không có validation station Mỹ Thành trong lượt này |
| R17 | NWIS | Không có local station Việt Nam đã xác minh; cần nguồn nước địa phương |
| R18 | AMS Market News | Giá/thị trường Hoa Kỳ không thay giá thu mua bắp non/đậu xanh ở địa phương |
| R19 | QuickStats | Thống kê Hoa Kỳ cấp county/state, không là field-level labels Mỹ Thành |
| R20 | OpenET | Chưa có product phù hợp Việt Nam trong lượt này; ET satellite-model estimates không tự là ground truth. Không chuyển mô tả nguồn thành xác minh tại ruộng |
| R21 | LANDFIRE | Phạm vi Hoa Kỳ theo Resources, ít ưu tiên cho so ba vụ ở Mỹ Thành |
| R22 | GEDI | Forest structure context; ít liên quan trực tiếp lúa–bắp non–đậu xanh. Không dùng biomass proxy để gán nhãn cây hằng năm |
| R23 | Sentinel-2 | Ưu tiên tiếp cho khối ~2 ha: geometry mask, red/NIR, SCL/cloud/shadow, pixel edges và chuỗi ngày; chưa tải imagery trong lượt này |
| R24 | ERA5 | Climate/reanalysis tham chiếu khi cần; phải chốt bản, grid/time accumulation và lineage; không lấp missing POWER rồi gọi thành một quan trắc nguyên bản |

[FAO GAEZ hiện hành](https://www.fao.org/gaez/en/) xác nhận có v5; chưa chọn version/layer, chưa tải raster GAEZ.

## Các sửa diễn giải cần giữ trong trao đổi team

- Soil moisture, soil health, rainfall, irrigation và ET là các đại lượng khác nhau.
- NASA/partner estimates và đồ thị đẹp chưa là ground truth; ảnh tải từ viewer không đồng nghĩa scientific raster có units.
- Resampling không tạo thêm chi tiết; ghi native support, CRS, QA, khoảng thời gian và phương pháp aggregate.
- Đổi physical scale/units là bước decode dữ liệu; StandardScaler/MinMaxScaler là lựa chọn của model sau split, chỉ fit train fold.
- Rainfall accumulation cần đủ thời gian hợp lệ; missing không phải zero. Composite NDVI không tự thành ngày gieo/thu hoặc crop species.
- Các reviewer, acceptance và transform còn mở được ghi trong `neurax-fieldshift-lab/docs/resource-eda/data-ai-review.md`.

## Mức xác minh và quyền dùng

Ngày audit: 2026-11-13. Trang challenge live trả 502; snapshot cung cấp được lưu riêng. POWER và ORNL có request URL, retrieval UTC, SHA-256 và bytes thực; CMR là metadata công khai. Một số trang Earthdata trả 403, SoilGrids FAQ timeout; giữ các giới hạn đó. SoilGrids license CC-BY-4.0 là thông tin từ pack; raw rasters chưa có để đối chiếu độc lập. Chính sách/citation từng product cần rà trước chia sẻ. Không tự xuất bản raw data, ảnh hoặc thay quyền repo.

Đợt này thực hiện nghiên cứu/EDA theo yêu cầu hiện tại, không huấn luyện hay triển khai submission. Giữ nguyên cảnh báo quy định thời điểm trong Lab; việc Resources công bố không được dùng để suy ra ngoại lệ.
