import os

# Default configuration for the health monitor
DEFAULT_CONFIG = {
    "cpu_threshold": 80.0,        # Percentage
    "memory_threshold": 80.0,      # Percentage
    "disk_threshold": 90.0,       # Percentage
    "check_interval": 5,          # Seconds
    "log_file": "system_health.log"
}

def load_config():
    """
    Load configuration from environment variables or return defaults.
    """
    return {
        "cpu_threshold": float(os.getenv("MONITOR_CPU_THRESHOLD", DEFAULT_CONFIG["cpu_threshold"])),
        "memory_threshold": float(os.getenv("MONITOR_MEM_THRESHOLD", DEFAULT_CONFIG["memory_threshold"])),
        "disk_threshold": float(os.getenv("MONITOR_DISK_THRESHOLD", DEFAULT_CONFIG["disk_threshold"])),
        "check_interval": int(os.getenv("MONITOR_INTERVAL", DEFAULT_CONFIG["check_interval"])),
        "log_file": os.getenv("MONITOR_LOG_FILE", DEFAULT_CONFIG["log_file"]),
    }
