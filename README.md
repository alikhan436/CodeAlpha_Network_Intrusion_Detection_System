# CodeAlpha Internship - Task 4: Network Intrusion Detection System (Snort Rule Configuration)

A rule-based Network Intrusion Detection System (NIDS) project demonstrating signature detection for web application attacks and network probes.

## Features
- **Snort Rule Definitions**: Custom rules configured in `local.rules` to detect ICMP probes, SQL Injection, and Directory Traversal attacks.
- **Traffic Inspection Engine**: A Python simulator (`nids_simulator.py`) that parses live network payloads and evaluates them against signature rules.
- **Alert System**: Triggers real-time alerts with Rule SIDs upon detecting malicious pattern matches.

## Prerequisites
- **Python**: Python 3.x installed.
- **Text Editor / IDE**: Visual Studio Code or any standard editor.

## How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/alikhan436/CodeAlpha_Network_Intrusion_Detection_System.git](https://github.com/alikhan436/CodeAlpha_Network_Intrusion_Detection_System.git)
   cd CodeAlpha_Network_Intrusion_Detection_System