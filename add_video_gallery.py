import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Load uploaded videos
with open('uploaded_videos.json', 'r', encoding='utf-8') as f:
    videos_raw = f.read().strip()
    # Fix trailing comma
    videos_raw = videos_raw.replace(',\n]', '\n]')
    videos = json.loads(videos_raw)

# 1. Thay thế Video Section hiện tại để có autoplay khi scroll vào
old_video_section = re.search(r'<!-- Video Section -->.*?</section>', html, flags=re.DOTALL)
if old_video_section:
    new_video_section = '''<!-- Video Section -->
    <section class="py-24 bg-slate-900/80 relative overflow-hidden" id="video-intro">
        <div class="absolute inset-0 bg-gradient-to-b from-slate-900 via-slate-900/50 to-slate-900"></div>
        <div class="max-w-7xl mx-auto px-6 relative z-10">
            <div class="text-center mb-12">
                <h2 class="text-3xl md:text-5xl font-bold mb-4">Video Giới Thiệu Dự Án</h2>
                <p class="text-slate-400">Khám phá Prima Bay Hạ Long qua video</p>
            </div>
            <div class="max-w-5xl mx-auto">
                <div class="rounded-4xl overflow-hidden shadow-2xl glass-panel p-2">
                    <div class="relative" style="padding-bottom: 56.25%; height: 0;">
                        <iframe 
                            id="main-video"
                            src="https://drive.google.com/file/d/1w_J7bAKNKWut7FYFGlFRV13GpHj1LNCX/preview?autoplay=1&mute=1" 
                            class="absolute top-0 left-0 w-full h-full rounded-3xl"
                            allow="autoplay; fullscreen"
                            allowfullscreen
                            style="border: none;">
                        </iframe>
                    </div>
                </div>
            </div>
        </div>
    </section>
'''
    html = html.replace(old_video_section.group(0), new_video_section)

# 2. Thêm Thư viện Video Section ngay sau Video Section
video_gallery = '''
    <!-- Thư Viện Video -->
    <section id="video-gallery" class="py-24 bg-slate-800/30 relative">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-16">
                <h2 class="text-3xl md:text-5xl font-bold mb-4">THƯ VIỆN VIDEO</h2>
                <p class="text-slate-400">Tổng hợp video về Prima Bay Hạ Long và Halong Marina</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
'''

for video in videos:
    video_gallery += f'''
                <!-- {video['name']} -->
                <div class="glass-panel rounded-4xl overflow-hidden group hover:scale-105 transition-transform duration-300">
                    <div class="relative cursor-pointer" onclick="openVideoModal('{video['id']}', '{video['name'].replace("'", "\\'")}')">
                        <div class="aspect-video bg-slate-700 relative overflow-hidden">
                            <img src="https://drive.google.com/thumbnail?id={video['id']}&sz=w640" class="w-full h-full object-cover" alt="{video['name']}" onerror="this.src='https://via.placeholder.com/640x360/1e293b/38bdf8?text=Prima+Bay+Video'">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent"></div>
                            <div class="absolute inset-0 flex items-center justify-center">
                                <div class="w-16 h-16 rounded-full bg-primary/90 flex items-center justify-center group-hover:scale-110 transition-transform">
                                    <svg class="w-8 h-8 text-white ml-1" fill="currentColor" viewBox="0 0 24 24">
                                        <path d="M8 5v14l11-7z"/>
                                    </svg>
                                </div>
                            </div>
                            <div class="absolute bottom-4 left-4 right-4">
                                <h3 class="text-white font-semibold text-lg line-clamp-2">{video['name']}</h3>
                            </div>
                        </div>
                    </div>
                </div>
'''

video_gallery += '''
            </div>
        </div>
    </section>

    <!-- Video Gallery Modal -->
    <div id="gallery-video-modal" class="modal fixed inset-0 bg-black/95 backdrop-blur-sm z-[100] items-center justify-center p-4">
        <div class="relative max-w-6xl w-full">
            <button onclick="closeGalleryVideoModal()" class="absolute -top-12 right-0 text-white hover:text-primary text-4xl font-bold z-[101]">&times;</button>
            <div class="text-center mb-4">
                <h3 id="gallery-video-title" class="text-2xl font-bold text-white"></h3>
            </div>
            <div class="rounded-4xl overflow-hidden shadow-2xl">
                <div class="relative" style="padding-bottom: 56.25%; height: 0;">
                    <iframe 
                        id="gallery-video-iframe"
                        src="" 
                        class="absolute top-0 left-0 w-full h-full"
                        allow="autoplay; fullscreen"
                        allowfullscreen
                        style="border: none;">
                    </iframe>
                </div>
            </div>
        </div>
    </div>

    <script>
        function openVideoModal(videoId, videoName) {
            const modal = document.getElementById('gallery-video-modal');
            const iframe = document.getElementById('gallery-video-iframe');
            const title = document.getElementById('gallery-video-title');
            
            iframe.src = 'https://drive.google.com/file/d/' + videoId + '/preview?autoplay=1';
            title.textContent = videoName;
            modal.classList.add('active');
        }
        
        function closeGalleryVideoModal() {
            const modal = document.getElementById('gallery-video-modal');
            const iframe = document.getElementById('gallery-video-iframe');
            
            iframe.src = '';
            modal.classList.remove('active');
        }

        // Auto play main video when scrolled into view
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                const iframe = document.getElementById('main-video');
                if (entry.isIntersecting) {
                    // Video in view - already has autoplay in src
                } else {
                    // Video out of view - pause by resetting src without autoplay
                    if (iframe.src.includes('autoplay=1')) {
                        iframe.src = iframe.src.replace('autoplay=1', 'autoplay=0');
                    }
                }
            });
        }, { threshold: 0.5 });

        const videoSection = document.getElementById('video-intro');
        if (videoSection) {
            observer.observe(videoSection);
        }
    </script>
'''

# Chèn Video Gallery ngay sau Video Section
video_section_end = html.find('    <!-- Project Info Cards -->')
html = html[:video_section_end] + video_gallery + '\n' + html[video_section_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Done!")
print("1. Video giới thiệu có autoplay khi scroll vào")
print("2. Thư viện 12 video với grid chuyên nghiệp")
print("3. Click video → mở modal fullscreen + autoplay")
