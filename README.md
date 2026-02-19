# Clínica Vida Saudável

![Hero Image](assets/new-hero-image.png)

## 🇧🇷 Português

Este repositório contém o código-fonte de um site estático para uma clínica médica, desenvolvido como parte de um desafio de HTML da DIO. O projeto demonstra a criação de um site responsivo e interativo, utilizando as melhores práticas de desenvolvimento web.

### 🚀 Tecnologias Utilizadas

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

### 📂 Estrutura do Projeto

```
Criando-seu-Primeiro-Site-Completo-com-HTML/
├── src/
│   ├── index.html
│   ├── sobre.html
│   ├── atendimento.html
│   └── contato.html
├── assets/
│   └── hero-image.png
│   └── project_structure.png
├── docs/
│   └── project_structure.mmd
├── config/
├── tests/
│   └── test_html_css.py
├── .gitignore
├── LICENSE
└── README.md
```

### 📊 Diagrama de Arquitetura

```mermaid
graph TD
    ROOT[Clínica Vida Saudável\nSite Multi-página HTML] --> IDX[index.html\nPágina Inicial]
    ROOT --> SOB[sobre.html\nSobre Nós]
    ROOT --> ATD[atendimento.html\nAtendimento]
    ROOT --> CON[contato.html\nContato]

    IDX --> IDX1[Hero Section\nBanner Principal]
    IDX --> IDX2[Serviços Oferecidos]
    IDX --> IDX3[Diferenciais da Clínica]
    IDX --> IDX4[CTA Agendamento]

    SOB --> SOB1[História da Clínica]
    SOB --> SOB2[Missão · Visão · Valores]
    SOB --> SOB3[Equipe Médica]

    ATD --> ATD1[Especialidades]
    ATD --> ATD2[Horários de Funcionamento]
    ATD --> ATD3[Como Agendar]

    CON --> CON1[Formulário de Contato]
    CON --> CON2[Endereço e Mapa]
    CON --> CON3[Telefone e E-mail]

    IDX & SOB & ATD & CON --> SHARED[Componentes Compartilhados]
    SHARED --> NAV[Navbar\nNavegação entre páginas]
    SHARED --> FTR[Footer\nRodapé]
```

### 📄 Páginas do Site

*   `index.html`: Página principal com uma visão geral da clínica, seus serviços e diferenciais.
*   `sobre.html`: Detalhes sobre a história da clínica, sua missão, visão e valores.
*   `atendimento.html`: Informações sobre os horários de funcionamento, especialidades e agendamento de consultas.
*   `contato.html`: Formulário de contato, endereço, mapa de localização e outras formas de comunicação.

### 🛠️ Como Visualizar e Usar

1.  **Clonar o repositório:**
    ```bash
    git clone https://github.com/galafis/Criando-seu-Primeiro-Site-Completo-com-HTML.git
    ```
2.  **Navegar até o diretório do projeto:**
    ```bash
    cd Criando-seu-Primeiro-Site-Completo-com-HTML
    ```
3.  **Abrir o site:**
    Abra o arquivo `src/index.html` em seu navegador web preferido para começar a navegar pelo site.

### 🤝 Contribuição

Este projeto foi desenvolvido por Gabriel Demetrios Lafis para fins educacionais e como parte de seu portfólio. Contribuições são bem-vindas, mas por favor, entre em contato com o autor antes de fazer grandes alterações.

### 📝 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🇬🇧 English

This repository contains the source code for a static website for a medical clinic, developed as part of a DIO HTML challenge. The project demonstrates the creation of a responsive and interactive website, using web development best practices.

### 🚀 Technologies Used

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

### 📂 Project Structure

```
Criando-seu-Primeiro-Site-Completo-com-HTML/
├── src/
│   ├── index.html
│   ├── sobre.html
│   ├── atendimento.html
│   └── contato.html
├── assets/
│   └── hero-image.png
│   └── project_structure.png
├── docs/
│   └── project_structure.mmd
├── config/
├── tests/
│   └── test_html_css.py
├── .gitignore
├── LICENSE
└── README.md
```

### 📊 Architecture Diagram

```mermaid
graph TD
    ROOT[Clínica Vida Saudável\nMulti-page HTML Site] --> IDX[index.html\nHome Page]
    ROOT --> SOB[sobre.html\nAbout Us]
    ROOT --> ATD[atendimento.html\nAppointments]
    ROOT --> CON[contato.html\nContact]

    IDX --> IDX1[Hero Section\nMain Banner]
    IDX --> IDX2[Services Offered]
    IDX --> IDX3[Clinic Differentials]
    IDX --> IDX4[Scheduling CTA]

    SOB --> SOB1[Clinic History]
    SOB --> SOB2[Mission · Vision · Values]
    SOB --> SOB3[Medical Team]

    ATD --> ATD1[Specialties]
    ATD --> ATD2[Operating Hours]
    ATD --> ATD3[How to Schedule]

    CON --> CON1[Contact Form]
    CON --> CON2[Address and Map]
    CON --> CON3[Phone and Email]

    IDX & SOB & ATD & CON --> SHARED[Shared Components]
    SHARED --> NAV[Navbar\nNavigation between pages]
    SHARED --> FTR[Footer]
```

### 📄 Website Pages

*   `index.html`: Main page with an overview of the clinic, its services, and differentiators.
*   `sobre.html`: Details about the clinic's history, mission, vision, and values.
*   `atendimento.html`: Information about operating hours, specialties, and appointment scheduling.
*   `contato.html`: Contact form, address, location map, and other communication methods.

### 🛠️ How to View and Use

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/galafis/Criando-seu-Primeiro-Site-Completo-com-HTML.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Criando-seu-Primeiro-Site-Completo-com-HTML
    ```
3.  **Open the website:**
    Open the `src/index.html` file in your preferred web browser to start browsing the website.

### 🤝 Contribution

This project was developed by Gabriel Demetrios Lafis for educational purposes and as part of his portfolio. Contributions are welcome, but please contact the author before making major changes.

### 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

