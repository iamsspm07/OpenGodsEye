# 🧠 GodsEye OSINT

AI-powered Open Source Intelligence (OSINT) platform for discovering, analyzing, and visualizing digital footprints across social, developer, professional, and content platforms.

GodsEye helps researchers, recruiters, cybersecurity professionals, and individuals understand publicly available online presence using AI-powered identity matching and digital footprint analysis.

---

## 🚀 Features

### 🔍 Multi-Platform Discovery

Discover publicly available profiles from:

- GitHub
- Kaggle
- LinkedIn
- Medium
- Dev.to
- Reddit
- Stack Overflow
- YouTube
- Instagram
- Twitter/X
- ResearchGate
- Personal Websites
- Blogs and Forums

---

### 🧠 AI Identity Resolution

Uses advanced NLP and similarity matching techniques:

- Sentence Transformers
- Cosine Similarity
- RapidFuzz Matching
- Semantic Search

to identify profiles likely belonging to the same individual.

---

### 📊 Digital Presence Analytics

Analyze:

- Developer Activity
- Social Activity
- Content Creation
- Community Participation
- Professional Presence
- Media Presence

---

### 🛡 Risk Assessment

Identify:

- Low Confidence Matches
- Duplicate Profiles
- Suspicious Accounts
- Incomplete Digital Presence

---

### 📈 Interactive Dashboard

Built with Streamlit:

- Real-Time Analysis
- Profile Categorization
- Digital Presence Metrics
- Behavioral Insights
- Summary Reports

---

## 🏗 Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
Search Engine
 │
 ▼
Identity Resolution
 │
 ▼
Platform Classification
 │
 ▼
Metrics Engine
 │
 ▼
Behavior Analysis
 │
 ▼
Summary Generation
```

---

## 🛠 Tech Stack

### Frontend

- Streamlit

### Artificial Intelligence

- Sentence Transformers
- RapidFuzz
- Scikit-Learn

### Data Processing

- Pandas
- NumPy

### Search & OSINT

- SearXNG
- BeautifulSoup
- Trafilatura

### Reporting

- python-docx
- python-pptx
- ReportLab

---

## 📂 Project Structure

```text
godseye-osint/

├── streamlit_app.py
├── requirements.txt
├── README.md
│
├── services/
│   ├── search_service.py
│   ├── identity_service.py
│   ├── parser_service.py
│   ├── metrics_service.py
│   ├── summary_service.py
│   ├── platform_registry.py
│   └── utils.py
│
├── assets/
│
└── reports/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/GodsEye-OSINT.git

cd GodsEye-OSINT
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

```bash
streamlit run streamlit_app.py
```

Application will start on:

```text
http://localhost:8501
```

---

## 📊 Example Workflow

1. Enter a person's name.
2. Search across public platforms.
3. Match profiles using AI.
4. Categorize discovered profiles.
5. Generate confidence scores.
6. Analyze digital behavior.
7. Produce a summarized report.

---

## 🎯 Use Cases

### Recruiters

Discover candidate portfolios and professional presence.

### Researchers

Perform open-source intelligence research.

### Developers

Analyze technical community participation.

### Cybersecurity Teams

Conduct ethical OSINT investigations.

### Personal Branding

Monitor and evaluate online presence.

---

## 🔒 Privacy & Ethics

GodsEye only processes publicly available information.

Users are responsible for complying with:

- Privacy Laws
- Platform Terms of Service
- Ethical OSINT Practices
- Local Regulations

This project is intended solely for educational, research, and legitimate intelligence-gathering purposes.

---

## 🌟 Future Roadmap

- AI-Powered Profile Summarization
- Local LLM Integration (Ollama)
- PDF Report Generation
- PPT Report Generation
- Advanced Risk Scoring
- Multi-Language Support
- Face Matching (Optional)
- Knowledge Graph Visualization
- Timeline-Based Activity Analysis
- PostgreSQL Integration

---

## 🤝 Contributing

Contributions are welcome.

### Steps

1. Fork the Repository
2. Create a Feature Branch

```bash
git checkout -b feature/new-feature
```

3. Commit Changes

```bash
git commit -m "Add new feature"
```

4. Push Changes

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

## 📜 License

MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to deal in the Software without restriction.

---

## ⭐ Support

If you find this project useful:

- Star the repository
- Fork the project
- Share with the community
- Contribute improvements

---

## 👨‍💻 Author

**Sujit Shibaprasad Maity**

Data Scientist | Machine Learning Engineer | AI Developer

---

## 🏷 Tags

```text
osint
digital-footprint
streamlit
python
machine-learning
artificial-intelligence
nlp
sentence-transformers
cybersecurity
identity-resolution
open-source-intelligence
web-scraping
data-science
github
kaggle
linkedin
analytics
```
