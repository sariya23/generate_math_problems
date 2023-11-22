from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat

class CreateFile:
    def __init__(self, data: list[str], file_format: str = 'tex'):
        self.data = data
        self.file_format = file_format
    
    
    def create_tex(self, header_for_document):
        geometry_options = {"tmargin": "1cm", "lmargin": "10cm"}
        doc = Document(geometry_options=geometry_options)

        with doc.create(Section('Задачи на интегралы')):
            with doc.create(Alignat(numbering=False, escape=False)) as agn:
                for expression in self.data:
                    agn.append(fr'$\int{expression}\\$')
    
        doc.generate_pdf('full', clean_tex=False)


if __name__ == '__main__':
    a = CreateFile(['16*x^3/3', '2*x'])
    a.create_tex('qwe')