# GenAI-RAG-Evaluator

## Overview

**GenAI-RAG-Evaluator** is a production-grade Retrieval-Augmented Generation (RAG) system designed to evaluate and optimize document-based question-answering pipelines. Built on industry-standard frameworks including LangChain, ChromaDB, and OpenAI APIs, this system provides end-to-end capabilities for ingesting documents, generating contextually relevant responses, and systematically evaluating output quality.

## About This Project

### Project Goals
- **Enable organizations** to build trustworthy AI-powered document Q&A systems
- **Measure and optimize** RAG pipeline performance through quantifiable metrics
- **Reduce hallucinations** and improve response accuracy with evidence-based evaluation
- **Accelerate development cycles** with automated quality assurance workflows

### Use Cases
- **Enterprise Knowledge Management** - Query internal documentation, policies, and procedures
- **Customer Support Automation** - Intelligent FAQ systems with measurable accuracy
- **Legal & Compliance** - Document review and regulatory question answering
- **Research & Academia** - Academic paper analysis and citation tracking
- **Financial Services** - Regulatory documentation and policy interpretation

### Target Audience
- **Data Scientists & ML Engineers** - Building and evaluating LLM applications
- **Software Development Teams** - Integrating RAG systems into production applications
- **Enterprise Organizations** - Implementing AI-driven information retrieval solutions
- **AI Researchers** - Benchmarking RAG performance and evaluation methodologies

### Key Benefits
- **Measurable Quality** - Quantify response accuracy and relevance before deployment
- **Production-Ready** - Scalable architecture suitable for enterprise environments
- **Easy Integration** - Clean APIs and modular design for seamless implementation
- **Transparency** - Understand model decisions through detailed evaluation reports
- **Cost Optimization** - Reduce model API calls through effective retrieval strategies

### Project Status
- **Current Version:** 1.0.0
- **Status:** Active Development
- **Last Updated:** September 2026

## Key Capabilities

### Document Processing
- Intelligent document ingestion with automatic chunking and preprocessing
- Vector embedding generation via ChromaDB for semantic search optimization
- Support for multiple document formats (PDF, text)

### Retrieval-Augmented Generation
- Advanced RAG pipeline powered by GPT-4o with optimized prompt engineering
- Context-aware response generation with configurable retrieval strategies
- Seamless integration with LangChain's composable architecture

### Quality Evaluation
- Automated evaluation framework using RAGAS metrics
- Assessment dimensions: Faithfulness, Answer Relevancy, and Context Precision
- Quantifiable performance benchmarking for continuous improvement

### User Interface
- Interactive Streamlit-based application for end-users
- Real-time performance monitoring and metrics visualization
- Intuitive query interface with result transparency

## Installation

### Prerequisites
- Python 3.12 or higher
- Virtual environment manager (venv recommended)
- OpenAI API key

### Setup Instructions

1. **Clone and navigate to the repository:**
   ```bash
   git clone repository
   cd GenAI-RAG-Evaluator
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your OpenAI API key
   ```

## Usage

### Running the Application

**Start the Streamlit interface:**
```bash
streamlit run app.py
```

The application will launch at `http://localhost:8501`

### Core Modules

- **`src/ingest.py`** - Document ingestion and preprocessing
- **`src/generator.py`** - RAG pipeline and response generation
- **`src/retriever.py`** - Vector database retrieval logic
- **`src/evaluate.py`** - RAGAS evaluation framework integration

## Architecture

```
GenAI-RAG-Evaluator/
├── app.py                 # Streamlit application entry point
├── src/
│   ├── ingest.py         # Document processing pipeline
│   ├── generator.py      # RAG generation engine
│   ├── retriever.py      # Semantic search retrieval
│   └── evaluate.py       # Evaluation metrics framework
├── data/                 # Document storage directory
├── requirements.txt      # Python dependencies
└── Dockerfile           # Container deployment configuration
```

## Requirements

See [requirements.txt](requirements.txt) for complete dependency list. Key packages include:

- **LangChain** (≥0.2.0) - Orchestration framework
- **ChromaDB** (≥0.5.0) - Vector database
- **RAGAS** (≥0.1.0) - Evaluation metrics
- **OpenAI** - Language model APIs
- **Streamlit** (≥1.35.0) - User interface framework

## Configuration

Environment variables (configure in `.env`):

```
OPENAI_API_KEY=api_key_here
```

## Deployment

### Docker

Build and run the application in a container:

```bash
docker build -t genai-rag-evaluator .
docker run -p 8501:8501 --env-file .env genai-rag-evaluator
```

## Contributing

Contributions are welcome. Please follow standard Git workflow:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit changes with clear messages
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues, questions, or feedback, please open an issue on the GitHub repository.

---

**Last Updated:** September 2026
