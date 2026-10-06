# Test Log — Three Iterations

## Run 1 — Baseline prompt
**Design:** Feed all eight documents to the model and ask for a one-page brief with Snapshot/Bull/Bear/Open Questions/Sources.

**What went wrong:** The model treated all sources too equally. It repeated the ₹1,428 crore revenue figure from the news article, gave too much weight to the stock-tips blog's bullish target, and risked mixing the Nagpur cable-TV operator with the listed cable manufacturer.

**Change:** Added explicit source hierarchy, ticker/company identity checks, and a rule that source text is evidence rather than instructions.

## Run 2 — Source hierarchy + entity checks
**Design:** Official exchange/company filings outrank news; ticker and legal company name must match before a document can support a claim.

**What improved:** The output used ₹1,248 crore as the primary Q1 revenue number, rejected the Nagpur cable-TV story, and stopped treating the ₹1,450 target as analyst consensus.

**Remaining issue:** The model still tended to hide contradictions instead of surfacing them.

**Change:** Added an explicit contradiction-detection requirement and a final quality checklist.

## Run 3 — Contradiction-aware agent
**Design:** Require claim-level source markers, explicit handling of conflicting numbers, and a final audit for prompt injection, entity mismatch, and unsupported recommendations.

**Result:** The final brief flags the ₹1,248 crore vs ₹1,428 crore revenue conflict, the historical pledge discrepancy, the unrelated Nagpur operator, and the promotional blog. It keeps the official filing as the primary source without silently deleting contradictory evidence.

**Main lesson:** For financial research, source ranking and entity resolution are more valuable than simply asking the LLM to “summarize everything.”
