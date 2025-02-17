import os
from app.utils import *
import platform
from lxml import etree
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Definição da classe 'notafiscal', que representa uma nota fiscal emitida para um paciente.
class notafiscal:
    # Método construtor (__init__) para inicializar os atributos da classe.
    def __init__(self, id_paciente, valor, data_emissao, hora):
        self.id_paciente = id_paciente  # Atributo que armazena o ID do paciente associado à nota fiscal.
        self.valor = valor  # Atributo que armazena o valor da nota fiscal.
        self.data_emissao = data_emissao  # Atributo que armazena a data de emissão da nota fiscal.
        self.hora = hora

        self.paciente = get_paciente_by_id(id_paciente)

    # Método que simula a emissão de uma nota fiscal.
    def emitir(self):
        
        def standard_name(prefix):
            date = self.data_emissao.split("-")
            date = "".join(date)

            sufix = "xml"
            if (prefix=="danfe"): sufix = "pdf"

            return f"nfes/{prefix}{date}.{sufix}"

        def criar_nfe_xml():
            nome_arquivo = standard_name("nfe")

            nfe = etree.Element("nfeProc", xmlns="http://www.portalfiscal.inf.br/nfe", versao="4.00")

            #Criando o elemento <NFe> dentro de <nfeProc>
            nfe_element = etree.SubElement(nfe, "NFe")

            # Criando o elemento <infNFe> dentro de <NFe>
            inf_nfe = etree.SubElement(nfe_element, "infNFe", Id="NFe12345678901234567890123456789012345678901234", versao="4.00")

            # Informações do emitente (empresa que emite a NFe)
            emitente = etree.SubElement(inf_nfe, "emit")
            etree.SubElement(emitente, "CNPJ").text = "12345678000195"
            etree.SubElement(emitente, "xNome").text = "Clínca Amaro"
            etree.SubElement(emitente, "xFant").text = "Clínica Amaro"
            endereco_emitente = etree.SubElement(emitente, "enderEmit")
            etree.SubElement(endereco_emitente, "xLgr").text = "Rua Francisco Marcelino Santana, 123"
            etree.SubElement(endereco_emitente, "xMun").text = "Crato"
            etree.SubElement(endereco_emitente, "UF").text = "CE"

            # Informações do destinatário (cliente que recebe a NFe)
            destinatario = etree.SubElement(inf_nfe, "dest")
            etree.SubElement(destinatario, "CPF").text = self.paciente[0][3]
            etree.SubElement(destinatario, "xNome").text = self.paciente[0][1]

            # Adicionando produtos
            det = etree.SubElement(inf_nfe, "det", nItem="1")
            prod = etree.SubElement(det, "prod")
            etree.SubElement(prod, "cProd").text = "001"
            etree.SubElement(prod, "xProd").text = "Consulta"
            etree.SubElement(prod, "vProd").text = f"{self.valor}"

            # Salvando o XML em um arquivo
            xml_str = etree.tostring(nfe, pretty_print=True, xml_declaration=True, encoding="utf-8")

            with open(nome_arquivo, "wb") as file:
                file.write(xml_str)

            return nome_arquivo

        # Criando DANFE em PDF
        def criar_danfe_pdf(xml_arquivo):
            nome_arquivo = standard_name("danfe")

            # Lendo o XML para extrair os dados
            tree = etree.parse(xml_arquivo)
            root = tree.getroot()

            # Extraindo informações
            ns = {"nfe": "http://www.portalfiscal.inf.br/nfe"}
            emitente_nome = root.find(".//nfe:emit/nfe:xNome", ns).text
            emitente_cnpj = root.find(".//nfe:emit/nfe:CNPJ", ns).text
            destinatario_nome = root.find(".//nfe:dest/nfe:xNome", ns).text
            destinatario_cpf = root.find(".//nfe:dest/nfe:CPF", ns).text
            produto_nome = root.find(".//nfe:prod/nfe:xProd", ns).text
            produto_valor = root.find(".//nfe:prod/nfe:vProd", ns).text

            # Criando o PDF
            c = canvas.Canvas(nome_arquivo, pagesize=letter)
            c.setFont("Helvetica-Bold", 14)
            c.drawString(200, 750, "DANFE - Documento Auxiliar da NFe")

            c.setFont("Helvetica", 10)
            c.drawString(50, 730, f"Emitente: {emitente_nome} - CNPJ: {emitente_cnpj}")
            c.drawString(50, 710, f"Destinatário: {destinatario_nome} - CPF: {destinatario_cpf}")
            c.drawString(50, 690, "Chave de Acesso: 1234 5678 9012 3456 7890 1234 5678 9012 3456")

            c.drawString(50, 650, "Produtos:")
            c.drawString(50, 630, "Nome do Produto   |   Valor")
            c.drawString(50, 610, f"{produto_nome}   |   R$ {produto_valor}")

            c.save()
            return nome_arquivo

        xml = criar_nfe_xml()
        danfe = criar_danfe_pdf(xml)
        
        so = platform.system()
        if so == "Windows":
            os.system(f'start "" "{danfe}"')
        elif so == "Linux":
            os.system(f'xdg-open "{danfe}"')


        

