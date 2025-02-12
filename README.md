🕸️ AI Web Scraper  
An intelligent web scraper built using **Selenium, BeautifulSoup, and LangChain's Ollama**.  
It automates data extraction from websites, cleans the content, and provides **AI-powered information parsing**.


🚀 Features
✔ **Automated Web Scraping** – Extracts text from any webpage  
✔ **AI-Powered Parsing** – Uses LangChain + Ollama for extracting specific information  
✔ **Data Cleaning** – Removes unnecessary HTML elements (scripts, styles, etc.)  
✔ **Streamlit UI** – User-friendly interface for easy interaction  
✔ **Chunk Processing** – Splits large text into smaller parts for better AI analysis  

## 🔧 Installation
Follow these steps to set up and run the AI Web Scraper on your system.

### 1️⃣ Clone the Repository
First, download the project files by cloning the GitHub repository:
```bash
git clone https://github.com/imrishi007/ai-web-scraper.git
cd ai-web-scraper
```

### 2️⃣ Install Dependencies
Make sure you have Python 3.x installed. Then, install all required libraries:

```bash
pip install -r requirements.txt
```

If requirements.txt is missing, manually install the dependencies :
```bash
pip install selenium beautifulsoup4 streamlit langchain_ollama ollama
```

### 3️⃣ Download and Set Up ChromeDriver  
To use **Selenium** for web scraping, you need **ChromeDriver** that matches your **Google Chrome version**. Follow these steps:  

### 4️⃣ Download ChromeDriver  
Visit the official ChromeDriver download page:  
👉 [ChromeDriver Downloads](https://googlechromelabs.github.io/chrome-for-testing/#stable)  

Select the version that **matches your Chrome version** and download the correct ChromeDriver for your operating system:  

- **Windows (64-bit)** → `chromedriver-win64.zip`  
- **Mac (Intel or Apple Silicon)** → `chromedriver-mac-x64.zip`  
- **Linux** → `chromedriver-linux64.zip`  

### 5️⃣ Extract and Replace ChromeDriver  
1️⃣ **Extract the `.zip` file** you downloaded.  
2️⃣ You will get a file named **`chromedriver.exe`**.  
3️⃣ **Replace** the existing `chromedriver.exe` in your project folder with the one you downloaded.  

> 🛑 **Windows 64-bit users can skip this step** because the correct version is already included.  

### 6️⃣ Install and Set Up Ollama  
This project uses **LangChain + Ollama** for AI-powered text extraction. You need to **install Ollama** to run it locally.

### 1️⃣ Install Ollama  
🔹 **Windows & Mac Users:** Download Ollama from the official site:  
👉 [Ollama Download](https://ollama.com/download)  

🔹 **Linux Users:** Run the following command:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

-> Now refer to the models on their github through this link - [Ollama Github](https://github.com/ollama/ollama?tab=readme-ov-file#model-library) 
-> Choose the model according to your need... I will be using the model **llama3.1**

To install the model run the following command - 
```bash
ollama pull ollama run llama3.1
```
This command will install the llama 3.1 on your desktop which will perform the AI operations locally...

## 🛠 How to Use the AI Web Scraper  
Follow these steps to **scrape and extract information** from any website.

### 1️⃣ Run the Web Scraper  
Launch the **Streamlit** interface by running the following command in your terminal:
```bash
streamlit run main.py
```

### 2️⃣ Enter the Website URL
1️⃣ Once the web app opens, enter the URL of the website you want to scrape.

2️⃣ Click **"Scrape Site"** to extract the content.

### 3️⃣ View & Clean Extracted Content
-> The extracted content will be displayed in the "View Content" section.

-> The scraper removes unnecessary scripts and styles, keeping only clean text.

4️⃣ Use AI to Extract Specific Information
1️⃣ Enter a query in "What do you want to parse?" (e.g., "Extract company names", "Find product details").

2️⃣ Click "Parse Content", and the AI will process the text to return relevant details.

### 5️⃣ Get AI-Powered Results
-> The AI (using LangChain & Ollama) will analyze the text and extract the exact information you requested.

-> The results will be displayed in the Streamlit app.