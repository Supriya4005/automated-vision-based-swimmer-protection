# Automated Vision-Based Surveillance System to Detect and Uplift Drowning Incidents in Swimming Pools

**Author:** Supriya N R

---

## 📌 Project Overview

This project implements an **Automated Vision-Based Surveillance System** for swimming pools to detect and prevent drowning incidents. The system uses **real-time computer vision and AI algorithms** to continuously monitor swimmers, identify signs of distress, and trigger immediate alerts for rapid intervention, enhancing overall safety.

---

## ⚙️ Technology Justification

* **OpenCV (>=4.9.0):** Used for real-time video capture, frame processing, and visual analysis. OpenCV is fast and efficient for real-time surveillance applications.
* **MediaPipe / Pose Estimation (>=0.10.8):** Provides accurate detection of human body landmarks, enabling the system to identify unusual postures indicative of drowning.
* **NumPy (>=1.24.0):** Facilitates numerical computations and array operations for feature extraction and processing.
* **TensorFlow / PyTorch (optional, >=2.13.0):** For implementing AI models to classify swimmer behavior and detect distress.
* **IoT Sensors (optional):** Integrates with wearable devices or pool sensors to enhance detection accuracy.

These libraries were chosen for their **real-time performance, accuracy, and reliability** in monitoring and detecting drowning incidents.

---

## ✋ Detection Methodology

1. **Video Input:** Real-time feed from pool cameras is captured using OpenCV.
2. **Pose / Motion Detection:** MediaPipe or AI-based algorithms detect swimmer body landmarks and analyze movements.
3. **Behavior Analysis:** The system identifies irregular or distressed movements, such as prolonged submersion or lack of limb motion.
4. **Alert Generation:** On detecting potential drowning, the system triggers immediate notifications for lifeguards or emergency responders.
5. **Result Display:** Alerts are displayed on the monitoring dashboard, enabling quick intervention.

---

## ⚙️ Setup and Execution Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/automated-pool-surveillance.git
cd automated-pool-surveillance
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run the application:**

```bash
python src/main.py
```

5. **Monitor the pool:**
   Open a browser or application interface (if included) to view real-time alerts and monitoring feed.

---

## 🛠 Repository Structure

```
automated-pool-surveillance/
├── README.md
├── requirements.txt
├── src/
│   ├── main.py
│   ├── detection.py
│   └── utils.py
├── models/        # Pre-trained AI models
├── data/          # Sample videos or datasets
└── static/        # optional static files
```

---

## 📜 License

This project is licensed under the MIT License.
