# TODO — Stock Sentiment Poller

## 🧩 Missing Features

- [ ] Add Reddit/Twitter/Stocktwits integration
- [ ] Add news source diversity (RSS, Google News API, etc.)
- [ ] Integrate LLMs for sentiment scoring (e.g., OpenAI, Claude)
- [ ] Add emotion tagging (fear, greed, uncertainty)

## 🛠️ Infrastructure Enhancements

- [ ] Add DLQ handling and retry support
- [ ] Refactor to support time-window-based aggregation
- [ ] Standardize sentiment schema output
- [ ] Enable configurable polling windows

## 📈 Monitoring & Logging

- [ ] Integrate Prometheus metrics (poll duration, source error rates)
- [ ] Add JSON log formatting with source+sentiment summary

## ✅ Security & Compliance

- [ ] Run Bandit + Safety
- [ ] Generate SBOM and enable Cosign signing
- [ ] Validate licenses with REUSE and license-checker
- [ ] Enable Semgrep for code-level security scanning

## 🧪 Testing & CI

- [ ] Add unit tests for all pollers
- [ ] Add test fixtures for source mock data
- [ ] Enforce pre-commit and CI parity

## 🧹 Code Hygiene

- [ ] Clean legacy comments and unused imports
- [ ] Ensure full type safety (`pyright`, `mypy`)
- [ ] Verify all docstrings with `pyment` or similar

## 🪄 Optional Enhancements

- [ ] Enable sentiment stream summarization every N minutes
- [ ] Build REST interface for sentiment snapshot access
