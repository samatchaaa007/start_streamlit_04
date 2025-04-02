import pandas as pd
from datetime import datetime
import os

def log_event(username, fullname, browser="Unknown", page="Unknown", event="visit_page", ip="Unknown"):
    log_path = "user_login_log.csv"
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "username": username,
        "fullname": fullname,
        "browser": browser,
        "page": page,
        "event": event,
        "ip": ip  # ✅ เพิ่ม IP เข้าไป
    }

    df = pd.DataFrame([log_entry])
    if os.path.exists(log_path):
        df.to_csv(log_path, mode='a', header=False, index=False)
    else:
        df.to_csv(log_path, index=False)