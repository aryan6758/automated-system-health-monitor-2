# Automated System Health Monitor

A lightweight, professional system monitoring tool designed to track key hardware metrics in real-time and provide proactive alerting when system resources reach critical thresholds.

## 🚀 Pitch
Keeping a system stable requires constant vigilance. The **Automated System Health Monitor** removes the guesswork by providing a continuous, real-time stream of your system's CPU, Memory, and Disk health. It's designed for developers and sysadmins who need a simple, "set-and-forget" utility to ensure their environment isn't about to crash under load.

## ✨ Features
- **Real-time Monitoring**: Continuous tracking of CPU, RAM, and Disk usage.
- **Configurable Thresholds**: Easily adjust what constitutes "Unhealthy" via environment variables.
- **Proactive Alerting**: Instant console alerts and persistent logging when metrics exceed defined limits.
- **Health Status Engine**: A simplified "Healthy/Unhealthy" status based on aggregate system state.
- **Low Overhead**: Built with `psutil` for high-performance, low-impact system polling.

## 🛠 Tech Stack
- **Language**: Python 3.10+
- **Core Library**: `psutil` (System utilities)
- **Testing**: `pytest` & `pytest-mock`
- **Configuration**: Environment-based dynamic config

## 📂 Project Structure
```text
.
├── health_monitor/
│   ├── __init__.py
│   ├── config.py    # Thresholds and environment configuration
│   ├── alerts.py    # Alerting and logging logic
│   └── monitor.py   # Core system metric collection engine
├── tests/
│   ├── __init__.py
│   └── test_monitor.py # Unit tests for monitoring logic
├── main.py          # CLI entry point and monitoring loop
└── requirements.txt # Project dependencies
```

## ⚙️ Setup
1. **Clone the repository** (or navigate to the folder).
2. **Activate your virtual environment**:
   ```powershell
   .\.venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage
Run the monitor directly from the root directory:
```bash
python main.py
```

### Customizing Thresholds
You can override the default thresholds (CPU: 80%, Mem: 80%, Disk: 90%) using environment variables:
```powershell
# Example for Windows PowerShell
$env:MONITOR_CPU_THRESHOLD=50.0
$env:MONITOR_MEM_THRESHOLD=60.0
python main.py
```

## 📊 Example Output
```text
--- Automated System Health Monitor ---
Press Ctrl+C to stop monitoring.

Status: Healthy | CPU: 12.2% | Mem: 67.1% | Disk: 48.3%
Status: Healthy | CPU: 15.8% | Mem: 67.2% | Disk: 48.3%
ALERT: CPU exceeded threshold! Current: 85.4%, Threshold: 80.0%
Status: Unhealthy | CPU: 85.4% | Mem: 67.5% | Disk: 48.3%
```

## 🧪 Running Tests
The project includes a comprehensive test suite to verify metric collection and alerting logic:
```bash
pytest tests/test_monitor.py
```

---
*Built with AI assistance*
