# generative-ai-learning-lab

End-to-end Generative AI learning and experimentation hub featuring LLM applications, RAG pipelines, prompt engineering, vector search, fine-tuning, and production-ready AI solutions.

## Repository Structure

```text
generative-ai-learning-lab/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── environment.yml
├── pyproject.toml
│
├── docs/
│   ├── fundamentals/
│   ├── llms/
│   ├── rag/
│   ├── fine-tuning/
│   └── vector-databases/
│
├── notebooks/
│   ├── 01_prompt_engineering.ipynb
│   ├── 02_embeddings.ipynb
│   ├── 03_rag_pipeline.ipynb
│   └── 04_agents.ipynb
│
├── projects/
│   ├── rag-document-qa/
│   │   ├── README.md
│   │   ├── app/
│   │   ├── data/
│   │   ├── config/
│   │   └── requirements.txt
│   ├── chat-with-pdf/
│   ├── ai-code-assistant/
│   ├── multi-agent-system/
│   └── genai-data-pipeline/
│
├── src/
│   ├── prompts/
│   ├── chains/
│   ├── rag/
│   ├── agents/
│   ├── embeddings/
│   └── utils/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── ingest_data.py
│   ├── build_index.py
│   └── evaluate_model.py
│
├── configs/
│   ├── model_config.yaml
│   ├── rag_config.yaml
│   └── pipeline_config.yaml
│
├── tests/
│   ├── test_rag.py
│   ├── test_prompts.py
│   └── test_utils.py
│
└── deployment/
    ├── docker/
    │   └── Dockerfile
    ├── k8s/
    └── api/
        └── fastapi_app.py
```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Notes

This repository is scaffolded for iterative learning and project expansion. Add your implementation files progressively under `src/` and `projects/`.
