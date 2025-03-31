# finetunning_fruit_recognition

# 🍎🍌 Fruit Recognition API with Deep Learning  

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)  
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12+-orange)](https://www.tensorflow.org/)  
[![Docker](https://img.shields.io/badge/Docker-Containers-blue)](https://www.docker.com/)  

An end-to-end deep learning system for fruit image classification, deployed as a Flask API with Docker.  

🔗 **Live Demo**: [Docker Hub Image](https://hub.docker.com/r/afdelk/afdel_fruit_recognition)  

---

## ✨ Features  
- **Image Classification**: Predicts 131 fruit types using fine-tuned VGG16 model (91% accuracy).  
- **REST API**: Flask endpoint (`/predict`) for real-time predictions.  
- **Dockerized**: Ready-to-deploy container with all dependencies.  
- **Data Augmentation**: Enhanced model robustness with rotated/flipped images.  

---

## 🛠️ Tech Stack  
- **Deep Learning**: `TensorFlow/Keras` (VGG16 transfer learning)  
- **Backend**: `Flask`  
- **Deployment**: `Docker`  
- **Dataset**: [Fruits-360 (Hugging Face)](https://huggingface.co/datasets/PedroSampaio/fruits-360)  

---

## 🚀 Quick Start  

### 1. Run with Docker  
```bash  
docker pull afdelk/afdel_fruit_recognition  
docker run -p 5000:5000 afdelk/afdel_fruit_recognition  
