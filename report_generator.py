# report_generator.py
from datetime import date
from pathlib import Path

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def save_report(content: str) -> dict:
    """Zapisuje raport jako .md i opcjonalnie konwertuje do .pdf"""
    today = date.today().isoformat()
    md_path = OUTPUT_DIR / f"report_{today}.md"
    md_path.write_text(content, encoding="utf-8")
    print(f"   📄 Raport zapisany: {md_path}")

    # Opcjonalnie: konwersja do PDF przez markdown + weasyprint
    try:
        import markdown
        from weasyprint import HTML
        html_content = markdown.markdown(content)
        pdf_path = OUTPUT_DIR / f"report_{today}.pdf"
        HTML(string=html_content).write_pdf(str(pdf_path))
        print(f"   📕 PDF zapisany: {pdf_path}")
        return {"status": "ok", "md": str(md_path), "pdf": str(pdf_path)}
    except ImportError:
        # weasyprint opcjonalny
        return {"status": "ok", "md": str(md_path)}