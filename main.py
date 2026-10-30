import os
import sys
import time
from pathlib import Path
import torch
from transformers import AutoModel, AutoTokenizer

LOCAL_MODEL_DIR = Path("models/unlimited-ocr-2")
DEFAULT_MODEL = str(LOCAL_MODEL_DIR) if LOCAL_MODEL_DIR.exists() else "baidu/Unlimited-OCR-2"
MODEL_PATH = os.environ.get("UNLIMITED_OCR_MODEL_PATH", DEFAULT_MODEL)
INPUTS_DIR = Path("inputs")
OUTPUTS_DIR = Path("outputs")
ASSETS_DIR = Path("assets")
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)


def load_model_and_tokenizer(model_name: str = MODEL_PATH):
    """Load Baidu Unlimited OCR 2 model and tokenizer natively using Transformers."""
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32
    
    model = AutoModel.from_pretrained(
        model_name,
        trust_remote_code=True,
        use_safetensors=True,
        torch_dtype=dtype,
        device_map="auto" if torch.cuda.is_available() else None,
    ).eval()
    return tokenizer, model


def run_task1_textbook_digitalizer(tokenizer, model):
    """Convert technical textbook into Markdown with code blocks and LaTeX math."""
    textbook_pdf = INPUTS_DIR / "technical_textbook.pdf"
    if not textbook_pdf.exists():
        return

    output_file = OUTPUTS_DIR / "textbook_digitalized.md"
    start_time = time.time()
    
    task_prompt = (
        "<image>Digitalize this textbook page. Convert text to clean Markdown, "
        "format Python code inside code blocks, and convert formulas into standard LaTeX."
    )
    
    parsed_text = model.infer(
        tokenizer,
        prompt=task_prompt,
        image_file=str(textbook_pdf),
        output_path=str(OUTPUTS_DIR / "t1_cache"),
        save_results=False
    )
    elapsed = time.time() - start_time
    
    report_content = f"""# Technical Textbook Digitalization Archive

- **Source Document**: `{textbook_pdf.name}` (*Think Python*)
- **Parser Engine**: Baidu Unlimited OCR 2
- **Processing Time**: `{elapsed:.2f}s`

---

## 📖 Extracted Chapter Content

{parsed_text}
"""
    output_file.write_text(report_content, encoding="utf-8")


def run_task2_financial_auditor(tokenizer, model):
    """Extract financial statements and tables from quarterly earnings reports."""
    fin_pdf = INPUTS_DIR / "annual_financial_report.pdf"
    if not fin_pdf.exists():
        return

    output_file = OUTPUTS_DIR / "financial_audit_dashboard.html"
    start_time = time.time()
    
    task_prompt = (
        "<image>Extract the financial statements. Reconstruct the revenue and balance sheet "
        "tables into clean Markdown, preserving numbers, column names, and totals."
    )
    
    parsed_text = model.infer(
        tokenizer,
        prompt=task_prompt,
        image_file=str(fin_pdf),
        output_path=str(OUTPUTS_DIR / "t2_cache"),
        save_results=False
    )
    elapsed = time.time() - start_time
    
    # Load separate HTML visualizer template
    template_path = ASSETS_DIR / "financial_dashboard_template.html"
    if template_path.exists():
        html = template_path.read_text(encoding="utf-8")
        html = html.replace("{{filename}}", fin_pdf.name)
        html = html.replace("{{elapsed}}", f"{elapsed:.2f}")
        html = html.replace("{{content}}", parsed_text)
    else:
        html = f"<html><body><h1>Financial Extract</h1><pre>{parsed_text}</pre></body></html>"
        
    output_file.write_text(html, encoding="utf-8")


def run_task3_research_assistant(tokenizer, model):
    """Parse two-column academic paper, preserving reading order, formulas, and tables."""
    paper_pdf = INPUTS_DIR / "attention_paper.pdf"
    if not paper_pdf.exists():
        return

    output_file = OUTPUTS_DIR / "research_paper_digest.md"
    start_time = time.time()
    
    task_prompt = (
        "<image>Parse this academic paper. Read the two columns in natural order, "
        "convert formulas into LaTeX blocks, and extract benchmark tables intact."
    )
    
    parsed_text = model.infer(
        tokenizer,
        prompt=task_prompt,
        image_file=str(paper_pdf),
        output_path=str(OUTPUTS_DIR / "t3_cache"),
        save_results=False
    )
    elapsed = time.time() - start_time
    
    digest_content = f"""# Academic Research Paper Digest

- **Source Document**: `{paper_pdf.name}` (*Attention Is All You Need*)
- **Evaluation Engine**: Baidu Unlimited OCR 2
- **Processing Time**: `{elapsed:.2f}s`

---

## 📑 Extracted Paper Content & Formulas

{parsed_text}
"""
    output_file.write_text(digest_content, encoding="utf-8")


def main():
    tokenizer, model = load_model_and_tokenizer()
    
    run_task1_textbook_digitalizer(tokenizer, model)
    run_task2_financial_auditor(tokenizer, model)
    run_task3_research_assistant(tokenizer, model)


if __name__ == "__main__":
    main()
