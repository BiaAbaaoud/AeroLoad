# ✈️ AeroLoad: Weight & Balance Visualizer

![Status](https://img.shields.io/badge/Status-Online-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue)

## 📋 Sobre o Projeto
O **AeroLoad** é uma aplicação de segurança aeronáutica desenvolvida para realizar o cálculo dinâmico de Peso e Balanceamento da aeronave **Cessna 172 Skyhawk**. 

Em aviação, operar uma aeronave fora dos limites de peso ou com o Centro de Gravidade (CG) deslocado pode ser catastrófico, afetando a estabilidade e a capacidade de recuperação de manobras. Este projeto resolve esse problema transformando cálculos manuais complexos em uma interface visual intuitiva e em tempo real.

## ⚠️ O Problema que Resolvemos
Calcular o peso e o balanceamento em planilhas de papel ou tabelas estáticas é demorado e suscetível a erros humanos. O AeroLoad elimina essa barreira, permitindo que o piloto:
1. Visualize instantaneamente se o peso total excede o **MTOW** (Maximum Takeoff Weight).
2. Identifique se o CG está dentro do **envelope de segurança** tanto na decolagem quanto no pouso (considerando a queima de combustível).

## 🛠️ Ferramentas Utilizadas
- **Python**: Linguagem core para processamento dos dados.
- **Streamlit**: Framework utilizado para criar a interface web de forma ágil.
- **Plotly**: Biblioteca de gráficos interativos para desenhar o envelope de voo.
- **Git & GitHub**: Controle de versão e hospedagem do código.

## 🧠 Desafios de Desenvolvimento
- **Precisão Matemática**: Traduzir braços (arms) e momentos da ficha técnica do Cessna 172 para algoritmos Python.
- **Visualização de Dados**: Plotar um gráfico de coordenadas poligonais que representasse fielmente o limite de manobra da aeronave.
- **User Experience (UX)**: Criar controles (sliders) que simulassem a ocupação real da aeronave (piloto, passageiros, bagagem).

## 🛤️ Passo a Passo da Construção
1. **Modelagem de Dados**: Definição das constantes da aeronave (Peso Vazio, Braços de Momento e Limites de CG).
2. **Desenvolvimento da Lógica**: Criação das funções que calculam o Momento Total e o CG resultante.
3. **Interface Interativa**: Implementação da barra lateral de inputs com Streamlit.
4. **Gráfico do Envelope**: Desenvolvimento do gráfico dinâmico com Plotly, mostrando a trajetória de queima de combustível.
5. **Deploy e Versionamento**: Configuração do Git para salvar o progresso e publicação no Streamlit Cloud.

## 🕹️ COMO USAR
1. **Configuração de Carga**: Na barra lateral esquerda, utilize os controles deslizantes para definir o peso do piloto, passageiros e a quantidade de combustível em litros.
2. **Análise de Métricas**: No topo da página, observe os indicadores coloridos. Se o peso exceder o limite, o sistema emitirá um alerta vermelho de **Voo Perigoso**.
3. **Gráfico de Estabilidade**: Verifique se o ponto branco (Decolagem) e o ponto ciano (Pouso) estão dentro da área verde do gráfico.
4. **Trajetória**: A linha amarela mostra como o equilíbrio do avião mudará conforme o combustível for consumido durante a viagem.

## ❓ Perguntas Frequentes (FAQ)

1. **Este gráfico serve para qualquer aeronave?** A lógica matemática (Cálculo de Momentos) é universal para a aviação. No entanto, este projeto foi modelado especificamente com os limites de peso e braços de momento do **Cessna 172 Skyhawk**. Para utilizá-lo em outras aeronaves, basta atualizar as constantes do envelope de segurança conforme o manual da fabricante (POH).

2. **O projeto é focado em Front-end ou Back-end?** O AeroLoad é uma aplicação **Full-stack**. O Python gerencia tanto o "Back-end" (cálculos de engenharia e lógica de segurança) quanto o "Front-end" (interface interativa e gráficos), graças ao framework Streamlit.

3. **O sistema funciona em tempo real?** Sim. A aplicação é reativa; cada vez que um parâmetro de carga é alterado pelo usuário, o sistema recalcula os dados instantaneamente e atualiza o gráfico sem a necessidade de recarregar a página.

4. **O projeto pode ser expandido?** Sim. A arquitetura atual permite a implementação futura de banco de dados para múltiplas aeronaves, conversão automática de unidades (Galões/Litros, Libras/Quilos) e integração com APIs de meteorologia para ajuste de densidade do ar.
---
**Desenvolvido com foco em segurança aérea por [Bia Abaoud](https://github.com/BiaAbaaoud)**