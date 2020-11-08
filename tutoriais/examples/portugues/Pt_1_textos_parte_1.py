import streamlit as st
import pandas as pd
from lib.base_dfs_and_lists import simple_df


def exemplo_textos_parte_1():
    st.write("___________________________________")

    st.write("Escrever textos com o streamlit é super fácil :)")

    st.write("É possível pular linhas usando esse comando (veja o código!) \n \n")

    st.write("\n\n")

    my_name = "Holzlsauer"  # Troque seu nome aqui
    my_age = 27  # E sua idade

    st.write("E também é possível usar string format!! \n")
    st.write(f"Meu nome é: {my_name}! Eu possuo {my_age} anos!")

    st.write(
        "\n\n E é possível fazer diversas outras coisas com o comando `write`, "
        "como por exemplo escrever um dataframe!"
    )
    st.write(pd.DataFrame(simple_df()))

    # Tente escrever alguma coisa a mais nesse código, talvez criar uma variável da sua cidade e printar ela
    # usando o `st.write`
    st.write("Streamlite ftw")


if __name__ == '__main__':
    exemplo_textos_parte_1()
