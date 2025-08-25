# -*- coding: utf-8 -*-
import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="Calculadora de Gold",
    page_icon="💰",
    layout="centered"
)

# --- Título e Descrição ---
st.title("💰 Calculadora de Custos em Gold")
st.write("Preencha as quantidades e os preços dos itens que você deseja comprar para calcular o custo total.")

# --- Lista de Itens ---
itens = [
    ("Aço Raro", "aco_raro"),
    ("Aço Épico", "aco_epico"),
    ("Orb Raro", "orb_raro"),
    ("Orb Épico", "orb_epico"),
    ("Shadow Stone Raro", "shadow_raro"),
    ("Shadow Stone Épico", "shadow_epico"),
    ("Cobre", "cobre"),
    ("Aço Negro", "aco_negro")
]

# --- Dicionários para Armazenar os Valores ---
quantidades = {}
precos = {}
custos_individuais = {}
custo_total_gold = 0.0

# --- Interface do Usuário ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🛒 Quantidades")
    for nome_item, key in itens:
        quantidades[key] = st.number_input(
            f"Qtd. de {nome_item}", 
            min_value=0,
            step=1,
            key=f"qtd_{key}"
        )

with col2:
    st.subheader("🪙 Preço Unitário (Gold)")
    for nome_item, key in itens:
        if quantidades[key] > 0:
            precos[key] = st.number_input(
                f"Preço de {nome_item}",
                min_value=0.00,
                step=0.01,
                format="%.2f",
                key=f"preco_{key}"
            )
        else:
            precos[key] = 0.0

# --- Cálculo e Exibição dos Resultados ---
st.divider()
st.header("📊 Resumo do Custo")

for nome_item, key in itens:
    if quantidades[key] > 0 and precos[key] > 0:
        custo = quantidades[key] * precos[key]
        custos_individuais[nome_item] = custo
        custo_total_gold += custo

if custo_total_gold > 0:
    for item, custo in custos_individuais.items():
        st.write(f"Custo para **{item}**: `{custo:,.2f} Gold`")

    st.success(f"**CUSTO TOTAL: {custo_total_gold:,.2f} Gold**")
else:
    st.info("Preencha as quantidades e preços para ver o cálculo.")