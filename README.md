# HOSPOT - All-In-One Medical Information App

Welcome to the official repository of **HOSPOT**, an all-in-one medical information app designed to assist international students in navigating the healthcare system in Korea.

## Overview

HOSPOT was created to address the challenges faced by international students when accessing medical services in Korea. Through user-friendly features such as a Symptom Checker, department-specific hospital information, and real-time translation services, HOSPOT aims to make healthcare more accessible and less daunting for non-Korean speakers.

## Features

### 1. Symptom Checker
- **Functionality**: Allows users to input symptoms and receive diagnostic recommendations.
- **Guidelines**: Operates based on Clinical Performance Examination (CPX) guidelines provided by the Health Insurance Review & Assessment Service.
- **Steps**: 
  1. Select the affected area.
  2. Choose main symptoms.
  3. Answer related questions.
  4. Receive a diagnosis and department recommendation.

### 2. Department Information
- **Functionality**: Provides detailed information about hospitals by department.
- **Accreditation**: Features hospitals certified by the Korea Institute for Healthcare Accreditation.
- **Additional Tools**: Includes a website (PC) version for broader accessibility.

### 3. Real-Time Translation
- **Functionality**: Offers real-time interpretation services through integration with BBB Korea, an NGO providing translation support.
- **Use Case**: Particularly useful for emergency situations or when visiting hospitals without a Korean-speaking companion.

## Motivation

Many international students have reported difficulties in accessing appropriate medical care due to language barriers and a lack of information. HOSPOT was developed in collaboration with KAIST International Students Association (KISA) to directly address these issues and provide a comprehensive solution.

## How to Run

### Prerequisites
Before you start, ensure you have the following installed:

- **Python 3.8+**
- **pip** (Python package installer)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ChaeWoojin/Hospot-App.git
   cd Hospot-App
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

1. **Start the application**:
   ```bash
   python manage.py runserver
   ```

2. **Access the app**:
   Open your browser and navigate to `http://localhost:5000` to start using HOSPOT.

## Future Plans

- **Hospital Rating Feature**: Adding a feature to accumulate and display user reviews, enhancing the quality of information.
- **Nationwide Expansion**: Scaling the service from Daejeon to cover all of Korea, making it accessible to a broader audience of international residents.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your improvements or new features. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please feel free to contact us through the issues page or directly via email.
