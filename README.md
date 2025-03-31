# Ice Breaker

A web application that crawls LinkedIn and X data about a person and customizes an ice breaker with them.

Project forked from https://github.com/emarco177/ice_breaker and is part of the LangChain course on Udemy:
https://www.udemy.com/course/langchain/.

---

## Initial setup

### 1. Install pipenv (Python virtual environment manager)
```bash
python3 -m pip install --user pipenv
```
This command installs pipenv, which is a tool that helps manage Python virtual environments. The `--user` flag installs the package for the current user, avoiding system-wide installation.

### 2. Create and activate a virtual environment
```bash
pipenv shell
```
This command creates a new Python virtual environment (if it doesn't exist) and activates it. Virtual environments help isolate project dependencies and prevent conflicts between different projects.

### 3. Install Langchain and related dependencies
```bash
pipenv install langchain
```
Installs the core Langchain library, which provides tools for building AI-powered applications with language models.

```bash
pipenv install langchain-openai
```
Adds OpenAI integration for Langchain, allowing you to use OpenAI's language models in your project.

```bash
pipenv install langchain-community
```
Installs community-contributed integrations and tools for Langchain, expanding its functionality.

```bash
pipenv install langchainhub
```
Adds access to the Langchain Hub, which provides pre-built prompts, chains, and other reusable components for AI development.

### 4. Install Black to format the code

```bash
pipenv install black
```

In Cursor, open the command palette and search for "Python: Select Interpreter" to select the virtual environment you created in step 2.

---

## Environment variables

To run this project, you will need to add the following environment variables to your .env file:

`OPENAI_API_KEY`

`SCRAPIN_API_KEY`

`TAVILY_API_KEY`

`TWITTER_API_KEY`

`TWITTER_API_SECRET`

`TWITTER_ACCESS_TOKEN`

`TWITTER_ACCESS_SECRET`

`LANGCHAIN_TRACING_V2`

`LANGCHAIN_API_KEY`

`LANGCHAIN_PROJECT` # Optional

---

## API services

> **Note**: This project uses paid API services:
> - [Scrapin.io](https://www.scrapin.io/?utm_campaign=influencer&utm_source=github&utm_medium=social&utm_content=edenmarco) for LinkedIn data scraping (20% discount available through this link, includes 20 free credits to start)
> - Twitter API (paid) for accessing Twitter data

> **Important note**: If you enable tracing by setting `LANGCHAIN_TRACING_V2=true`, you must have a valid LangSmith API key set in `LANGCHAIN_API_KEY`. Without a valid API key, the application will throw an error. If you don't need tracing, simply remove or comment out these environment variables.

---

## Run Locally

### 1. Go to the project directory
```bash
  cd langchain-ice-breaker
```

### 2. Install dependencies
```bash
  pipenv install
```

### 3. Start the flask server
```bash
  pipenv run app.py
```

### 4. Run tests
```bash
  pipenv run pytest .
```
