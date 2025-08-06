# 🚀 Streamlit Web Application

Welcome to the **Delivery Time Prediction App** — an intelligent web application built to optimize last-mile food delivery by providing accurate delivery time estimates. This Streamlit-powered interface makes machine learning predictions accessible through an intuitive web interface.

## 🎯 Application Overview

This web application leverages real Swiggy delivery data and advanced machine learning models to provide accurate delivery time predictions. The app features a clean, user-friendly interface that allows users to input delivery parameters and receive instant predictions.

### Key Features
- **Interactive Prediction Interface**: Easy-to-use forms for inputting delivery parameters
- **Real-time Predictions**: Instant delivery time estimates using trained ML models
- **Data Visualization**: Charts and insights about delivery patterns
- **Responsive Design**: Works on desktop and mobile devices
- **Model Explanations**: Understanding what factors influence predictions

## 📊 Prediction Factors

The application considers multiple factors when predicting delivery times:

### 📦 Order Details
- **Order Type**: Meal, Snack, Drink, Dessert
- **Order Time**: Morning, Afternoon, Evening, Night
- **Distance**: Delivery distance in kilometers
- **Ratings**: Restaurant and delivery ratings

### 🌦️ Environmental Factors
- **Weather Conditions**: Clear, Cloudy, Rain, Storm
- **Traffic Level**: Low, Medium, High, Jam
- **Festival Period**: Special events and holidays
- **Weekend Status**: Weekend vs. weekday deliveries
- **City Type**: Metropolitan, Urban, Suburban

### 🛵 Logistics Information
- **Vehicle Type**: Motorcycle, Car, Bicycle
- **Vehicle Condition**: Excellent, Good, Average
- **Multiple Deliveries**: Single vs. batch deliveries
- **Pickup Time**: Food preparation duration

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Navigate to the app directory**:
   ```bash
   cd streamlit_app
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### 🏃‍♂️ Running the Application

1. **Start the Streamlit server**:
   ```bash
   streamlit run app.py
   ```

2. **Access the application**:
   - Open your web browser
   - Navigate to `http://localhost:8501`
   - The application will load automatically

3. **Alternative port** (if 8501 is busy):
   ```bash
   streamlit run app.py --server.port 8502
   ```

## 🖥️ Application Structure

### File Organization
```
streamlit_app/
├── app.py                    # Main application entry point
├── Home.py                   # Home page component
├── Time_prediction.py        # Prediction interface
├── requirements.txt          # Python dependencies
├── swiggy_imputed_data.pkl   # Preprocessed data for reference
└── readme.md                 # This documentation
```

### Page Navigation
- **Home Page**: Project overview, methodology, and insights
- **Prediction Page**: Interactive form for delivery time predictions

## 🔧 Application Features

### Home Page Features
- **Project Introduction**: Overview of the delivery time prediction system
- **Dataset Insights**: Key statistics and patterns from the data
- **Model Performance**: Accuracy metrics and validation results
- **Methodology Explanation**: How the prediction system works

### Prediction Page Features
- **Interactive Form**: User-friendly input fields for all prediction parameters
- **Real-time Validation**: Input validation with helpful error messages
- **Instant Predictions**: Fast response times for prediction requests
- **Result Visualization**: Clear display of predicted delivery times
- **Confidence Intervals**: Uncertainty estimates for predictions
- **Feature Importance**: Which factors most influence the prediction

## 📱 User Interface Guide

### Using the Prediction Interface

1. **Select Navigation**: Use the sidebar to navigate between pages
2. **Input Parameters**:
   - Fill in order details (type, distance, ratings)
   - Select environmental conditions (weather, traffic)
   - Choose vehicle and logistics information
3. **Get Prediction**: Click the "Predict Delivery Time" button
4. **Interpret Results**: Review the predicted time and contributing factors

### Input Validation
- **Distance**: Must be between 0.1 and 50 km
- **Ratings**: Scale from 1.0 to 5.0
- **Pickup Time**: Reasonable preparation time (5-60 minutes)
- **Required Fields**: All fields must be completed for prediction

## 📊 Model Integration

### Model Loading
```python
import pickle
import streamlit as st

@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()
```

### Prediction Pipeline
```python
def predict_delivery_time(features):
    # Preprocess input features
    processed_features = preprocess_input(features)
    
    # Make prediction
    prediction = model.predict([processed_features])
    
    # Post-process results
    delivery_time = round(prediction[0], 1)
    
    return delivery_time
```

## 🎨 Customization Options

### Styling and Themes
```python
# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #FF6B6B;
        text-align: center;
    }
    .prediction-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)
```

### Configuration Options
```python
# Streamlit configuration
st.set_page_config(
    page_title="Delivery Time Prediction",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

## 📈 Performance Optimization

### Caching Strategies
- **Model Caching**: `@st.cache_resource` for model loading
- **Data Caching**: `@st.cache_data` for data preprocessing
- **Session State**: Storing user inputs across page refreshes

### Loading Times
- **Initial Load**: ~2-3 seconds (model loading)
- **Predictions**: <1 second response time
- **Page Navigation**: Instant switching between pages

## 🔧 Development & Deployment

### Local Development
```bash
# Install development dependencies
pip install streamlit-dev

# Run with hot reload
streamlit run app.py --server.runOnSave true
```

### Production Deployment

#### Streamlit Cloud
1. Push code to GitHub repository
2. Connect repository to Streamlit Cloud
3. Deploy with automatic requirements installation

#### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Heroku Deployment
```bash
# Create Procfile
echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Deploy to Heroku
heroku create your-app-name
git push heroku main
```

## 📸 Application Screenshots

### Home Page Overview
![Home Page 1](Streamlit_home_page-0001.jpg)
*Welcome screen with project introduction and navigation*

![Home Page 2](Streamlit_home_page-0002.jpg)
*Dataset insights and key statistics*

![Home Page 3](Streamlit_home_page-0003.jpg)
*Model performance metrics and methodology*

### Prediction Interface
![App Page 1](Streamlit_app_page-0001.jpg)
*Order details input form*

![App Page 2](Streamlit_app_page-0002.jpg)
*Environmental factors selection*

![App Page 3](Streamlit_app_page-0003.jpg)
*Logistics information input*

![App Page 4](Streamlit_app_page-0004.jpg)
*Prediction results and insights*

## 🔍 Troubleshooting

### Common Issues

#### Import Errors
```bash
# Solution: Install missing dependencies
pip install -r requirements.txt
```

#### Port Already in Use
```bash
# Solution: Use different port
streamlit run app.py --server.port 8502
```

#### Model Loading Issues
```bash
# Check if model file exists
ls -la *.pkl

# Verify Python version compatibility
python --version
```

#### Performance Issues
- Clear Streamlit cache: Press 'C' in the running app
- Restart the application: Ctrl+C and rerun
- Check system resources: Memory and CPU usage

## 📋 Dependencies

### Core Requirements
```txt
streamlit==1.45.1          # Web framework
scikit-learn==1.6.1        # Machine learning
pandas==2.2.3              # Data manipulation
numpy==2.1.3               # Numerical computing
```

### ML Libraries
```txt
xgboost==3.0.2             # Gradient boosting
lightgbm==4.6.0            # Light gradient boosting
joblib==1.4.2              # Model serialization
```

### Visualization
```txt
matplotlib==3.10.0         # Basic plotting
seaborn==0.13.2            # Statistical visualization
shap==0.48.0               # Model explanations
```

## 🤝 Contributing

### Adding New Features
1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/new-feature`
3. **Implement changes** in the appropriate files
4. **Test thoroughly** with different input combinations
5. **Update documentation** if needed
6. **Submit pull request** with clear description

### Code Style Guidelines
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Add docstrings for functions
- Maintain consistent formatting

### Testing Guidelines
```python
# Example test for prediction function
def test_prediction_validity():
    sample_input = create_sample_input()
    result = predict_delivery_time(sample_input)
    assert 10 <= result <= 90  # Reasonable delivery time range
```

## 📞 Support & Feedback

### Getting Help
- **Documentation**: Check this README and main project docs
- **Issues**: Create GitHub issue with detailed problem description
- **Community**: Join project discussions

### Feedback
- **Feature Requests**: Suggest improvements via GitHub issues
- **Bug Reports**: Include steps to reproduce and system information
- **Performance**: Report slow loading times or prediction delays

---

**Built with ❤️ using Streamlit for better delivery predictions**
