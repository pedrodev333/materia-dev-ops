from docx import Document

doc = Document("template.docx")

for p in doc.paragraphs:
    if "{nome}" in p.text:
        p.text = p.text.replace("{name}", "João")
    if "{data}" in p.text:
        p.text = p.text.replace("{date}", "16/04/2026")

doc.save("output.docx")