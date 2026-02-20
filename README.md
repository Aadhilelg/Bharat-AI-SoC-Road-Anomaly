# Road Anomaly Detection - Bharat AI-SoC 2026

## Optimization & Performance
* **SoC Acceleration:** Implemented using LiteRT with the XNNPACK CPU delegate for the Broadcom BCM2711 SoC.
* **Headless Deployment:** Used `opencv-python-headless` to eliminate display server overhead, maximizing resources for AI inference.
* **Throughput:** ~6.9 FPS achieved on a 64-bit architecture.

## Hardware Integration
* **Buzzer:** Physical Pin 12 (GPIO 18)
* **LED:** Physical Pin 18 (GPIO 24)
* **Power/Cooling:** Physical Pin 2 (5V) and Physical Pin 6 (GND)
* 
