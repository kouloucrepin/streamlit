import streamlit as st


import plotly.express as px
st.set_page_config(layout="wide")
st.markdown("""<style>
.stApp {
    background-color: skyblue;  # Remplacez 'lightblue' par la couleur de votre choix
}
[data-testid="stSidebar"] {
        background-color: black;
        font-color:white
    }
    
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] div,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] span,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] label,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h1,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h4,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h5,
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h6 {
        color: white;  /* Remplacez par la couleur de votre choix */
    }
.stApp header {
        background-color: lightgreen;
    }
</style>""", unsafe_allow_html=True)




st.sidebar.write("BIENVENU")

# Créer un graphique Plotly Express
fig = px.bar(x=[1, 2, 3], y=[4, 5, 6],title='Titre du Graphique',
             width=400, height=300,orientation="h",color=["1", "2", "3"])

# Définir la bordure du graphique
fig.update_layout(title=dict(font=dict(size=26, color='black'),x=0.25),
                  paper_bgcolor='lightgray',plot_bgcolor="lightgray",
                  xaxis=dict(color="black"),yaxis=dict(title=""),
                  margin=dict(l=0, r=0, b=0, t=50),bargap=0,
                  legend={
        "title":{
            'text': ""
            },
        'yanchor': 'bottom',
         "orientation":"h",
         "x":0.2
    }
                  )
fig.update_traces(width=0.5)

# Données pour la première figure
df1 = px.data.tips()

# Créer la première figure
fig1 = px.scatter(df1, x="total_bill", y="tip", color="day",title="Repartition 2",height=300)
fig1.update_layout(
    legend=dict(
        title={
            'text': "",
            'font': {
                'size': 14,
                'color': "black"
            }
        },
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    ),
    paper_bgcolor='lightgray',plot_bgcolor="lightgray",
    title=dict(font=dict(size=26, color='black'),x=0.25),
    margin=dict(t=50)
)




# Afficher le graphique
col1,col2 = st.columns([2,1])
with col1:
   st.plotly_chart(fig,use_container_width=True)     

with col2:
   st.plotly_chart(fig1,use_container_width=True)     
   
   
   

# Données pour la première figure
df1 = px.data.tips()

# Créer la première figure
fig1 = px.scatter(df1, x="total_bill", y="tip", color="day",height=350)
fig1.update_layout(
    legend=dict(
        title={
            'text': "Légende 1",
            'font': {
                'size': 14,
                'color': "black"
            }
        },
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    ),
    paper_bgcolor='lightgray',plot_bgcolor="lightgray"
)

# Données pour la deuxième figure
df2 = px.data.gapminder().query("year == 2007")

# Créer la deuxième figure
fig2 = px.scatter(df2, x="gdpPercap", y="lifeExp", size="pop", color="continent",height=350, hover_name="country")
fig2.update_layout(
    legend=dict(
        title={
            'text': "Légende 2",
            'font': {
                'size': 14,
                'color': "black"
            }
        },
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    ),
    paper_bgcolor='lightgray',plot_bgcolor="lightgray"
)

# Données pour la troisième figure
df3 = px.data.tips()

# Créer la troisième figure
fig3 = px.bar(df3, x="day", y="total_bill", color="sex",height=350)
fig3.update_layout(
    legend=dict(
        title={
            'text': "Légende 3",
            'font': {
                'size': 14,
                'color': "black"
            }
        },
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    ),
    paper_bgcolor='lightgray',plot_bgcolor="lightgray"
)

# Afficher les trois figures dans Streamlit
col1, col2, col3 = st.columns(3)
with col1:
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.plotly_chart(fig2, use_container_width=True)
with col3:
    st.plotly_chart(fig3, use_container_width=True)