import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the end of #san-pham section (the "Bàn Giao & Tiện Ích" part) with the full Tiện ích hấp dẫn
old_ban_giao = r'<!-- Bàn Giao & Tiện Ích -->.*?</div>\s*</section>'
new_tien_ich = """
            <!-- BÀN GIAO NỘI THẤT CĂN HỘ PRIMA BAY HẠ LONG -->
            <div class="mb-16 mt-16">
                <h3 class="text-2xl font-bold text-sky-400 mb-6 uppercase text-center">BÀN GIAO NỘI THẤT CĂN HỘ PRIMA BAY HẠ LONG</h3>
                <p class="text-slate-300 leading-relaxed mb-4 text-center max-w-4xl mx-auto">Căn hộ Prima Bay Hạ Long được bàn giao theo tiêu chuẩn hoàn thiện cao cấp với phong cách hiện đại, tối ưu công năng và đề cao trải nghiệm nghỉ dưỡng ven biển. Tại Prima Bay từng căn hộ được thiết kế nhằm mang đến không gian sống sang trọng, tiện nghi và hài hòa với thiên nhiên. Mỗi căn hộ được bố trí khoa học với hệ cửa kính lớn đón ánh sáng tự nhiên, vật liệu hoàn thiện tinh tế cùng tông màu thanh lịch, tạo cảm giác rộng rãi và thoải mái. Không chỉ đáp ứng nhu cầu an cư, Prima Bay Hạ Long còn hướng đến chuẩn sống nghỉ dưỡng đẳng cấp dành cho cư dân.</p>
            </div>

            <!-- TIỆN ÍCH HẤP DẪN -->
            <div class="mb-16 mt-20 text-center">
                <h3 class="text-4xl md:text-5xl font-bold text-yellow-500 mb-4 uppercase tracking-wider">TIỆN ÍCH HẤP DẪN</h3>
                <div class="w-24 h-1 mx-auto rounded-full bg-gradient-to-r from-yellow-500 to-teal-600 mb-8"></div>
                <p class="text-slate-300 leading-relaxed max-w-5xl mx-auto text-lg md:text-xl font-medium">
                    <strong class="text-yellow-500 font-bold">Prima Bay Hạ Long</strong> tọa lạc ngay trung tâm <strong>Halong Marina</strong>, sở hữu hệ tiện ích nghỉ dưỡng – giải trí – thương mại đồng bộ, mang đến trải nghiệm sống đẳng cấp giữa lòng di sản biển. Dự án với vị trí liền kề <strong>hồ nhạc nước Halo Bay Show</strong>, quảng trường biển, bến du thuyền cùng chuỗi nhà hàng, café, phố đi bộ... Bên trong khu căn hộ là hệ tiện ích cao cấp gồm: <strong>hồ bơi vô cực</strong>, sky lounge, phòng gym – yoga, khu vui chơi trẻ em, trung tâm thương mại, khu BBQ ngoài trời, vườn cảnh quan và khu thư giãn riêng tư chuẩn nghỉ dưỡng với tầm nhìn panorama hướng <strong>Vịnh Hạ Long.</strong>
                </p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mt-10">
                    <div class="rounded-3xl overflow-hidden glass-panel">
                        <a href="https://primahalong.com/wp-content/uploads/2026/05/tien-ich-cafe-aria-bay-ha-long.webp" class="glightbox">
                            <img src="https://primahalong.com/wp-content/uploads/2026/05/tien-ich-cafe-aria-bay-ha-long.webp" class="w-full h-auto object-cover img-hover" alt="Tiện ích Cafe Prima Bay">
                        </a>
                    </div>
                    <div class="rounded-3xl overflow-hidden glass-panel">
                        <a href="https://primahalong.com/wp-content/uploads/2026/05/du-an-Prima-bay-ha-long-aqua-city-ha-long5.jpg" class="glightbox">
                            <img src="https://primahalong.com/wp-content/uploads/2026/05/du-an-Prima-bay-ha-long-aqua-city-ha-long5.jpg" class="w-full h-auto object-cover img-hover" alt="Tiện ích Aqua City Prima Bay">
                        </a>
                    </div>
                </div>
            </div>

            <!-- MẢNH GHÉP MỚI CHO HALONG MARINA -->
            <div class="mb-16 mt-20">
                <h3 class="text-3xl font-bold text-sky-400 mb-8 uppercase text-center">PRIMA BAY HALONG MẢNH GHÉP MỚI CHO HALONG MARINA</h3>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
                    <div class="space-y-4">
                        <div class="flex items-center gap-4 bg-slate-800/50 p-4 rounded-2xl">
                            <div class="text-3xl">🌊</div>
                            <h4 class="text-xl font-bold text-white">Cách bãi biển chỉ vài bước chân</h4>
                        </div>
                        <div class="flex items-center gap-4 bg-slate-800/50 p-4 rounded-2xl">
                            <div class="text-3xl">🚶‍♂️</div>
                            <h4 class="text-xl font-bold text-white">Gần quảng trường biển, phố đi bộ</h4>
                        </div>
                        <div class="flex items-center gap-4 bg-slate-800/50 p-4 rounded-2xl">
                            <div class="text-3xl">🛥️</div>
                            <h4 class="text-xl font-bold text-white">Kết nối nhanh Tuần Châu – Hòn Gai</h4>
                        </div>
                        <div class="flex items-center gap-4 bg-slate-800/50 p-4 rounded-2xl">
                            <div class="text-3xl">🌅</div>
                            <h4 class="text-xl font-bold text-white">View trực diện vịnh Hạ long</h4>
                        </div>
                    </div>
                    <div>
                        <p class="text-slate-300 leading-relaxed mb-4">Trong những năm qua, Hạ Long Marina là điểm đến của các sự kiện như:</p>
                        <ul class="space-y-2 text-slate-300 list-disc list-inside">
                            <li>Đăng cai show trình diễn thời trang của 75 Hoa hậu Hòa bình Quốc tế 2023</li>
                            <li>Giải chạy VnExpress Marathon Amazing Ha Long 2023 quy tụ 11.000 vận động viên</li>
                            <li>Ngày hội chào hè Hi! Summer với hơn 12.000 lượt du khách tham dự</li>
                            <li>Đại tiệc âm nhạc – ẩm thực Kool Fest (tháng 7)</li>
                            <li>Chuỗi sự kiện Halong Street Travel Fest</li>
                            <li>Masterchef Quảng Ninh...</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

html = re.sub(old_ban_giao, new_tien_ich, html, flags=re.DOTALL)

# 2. Add Professional Footer replacing the contact-modal scripts/closing body
# Search for Contact Modal block to replace the end part
footer_html = """
    <!-- Footer Chuyên Nghiệp -->
    <footer class="bg-slate-950 border-t border-white/10 pt-20 pb-10 mt-10">
        <div class="max-w-7xl mx-auto px-6">
            <div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-16">
                <!-- Cột 1 -->
                <div class="col-span-1 md:col-span-1">
                    <div class="text-3xl font-bold tracking-tighter text-white mb-6">PRIMA <span class="text-primary">BAY</span></div>
                    <p class="text-slate-400 leading-relaxed mb-6">Tổ hợp 2 tòa căn hộ cao cấp DV2 & DV3 tọa lạc tại trung tâm Halong Marina, sở hữu vị trí đắt giá ngay mặt đường Hoàng Quốc Việt.</p>
                </div>
                
                <!-- Cột 2 -->
                <div class="col-span-1 md:col-span-1">
                    <h4 class="text-white font-bold mb-6 uppercase tracking-wider">Thông Tin Liên Hệ</h4>
                    <ul class="space-y-4 text-slate-400">
                        <li class="flex items-start gap-3">
                            <span class="text-primary">📍</span>
                            <span>Đường Hoàng Quốc Việt, Khu đô thị Halong Marina, P. Hùng Thắng, TP. Hạ Long</span>
                        </li>
                        <li class="flex items-center gap-3">
                            <span class="text-primary">☎️</span>
                            <span><a href="tel:0914479692" class="hover:text-white transition">0914.479.692</a></span>
                        </li>
                        <li class="flex items-center gap-3">
                            <span class="text-primary">📧</span>
                            <span><a href="mailto:cong.daianland@gmail.com" class="hover:text-white transition">cong.daianland@gmail.com</a></span>
                        </li>
                    </ul>
                </div>
                
                <!-- Cột 3 -->
                <div class="col-span-1 md:col-span-1">
                    <h4 class="text-white font-bold mb-6 uppercase tracking-wider">Liên Kết Nhanh</h4>
                    <ul class="space-y-3 text-slate-400">
                        <li><a href="#tong-quan" class="hover:text-primary transition">Tổng Quan Dự Án</a></li>
                        <li><a href="#vi-tri" class="hover:text-primary transition">Vị Trí Tiềm Năng</a></li>
                        <li><a href="#san-pham" class="hover:text-primary transition">Mặt Bằng & Sản Phẩm</a></li>
                        <li><a href="#thuc-te" class="hover:text-primary transition">Hình Ảnh Thực Tế</a></li>
                    </ul>
                </div>

                <!-- Cột 4 -->
                <div class="col-span-1 md:col-span-1">
                    <h4 class="text-white font-bold mb-6 uppercase tracking-wider">Phát Triển Dự Án</h4>
                    <ul class="space-y-3 text-slate-400">
                        <li><strong>Chủ đầu tư:</strong> BIM Land – Thành viên BIM Group</li>
                        <li><strong>Tổng thầu:</strong> Hoà Bình Group</li>
                        <li><strong>Thiết kế:</strong> Mercurio Design Lab</li>
                        <li><strong>Phân phối:</strong> Trung Thực Land</li>
                    </ul>
                </div>
            </div>
            
            <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
                <p class="text-slate-500 text-sm">© 2026 Prima Bay Halong. Bản quyền thuộc về Chủ Đầu Tư.</p>
                <div class="text-slate-500 text-sm">
                    Phát triển bởi <strong class="text-slate-300">Trung Thực Land</strong>
                </div>
            </div>
        </div>
    </footer>

    <!-- Contact Modal -->
"""

# Replace Contact Modal start to inject footer right before it
html = html.replace('<!-- Contact Modal -->', footer_html)

# 3. Fix JS for GLightbox to select ALL images correctly
old_js = """            // Thêm class glightbox vào tất cả các link ảnh
            document.querySelectorAll('a[href*=".jpg"]').forEach(link => {
                if (link.href.includes('assets/')) {
                    link.classList.add('glightbox');
                }
            });"""

new_js = """            // Thêm class glightbox vào tất cả các link ảnh
            document.querySelectorAll('a').forEach(link => {
                const href = link.getAttribute('href');
                if (href && href.match(/\.(jpeg|jpg|gif|png|webp|JPG|PNG)$/i)) {
                    link.classList.add('glightbox');
                    // Đảm bảo không có target="_blank" làm mở tab mới
                    link.removeAttribute('target');
                }
            });
            
            // Xử lý cả những ảnh nằm trong thẻ a data-fslightbox
            document.querySelectorAll('a[data-fslightbox]').forEach(link => {
                link.classList.add('glightbox');
                link.removeAttribute('data-fslightbox');
                link.removeAttribute('target');
            });"""

html = html.replace(old_js, new_js)

# Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
