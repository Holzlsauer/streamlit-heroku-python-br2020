import streamlit as st
import pandas as pd

from lib.create_plot import CreatePlot

DATASET = "datasets/mcdonalds_nutrition_facts.csv"


def main():
    st.title("Streamlit/Heroku")
    st.markdown("""
        Projeto desenvolvido em workshop durante o Python Brasil 2020

        ## Inspeção de dados nutricionais do cardápio do mcdonalds

        Selecione na sidebar as colunas desejadas
    """)

    df = pd.read_csv(DATASET)
    colunas = df.columns

    colunas_to_df = [a for a in colunas if st.checkbox(a)]
    df_to_st = df[colunas_to_df]
    st.dataframe(df_to_st)

    st.markdown("Selecione na lateral uma coluna para ser exibida no histograma")
    col = st.sidebar.selectbox("Coluna do histograma", colunas)

    hist = CreatePlot(df).histogram_plot(col)
    st.plotly_chart(hist, use_container_width=True)

    st.bar_chart(df["Category"])


if __name__ == "__main__":
    main()
