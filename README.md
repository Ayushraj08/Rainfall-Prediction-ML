# 🌧️ Rainfall Prediction Web App

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-ff4b4b.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue.svg)](https://www.linkedin.com/in/YOUR-LINKEDIN/)

**Demo Link:** https://rainfall-prediction-ml.streamlit.app/


---

## 📌 Project Overview
The **Rainfall Prediction Web App** is a machine learning-based tool built using **Python** and **Streamlit** to predict whether it will rain or not based on environmental factors such as temperature, humidity, pressure, cloud cover, wind speed, and sunshine hours.  

This project is aimed at helping **farmers, researchers, meteorologists, and students** understand rainfall predictions in an interactive and user-friendly way.

---

## 🚀 Features
✅ User-friendly **Streamlit UI**  
✅ Input parameters for rainfall prediction  
✅ ML Model (trained using `scikit-learn`) for accurate results  
✅ Beautiful **prediction results with emojis** (Rain or No Rain 🌧️☀️)  
✅ Charts for visualization (Humidity vs Rainfall trend, Sunshine vs Rainfall, etc.)  
✅ Footer with **About, Developer, Contact, Version** info  
✅ Fully open-source with **MIT License**  

---

## 📂 Project Structure
```plaintext
Rainfall-Prediction-Using-ML/
│
│── app.py # Main Streamlit app
│── model.pkl # Trained ML model
│── requirements.txt # Dependencies
│── README.md # Documentation
│── Rainfall.csv # Data used for training
```


---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR-USERNAME/Rainfall-Prediction-Using-ML.git
cd Rainfall-Prediction-Using-ML
```
2️⃣ Create & activate virtual environment (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```
3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Run the Streamlit app
```bash
streamlit run app.py
```

## 📊 Input Parameters

The app takes the following inputs:
- 🌡️ **Max Temperature**
- 💧 **Humidity**
- 🌥️ **Cloud Cover**
- 🌬️ **Wind Speed**
- ☀️ **Sunshine Hours**
- 📉 **Pressure**
- 🌧️ **Rainfall (previous records)**


## 📸 Screenshots
<img width="1894" height="926" alt="Screenshot 2025-08-26 033451" src="https://github.com/user-attachments/assets/6aa63005-d762-4ae7-a91f-13f6e8586b74" />


## 🔧 Technologies Used

- Python 🐍
- Streamlit (for Web App UI)
- Scikit-learn (ML Model)
- Pandas & Numpy (Data Processing)
- Matplotlib/Seaborn (Data Visualization)

## 📈 Future Improvements

- Add real-time weather API integration
- Deploy app on Streamlit Cloud / Heroku / AWS
- Enhance model with deep learning (LSTM for time-series)
- Mobile-friendly responsive UI

## 🤝 Contribution
```plain text
Contributions are welcome! Follow these steps:
Fork this repo 🍴
Create a new branch (feature-xyz)
Commit changes (git commit -m 'Add new feature')
Push to branch (git push origin feature-xyz)
Create a Pull Request
```
## 📬 Contact

- 👨‍💻 **Developer:** Ayush Raj
- **LinkedIn** : https://www.linkedin.com/in/ayussh-raj/
- 🔗: https://ayussh-portfolio.vercel.app/
- 📧 **Email**: rajaayushwow0@example.com
- **Demo link:** https://rainfall-prediction-ml.streamlit.app/

