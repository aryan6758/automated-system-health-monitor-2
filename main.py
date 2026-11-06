import time
import sys
from health_monitor.monitor import SystemMonitor
from health_monitor.config import load_config

def main():
    print("--- Automated System Health Monitor ---")
    print("Press Ctrl+C to stop monitoring.\n")

    monitor = SystemMonitor()
    config = load_config()

    try:
        while True:
            status = monitor.check_health()
            print(f"Status: {status['status']} | CPU: {status['cpu']}% | Mem: {status['memory']}% | Disk: {status['disk']}%")
            time.sleep(config["check_interval"])
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
