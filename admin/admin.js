// Firebase configuration - phải giống với index.html
const firebaseConfig = {
    apiKey: "AIzaSyBJOXRce0Og0Wxi5D98giQzOd1TMXNIyHM",
    authDomain: "prima-bay-halong.firebaseapp.com",
    databaseURL: "https://prima-bay-halong-default-rtdb.firebaseio.com",
    projectId: "prima-bay-halong",
    storageBucket: "prima-bay-halong.firebasestorage.app",
    messagingSenderId: "80581247519",
    appId: "1:80581247519:web:38882e79dd9d1cb85c8b2a",
    measurementId: "G-1SEWQ99T3V"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const db = firebase.database();

// Admin credentials - so sánh trực tiếp
const ADMIN_USERNAME = "congnt1605";
const ADMIN_PASSWORD = "Cn160520";

let customersRef = null;

// DOM Elements
const loginModal = document.getElementById('login-modal');
const loginForm = document.getElementById('login-form');
const loginError = document.getElementById('login-error');
const adminHeader = document.getElementById('admin-header');
const statsCards = document.getElementById('stats-cards');
const customersContainer = document.getElementById('customers-container');
const customersTable = document.getElementById('customers-table');
const totalCustomersEl = document.getElementById('total-customers');
const calledCustomersEl = document.getElementById('called-customers');
const pendingCustomersEl = document.getElementById('pending-customers');

// Check session storage for login status
const storedUsername = sessionStorage.getItem('adminUsername');
const storedPassword = sessionStorage.getItem('adminPassword');

if (storedUsername === ADMIN_USERNAME && storedPassword === ADMIN_PASSWORD) {
    loginModal.style.display = 'none';
    adminHeader.style.display = 'flex';
    statsCards.style.display = 'grid';
    customersContainer.style.display = 'block';
    loadCustomers();
} else {
    loginModal.style.display = 'flex';
}

// Xử lý login
loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('login-username').value.trim();
    const password = document.getElementById('login-password').value.trim();
    
    loginError.classList.add('hidden');
    
    if (username === ADMIN_USERNAME && password === ADMIN_PASSWORD) {
        // Lưu vào session
        sessionStorage.setItem('adminUsername', username);
        sessionStorage.setItem('adminPassword', password);
        
        loginModal.style.display = 'none';
        adminHeader.style.display = 'flex';
        statsCards.style.display = 'grid';
        customersContainer.style.display = 'block';
        loadCustomers();
    } else {
        loginError.textContent = 'Sai username hoặc mật khẩu!';
        loginError.classList.remove('hidden');
    }
});

// Logout
function logout() {
    sessionStorage.removeItem('adminUsername');
    sessionStorage.removeItem('adminPassword');
    location.reload();
}

// Đọc danh sách khách hàng từ Firebase
function loadCustomers() {
    if (!customersRef) {
        customersRef = db.ref('customers');
    }
    
    customersRef.on('value', snapshot => {
        const customers = snapshot.val();
        if (!customers) {
            updateStats(0, 0, 0);
            customersTable.innerHTML = '<tr><td colspan="7" class="px-6 py-8 text-center text-slate-400">Chưa có khách hàng nào</td></tr>';
            return;
        }
        
        const customersArray = Object.entries(customers).map(([id, data]) => ({
            id,
            ...data,
            timestamp: data.timestamp || 0
        }));
        
        // Sắp xếp theo thời gian (mới nhất lên đầu)
        customersArray.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
        
        // Render bảng
        customersTable.innerHTML = customersArray.map(customer => `
            <tr class="hover:bg-white/5 transition">
                <td class="px-6 py-4 text-slate-300 text-sm">
                    ${new Date(customer.timestamp || Date.now()).toLocaleString('vi-VN')}
                </td>
                <td class="px-6 py-4 font-medium text-white">${escapeHtml(customer.name)}</td>
                <td class="px-6 py-4 text-sky-300">${escapeHtml(customer.phone)}</td>
                <td class="px-6 py-4 text-slate-300 text-sm">${escapeHtml(customer.email || '-')}</td>
                <td class="px-6 py-4">
                    <textarea 
                        class="w-full px-3 py-2 rounded-xl bg-white/5 border border-white/10 focus:border-sky-400 focus:outline-none text-sm resize-none"
                        rows="2"
                        oninput="updateNote('${customer.id}', this.value)"
                        placeholder="Ghi chú..."
                    >${escapeHtml(customer.note || '')}</textarea>
                </td>
                <td class="px-6 py-4">
                    <button 
                        onclick="toggleCalled('${customer.id}', ${customer.called || false})"
                        class="${(customer.called || false) ? 'called-true' : 'called-false'} text-white px-4 py-2 rounded-xl font-medium transition flex items-center gap-2"
                    >
                        ${(customer.called || false) ? '✓ Đã gọi' : '⬜ Chưa gọi'}
                    </button>
                </td>
                <td class="px-6 py-4">
                    <button onclick="deleteCustomer('${customer.id}')" class="text-red-400 hover:text-red-300 text-sm">
                        🗑️ Xóa
                    </button>
                </td>
            </tr>
        `).join('');
        
        // Cập nhật thống kê
        const total = customersArray.length;
        const called = customersArray.filter(c => c.called).length;
        const pending = total - called;
        updateStats(total, called, pending);
    });
}

// Cập nhật ghi chú
async function updateNote(customerId, note) {
    try {
        await db.ref(`customers/${customerId}/note`).set(note);
        console.log('Updated note for', customerId);
    } catch (error) {
        console.error('Error updating note:', error);
    }
}

// Đánh dấu đã gọi hoặc chưa gọi
async function toggleCalled(customerId, currentStatus) {
    const newStatus = !currentStatus;
    try {
        await db.ref(`customers/${customerId}/called`).set(newStatus);
        console.log(`Updated called status for ${customerId}: ${newStatus}`);
    } catch (error) {
        console.error('Error updating called status:', error);
    }
}

// Xóa khách hàng
async function deleteCustomer(customerId) {
    if (!confirm('Bạn có chắc muốn xóa khách hàng này?')) return;
    
    try {
        await db.ref(`customers/${customerId}`).remove();
        console.log('Deleted customer:', customerId);
    } catch (error) {
        console.error('Error deleting customer:', error);
    }
}

// Cập nhật thống kê
function updateStats(total, called, pending) {
    totalCustomersEl.textContent = total;
    calledCustomersEl.textContent = called;
    pendingCustomersEl.textContent = pending;
}

// Helper: escape HTML để tránh XSS
function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Auto-refresh mỗi 30 giây
setInterval(() => {
    loadCustomers();
}, 30000);