# Super Investing — AI Research Agent

A small document-grounded AI agent that takes an NSE ticker plus a folder of retrieved research documents and produces a one-page retail-investor research brief.

## Design

- **LLM:** Google Gemini 3.5 Flash using the Google GenAI Python SDK.
- **Architecture:** Single-pass document-grounded research agent with a dedicated research system prompt.
- **Retrieval:** Local folder ingestion. The supplied research pack is small enough to fit directly into the model context.
- **Guardrails:** Source hierarchy, entity disambiguation, prompt-injection resistance, contradiction detection, claim-level citations, and no unsupported investment recommendation.

## Run
$env:GEMINI_API_KEY="your-key"
python agent.py --ticker SRVCABLE --docs research_pack --out brief.md
Install dependencies:

```bash
pip install -r requirements.txt