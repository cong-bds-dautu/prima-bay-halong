import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Đổi vị trí Video Intro và Video Gallery
# Tìm Video Gallery section
video_gallery_match = re.search(r'(<!-- Thư Viện Video -->.*?<!-- Video Gallery Modal -->.*?</script>)', html, flags=re.DOTALL)
video_gallery = video_gallery_match.group(1) if video_gallery_match else ''

# Tìm Video Intro section
video_intro_match = re.search(r'(<!-- Video Section -->.*?</section>)', html, flags=re.DOTALL)
video_intro = video_intro_match.group(1) if video_intro_match else ''

# Xóa cả 2 sections khỏi vị trí cũ
html = html.replace(video_gallery, '<!-- VIDEO_GALLERY_PLACEHOLDER -->')
html = html.replace(video_intro, '<!-- VIDEO_INTRO_PLACEHOLDER -->')

# Đặt lại theo thứ tự: Video Intro trước, Video Gallery sau
html = html.replace('<!-- VIDEO_GALLERY_PLACEHOLDER -->', video_intro)
html = html.replace('<!-- VIDEO_INTRO_PLACEHOLDER -->', video_gallery)

# 2. Thêm nút "Xem Thêm Video" và ẩn gallery mặc định
# Thay đổi Video Gallery section: thêm display:none và nút toggle
old_gallery_section = r'(<section id="video-gallery" class="py-24 bg-slate-800/30 relative">)'
new_gallery_section = r'<section id="video-gallery" class="py-24 bg-slate-800/30 relative" style="display: none;">'
html = re.sub(old_gallery_section, new_gallery_section, html)

# Thêm nút "Xem Thêm Video" vào cuối Video Intro section
video_intro_end = r'(</div>\s*</div>\s*</section>\s*<!-- Thư Viện Video -->)'
button_html = '''            <div class="text-center mt-10">
                <button onclick="toggleVideoGallery()" id="toggle-gallery-btn" class="bg-primary hover:bg-sky-400 text-white px-10 py-4 rounded-full font-bold text-lg transition shadow-xl shadow-primary/30 inline-flex items-center gap-3">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                    </svg>
                    <span id="gallery-btn-text">Xem Thêm Video</span>
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                    </svg>
                </button>
            </div>
        </div>
    </section>

    <!-- Thư Viện Video -->'''
html = re.sub(video_intro_end, button_html, html)

# 3. Thêm JS function để toggle gallery
toggle_script = '''
    <script>
        function toggleVideoGallery() {
            const gallery = document.getElementById('video-gallery');
            const btn = document.getElementById('toggle-gallery-btn');
            const btnText = document.getElementById('gallery-btn-text');
            
            if (gallery.style.display === 'none') {
                gallery.style.display = 'block';
                btnText.textContent = 'Ẩn Thư Viện Video';
                // Smooth scroll to gallery
                setTimeout(() => {
                    gallery.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }, 100);
            } else {
                gallery.style.display = 'none';
                btnText.textContent = 'Xem Thêm Video';
                // Scroll back to video intro
                document.getElementById('video-intro').scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    </script>
'''

# Thêm script trước closing </body>
html = html.replace('</body>', toggle_script + '\n</body>')

# 4. Update navbar link
html = html.replace('<a href="#video-gallery"', '<a href="#video-intro"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Done!")
print("1. Video Giới Thiệu → lên trước Thư Viện Video")
print("2. Thư Viện Video → ẩn mặc định")
print("3. Nút 'Xem Thêm Video' → hiện/ẩn thư viện")
print("4. Navbar → trỏ về Video Intro")
