# AI Internship Matching RAG  
# 实习岗位匹配与项目证据检索工具

This is a small privacy-aware RAG-style project for matching internship job descriptions with anonymized resume content and public GitHub project evidence.

我做这个项目的出发点很实际：投实习的时候，经常会遇到一个问题——一个岗位 JD 看起来好像能投，但我的简历和项目经历到底能不能支撑这些要求？哪些能力可以放心写，哪些其实还没有足够证据？

所以这个项目不是想做一个“万能职业规划 AI”，而是做一个更具体的小工具：

> 输入一份实习岗位 JD，系统从脱敏简历摘要和 GitHub 项目材料里检索证据，然后告诉我：哪些技能有支撑，哪些技能还比较薄弱。

当前版本不会训练模型，也不会微调大模型，更不会把真实简历上传或写进公开仓库。它只是一个本地运行的检索与匹配原型。

---

## Why this project

在修改简历或者准备投递时，最容易出现两种情况：

第一种是低估自己。  
明明做过相关项目，但没有把项目和 JD 要求对应起来，简历上写得很弱。

第二种是高估自己。  
看到 JD 里写了 RAG、LLM、automation、SQL、machine learning，就想往简历里补，但实际上项目证据并不充分。

所以我希望这个工具能起到一个“刹车”和“提醒”的作用：

```text
No evidence, no claim.
没有证据，就不要乱写。
```

它不会帮用户编经历，而是尽量基于已有材料判断：  
哪些内容可以写进简历，哪些内容应该谨慎，哪些内容需要后续补项目。

---

## What it does

Given an internship job description, the app will:

- extract skill keywords from the JD;
- search relevant evidence from anonymized resume and project summaries;
- show which skills are supported by evidence;
- mark missing or weakly supported skills;
- generate a simple Markdown match report.

中文来说，就是：

```text
岗位 JD → 技能要求 → 检索个人项目证据 → 判断匹配度 → 输出报告
```

当前系统会读取这些材料：

- anonymized resume summary；
- public GitHub project summaries；
- this RAG project summary；
- sample job descriptions for testing.

真实简历、联系方式、私人投递记录不会放进公开仓库。

---

## Current status

Current version: `v0.2 MVP`

目前已经跑通的功能：

- Streamlit local app；
- JD input；
- Markdown document loading；
- text chunking；
- regex-based skill extraction；
- TF-IDF retrieval；
- cosine similarity ranking；
- skill coverage calculation；
- structured match report generation；
- privacy-aware project structure；
- retrieval leakage fix；
- false positive fix for `R` skill detection。

比较重要的一点是：  
**JD 只作为 query，不会被放进 evidence corpus。**

早期版本里，系统会把 sample JD 自己也检索出来，导致 similarity score 直接变成 1.0000，技能覆盖率虚高。现在已经修掉了这个问题。

---

## What it does not do yet

This project is still an MVP. It does not currently include:

- LLM-based generation；
- OpenAI / Claude API calls；
- fine-tuning；
- dense embedding retrieval；
- FAISS or Chroma；
- PDF resume parsing；
- cloud deployment；
- automated job application.

所以它目前更准确的定位是：

```text
RAG-style retrieval MVP
```

而不是：

```text
full LLM career assistant
```

比如当前测试里，如果 JD 要求 `LLM`，系统会把它标记为 missing or weakly supported，因为当前项目还没有真正接入 LLM 模块。这是有意保留的边界，不想为了好看而乱写。

---

## Example output

A sample AI internship JD may contain skills such as:

```text
automation
data analysis
documentation
llm
machine learning
prompt engineering
python
rag
report
```

The app may return:

```text
Covered Skills:
- automation
- data analysis
- documentation
- machine learning
- prompt engineering
- python
- rag
- report

Missing or Weakly Supported Skills:
- llm
```

This means the current evidence base supports RAG-style retrieval, Python, reporting, and automated match report generation, but does not yet support a real LLM module.

---

## Project structure

```text
ai-internship-matching-rag/
├── README.md
├── requirements.txt
├── .gitignore
├── app/
│   └── streamlit_app.py
├── src/
│   ├── document_loader.py
│   ├── anonymizer.py
│   ├── chunker.py
│   ├── jd_parser.py
│   ├── retriever.py
│   ├── scoring.py
│   └── report_generator.py
├── public_docs/
│   ├── sample_resume_anonymized.md
│   ├── sample_job_descriptions/
│   └── github_project_summaries/
├── private_data/
├── vector_store/
├── outputs/
└── docs/
    ├── methodology.md
    ├── privacy_design.md
    └── limitations.md
```

---

## How it works

### 1. Evidence corpus

The app only searches evidence documents, such as:

- anonymized resume summary;
- GitHub project summaries;
- this project’s own evidence summary.

The job description itself is excluded from the evidence corpus.

```text
JD = query
Resume / projects = evidence
```

This prevents the system from treating the JD as proof of the user’s ability.

---

### 2. Chunking

Documents are split into smaller chunks before retrieval.

This makes the retrieved evidence more specific. Instead of returning an entire resume or project description, the system can return a smaller section that is more directly related to the JD.

---

### 3. Skill extraction

The app uses regex-based skill extraction.

I first used simple substring matching, but that created false positives. For example, the skill `R` could be incorrectly detected inside words like `reports` or `requirements`.

The current version only detects `R` when the JD explicitly mentions something like:

```text
R
R language
R programming
```

This is a small fix, but it makes the report much more reliable.

---

### 4. Retrieval

The current retrieval method is:

```text
TF-IDF + cosine similarity
```

This is not the most advanced retrieval method, but it is transparent and easy to debug.

For this stage, I prefer a simple method that I can explain clearly rather than a more complex pipeline that looks impressive but is hard to inspect.

---

### 5. Report generation

The report includes:

- detected skills;
- covered skills;
- missing or weakly supported skills;
- retrieved evidence chunks;
- similarity scores;
- resume-safety notes.

The current report generator is rule-based. It does not call an LLM.

---

## Privacy design

Privacy is one of the main design constraints of this project.

The public repository should not contain:

- real phone number;
- email address;
- WeChat ID;
- full real resume;
- private application notes;
- real application records;
- enterprise internal data;
- unauthorized research data;
- sensitive personal files.

The folder design is:

```text
public_docs/
```

For anonymized samples and public project summaries.

```text
private_data/
```

For local private files only. This folder is ignored by git.

```text
vector_store/
```

For local indexes or embeddings. This folder is also ignored by git.

Even embeddings may still contain recoverable semantic information, so they should not be committed to GitHub.

---

## Current evidence documents

The current public evidence corpus includes:

- anonymized resume summary;
- Beijing PM2.5 forecasting project;
- earthquake-tsunami logistic regression project;
- diabetes classification ML project;
- AI internship matching RAG project.

These documents are stored under:

```text
public_docs/
```

They are used only as demo evidence for the local retrieval pipeline.

---

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app/streamlit_app.py
```

Open in browser:

```text
http://localhost:8501
```

---

## Tech stack

- Python
- Streamlit
- scikit-learn
- TF-IDF
- cosine similarity
- regex
- Markdown documents

---

## Limitations

This project is still simple.

Main limitations:

- TF-IDF may miss semantically related evidence if the wording is different;
- skill extraction depends on predefined regex patterns;
- the report generator is not LLM-based yet;
- the app does not parse PDF or DOCX resumes;
- the app does not verify whether each GitHub project is fully reproducible;
- no retrieval evaluation dataset has been added yet;
- no deployment has been done.

These limitations are intentional at this stage. The priority is to make a small, safe, explainable MVP first.

---

## Future improvements

Next steps I want to add:

1. sentence-transformers embedding retrieval;
2. FAISS or Chroma local vector search;
3. retrieval evaluation with manually labeled JD-project pairs;
4. better skill extraction rules;
5. optional LLM-based report generation;
6. stricter anonymization before any LLM call;
7. Markdown / PDF export;
8. simple unit tests;
9. better Streamlit UI.

I will not add LLM generation until the privacy boundary is clear.

---

## What I learned

This project helped me practice:

- structuring a small AI application;
- separating public demo data from private data;
- building a simple retrieval pipeline;
- avoiding retrieval leakage;
- reducing false positive skill matching;
- generating evidence-grounded reports;
- documenting what the project can and cannot do.

The main value of this project is not that the model is complicated.  
The value is that it turns a real job-search problem into a working, privacy-aware retrieval prototype.

---

## License

This project is for educational and portfolio demonstration purposes.

Before using real personal materials, users should check privacy risks and make sure private files are not committed to public repositories.