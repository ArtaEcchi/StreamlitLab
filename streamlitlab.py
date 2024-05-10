import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных
excel_files = {
    'Казахстан': [
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/kz_2014.xlsx',
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/kz_2015.xlsx',
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/kz_2016.xlsx',
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/kz_2017.xlsx'
    ],
    'Таджикистан': [
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/tjk_2014.xlsx',
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/tjk_2015.xlsx',
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/tjk_2016.xlsx',
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/tjk_2017.xlsx'
    ],
    'Кыргызстан': [
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/kgz_2014.xlsx',
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/kgz_2015.xlsx',
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/kgz_2016.xlsx',
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/kgz_2017.xlsx'
    ],
    'Узбекистан': [
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/uzb_2014.xlsx',
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/uzb_2015.xlsx',
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/uzb_2016.xlsx',
        'https://raw.githubusercontent.com/ArtaEcchi/StreamlitLab/main/uzb_2017.xlsx'
    ]
}

# Заголовок
st.title('Лабораторная работа №14-15')

# Боковая панель
page = st.sidebar.radio('Выберите страницу', ['Главная', 'Казахстан', 'Таджикистан', 'Кыргызстан', 'Узбекистан', 'Общий график'])

if page == 'Главная':
    st.write('## Разбор лабораторной работы')
    st.write(f'Данная лабораторная работа построена на базе прошлых работа и является заключительнойgit --version')
elif page in ['Казахстан', 'Таджикистан', 'Кыргызстан', 'Узбекистан']:
    country = page
    st.write(f'## {country}')
    st.write(f'График для {country}')
    dfs = [pd.read_excel(url) for url in excel_files[country]]
    prob_mod_sev_values = {
        'Казахстан': [0.0737473506983265, 0.044529239425859325, 0.07208697980276833, 0.09025550050680399],
        'Таджикистан': [0.13234311608076732, 0.11086727498562164, 0.19598527440470287, 0.23921461895440915],
        'Кыргызстан': [0.1875365079274166, 0.21059007745097164, 0.19581301002148638, 0.19449654750600165],
        'Узбекистан': [0.09872602667454446, 0.12482079148104783, 0.1033934827101725, 0.16342414956949367]
    }
    years = range(2014, 2018)
    plt.figure(figsize=(10, 6))
    plt.title(country)
    plt.plot(years, prob_mod_sev_values[country], marker='o', linestyle='-')
    plt.xticks(years)
    plt.yticks(np.arange(0, 0.31, 0.05))
    plt.grid(True)
    st.pyplot(plt)
else:
    prob_mod_sev_values = {
        'Казахстан': [0.0737473506983265, 0.044529239425859325, 0.07208697980276833, 0.09025550050680399],
        'Таджикистан': [0.13234311608076732, 0.11086727498562164, 0.19598527440470287, 0.23921461895440915],
        'Кыргызстан': [0.1875365079274166, 0.21059007745097164, 0.19581301002148638, 0.19449654750600165],
        'Узбекистан': [0.09872602667454446, 0.12482079148104783, 0.1033934827101725, 0.16342414956949367]
    }
    st.write('## Общий график')
    plt.figure(figsize=(10, 6))
    for country, data in prob_mod_sev_values.items():
        plt.plot(range(2014, 2018), data, marker='o', linestyle='-', label=country)
    plt.title('Средняя Азия')
    plt.xlabel('Год')
    plt.ylabel('Вероятность')
    plt.xticks(range(2014, 2018))
    plt.yticks(np.arange(0, 0.31, 0.05))
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)