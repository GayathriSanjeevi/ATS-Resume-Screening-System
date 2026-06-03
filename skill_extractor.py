#skill_database=['Python','r','sql','machine learning','deep learning','nlp','tensorflow','pandas','numpy','aws','power bi','tableau','excel']

skill_database = [

# Programming Languages
"python", "java", "c++", "c", "r", "sql", "scala", "matlab",
"javascript", "typescript", "go", "rust",

# Python Libraries
"numpy", "pandas", "matplotlib", "seaborn", "plotly",
"scipy", "statsmodels", "scikit-learn", "nltk", "spacy",
"beautifulsoup", "requests", "flask", "streamlit",
"fastapi", "django", "pytorch", "tensorflow", "keras",
"xgboost", "lightgbm", "catboost",

# Machine Learning
"machine learning", "supervised learning",
"unsupervised learning", "reinforcement learning",
"classification", "regression", "clustering",
"feature engineering", "model evaluation",
"cross validation", "hyperparameter tuning",

# Deep Learning
"deep learning", "neural networks", "cnn", "rnn",
"lstm", "gru", "transformers", "bert", "gpt",
"transfer learning", "computer vision",

# NLP
"natural language processing", "nlp",
"text classification", "sentiment analysis",
"named entity recognition", "tokenization",
"lemmatization", "stemming",
"word embeddings", "bert", "gpt",

# Data Analytics
"data analysis", "data analytics",
"data cleaning", "data wrangling",
"exploratory data analysis", "eda",
"business analytics", "reporting",
"dashboarding", "data visualization",

# Statistics
"statistics", "hypothesis testing",
"probability", "a b testing",
"time series analysis",
"statistical modeling",
"bayesian statistics",

# Databases
"mysql", "postgresql", "sql server",
"mongodb", "oracle", "sqlite",
"snowflake", "redshift",

# Big Data
"hadoop", "spark", "pyspark",
"hive", "kafka", "databricks",

# Cloud
"aws", "azure", "google cloud",
"gcp", "s3", "ec2", "lambda",
"azure machine learning",
"vertex ai",

# BI Tools
"power bi", "tableau",
"excel", "power query",
"power pivot", "looker",

# Excel Skills
"vlookup", "xlookup",
"pivot tables", "macros",
"excel dashboards",

# MLOps
"mlops", "docker", "kubernetes",
"jenkins", "github actions",
"model deployment",

# Version Control
"git", "github", "gitlab",

# Deployment
"flask", "streamlit",
"fastapi", "rest api",

# AI Tools
"chatgpt", "langchain",
"llamaindex", "prompt engineering",
"retrieval augmented generation",
"rag", "vector databases",
"faiss", "pinecone",

# Data Engineering
"etl", "elt",
"data pipelines",
"airflow",
"data warehousing",

# Soft Skills
"communication",
"problem solving",
"critical thinking",
"teamwork",
"leadership",
"presentation skills"
]
def skill_extraction(resume,jd):
    resume_skills=[]
    jd_skills=[]
    for i in skill_database:
        if i in resume:
            resume_skills.append(i)
        if i in jd:
            jd_skills.append(i)

    matching_skills=[]
    missing_skills=[]
    for i in jd_skills:
        if i in resume_skills:
            matching_skills.append(i)
        else:
            missing_skills.append(i)

    return resume_skills,jd_skills, matching_skills,missing_skills

    