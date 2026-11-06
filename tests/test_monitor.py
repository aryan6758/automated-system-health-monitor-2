import pytest
from unittest.mock import patch, MagicMock
from health_monitor.monitor import SystemMonitor

def test_get_cpu_usage():
    with patch('psutil.cpu_percent', return_value=50.0):
        monitor = SystemMonitor()
        assert monitor.get_cpu_usage() == 50.0

def test_get_memory_usage():
    mock_mem = MagicMock()
    mock_mem.percent = 60.0
    with patch('psutil.virtual_memory', return_value=mock_mem):
        monitor = SystemMonitor()
        assert monitor.get_memory_usage() == 60.0

def test_get_disk_usage():
    mock_disk = MagicMock()
    mock_disk.percent = 70.0
    with patch('psutil.disk_usage', return_value=mock_disk):
        monitor = SystemMonitor()
        assert monitor.get_disk_usage() == 70.0

def test_check_health_healthy():
    with patch('psutil.cpu_percent', return_value=10.0), \
         patch('psutil.virtual_memory') as mock_mem, \
         patch('psutil.disk_usage') as mock_disk:

        mock_mem.return_value.percent = 10.0
        mock_disk.return_value.percent = 10.0

        monitor = SystemMonitor()
        status = monitor.check_health()
        assert status["status"] == "Healthy"

def test_check_health_unhealthy():
    # Set CPU to exceed default 80% threshold
    with patch('psutil.cpu_percent', return_value=90.0), \
         patch('psutil.virtual_memory') as mock_mem, \
         patch('psutil.disk_usage') as mock_disk:

        mock_mem.return_value.percent = 10.0
        mock_disk.return_value.percent = 10.0

        monitor = SystemMonitor()
        status = monitor.check_health()
        assert status["status"] == "Unhealthy"
