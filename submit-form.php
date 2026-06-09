<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $data = json_decode(file_get_contents('php://input'), true);
    
    $name = isset($data['name']) ? htmlspecialchars($data['name']) : '';
    $phone = isset($data['phone']) ? htmlspecialchars($data['phone']) : '';
    $email = isset($data['email']) ? htmlspecialchars($data['email']) : '';
    
    if (empty($name) || empty($phone)) {
        echo json_encode(['success' => false, 'message' => 'Thiếu thông tin bắt buộc']);
        exit;
    }
    
    // Lưu vào file CSV
    $timestamp = date('Y-m-d H:i:s');
    $row = [$timestamp, $name, $phone, $email];
    
    $file = 'customers.csv';
    $isNewFile = !file_exists($file);
    
    $fp = fopen($file, 'a');
    
    // Ghi header nếu file mới
    if ($isNewFile) {
        fputcsv($fp, ['Thời gian', 'Họ tên', 'Số điện thoại', 'Email']);
    }
    
    fputcsv($fp, $row);
    fclose($fp);
    
    echo json_encode(['success' => true, 'message' => 'Đã lưu thông tin thành công']);
} else {
    echo json_encode(['success' => false, 'message' => 'Chỉ chấp nhận POST request']);
}
?>
