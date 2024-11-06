import streamlit as st


# Função para exibir o currículo
def exibir_curriculo():
    st.header("Currículo Profissional")
    
    # Foto do desenvolvedor
    st.image("foto_perfil.jpg", width=200)  # Substitua com o caminho da imagem
    st.markdown("### Nome: Nicolas Alves")
    
    # Tópicos do currículo
    st.subheader("Habilidades Técnicas")
    st.write("""
        - Python, JavaScript, HTML, CSS, SQL
        - Frameworks: Flask, Django, React, Vue.js
        - Banco de dados: MySQL, PostgreSQL, MongoDB
        - Controle de versão: Git, GitHub
        - Ferramentas: Docker, AWS, VS Code
    """)

    st.subheader("Educação")
    st.write("""
        - Bacharelado em Ciência da Computação, Universidade XYZ (2015-2019)
    """)

    st.subheader("Projetos e Realizações")
    st.write("""
        - **Sistema de Gestão de Tarefas:** Desenvolvido em Python usando Flask. Permite a criação, edição e deleção de tarefas em tempo real.
        - **E-commerce com React:** Plataforma de vendas online com integração de carrinho de compras e pagamento, desenvolvido com React e Node.js.
    """)

    st.subheader("Idiomas")
    st.write("""
        - Português (Nativo)
        - Inglês (Avançado)
    """)

    st.subheader("Cursos e Treinamentos")
    st.write("""
        - Certificação em Desenvolvimento Web Completo - Udemy (2020)
        - Curso de Machine Learning - Coursera (2021)
    """)

    st.subheader("Referências Profissionais")
    st.write("""
        - Maria Souza - Gerente de TI, Empresa XYZ - (maria@xyz.com)
        - Carlos Lima - CTO, Empresa ABC - (carlos@abc.com)
    """)

    st.subheader("Contatos")
    st.write("""
        - **E-mail:** nicolasdanilo.contato@gmail.com
        - **LinkedIn:** [linkedin.com/in/nicolas alves](https://br.linkedin.com/in/lin-nicolasalves?trk=people-guest_people_search-card)
        - **GitHub:** [github.com/joaosilva](https://github.com/joaosilva)
        - **Site:** [www.joaosilva.dev](https://www.joaosilva.dev)
    """)

# Função para exibir o portfólio de projetos
def exibir_portfolio():
    st.header("Portfólio de Projetos")
    st.write("""
        Aqui estão alguns dos projetos em que trabalhei:
    """)

    # Projeto 1
    st.subheader("Sistema de Gestão de Tarefas")
    st.write("""
        Um sistema de gerenciamento de tarefas com interface simples, onde os usuários podem criar, editar e excluir tarefas.
        - **Tecnologias usadas:** Python, Flask, SQLite
        - **GitHub:** [github.com/joaosilva/todolist](https://github.com/joaosilva/todolist)
    """)
    st.image("projeto1.png", width=400)  # Imagem do projeto (substitua com caminho real)

    # Projeto 2
    st.subheader("E-commerce com React")
    st.write("""
        Uma plataforma de e-commerce com integração de carrinho de compras e pagamento.
        - **Tecnologias usadas:** React, Node.js, MongoDB
        - **GitHub:** [github.com/joaosilva/ecommerce](https://github.com/joaosilva/ecommerce)
    """)
    st.image("projeto2.png", width=400)  # Imagem do projeto (substitua com caminho real)

# Função principal que cria o menu lateral
def main():
    # Configuração do layout
    st.set_page_config(page_title="Portfólio de Nicolas Alves", layout="wide")
    
    # Menu lateral
    menu = ["Início", "Currículo", "Portfólio", "Contato"]
    escolha = st.sidebar.radio("Navegação", menu)

    # Exibir conforme a escolha do menu
    if escolha == "Início":
        st.title("Bem-vindo ao meu Portfólio!")
        st.markdown("""
            Olá, sou Nicolas Alves, desenvolvedor de software com experiência em diversas tecnologias. 
            Navegue pelo meu portfólio para conhecer meus projetos, habilidades e mais.
        """)
    elif escolha == "Currículo":
        exibir_curriculo()
    elif escolha == "Portfólio":
        exibir_portfolio()
    elif escolha == "Contato":
        st.header("Entre em Contato")
        st.write("""
            Se você quiser discutir uma oportunidade ou colaboração, me envie uma mensagem!
        """)
        st.write("E-mail: joao.silva@email.com")
        st.write("LinkedIn: [https://br.linkedin.com/in/lin-nicolasalves?trk=people-guest_people_search-card)")
        st.write("GitHub: [github.com/joaosilva](https://github.com/joaosilva)")

if __name__ == "__main__":
    main()
