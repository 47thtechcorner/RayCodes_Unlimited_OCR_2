<div align="center">
  <a href="https://youtu.be/azd2H0Riid4">
    <img src="https://img.youtube.com/vi/azd2H0Riid4/0.jpg" alt="Baidu's New AI Beats Google at 300-Page OCR on 2GB GPU! (Unlimited OCR 2 Review)">
  </a>
  <h3>📺 <a href="https://youtu.be/azd2H0Riid4">Watch the full video walkthrough on YouTube</a></h3>
</div>

# Baidu Unlimited OCR 2: 3B MoE Ultra-Long Document Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Model Size: 3.34B](https://img.shields.io/badge/Model%20Size-3.34B%20MoE-purple.svg)](https://huggingface.co/baidu/Unlimited-OCR-2)
[![Active Params: 500M](https://img.shields.io/badge/Active%20Params-~500M%20Tokens-emerald.svg)](https://huggingface.co/baidu/Unlimited-OCR-2)
[![MarathonDocBench: 77.06](https://img.shields.io/badge/MarathonDocBench-77.06%20Score-coral.svg)](https://huggingface.co/datasets/baidu/MarathonDocBench)
[![KV Cache Peak: 1.77GB](https://img.shields.io/badge/Peak%20KV--Cache-1.77%20GB-brightgreen.svg)](https://huggingface.co/baidu/Unlimited-OCR-2)

> "Baidu Unlimited OCR 2 breaks the long-document KV-Cache bottleneck with Sparse Reference Sliding Window Attention (SR-SWA) and a 3.34B MoE architecture that activates only ~500M parameters per token, delivering 300-page single-shot OCR parsing with 7x faster decoding."

---

## 📊 Production Test Workflows

| Workflow | Capability Tested | Input Artifact | Expected Deliverable |
| :--- | :--- | :--- | :--- |
| **Legacy Technical Textbook Digitalizer** | Cross-page chapter hierarchy, algorithmic code blocks & geometric proofs | Complete 244-page computer science and algorithms textbook volume | Formatted Markdown textbook archive with syntax-highlighted code and LaTeX geometric formulations |
| **Enterprise Financial Auditor** | Multi-page quarterly earnings audit, statement of operations & margin extraction | Corporate quarterly financial filing and investor deck | Executive financial audit dashboard with revenue reconciliation and margin matrices |
| **Offline Academic Research Assistant** | Multi-column PDF parsing, inline citations, structured tables & reading order preservation | Dense peer-reviewed multi-page machine learning paper | Structured scientific research summary with tables, algorithmic formulas and paper synthesis |

---

## ⚡ Quick Start (Windows PowerShell)

### Step 1: Environment Setup & Weights Download
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install torch torchvision pillow transformers huggingface-hub tokenizers addict einops easydict pymupdf pypdf

hf download baidu/Unlimited-OCR-2 --local-dir models/unlimited-ocr-2
```

### Step 2: Run Production Pipeline
```powershell
python main.py
```

---

## 🛠️ Practical Use Cases

- 🛡️ **Long-Horizon Legal Discovery**: Ingest 300-page court filings, merger agreements, and multi-jurisdiction exhibits in a single request without context truncation or cloud token bills.
- 🔬 **Offline Scientific Knowledge Mining**: Parse entire repositories of arXiv, PubMed, and patent filings into structured markdown graphs with accurate mathematical notation.
- ⚡ **Automated Enterprise Financial Auditing**: Read dense multi-page balance sheets, cash flow tables, and footnote disclosures directly into machine-readable structures.
- 📚 **University Textbook Modernization**: Digitalize physical calculus, physics, and engineering manuals with intact equation typesetting and nested diagram hierarchies.

---

## 🗺️ Future Feature Roadmap

- 🚀 **vLLM & SGLang High-Throughput Serving Adapter**: Zero-copy continuous batching server integration for enterprise document queues.
- 🔍 **Interactive Web Layout Inspector**: Visual bounding-box validation canvas for verifying multi-column bounding boxes side-by-side.
- 🧠 **Multi-Document Cross-Referencing Engine**: Global reference graph linking formulas and figures across hundreds of separate PDFs.
- 📦 **4-bit GGUF & ONNX Runtime Quantization**: Sub-4GB consumer laptop execution for zero-GPU ultra-portable laptops.

---

## 🏷️ Search & Discovery Keywords
unlimited ocr 2, baidu ocr, baidu unlimited ocr, unlimited ocr, unlimited-ocr-2, deepseek ocr, multi page ocr, local ocr model, local document ai, paddleocr alternative, mineru alternative, gemini flash ocr, qwen ocr alternative, kv cache compression, low memory ocr, pdf to markdown, local pdf parser, document extraction ai, table extraction ai, omnidocbench, offline pdf parser, Unlimited OCR 2, Unlimited-OCR-2, Baidu OCR, Baidu Unlimited OCR, Unlimited OCR, Baidu AI
