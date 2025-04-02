# user_data.py

users = {
    "admin": {
        "password": "admin123",
        "fullname": "สมชาย แอดมิน",
        "position": "หัวหน้าระบบ",
        "department": "ฝ่าย AD DA",
        "profile_pic": "assets/profiles/admin.jpg"
    },
    "user1": {
        "password": "pass1",
        "fullname": "วิภา สมบูรณ์",
        "position": "เจ้าหน้าที่วิเคราะห์",
        "department": "ฝ่าย DATA",
        "profile_pic": "assets/profiles/user1.jpg"
    },
    "user2": {
        "password": "pass2",
        "fullname": "จักรกฤษณ์ ทดสอบ",
        "position": "เจ้าหน้าที่ทั่วไป",
        "department": "ฝ่ายบริการ IT",
        "profile_pic": "assets/profiles/user2.jpg"
    }
}

user_permissions = {
    "admin": ["Page 1", "Page 2", "Page 3", "Page 4", "Page 5", "Page 6"],
    "user1": ["Page 1", "Page 2"],
    "user2": ["Page 1", "Page 5"]
}