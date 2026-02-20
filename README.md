# Road Anomaly Detection (Bharat AI-SoC 2026)

## Implementation Details
* **Inference Engine:** LiteRT (TensorFlow Lite) using XNNPACK CPU Delegate.
* **Architecture:** 64-bit (aarch64) optimization for Raspberry Pi 4.
* **Optimization:** Headless OpenCV deployment and asynchronous GPIO threading for low-latency alerts.

## Performance Metrics
* **Throughput:** ~6.9 FPS
* **Latency:** ~145ms
* 
