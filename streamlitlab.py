import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_echarts import st_echarts

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
    st.write(f'Данная лабораторная работа построена на базе прошлых работа и является заключительной.')
    st.write(f'Абстракт: Достижение голода и обеспечение продовольственной безопасности - это одна из целей устойчивого развития, '
             f'но ее достижение сталкивается с вызовами из-за экономических и политических кризисов во многих странах. '
             f'В данном исследовании мы анализировали изменения в продовольственной безопасности в странах Центральной Азии (Казахстан, Узбекистан и другие) в период с 2014 по 2017 год. '
             f'На основе данных, полученных из наших графиков, выявлено, '
             f'что большинство этих стран столкнулись с увеличением уровня продовольственной нехватки в течение исследуемого периода. '
             f'Однако, как и в других регионах, наблюдались различия между странами. Некоторые страны, такие как Казахстан, показали снижение уровня продовольственной безопасности, тогда как другие, например, Узбекистан, продемонстрировали положительную динамику. '
             f'Анализ позволяет утверждать, что факторы, такие как уровень бедности, образование, семейное положение и социальная поддержка, играют важную роль в определении уровня продовольственной безопасности в этих странах. '
             f'Это исследование подчеркивает необходимость разработки и реализации эффективных экономических и социальных стратегий для обеспечения продовольственной безопасности в регионе.')
    st.write(f'')
    st.write(f'Далее представлены построенные графики на основе данныз с 2014 по 2017 годы по странам Центральной Азии.')
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
    option = {
        "xAxis": {
            "type": "category",
            "data": [2014, 2015, 2016, 2017],
        },
        "yAxis": {"type": "value"},
        "series": [{"data": prob_mod_sev_values[country], "type": "line"}],
    }
    st_echarts(
        options=option, height="400px",
    )
else:
    st.write('## Общий график')
    option = {
        "title": {"text": "Страны: "},
        "tooltip": {"trigger": "axis"},
        "legend": {"data": ["Казахстан", "Таджикистан", "Кыргызстан", "Узбекистан"]},
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "toolbox": {"feature": {"saveAsImage": {}}},
        "xAxis": {
            "type": "category",
            "boundaryGap": False,
            "data": [2014, 2015, 2016, 2017],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"name": "Казахстан", "type": "line", "data": [0.0737473506983265, 0.044529239425859325, 0.07208697980276833, 0.09025550050680399]},
            {"name": "Таджикистан", "type": "line", "data": [0.13234311608076732, 0.11086727498562164, 0.19598527440470287, 0.23921461895440915]},
            {"name": "Кыргызстан", "type": "line", "data": [0.1875365079274166, 0.21059007745097164, 0.19581301002148638, 0.19449654750600165]},
            {"name": "Узбекистан", "type": "line", "data": [0.09872602667454446, 0.12482079148104783, 0.1033934827101725, 0.16342414956949367]}
        ],
    }
    st_echarts(options=option, height="400px")