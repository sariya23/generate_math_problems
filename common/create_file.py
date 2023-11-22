from pylatex import Document, Section, Math, Center, MiniPage, NoEscape, HorizontalSpace, FlushLeft


class CreateFile:
    def __init__(self, data: list[str]):
        self.data = data
    
    def generate_pdf_tex_file_with_expressions(self, file_name: str, is_pure_input: bool, title_for_document: str):
        geometry_options = {"tmargin": "1cm"}
        doc = Document(geometry_options=geometry_options)

        with doc.create(Center()) as center:
            with center.create(Section(title_for_document)) as section:
                section.numbering = None

        with doc.create(MiniPage(align='left')) as minipage:
            for index, expression in enumerate(self.data):
                minipage.append(NoEscape(fr'{index + 1}) '))

                if is_pure_input:
                    minipage.append(Math(data=fr'{expression}', inline=True, escape=False))
                else:
                    minipage.append(Math(data=fr'\int{expression},dx', inline=True, escape=False))
                
                if index % 2 == 0:
                    minipage.append(HorizontalSpace(f'{(len(expression) + len(str(index))) * 3}pt'))
                else:
                    minipage.append(NoEscape(r'\\'))
                    minipage.append(NoEscape(r'\\'))
        doc.generate_pdf(f'/home/nikita/dev/generate_math_problems/static/generated_files/{file_name}', clean_tex=False)        
        

    def generate_pdf_tex_expressions(self, file_name: str):
        geometry_options = {"tmargin": "1cm"}
        doc = Document(geometry_options=geometry_options)

        with doc.create(Center()) as center:
            with center.create(Section('SOLVE IT NOW!!!')) as section:
                section.numbering = None
        with doc.create(MiniPage(align='left')) as minipage:
            for index, expression in enumerate(self.data):
                minipage.append(NoEscape(fr'{index + 1}) '))
                minipage.append(Math(data=fr'\int{expression},dx', inline=True, escape=False))
                if index % 2 == 0:
                    minipage.append(HorizontalSpace(f'{(len(expression) + len(str(index))) * 3}pt'))
                else:
                    minipage.append(NoEscape(r'\\'))
                    minipage.append(NoEscape(r'\\'))
        doc.generate_pdf(f'/home/nikita/dev/generate_math_problems/static/generated_files/{file_name}', clean_tex=False)
    
    def generate_pdf_tex_answers(self, file_name):
        geometry_options = {"tmargin": "1cm"}
        doc = Document(geometry_options=geometry_options)

        with doc.create(Center()) as center:
            with center.create(Section('ANSWERS!!!')) as section:
                 section.numbering = None

        with doc.create(MiniPage(align='left')) as minipage:
            for index, expression in enumerate(self.data):
                minipage.append(NoEscape(fr'{index + 1}) '))
                minipage.append(Math(data=fr'{expression}', inline=True, escape=False))
                if index % 2 == 0:
                    minipage.append(HorizontalSpace(f'{(len(expression) + len(str(index))) * 3}pt'))
                else:
                    minipage.append(NoEscape(r'\\'))
                    minipage.append(NoEscape(r'\\'))
        doc.generate_pdf(f'/home/nikita/dev/generate_math_problems/static/generated_files/{file_name}', clean_tex=False)


if __name__ == '__main__':
    a = CreateFile(['16*x^3/3', '2*x'])
    a.generate_pdf_tex()