from pylatex import Document, Section, Math, Center, MiniPage, NoEscape


class CreateFile:
    def __init__(self, data: list[str]):
        self.data = data
    
    def generate_pdf_tex(self):
        geometry_options = {"tmargin": "1cm", "lmargin": "10cm"}
        doc = Document(geometry_options=geometry_options)

        with doc.create(Center()) as center:
            with center.create(Section('SOLVE IT NOW!!!')) as section:
                 section.numbering = None

        with doc.create(MiniPage(align='left')) as minipage:
            for expression in self.data:
                minipage.append(Math(data=fr'\int{expression},dx', inline=True, escape=False))
                minipage.append(NoEscape(r'\\'))
                minipage.append(NoEscape(r'\\'))
        doc.generate_pdf('/home/nikita/dev/generate_math_problems/static/generated_files/full', clean_tex=False)


if __name__ == '__main__':
    a = CreateFile(['16*x^3/3', '2*x'])
    a.generate_pdf_tex()