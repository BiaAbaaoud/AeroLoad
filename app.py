import streamlit as st
import plotly.graph_objects as go

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="AeroLoad Pro", layout="wide")
st.title("✈️ AeroLoad: Weight & Balance Visualizer")

# --- 2. INPUTS NA SIDEBAR ---
st.sidebar.header("📦 Configuração de Carga")
w_pilot = st.sidebar.slider("Piloto (kg)", 40, 150, 80)
w_pass = st.sidebar.slider("Passageiro Dianteiro (kg)", 0, 150, 0)
w_rear = st.sidebar.slider("Passageiros Traseiros (kg)", 0, 200, 0)
fuel_l = st.sidebar.slider("Combustível (Litros)", 0, 200, 100)
w_bag = st.sidebar.number_input("Bagagem (kg)", 0, 54, 0)

# --- 3. CÁLCULOS TÉCNICOS (Cessna 172) ---
EMPTY_WEIGHT = 744.0
MTOW = 1157.0
w_fuel = fuel_l * 0.721

# Cálculo Decolagem
total_w = EMPTY_WEIGHT + w_pilot + w_pass + w_rear + w_fuel + w_bag
# Momentos baseados nos braços (arms) reais em metros
moment = (744*0.98) + (w_pilot+w_pass)*0.94 + (w_rear*1.85) + (w_fuel*1.22) + (w_bag*2.41)
cg_takeoff = moment / total_w

# Cálculo Pouso (Simulando queima total de combustível)
zfw_w = total_w - w_fuel
zfw_moment = moment - (w_fuel * 1.22)
cg_landing = zfw_moment / zfw_w if zfw_w > 0 else 0

# --- 4. ALERTAS E MÉTRICAS ---
# Verifica se o peso e o CG (decolagem e pouso) estão dentro dos limites
safe = (total_w <= MTOW) and (0.88 <= cg_takeoff <= 1.20) and (0.88 <= cg_landing <= 1.20)
status = "✅ VOO SEGURO" if safe else "🚨 ALARME: VOO PERIGOSO"

if safe: 
    st.success(status)
else: 
    st.error(status)

c1, c2, c3 = st.columns(3)
c1.metric("Peso Decolagem", f"{total_w:.2f} kg", 
          delta=f"{total_w-MTOW:.1f} kg" if total_w > MTOW else None, delta_color="inverse")
c2.metric("CG Decolagem", f"{cg_takeoff:.3f} m")
c3.metric("CG Pouso", f"{cg_landing:.3f} m")

# --- 5. GRÁFICO DE ENVELOPE DINÂMICO ---
fig = go.Figure()

# Envelope Verde (Área de Segurança)
fig.add_trace(go.Scatter(
    x=[0.88, 0.88, 1.05, 1.20, 1.20, 0.88],
    y=[600, 880, 1157, 1157, 600, 600],
    fill="toself",
    name='Área Segura',
    fillcolor='rgba(0, 255, 0, 0.2)', 
    line=dict(color='green', width=2)
))

# Trajetória de Voo (Decolagem -> Pouso)
fig.add_trace(go.Scatter(
    x=[cg_takeoff, cg_landing],
    y=[total_w, zfw_w],
    mode='lines+markers+text',
    name='Trajetória de Queima',
    text=["DECOLAGEM", "POUSO"],
    textposition="top center",
    line=dict(color='yellow' if safe else 'red', width=4),
    marker=dict(size=12, color=['white', 'cyan'])
))

fig.update_layout(
    title="Gráfico de Estabilidade Longitudinal",
    xaxis_title="Centro de Gravidade (Metros)",
    yaxis_title="Peso Total (kg)",
    template="plotly_dark",
    xaxis=dict(range=[0.8, 1.3], gridcolor='gray'),
    yaxis=dict(range=[500, 1300], gridcolor='gray'),
    height=600
)

st.plotly_chart(fig, use_container_width=True)