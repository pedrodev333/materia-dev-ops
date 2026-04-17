from docx import Document


userName = input("Digite um nome:")
userDate = input("Digite uma data (dd/mm/aaaa):")




doc = Document("template.docx")

for p in doc.paragraphs:
    if "{nome}" in p.text:
        p.text = p.text.replace("{nome}", userName)
    if "{data}" in p.text:
        p.text = p.text.replace("{data}", userDate)

doc.save("output.docx")