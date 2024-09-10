from fpdf import FPDF

class PDF(FPDF):

    def titulo(self, label):
        self.set_font('helvetica', 'B', size=24)
        self.cell(0, 60, label, 0, 1, 'C')

    def sub_titulo(self, label):
        self.set_font('helvetica', 'I', size=16)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def linha_centralizada(self, label):
        self.set_font('helvetica', '', size=12)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def titulo_base(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 8, label, 0, 1, 'L')
        self.ln()
        
    def destaque(self, label):
        self.set_font('helvetica', 'B', size=14)
        self.cell(0, 4, label, 0, 1, 'L')
        self.ln()

    def paragrafo(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 6, text)
        self.ln()

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)

pdf = PDF()

# ------------- Fazendo a capa -------------
pdf.add_page()

pdf.titulo("Análise da Desigualdade na Educação Brasileira")
pdf.sub_titulo("Usando dados públicos para entender problemas")
pdf.imagem("imagem_capa.png", 40, 90, 130)
pdf.ln(160)
pdf.linha_centralizada("Autor: Luan F. Soares")
pdf.linha_centralizada("Data: 7 de Setembro de 2024")

# ------------- 2 pagina -------------
pdf.add_page()

pdf.titulo_base("Introdução")

pdf.paragrafo("A educação é um dos pilares básicos para a formação de uma sociedade mais justa e igualitária. Mesmo com avanços consideráveis ao longo das últimas décadas, o Brasil ainda apresenta situações que comprometem a quantidade e a qualidade da educação ofertada, sobretudo no ensino superior. Tais contextos estão vinculados a fatores regionais, econômicos, sociais e administrativos que criam realidades distintas e complexas em um país de dimensões territoriais diversificadas. ")

pdf.paragrafo("Neste sentido, este relatório visa analisar a desigualdade da educação brasileira, especialmente na graduação. Utilizando-se de dados públicos, propõe-se a identificar os padrões de distribuição de oportunidades educacionais entre as regiões do país, e se fatores como a categoria administrativa das instituições de ensino possuem relação com a demanda e a oferta de ensino superior de qualidade. Desta forma, a análise dos resultados almeja não apenas indicar onde estamos, mas contribuir com a discussão acerca de políticas públicas que podem minimizar a desigualdade educacional e promover um sistema mais inclusivo.")

pdf.paragrafo("O arquivo utilizado para esta análise foi obtido na plataforma MEC e contém dados de 902.676 cursos de graduação no Brasil, distribuídos por 18 colunas. As colunas fornecem informações como: Código e Nome da Instituição de Ensino (IES), Categoria Administrativa (pública, privada, etc.), Organização Acadêmica (universidade, centro universitário, etc.), Nome e Grau do Curso (bacharelado, licenciatura, etc.), Modalidade de Ensino (presencial, educação a distância), Vagas Autorizadas, Município, UF e Região")

# pdf.imagem("2_Gráfico_Cursos_por_Região.png", 30, 105, 150)
# pdf.ln(120)

# ------------- 3 pagina -------------
pdf.add_page()

pdf.titulo_base("Desenvolvimento")

pdf.destaque("1. Distribuição de Vagas")

pdf.paragrafo("Analisando os gráficos 1 (Total de vagas autorizadas por região) e 2 (Distribuição de cursos por região), podemos notar uma concentração significativa de vagas nas regiões Sudeste e Nordeste. Essa disparidade pode ser explicada por diversos fatores, como a maior densidade populacional, a presença de grandes centros urbanos e um histórico de investimento em educação nessas regiões. A região Sudeste se destaca com o maior número de vagas, o que pode indicar uma maior oferta de cursos e instituições de ensino nessa região. Essa concentração pode gerar desigualdades no acesso à educação de qualidade para as demais regiões.")

pdf.imagem("Gráfico_Vagas_por_Região.png", 40, 90, 130)
pdf.imagem("Gráfico_Cursos_por_Região.png", 40, 196, 130)

# ------------- 4 pagina -------------

pdf.add_page()
pdf.destaque("2. Carga Horária Média")

pdf.paragrafo("Iniciando a análise dos dados, ao verificar os gráficos apresentados abaixo, temos uma visão geral interessante sobre a carga horária média dos cursos.")

pdf.imagem("Gráfico_Carga_Horaria_por_Grau.png", 40, 40, 130)
pdf.imagem("Gráfico_Carga_Horaria_por_Região.png", 40, 170, 130)

# ------------- 5 pagina -------------

pdf.add_page()

pdf.paragrafo("É esperado que a carga horária média tenha uma variação significante entre as diferentes regiões do país. Algumas regiões concentram cursos com cargas horárias mais elevadas, enquanto outras apresentam médias menores.")

pdf.paragrafo("A região também exerce um papel importante na determinação da carga horária média. Algumas regiões concentram instituições com cargas horárias mais elevadas, enquanto outras apresentam médias menores.")

pdf.destaque("3. Modalidades de Ensino")

pdf.paragrafo("O gráfico de pizza apresentado abaixo demonstra de forma clara a predominância da educação a distância no cenário educacional brasileiro, representando 92% da oferta total de cursos. Em contrapartida, a educação presencial corresponde a apenas 8% do total.")

pdf.imagem("Gráfico_Modalidade_Ensino.png", 40, 90, 130)
pdf.ln(110)

pdf.paragrafo("A expressiva porcentagem da educação a distância indica uma tendência crescente de adesão a essa modalidade de ensino no Brasil. Fatores como a flexibilidade de horários, a possibilidade de estudar em qualquer lugar e o menor custo podem ter impulsionado essa expansão.")

pdf.paragrafo("Apesar do crescimento, a educação a distância enfrenta desafios como a necessidade de maior acesso à internet e equipamentos tecnológicos, além da questão da qualidade do ensino e do acompanhamento dos estudantes.")

pdf.paragrafo("É importante ressaltar que a educação a distância e a presencial não são excludentes, mas sim complementares. Muitas instituições oferecem cursos híbridos, combinando atividades presenciais e online.")

# ------------- 6 pagina -------------
pdf.add_page()

pdf.paragrafo('Ao observarmos a distribuição das modalidades de ensino (presencial e a distância) nas diferentes regiões do país, apesar da predominância da educação a distância, podemos identificar variações signifiativas entre as regiões, o que levanta certos questionamentos como: "Quais os fatores que explicam a maior oferta de cursos  distância em algumas regiões?". Dentre as considerações, podemos citar como fatores relevantes a disponibilidade de infraestrutura tecnológica, as políticas públicas de incentivo à educação e a demanda dos estudantes')

pdf.imagem("Gráfico_Modalidade_por_Região.png", 40, 50, 130)
pdf.ln(130)

pdf.paragrafo("Realizando uma análise mais aprofundada, conseguimos verificar a distribuição dos cursos pela modalidade de ensino (presenciais e a distância) de acordo com cada categoria administrativa (especial, privada com fins lucrativos, privada sem fins lucrativos, pública estadual, pública federal e pública municipal), conforme os gráficos a seguir: ")

pdf.imagem("Gráfico_Modalidade_para_Especial.png", 50, 210, 90)

# ------------- 7 pagina -------------

pdf.add_page()

pdf.imagem("Gráfico_Modalidade_para_Pública Estadual.png", 50, 15, 100)
pdf.imagem("Gráfico_Modalidade_para_Pública Federal.png", 50, 85, 100)
pdf.imagem("Gráfico_Modalidade_para_Pública Municipal.png", 50, 155, 100)
pdf.imagem("Gráfico_Modalidade_para_Privada com fins lucrativos.png", 50, 225, 100)

pdf.add_page()

pdf.imagem("Gráfico_Modalidade_para_Privada sem fins lucrativos.png", 50, 15, 110)

pdf.ln(70)

pdf.destaque("4. Situação dos Cursos")

pdf.paragrafo("A maioria dos cursos nas diferentes regiões encontra-se em atividade, o que indica uma ampla oferta de cursos no ensino superior brasileiro.")

pdf.paragrafo("A taxa de extinção de cursos varia entre as regiões, com algumas regiões apresentando uma taxa maior. Essa variação pode estar relacionada a fatores como a demanda do mercado de trabalho, a qualidade dos cursos e a disponibilidade de recursos financeiros.")
pdf.imagem("Gráfico_Situacao_Cursos.png", 35, 140, 130)
# ------------- 8 pagina -------------

pdf.add_page()

pdf.imagem("Gráfico_Situacao_por_Região.png", 35, 10, 130)

pdf.ln(90)

pdf.destaque("5. Proporção de Categorias Administrativas por Região")

pdf.paragrafo("A proporção de cada categoria administrativa varia significativamente entre as regiões, mas é evidente a predominância de instituições privadas com fins lucrativos em todas elas, especialmente no Sudeste. Isso indica uma forte presença do setor privado na oferta de ensino superior no Brasil.")

pdf.paragrafo(" Já em relação às instituições especiais (como as comunitárias e filantrópicas), podemos observar que apresentam uma participação relativamente pequena em todas as regiões.")

pdf.imagem("Gráfico_Categorias_por_Região.png", 40, 160, 150)

pdf.add_page()

pdf.imagem("Gráfico_Categorias_Adm_Região_CENTRO_OESTE.png", 40, 10, 150)
pdf.imagem("Gráfico_Categorias_Adm_Região_NORDESTE.png", 40, 110, 150)
pdf.imagem("Gráfico_Categorias_Adm_Região_NORTE.png", 40, 210, 150)

pdf.add_page()
pdf.imagem("Gráfico_Categorias_Adm_Região_SUDESTE.png", 40, 10, 150)
pdf.imagem("Gráfico_Categorias_Adm_Região_SUL.png", 40, 110, 150)

pdf.ln(190)

pdf.paragrafo(" Analisando estes dados, podemos inferir que a concentração de instituições privadas com fins lucrativos em determinadas regiões pode limitar o acesso de estudantes de baixa renda ao ensino superior.")






# # -------------  página -------------
pdf.add_page()

pdf.titulo_base("Conclusão")

pdf.paragrafo(" A análise do caso evidencia uma profunda desigualdade na distribuição de vagas e oferta de ensino superior no Brasil, em particular entre regiões do país. A concentração de vagas no Sudeste e Nordeste reflete os fatores econômicos e demográficos que fizeram com que o desenvolvimento de centros mais robustos se concentrasse nessas áreas.")

pdf.paragrafo("Mas, ao mesmo tempo, a predominância da educação a distância, que responde por 92% da oferta de cursos, demonstra uma adaptação crescente às necessidades de flexibilização no ensino. Contudo, a qualidade e a acessibilidade da tecnologia ainda são um problema, especialmente para estudantes de áreas remotas e mal equipadas.")

pdf.paragrafo("Além disso, a presença de instituições lucrativas privadas em todo o país, principalmente no Sudeste, sugere uma barreira para os estudantes de baixa renda devido a os altos custos que as instituições podem cobrar.")

pdf.paragrafo("Assim, pode-se concluir que, embora o Brasil tenha progredido na expansão do ensino superior, desigualdades significativas ainda estão presentes em termos regionais e econômicos. Portanto, cabe ao poder público e às instituições buscá-las ativamente através de políticas para outro mais justo que leve em consideração a realidade regional do Brasil da influência econômica de estudantes.")

pdf.output("relatório.pdf")