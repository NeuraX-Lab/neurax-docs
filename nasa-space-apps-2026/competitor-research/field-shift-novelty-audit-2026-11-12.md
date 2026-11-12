# AgroTwin có gì mới? Đối chiếu Field Shift công khai

> 12/11/2026. So proposal và scope mô phỏng hiện tại với tài liệu public. Đây là audit độ trùng ý tưởng, chưa so hiệu năng sản phẩm hoặc quyết định tư cách thi của đội khác.

## Trạng thái nhánh docs

Checkout: `docs/skills-and-alignment-2026-11-06`, HEAD `1472b6c`. Sau fetch origin, HEAD và remote cùng nhánh không chênh commit (0/0); origin/main vẫn ở `7d691d3`. Working tree có proposal/PDF sửa và hai tài liệu case mới từ các lượt trước; giữ nguyên, không reset. Nghiên cứu này bổ sung vào nhánh đang dùng, không commit/push/merge.

Trước lượt này, competitor-research và past-winners mới có ghi chú giả thuyết chưa dẫn từng project. Proposal đã bổ sung một số nguồn nhưng chưa cập nhật Orion mới nhất hoặc game local Việt Nam. Không dùng ranking cũ làm bằng chứng tính mới.

## Hai dự án trùng trực tiếp

### Orion / Field Shift

Nguồn [README cố định commit 4a80fa8ddb7dab99e2bf27cdfb95432a94fe6001, 11/11/2026](https://github.com/Zul-Qarnain/field-shift/blob/4a80fa8ddb7dab99e2bf27cdfb95432a94fe6001/README.md), đọc qua GitHub connector 12/11. Repo tự giới thiệu là dự án Field Shift 2026 của Team Orion, Bangladesh; chưa xác nhận tư cách/kết quả từ BTC.

README mô tả NASA POWER/GPM/MERRA-2, lọc ràng buộc rồi xếp hạng, ưu tiên và kịch bản, giải thích/provenance, Bangla/English, snapshot khi live lỗi. Có Niño 3.4/DMI làm đầu vào forecast. Vì vậy NASA + luân canh + ENSO + giải thích + fallback đều có phần trùng, không phải khác biệt tự thân của NeuraX.

Đã đọc [MODEL_CARD cùng commit](https://github.com/Zul-Qarnain/field-shift/blob/4a80fa8ddb7dab99e2bf27cdfb95432a94fe6001/MODEL_CARD.md): còn ghi validating/not shipped và UI dùng climatology tới khi vượt baseline, trong khi README gọi nhánh ML là built. Ghi nhận tài liệu chưa nhất quán; không suy forecast đã được xác thực. Không chạy lại test hoặc so metric với AgroTwin. Số test/metric tác giả công bố không phải phép đo của NeuraX.

### GreenOrbit

Nguồn [README cố định commit c9b3961caaa061a8a3af28963f7743bcdbecf91f, 10/10/2026](https://github.com/yunusarfat/Nasa-space_challenge-2026-GreenOrbit/blob/c9b3961caaa061a8a3af28963f7743bcdbecf91f/README.md), đọc qua GitHub connector 12/11. Tự giới thiệu Field Shift 2026, chưa xác nhận award/registration.

Mô tả map, POWER monthly 2015–2024, ba rotation, ưu tiên nước/lợi nhuận/đất, kịch bản tăng nhiệt tới +4°C, frontend gọi API. Multi-year rotation simulator nằm roadmap: không gọi nó là tính năng đã hoàn tất. Chưa audit công thức hoặc runtime; README không chứng minh ranking đúng nông học.

## Đối chiếu thành phần ý tưởng

| Thành phần AgroTwin đề xuất | Evidence về phần đã có | Kết luận độ mới |
| --- | --- | --- |
| NASA + map/chart + lựa chọn cây | Orion, GreenOrbit; winner nông nghiệp 2024 | Phổ biến trong mẫu khảo sát |
| So rotation + ưu tiên/scenario | Hai repo trực tiếp | Chưa mới |
| ENSO làm input | Orion có Niño 3.4/DMI cho forecast | Không thể claim riêng đầu vào ENSO là mới; vai trò triển khai có thể khác |
| Nguồn, why, QA, fallback | Orion mô tả nhiều phần tương tự | Điều cần có để đáng tin; chưa là lợi thế độc quyền |
| Farm/game/simulation nông nghiệp | Zumorroda-X global 2025, Lotus Data Voyage local 2025 | Không mới ở mức loại sản phẩm |
| Sensor thật kết nối phần mềm | Chưa khảo sát đủ để kết luận tổ hợp này độc nhất | Demo tích hợp tiềm năng; không tự tạo mới về khoa học |
| Chip nội địa | Thông tin user; chờ model/datasheet | Nguồn lực/câu chuyện team, chưa chứng minh novel algorithm hoặc bảo mật |
| Case Đức Lập, nguồn đất–cây–mùa địa phương | Khác phạm vi địa lý so hai repo Bangladesh | Khác bối cảnh, chưa tự chứng minh đóng góp kỹ thuật mới |

Nguồn winner và local: [review bằng chứng](../past-winners/evidence-review-2026-11-12.md). Không thấy trong README không đồng nghĩa đối thủ không làm; không có kết quả tìm kiếm không chứng minh tính đầu tiên.

## Kết luận thẳng

AgroTwin hiện là tổ hợp ý tưởng phù hợp đề nhưng có độ trùng đáng kể. Chưa có bằng chứng tính mới khoa học, thuật toán, phần cứng hoặc tổ hợp độc nhất. Chưa có kết quả implementation/đánh giá để nói tốt hơn Orion/GreenOrbit. Vẫn có thể tạo giá trị qua áp dụng đúng bối cảnh và thực hiện tốt; khác biệt hữu ích không bắt buộc là phát minh hoàn toàn mới.

Khuyến nghị không thêm dataset/AI/3D để cố tạo vẻ mới. Tập trung một đóng góp có thể kiểm: giúp người review một case địa phương hiểu **vì sao một kế hoạch bị loại, điều kiện nào làm hai kế hoạch đổi hạng, và còn thiếu dữ liệu gì để quyết định**. Cần chứng minh người dùng làm việc đó tốt hơn khi dùng công cụ so với xem chart/bảng tĩnh; đây là giả thuyết đóng góp, chưa là tính năng độc nhất.

## Một đường demo có cơ sở để khác biệt

1. Case Đức Lập có nguồn, hiện trạng xác nhận, ràng buộc đất/nước/mùa và ít nhất hai phương án hợp lệ để so.
2. Cùng một lịch mùa vụ, bật ưu tiên/kịch bản có nhãn; kết quả chỉ rõ criterion và nguồn nào làm đổi hạng hoặc khiến kết quả cần review.
3. Mở evidence packet tái tính được: input/version, rule, score breakdown, unknown, điều kiện có thể đổi kết luận.
4. Ô sensor live riêng minh họa raw/index, quality và stale; muốn đưa vào what-if thì bật sandbox rõ. Không dùng số đo chậu để thay dữ liệu ruộng.
5. Thực hiện một review độc lập và một thử nghiệm người dùng có ghi nhận. Không cần phần này đạt statistical significance để có feedback; cũng không suy vài người thành population impact.

Nếu sensor không giúp người xem hiểu hơn và mất thời gian tích hợp, giữ nó là phụ lục demo. Nếu không đủ K1 địa phương thì case chưa sẵn sàng xuất khuyến nghị thật dù UI đẹp. Định vị nông dân dùng trực tiếp còn là giả thuyết: có thể cần người tư vấn hỗ trợ ở pilot, nhưng không tự đổi user đã được team xác nhận.

## Đánh giá câu chuyện và tiềm năng theo bằng chứng

Framing hiện tại “Việt Nam, El Niño, an ninh lương thực, chip nội địa, farm mô phỏng” có quá nhiều trục để mở pitch. Đề xuất một trục: nông dân cân nhắc đổi luân canh trước mùa vụ khi nguồn nước không chắc chắn. NASA bổ sung lịch sử môi trường; K1 đặt giới hạn địa phương; ENSO cung cấp bối cảnh có ngày; sensor thể hiện quan sát tại điểm; kết quả là lựa chọn được giải thích và bước kiểm tiếp.

Đây là khả năng kể chuyện tốt hơn theo nhận định thiết kế, chưa có rehearsal/user study. Không kể nông dân hư cấu như người đã phỏng vấn, không hứa tăng năng suất/nước tiết kiệm hoặc bảo đảm an ninh lương thực. Câu chuyện chip chỉ nên chiếm phần tích hợp tương xứng bằng chứng.

Tiềm năng có điều kiện: dự án bám bài toán, có tương tác dễ nhớ và sáu vai trò hữu ích. Rủi ro lớn nhất là nguồn K1, dữ liệu thật, người review và chứng minh tiện ích. Hiện chưa đủ cơ sở ước lượng khả năng thắng local/global hoặc gán điểm NASA. Xem các hạng mục như lăng kính chất lượng, không chọn giải làm lý do thêm feature.

## Ưu tiên công việc

| Thứ tự | Evidence cần tạo | Owner đề xuất |
| --- | --- | --- |
| 1 | Một case sheet địa phương có nguồn và khoảng trống | Bích + Hưng |
| 2 | Một sample NASA audit được, không chỉ docs | Việt + Quang Luật |
| 3 | Rotation/constraint có nguồn và phép tính kiểm độc lập | Hưng + Bích + Quang Luật |
| 4 | Một flow UI cho so kế hoạch, why-not, đổi kết luận | Hiếu + Hưng |
| 5 | Log thật và adapter khi nhận thông số chip | An + Quang Luật |
| 6 | Rehearsal với người chưa biết dự án; lưu feedback | Cả team |

Cập nhật sau audit: proposal/PDF 0.4 ngày 12/11 đã tích hợp kết luận có điều kiện và [phương án local/global](../planning/local-to-global-strategy.md); hardware paper 0.3 ghi trạng thái HTTPSLAB chờ thông số, không đoán wiring. Không commit/push/publish trong lượt audit.
