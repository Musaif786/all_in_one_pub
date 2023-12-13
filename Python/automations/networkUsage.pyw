import psutil

# Get network usage statistics
network = psutil.net_io_counters()

# Convert bytes to gigabytes (1 GB = 1024^3 bytes)
bytes_sent_gb = network.bytes_sent / (1024 ** 2)
bytes_recv_gb = network.bytes_recv / (1024 ** 2)

print(f"Bytes Sent: {bytes_sent_gb:.2f} MB")
print(f"Bytes Received: {bytes_recv_gb:.2f} MB")
