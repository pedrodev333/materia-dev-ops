from docx import Document

doc = Document("template.docx")

for p in doc.paragraphs:
    if "{nome}" in p.text:
        p.text = p.text.replace("{nome}", "João")
    if "{data}" in p.text:
        p.text = p.text.replace("{data}", "16/04/2026")

doc.save("output.docx")