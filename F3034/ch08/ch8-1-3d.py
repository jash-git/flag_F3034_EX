import docx
from docx.shared import Cm

doc = docx.Document("Word文件範例4.docx")
doc.add_picture("koala.png", width=Cm(3))
doc.save("Word文件範例5.docx")
