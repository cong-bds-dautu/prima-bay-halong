import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Thay thế nút "Khám Phá Dự Án" để mở video modal
old_button = r'<button class="w-full sm:w-auto bg-white text-slate-900 px-8 py-4 rounded-full font-semibold hover:bg-slate-100 transition shadow-xl">\s*Khám Phá Dự Án\s*</button>'
new_button = '<button onclick="document.getElementById(\'video-modal\').classList.add(\'active\')" class="w-full sm:w-auto bg-white text-slate-900 px-8 py-4 rounded-full font-semibold hover:bg-slate-100 transition shadow-xl">Khám Phá Dự Án</button>'
html = re.sub(old_button, new_button, html)

# 2. Thay thế TẤT CẢ nút "Tải File Trình Chiếu" để mở form đăng ký
old_download = r'<button class="glass-panel text-white px-8 py-4 rounded-full font-medium hover:bg-white/10 transition">\s*Tải File Trình Chiếu[^<]*</button>'
new_download = '<button onclick="document.getElementById(\'contact-modal\').classList.add(\'active\')" class="glass-panel text-white px-8 py-4 rounded-full font-medium hover:bg-white/10 transition">Đăng Ký Nhận Tài Liệu</button>'
html = re.sub(old_download, new_download, html, flags=re.DOTALL)

# 3. Thêm Video Modal (với nút thoát X)
video_modal = '''
    <!-- Video Modal -->
    <div id="video-modal" class="modal fixed inset-0 bg-black/90 backdrop-blur-sm z-[100] items-center justify-center p-4">
        <div class="relative max-w-6xl w-full">
            <button onclick="document.getElementById('video-modal').classList.remove('active'); document.getElementById('modal-video-iframe').src = document.getElementById('modal-video-iframe').src;" class="absolute -top-12 right-0 text-white hover:text-primary text-4xl font-bold z-[101]">&times;</button>
            <div class="rounded-4xl overflow-hidden shadow-2xl">
                <div class="relative" style="padding-bottom: 56.25%; height: 0;">
                    <iframe 
                        id="modal-video-iframe"
                        src="https://drive.google.com/file/d/1w_J7bAKNKWut7FYFGlFRV13GpHj1LNCX/preview" 
                        class="absolute top-0 left-0 w-full h-full"
                        allow="autoplay; fullscreen"
                        allowfullscreen
                        style="border: none;">
                    </iframe>
                </div>
            </div>
        </div>
    </div>
'''

# Chèn Video Modal ngay trước Contact Modal
html = html.replace('    <!-- Contact Modal -->', video_modal + '\n    <!-- Contact Modal -->')

# 4. Sửa JS GLightbox để bắt TẤT CẢ ảnh trong Visual Showcase
old_lightbox_init = r"document\.addEventListener\('DOMContentLoaded', function\(\) \{[^}]+\}\);"
new_lightbox_init = '''document.addEventListener('DOMContentLoaded', function() {
            // Khởi tạo GLightbox với cấu hình đầy đủ
            const lightbox = GLightbox({
                selector: 'a.glightbox',
                touchNavigation: true,
                loop: true,
                autoplayVideos: false,
                closeOnOutsideClick: true,
                zoomable: true,
                draggable: true,
                openEffect: 'zoom',
                closeEffect: 'fade',
                slideEffect: 'slide',
                moreText: 'Xem thêm',
                moreLength: 60,
                svg: {
                    close: '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>',
                    next: '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>',
                    prev: '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>'
                }
            });
            
            // Thêm class glightbox vào TẤT CẢ các link ảnh (bao gồm cả Visual Showcase)
            document.querySelectorAll('a').forEach(link => {
                const href = link.getAttribute('href');
                if (href && href.match(/\\.(jpeg|jpg|gif|png|webp|JPG|PNG)$/i)) {
                    link.classList.add('glightbox');
                    link.removeAttribute('target');
                    // Xóa data-fslightbox nếu có
                    if (link.hasAttribute('data-fslightbox')) {
                        link.removeAttribute('data-fslightbox');
                    }
                }
            });
            
            // Refresh lightbox để nhận ảnh mới
            lightbox.reload();
        });'''

html = re.sub(old_lightbox_init, new_lightbox_init, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Done!")
print("1. Nút 'Khám Phá Dự Án' → mở video modal")
print("2. Nút 'Tải File Trình Chiếu' → mở form đăng ký")
print("3. Tất cả ảnh → click phóng to")
print("4. Email → congnt@trungthucland.vn")
