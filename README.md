# Interactive Twitter Sentiment Dashboard

An interactive Python dashboard that collects recent tweets from Twitter, performs sentiment analysis, summarizes them with AI, and visualizes trends. Keywords and tweet limits are configurable for flexibility.

---

## Features

- **Real-time tweet collection** using Tweepy  
- **Text preprocessing** to clean tweets  
- **Sentiment analysis** with VADER Sentiment  
- **AI-based summarization** using Facebook BART model  
- **Visualizations** of sentiment trends  
- **Configurable keywords & tweet limits**  
- **Word clouds & hashtag frequency charts**  
- **Email alerts** for sentiment thresholds *(optional)*  

---

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/Sumayya-Samreen/Interactive-Twitter-Sentiment-Dashboard.git
    cd Interactive-Twitter-Sentiment-Dashboard
    ```

2. **Create and configure `.env`**
    Copy the template:
    ```bash
    cp .env.template .env
    ```
    Then edit `.env` to add your credentials and preferences.

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download required NLTK data**
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('vader_lexicon')
    ```

---

## Usage

Run the dashboard:
```bash
python main.py
```

The dashboard will:
- Search tweets for each keyword
- Clean and preprocess the tweets
- Compute sentiment scores
- Generate AI summaries
- Display sentiment trend plots

---

## Project Structure

```
twitter_sentiment/
│── main.py
│── preprocess.py
│── sentiment.py
│── summarizer.py
│── twitter_search.py
│── visualize.py
│── advanced_features.py
│── config.py
│── requirements.txt
│── .env.template
│── README.md
```

---

## `.env.template`

Create your `.env` file based on this template:

```
BEARER_TOKEN=YOUR_TWITTER_BEARER_TOKEN
TRACK_KEYWORDS=#AI,#MachineLearning,Python
MAX_TWEETS=50

# OPTIONAL — Email settings (only if using email alerts)
# EMAIL_USER=your_email@example.com
# EMAIL_PASSWORD=your_email_password
# SMTP_SERVER=smtp.example.com
# SMTP_PORT=587
```

---

## Notes

- Requires a Twitter Developer account for the **Bearer Token**.  
- Free tier accounts have rate limits; the script handles rate limiting automatically.  
- **Due to monthly API usage caps on Twitter’s free tier, this project currently uses mock tweets for demonstration once the limit is reached.**  
- To use **real tweets without mock data**, upgrade to a Twitter Developer paid tier or ensure you have enough monthly API allowance.  
- Then in the file `twitter_search.py`, adjust the `USE_MOCK_DATA` flag to `False`:  
  ```python
  USE_MOCK_DATA = False
  ```
- `.env` is ignored via `.gitignore` for security.

---

## How to Deploy

You can deploy this Interactive Twitter Sentiment Dashboard locally or on a cloud service like Heroku or Streamlit Cloud.

### Local Deployment
1. Clone the repository:
    ```bash
    git clone https://github.com/Sumayya-Samreen/Interactive-Twitter-Sentiment-Dashboard.git
    cd Interactive-Twitter-Sentiment-Dashboard
    ```
2. Set up your virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Mac/Linux
    .\.venv\Scripts\activate   # Windows
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Create and configure `.env` from `.env.template`:
    ```bash
    cp .env.template .env
    ```
    Then add your credentials and preferences.
5. Run:
    ```bash
    python main.py
    ```

### Cloud Deployment (Streamlit Cloud Example)
1. Push your repository to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and log in.
3. Connect your GitHub repo.
4. Set environment variables (BEARER_TOKEN, TRACK_KEYWORDS, MAX_TWEETS) in the Streamlit Cloud dashboard.
5. Deploy your app.

---

## Pro Tip for Recruiters / Collaborators
This project demonstrates a complete natural language processing (NLP) and AI pipeline, from real-time data collection and preprocessing to sentiment analysis, AI-based summarization, and interactive visualization. It highlights expertise in API integration, text analytics, machine learning, data visualization, and end-to-end workflow implementation, making it a strong portfolio example for roles in AI engineering, data science, and NLP application development.

---

## Author
**Sumayya Samreen — M.Sc. in Artificial Intelligence**<br>
Focused on developing practical AI solutions for real-time data analysis, natural language understanding, and interactive data visualization.

