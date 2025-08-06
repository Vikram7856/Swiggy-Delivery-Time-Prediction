# Datasets Directory

This directory contains the dataset used for training and evaluating the delivery time prediction model. The data is based on real-world Swiggy delivery records and includes comprehensive features that help accurately predict delivery times.

## Data Structure

### Feature Categories

#### 📦 Order Context Features
| Feature | Type | Description | Example Values |
|---------|------|-------------|----------------|
| `type_of_order` | Categorical | Type of food order | Meal, Snack, Drink, Dessert |
| `order_time_of_day` | Categorical | Time period of order | Morning, Afternoon, Evening, Night |
| `distance` | Numerical | Delivery distance (km) | 0.5 - 15.0 |
| `ratings` | Numerical | Restaurant/delivery ratings | 1.0 - 5.0 |

#### 🌦️ Environmental Features
| Feature | Type | Description | Example Values |
|---------|------|-------------|----------------|
| `weather` | Categorical | Weather conditions | Clear, Cloudy, Rain, Storm |
| `traffic` | Categorical | Traffic density level | Low, Medium, High, Jam |
| `festival` | Binary | Festival period indicator | 0, 1 |
| `city_type` | Categorical | Urban classification | Metropolitan, Urban, Suburban |
| `is_weekend` | Binary | Weekend indicator | 0, 1 |

#### 🛵 Logistics Features
| Feature | Type | Description | Example Values |
|---------|------|-------------|----------------|
| `type_of_vehicle` | Categorical | Delivery vehicle type | Motorcycle, Car, Bicycle |
| `vehicle_condition` | Categorical | Vehicle condition status | Excellent, Good, Average |
| `multiple_deliveries` | Binary | Multiple delivery batch | 0, 1 |
| `pickup_time` | Numerical | Food preparation time (min) | 5 - 45 |

#### 🎯 Target Variable
| Feature | Type | Description | Range |
|---------|------|-------------|--------|
| `delivery_time` | Numerical | Total delivery time (minutes) | 10 - 90 |

## Cities Data Visualization

Below is a visualization of the geographic distribution of cites from the dataset:

![Cities Data](cities_data.png)

