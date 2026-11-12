# Kiểm lại địa bàn, cảm biến và ENSO — 12/11/2026

## Kết luận để team quyết định

**Chưa chứng minh Mỹ Thành là địa điểm tối ưu hoặc một ruộng đủ điều kiện trồng hai phương án.** Có thể giữ xã Mỹ Thành làm phạm vi prototype phân tích từ xa: có bối cảnh nông nghiệp, nguồn dữ liệu đã tải và ranh hành chính truy xuất được. Chốt phạm vi này giúp bắt đầu xây dựng; không đồng nghĩa chốt khuyến cáo sản xuất. Không cần khảo sát để chạy prototype kịch bản, nhưng không được nhận là đã kiểm chứng ngoài đồng.

Hai phương án thiết kế để thảo luận vẫn là **lúa–bắp non–lúa** và **lúa–đậu xanh–lúa**, với lúa liên tục làm đối chứng tham khảo từ nghiên cứu lịch sử Cai Lậy/Long Khánh. Chúng chưa được xác nhận là lịch canh tác hiện tại của Mỹ Thành. Không chuyển thời gian sinh trưởng bắp hạt/đậu phộng từ case Đức Lập sang hai cây này. Chưa có căn cứ định lượng năng suất, lợi nhuận hoặc tiết kiệm nước tại Mỹ Thành.

## 1. Sửa lỗi polygon: chính xác ở cấp nào?

Hình thoi khoảng 17,1 ha cũ là vùng do người phân tích chọn trên ảnh. Nó cắt nhiều ô canh tác và dải cây; chưa đối chiếu ranh thửa, loại cây hay chủ ruộng. Gọi vùng này là khu ruộng đã chốt là quá sớm. Các file `illustrative-*` và ảnh cũ chỉ giữ để truy vết, không dùng làm ranh ruộng trong sản phẩm.

Ranh chính mới **AOI-MT-ADMIN-v1** lấy từ [bản đồ của NXB Tài nguyên–Môi trường và Bản đồ Việt Nam](https://sapnhap.bando.com.vn): POST `/pread_json`, form `id=diaphanhanhchinhcapxa_2025.464`. Dữ liệu trả xã Mỹ Thành, Đồng Tháp, từ Phú Nhuận + Mỹ Thành Bắc + Mỹ Thành Nam; diện tích thuộc tính nguồn **52,3 km²**, không phải diện tích ruộng tính lại.

- Giữ geometry nguồn, chỉ bỏ tọa độ đóng vòng bị lặp liên tiếp; không tự thêm góc hoặc nắn theo ảnh.
- Kiểm thứ tự kinh độ/vĩ độ EPSG:4326, vòng khép kín, bounds; dựng ảnh bằng extent thực của export.
- Geometry khớp bản lưu tham khảo sau chuẩn hóa. Bản tham khảo dẫn cùng nguồn, nên đây **không phải hai khảo sát độc lập**.
- Đây là ranh hành chính theo nguồn bản đồ, không xác nhận pháp lý địa chính, độ chính xác đo đạc, quyền sử dụng, cây trồng hay đất đồng nhất.
- Cần phân biệt ruộng cây hằng năm / vườn cây / nước / dân cư trước khi tổng hợp raster nông nghiệp. Chưa có mask đã kiểm toàn xã; không lấy thống kê 419 pixel của mẫu 17 ha cũ áp cho toàn xã.

[Bản đồ sửa](maps/my-thanh-commune-aoi.png) · [GeoJSON](aoi.geojson) · [KML](aoi.kml) · [tọa độ các đỉnh](coordinates.csv) · [manifest và SHA nguồn](aoi-manifest.json).

## 2. Cảm biến đặt ở HCM có dùng được không?

**Dùng được để chứng minh chuỗi đo → truyền dữ liệu → hiển thị → phản ứng của mô phỏng. Chưa thể gọi là đo đất Mỹ Thành.** Chip nội địa không tự bảo đảm độ chính xác nông học. HTTPSLAB đã đồng ý cho mượn theo thông tin team; model chip/board, loại probe, datasheet và SDK vẫn chờ.

| Mặt cần kiểm | Cách làm khả thi | Điều chưa được tuyên bố |
| --- | --- | --- |
| Điện và giao tiếp | Đối chiếu nguồn cấp, mức logic/ADC, bus, SDK, payload, timestamp theo datasheet thực | Chưa khẳng định probe bất kỳ cắm được vào board |
| Độ ẩm đất | Dùng giá thể có nguồn rõ tại bàn HCM; ghi trạng thái khô/ướt, lặp chu kỳ và lưu số đo | Không lấy ngưỡng chậu áp trực tiếp cho ruộng từ xa |
| Hiệu chuẩn | Làm đúng quy trình nhà sản xuất; muốn VWC cần tham chiếu hàm lượng nước trên thể tích và kiểm riêng giá thể | Hai mốc khô/ướt đơn giản chỉ là chỉ số tương đối, không tự thành % VWC |
| pH/EC nếu có | Chỉ thêm khi probe, dung dịch chuẩn, quy trình và khả năng tích hợp đã rõ | Không suy EC từ pH hoặc gọi số chậu là EC ruộng |
| Nhãn dữ liệu | `HCM_tabletop`, vị trí đo thật, thời điểm và phạm vi hiệu chuẩn; farm ảo ghi `scenario` | Không giả telemetry Mỹ Thành hoặc dùng demo làm kiểm định NASA |

[Tài liệu hiệu chuẩn của METER](https://publications.metergroup.com/Sales%20and%20Support/METER%20Environment/Website%20Articles/how-calibrate-soil-moisture-sensors.pdf) giải thích hiệu chuẩn theo đất; nguyên lý này không phải chứng nhận cho probe chưa biết của team. Texture, bulk density và độ mặn có thể ảnh hưởng phép đo. SoilGrids không thay được mẫu đất đại diện hoặc phép đo tham chiếu. Pha giá thể có tỷ lệ cát/sét gần mean mô hình cũng không tái tạo được cấu trúc và tính chất đất thực.

**Backup:** không có probe tương thích thì replay bản ghi cảm biến có nguồn hoặc dữ liệu kịch bản, gắn nhãn rõ; giữ demo phần dữ liệu vệ tinh và quyết định. Không tạo dữ liệu rồi ghi là số đo thật. Nếu có probe nhưng không hiệu chuẩn VWC, demo chỉ số độ ẩm tương đối là đủ.

## 3. Đưa El Niño vào thế nào cho đúng?

Có cơ sở dùng ENSO làm **bối cảnh khí hậu và đầu vào kịch bản chuẩn bị mùa vụ**. Trang [NOAA CPC](https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml) đọc ngày 12/11/2026 vẫn hiển thị bản phát hành **08/10/2026**, trạng thái El Niño Advisory, lịch bản kế tiếp 12/11. Không ghi là đã đọc bản tháng 11 khi trang chưa thay. [Bản tháng 10 lưu trữ](https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_disc_oct2026/ensodisc.shtml).

Luồng hợp lý: outlook ENSO có ngày nguồn → xem bất thường mưa/nhiệt lịch sử địa phương → chạy kịch bản nóng/khô do người dùng chọn → so sánh độ nhạy của các phương án với giả định minh bạch. Khi chưa kiểm quan hệ địa phương, không tự gắn hệ số “El Niño giảm mưa X%”, xác suất hạn tại ruộng hoặc dự báo năng suất. ENSO có thể kéo dài nhiều mùa, không là biến cảm biến đo tại chậu. Outlook hiện tại cũng không được đưa ngược vào dữ liệu lịch sử như thông tin đã biết lúc đó.

POWER 2015–2025 đã có để khám phá; 11 năm và dữ liệu coarse không đủ tự bảo đảm mô hình tác động ENSO đáng tin. Trước pitching cần kiểm lại ngày bản tin; NASA cung cấp dữ liệu khí tượng, NOAA cung cấp outlook ENSO, giữ đúng attribution.

## 4. Cần Giờ có phải lựa chọn tốt?

**Có, là option nghiên cứu thực sự; không thể loại bằng lý do “chỉ có rừng ngập mặn”.** Tuy nhiên gần HCM không giải quyết thiếu khảo sát khi team đã xác nhận không thể đi đo. Địa bàn này phù hợp hơn nếu trọng tâm chuyển sang thích ứng mặn/phèn và quyết định đất–nước.

Nguồn mạnh: [luận án Nguyễn Tân Xuân Tùng, IUH, 2025, tệp công bố 2026](https://ipe.iuh.edu.vn/uploads/2026/03/1.-LUAN-AN-TIEN-SI_NGUYEN-TAN-XUAN-TUNG.pdf), *Cải tạo các thành phần hóa học của đất phèn nhiễm mặn bằng vật liệu thân thiện môi trường trong bối cảnh biến đổi khí hậu*. Đã đọc phương pháp: khảo sát 135 hộ, 136 mẫu đất trong năm 2022; thí nghiệm lúa tại Bình Khánh, Cần Giờ cũ, tháng 7–12/2022, **500 m²**, tọa độ công bố **10.638770 N, 106.781880 E** (PDF trang 64–65, số in 47–48). Đây là vị trí thí nghiệm lịch sử, không phải ranh đất hoặc hiện trạng 2026.

Nghiên cứu dùng lúa Ba Bụi, bối cảnh lúa–tôm; đất phân loại Salic Thionic Fluvisol, thí nghiệm so sánh vật liệu cải tạo với đối chứng, sáu nghiệm thức và bốn lần lặp. **Không phải thử nghiệm hai phương án luân canh cây trồng thay thế.** Thí nghiệm cải thìa trong cùng luận án nằm tại Kiểng Phước, Gò Công Đông, không được chuyển thành kết quả Cần Giờ. Bảng/tóm tắt công bố không đồng nghĩa team đã có raw observations.

| Tiêu chí của MVP hiện tại | Mỹ Thành / bối cảnh Cai Lậy | Bình Khánh / Cần Giờ |
| --- | --- | --- |
| So sánh hai phương án luân canh cây | Có tài liệu lịch sử vùng cho bắp non, đậu xanh; chưa xác minh tại xã | Nguồn tìm được mạnh về cải tạo đất và lúa–tôm, chưa đủ cho hai phương án cây thay thế |
| Dữ liệu đã tải và audit | POWER, SoilGrids, ảnh, ranh nguồn đã có | Có luận án đất/field trial cụ thể; chưa lấy và audit chuỗi NASA tại điểm này |
| Khó khăn chính | Crop mask, nước tưới, lịch canh tác và sự chuyển giao nghiên cứu vùng | Mặn/phèn, động thái nước, EC và thay đổi phạm vi sang nông–ngư nghiệp |
| Giá trị câu chuyện | Ra quyết định mùa vụ có giải thích, không phóng đại điều kiện đất | Thích ứng ven biển rõ, nhưng tăng yêu cầu dữ liệu nước/EC và nông học |

[UNESCO Cần Giờ](https://www.unesco.org/en/mab/can-gio-mangrove?hub=66925) cung cấp bối cảnh hệ sinh thái ven biển; không dùng mô tả khu dự trữ sinh quyển để kết luận mọi thửa nông nghiệp đều có cùng đất/mặn.

**Khuyến nghị:** giữ Mỹ Thành ở cấp xã cho prototype hiện tại để tận dụng dữ liệu đã kiểm và câu hỏi luân canh. Giữ Bình Khánh là phương án chuyển hướng có nguồn, không đổi chỉ vì gần nhà. Nếu cần sản phẩm khuyến cáo cho ruộng thật ngay thì **chưa địa bàn nào trong hai case đạt chuẩn bằng chứng**.

## 5. Phần việc tiếp theo, không cần thực địa

1. Bích rà đất–nước–cây–mùa bằng tài liệu cho xã nguồn, ghi rõ năm/vị trí/phương pháp; ưu tiên nước tưới, thoát nước, lịch mùa và điều kiện hai cây thay thế. Chỗ thiếu giữ unknown, không điền bằng mean SoilGrids.
2. Từ AOI cấp xã, lập mask cây hằng năm có nhãn nguồn và độ tin cậy bằng chuỗi ảnh; dùng `unknown` ở chỗ chưa rõ. Nếu cần demo một ô, gọi là ô mô phỏng minh họa, không “ruộng đã xác minh”.
3. Chốt tiêu chí so sánh và điều kiện loại trừ; thiếu đất/nước thì trả “chưa đủ thông tin” thay vì tự chấm phù hợp. Không đợi hardware mới xây flow này.
4. Khi nhận datasheet, kiểm tích hợp và hiệu chuẩn bàn HCM; hiển thị tách số đo thật và trạng thái farm ảo. ENSO giữ là outlook có ngày và kịch bản độ nhạy.

Chỉ cập nhật hồ sơ nghiên cứu; chưa đưa kết luận này vào proposal/PDF, chưa commit hoặc push.
