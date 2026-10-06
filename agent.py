import argparse
import os
import pathlib

from google import genai
from google.genai import types


SYSTEM = pathlib.Path(__file__).with_name(
    "system_prompt.md"
).read_text(encoding="utf-8")


def load_docs(folder):
    docs = []

    for p in sorted(pathlib.Path(folder).glob("*.md")):
        if p.name == "README.md":
            continue

        docs.append(
            f"\n===== {p.name} =====\n"
            f"{p.read_text(encoding='utf-8')}"
        )

    return "\n".join(docs)


def run(ticker, folder):
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise SystemExit("Set GEMINI_API_KEY first.")

    client = genai.Client(api_key=api_key)

    docs = load_docs(folder)

    user = f"""
Ticker: {ticker}

Assume today is 23 September 2026.

Produce the required research brief from the supplied documents.

DOCUMENTS:
{docs}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=user,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM,
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=True
            )
        )
    )

    return response.text


if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument("--ticker", default="SRVCABLE")
    ap.add_argument("--docs", default="research_pack")
    ap.add_argument("--out", default="brief.md")

    args = ap.parse_args()

    output = run(
        args.ticker,
        args.docs
    )

    pathlib.Path(args.out).write_text(
        output,
        encoding="utf-8"
    )

    print(output)