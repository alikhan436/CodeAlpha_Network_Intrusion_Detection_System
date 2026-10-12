import re

# Simulated Detection Rules
RULES = [
    {"id": 1000001, "msg": "[NIDS ALERT] ICMP Ping Traffic Detected", "pattern": r"ICMP"},
    {"id": 1000002, "msg": "[NIDS ALERT] Potential SQL Injection Attempt", "pattern": r"(SELECT|UNION|INSERT|DROP)", "flags": re.IGNORECASE},
    {"id": 1000003, "msg": "[NIDS ALERT] Directory Traversal Attempt", "pattern": r"(\.\./|/etc/passwd)", "flags": re.IGNORECASE}
]

# Simulated Incoming Traffic Stream
traffic_logs = [
    "GET /index.php?user=1 OR SELECT * FROM users HTTP/1.1",
    "PING Request from 192.168.1.15 to 192.168.1.1 [ICMP]",
    "GET /download.php?file=../../etc/passwd HTTP/1.1",
    "POST /login.php HTTP/1.1 Body: username=admin&password=123"
]

print("--- Network Intrusion Detection System (NIDS) Engine Active ---")
print("Monitoring real-time traffic for rule matches...\n")

for packet in traffic_logs:
    print(f"[PACKET INSPECT]: {packet}")
    alert_triggered = False
    
    for rule in RULES:
        flags = rule.get("flags", 0)
        if re.search(rule["pattern"], packet, flags):
            print(f"  >>> ALERT TRIGGERED [Rule SID: {rule['id']}]: {rule['msg']}")
            alert_triggered = True
            
    if not alert_triggered:
        print("  [STATUS]: Traffic Clean")
    print("-" * 65)