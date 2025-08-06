# 🚚 Swiggy Delivery Time Prediction

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-red)](https://streamlit.io/)
[![MLflow](https://img.shields.io/badge/MLflow-Enabled-green)](https://mlflow.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This project predicts food delivery times using real Swiggy order data and machine learning. It analyzes factors like order type, traffic conditions, weather, and delivery vehicle characteristics to provide accurate delivery time estimates, helping optimize last-mile delivery operations.

## 🎯 Project Overview

The system uses advanced machine learning algorithms to predict delivery times by considering:
- **Order Context**: Type, timing, distance, and customer ratings
- **Environmental Factors**: Weather conditions, traffic, festivals, and city characteristics
- **Logistics Information**: Vehicle type, condition, multiple deliveries, and pickup times

## 📊 Dataset Summary

- **Records**: 45,073 delivery orders
- **Features**: 19 comprehensive attributes
- **Source**: Real Swiggy delivery data

### Data Categories:
- 📦 **Order Context**: `type_of_order`, `order_time_of_day`, `distance`, `ratings`
- 🌦️ **Environment**: `weather`, `traffic`, `festival`, `city_type`, `is_weekend`
- 🛵 **Logistics**: `type_of_vehicle`, `vehicle_condition`, `multiple_deliveries`, `pickup_time`

## 🛠️ Tech Stack

- **Languages & Libraries**: Python, Scikit-learn, Pandas, NumPy
- **Machine Learning**: XGBoost, LightGBM, Stacking Regressor
- **Web Framework**: Streamlit
- **Model Management**: MLflow, Optuna
- **Data Processing**: Custom preprocessing pipelines with imputation, encoding, and scaling
- **Serialization**: Pickle, Joblib
- **Visualization**: Matplotlib, Seaborn, SHAP

## 📁 Project Structure

```
├── README.md                    # Main project documentation
├── datasets/                    # Dataset files and documentation
│   ├── readme.md               # Dataset description
│   └── cities_data.png         # Geographic data visualization
├── feature_engineering/         # Data preprocessing and feature engineering
│   ├── README.md               # Feature engineering documentation
│   ├── Data_Cleaning.ipynb     # Data cleaning notebook
│   ├── Food_Delivery_EDA.ipynb # Exploratory data analysis
│   └── Missing_value_imputation.ipynb # Data imputation strategies
├── models/                      # Trained models and experiments
│   ├── README.md               # Model documentation
│   ├── pipeline.png            # Model pipeline visualization
│   ├── metrices.png           # Performance metrics
│   └── *.ipynb                # Model training notebooks
└── streamlit_app/              # Web application
    ├── readme.md               # App-specific documentation
    ├── requirements.txt        # Python dependencies
    ├── app.py                  # Main application entry point
    ├── Home.py                 # Home page component
    └── Time_prediction.py      # Prediction interface
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Swiggy-Delivery-Time-Prediction
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   cd streamlit_app
   pip install -r requirements.txt
   ```

### 🏃‍♂️ Running the Application

1. **Start the Streamlit app**:
   ```bash
   cd streamlit_app
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Use the application**:
   - Navigate through the sidebar menu
   - Input delivery parameters in the prediction page
   - Get real-time delivery time estimates

### 🔧 Usage Examples

#### Web Interface
1. Select "Prediction" from the sidebar
2. Fill in the delivery details:
   - Order type (Snack, Meal, Drink, etc.)
   - Distance, weather conditions, traffic level
   - Vehicle information and delivery context
3. Click "Predict" to get estimated delivery time

#### Programmatic Usage
```python
# Load the trained model
import pickle
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Make predictions
delivery_features = [...] # Your feature vector
predicted_time = model.predict([delivery_features])
```

## 📈 Model Performance

Our ensemble model combines multiple algorithms for optimal performance:
- **Base Models**: Random Forest, LightGBM, XGBoost
- **Meta-Model**: Stacking Regressor
- **Hyperparameter Tuning**: Optuna optimization
- **Validation**: Cross-validation with time-based splits

For detailed metrics and performance analysis, see the [models README](models/README.md).

## 🔗 Resources & Links

- 📊 [MLflow Dashboard](https://dagshub.com/vkyadav7635/Swiggy-Delivery-Time-Prediction.mlflow) - Model tracking and experiments
- 🗂️ [Google Drive](https://drive.google.com/drive/folders/1amTEFs91NO_icdShALPP7RNdAg5ZMk35) - Data and model artifacts
- 📝 [Feature Engineering Guide](feature_engineering/README.md) - Data preprocessing details
- 🤖 [Model Documentation](models/README.md) - Training and evaluation details

## 📸 Application Preview

### Home Page
![Home Page 1](Streamlit_home_page-0001.jpg)
![Home Page 2](Streamlit_home_page-0002.jpg)
![Home Page 3](Streamlit_home_page-0003.jpg)

### Prediction Interface
![App Page 1](Streamlit_app_page-0001.jpg)
![App Page 2](Streamlit_app_page-0002.jpg)
![App Page 3](Streamlit_app_page-0003.jpg)
![App Page 4](Streamlit_app_page-0004.jpg)

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Commit your changes: `git commit -m 'Add feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

### Development Setup

1. Follow the installation instructions above
2. Install development dependencies: `pip install -r requirements-dev.txt` (if available)
3. Run tests: `python -m pytest` (if tests are available)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Swiggy for providing the dataset
- The open-source community for the amazing tools and libraries
- Contributors who helped improve this project

## 📞 Support

If you encounter any issues or have questions:
1. Check the [documentation](docs/) for common solutions
2. Search existing [issues](../../issues) on GitHub
3. Create a new issue with detailed information

---

**Made with ❤️ for better delivery predictions**

