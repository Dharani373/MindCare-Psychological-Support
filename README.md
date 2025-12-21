#  Digital Mental Health Support System

A web-based mental health support platform designed to help students **assess stress levels**, **track mental well-being over time**, and **receive emotional support** using **machine learning–based sentiment analysis** and interactive visualizations.

---

##  Project Overview

The **Digital Mental Health Support System** addresses increasing academic stress among students by providing a structured stress assessment, long-term stress tracking, and an AI-assisted emotional support interface.  
The system focuses on **self-awareness, early detection, and ethical AI usage**, while clearly stating that it is **not a replacement for professional mental health care**.

---

##  Objectives

- To assess user stress levels using standardized questionnaires  
- To analyze emotional sentiment using machine learning  
- To track stress trends over time through visual graphs  
- To provide ethical AI-based emotional support  
- To improve mental health awareness among students  

---

##  Technology Stack

###  Frontend
- HTML5  
- CSS3  
- JavaScript  

###  Backend
- Python  
- Django Framework  

###  Database
- SQLite (Django default database)

###  Machine Learning
- Scikit-learn  
- Naive Bayes Classifier  
- TF-IDF Vectorization  

###  Data Visualization
- Chart.js  

---

##  Core Features

###  User Authentication
- Secure login and logout
- User-specific data isolation

###  Stress Assessment
- Questionnaire-based stress evaluation
- Automatic score calculation
- Stress level classification (Low / Moderate / High)

### Stress History & Visualization
- Stores all stress assessments with timestamps
- Line graph visualization showing stress trends
- Helps users identify mental health patterns over time

### AI Emotional Support Chat
- ML-based sentiment analysis
- Classifies messages as Positive, Neutral, or Negative
- Crisis detection with red alert UI
- Ethical disclaimer included

### User Profile Management
- Editable personal details (Full Name, Date of Birth, Profession)
- Profile avatar (image or default letter-based avatar)
- Controlled edit → save workflow
- Stress summary displayed on profile page

---

## Machine Learning Usage

### Algorithm Used: **Naive Bayes Classifier**

The Naive Bayes classifier is used for **sentiment analysis** of user messages in the AI support chat.

#### Why Naive Bayes?
- Efficient for text classification
- Lightweight and fast
- Performs well on small datasets
- Easy integration with web applications

#### Sentiment Categories:
- Positive  
- Neutral  
- Negative  

The sentiment output is used for:
- AI chat responses
- Crisis detection
- Emotional trend understanding

---

## Data Visualization

- Stress scores are plotted over time using Chart.js
- Line charts resemble stock market trends
- Enables users to understand stress fluctuations visually

---

## Error Handling & Reliability

The system gracefully handles:
- Missing user profile records
- Incomplete form submissions
- Invalid or empty inputs
- Database mismatches
- Template rendering errors

Techniques used:
- Server-side validation
- Conditional rendering
- Defensive programming
- Django error tracing

---

## Security Measures

- Login required for sensitive pages
- CSRF protection enabled
- User-specific data access
- No exposure of ML model internals or sensitive data

---

## Advantages

- Cost-effective solution
- Real machine learning integration
- Ethical and responsible AI usage
- User-friendly and professional UI
- Scalable and maintainable architecture
- Suitable for academic and real-world demonstration

---

## Limitations

- Not a replacement for professional mental health treatment
- Uses classical machine learning (not deep learning)
- Stress assessment is based on self-reported data
- Requires internet access

---

