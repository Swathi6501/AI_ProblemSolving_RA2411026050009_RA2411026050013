import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import time
from csp_solver import map_coloring_with_steps

# ================= PAGE =================
st.set_page_config(page_title="AI Map Coloring CSP", layout="wide")

# ================= PREMIUM FONT + STYLE =================
st.markdown("""
<style>
/* 🌈 BACKGROUND */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(120deg, #ffd6e0, #c1f0dc, #c7d2ff, #ffe9f3);
    background-size: 400% 400%;
    animation: bgFlow 16s ease infinite;
}

@keyframes bgFlow {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* 🎨 ULTIMATE FONT - SYNE (SUPER MODERN + ELEGANT + PERFECT) */
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"], .stMarkdown {
    font-family: 'Syne', -apple-system, BlinkMacSystemFont, sans-serif !important;
    font-size: 15.8px;
    font-weight: 400;
    line-height: 1.65;
    letter-spacing: -0.01em;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    color: #1e293b !important;
    letter-spacing: -0.025em;
}

/* 🌈 BUTTON */
.stButton > button {
    background: linear-gradient(135deg, #f472b6 0%, #60a5fa 50%, #34d399 100%);
    color: white !important;
    border-radius: 14px;
    padding: 14px 28px;
    font-weight: 600;
    font-size: 16px;
    border: none;
    transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    box-shadow: 0 10px 30px rgba(244, 114, 182, 0.4);
    font-family: 'Syne', sans-serif !important;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 15px 40px rgba(96, 165, 250, 0.5);
    background: linear-gradient(135deg, #ec4899 0%, #3b82f6 50%, #10b981 100%);
}

/* 📚 CONTAINERS */
.edu-container {
    background: rgba(255,255,255,0.98);
    border-radius: 24px;
    padding: 2.5rem;
    box-shadow: 0 25px 80px rgba(0,0,0,0.12);
    border: 1px solid rgba(255,255,255,0.9);
    margin: 2rem 0;
}

.step-explanation {
    background: linear-gradient(135deg, #fef7ff 0%, #f0f9ff 50%, #f0fdf4 100%);
    border-radius: 16px;
    padding: 1.3rem;
    border-left: 6px solid #ec4899;
    margin: 0.8rem 0;
    box-shadow: 0 8px 25px rgba(244, 114, 182, 0.15);
}

.color-table { background: rgba(255,255,255,0.9); border-radius: 12px; border: 1px solid #e2e8f0; font-size: 14px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); }

.summary-card {
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    border-radius: 16px;
    padding: 1.5rem;
    border-left: 5px solid #10b981;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown("""
<div style='text-align: center; padding: 2.5rem 0 1.5rem 0;'>
    <h1 style='font-size: 3rem; color: #1e293b; margin: 0 0 0.8rem 0; letter-spacing: -0.03em;'>
        🧠 Map Coloring CSP
    </h1>
    <p style='color: #64748b; font-size: 1.25rem; font-weight: 500; margin: 0; max-width: 600px; margin: 0 auto;'>
        Learn Backtracking Algorithm Step-by-Step
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ================= INPUT =================
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📝 Your Map Data")
    st.markdown("<small><code>A:B,C</code> = Region A borders B and C</small>", unsafe_allow_html=True)
    graph_input = st.text_area("", height=130, placeholder="A:B,C\nB:A,D\nC:A\nD:B")

with col2:
    st.markdown("### 🎯 The Challenge")
    st.markdown("""
    <div class='summary-card'>
    <strong>Rule:</strong> Adjacent regions <strong>cannot</strong> have same color<br>
    <strong>Colors:</strong> 🔴Red 🟢Green 🔵Blue 🟡Yellow<br>
    <strong>AI Goal:</strong> Color entire map perfectly
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ================= ANIMATION =================
if st.button("▶️ Start Animation", use_container_width=True):
    if not graph_input.strip():
        st.error("⚠️ Enter map data first")
        st.stop()

    graph = {}
    for line in graph_input.split("\n"):
        if ":" in line.strip():
            node, neighbors = line.split(":", 1)
            graph[node.strip()] = [n.strip() for n in neighbors.split(",") if n.strip()]

    st.markdown('<div class="edu-container">', unsafe_allow_html=True)
    st.markdown("## 📈 Step-by-Step Learning")
    
    with st.spinner("Analyzing map..."):
        steps = map_coloring_with_steps(graph, ["Red", "Green", "Blue", "Yellow"])
    
    G = nx.Graph()
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    graph_col, explanation_col = st.columns([0.6, 1.4])  # Even tighter for small graph
    progress = st.progress(0)
    
    step_explanations = [
        "🔍 <strong>1. Start with Region A</strong><br>No colors assigned yet. Pick first region.",
        "🎨 <strong>2. Try Red for A</strong><br>A has no colored neighbors. Red ✓ works!",
        "🔍 <strong>3. Move to Region B</strong><br>B neighbors A (Red). Cannot use Red.",
        "⚠️ <strong>4. Green fails for B</strong><br>Try next color... Blue available.",
        "✅ <strong>5. Blue ✓ for B</strong><br>Neighbors approve. Lock in Blue.",
        "🔄 <strong>6. Continue process</strong><br>Next region → try colors → check conflicts.",
        "✨ <strong>7. Backtrack example</strong><br>If conflict found, undo and retry.",
        "🎉 <strong>8. Solution complete!</strong><br>All regions colored perfectly."
    ]
    
    for i, step in enumerate(steps):
        with graph_col:
            # EXTREMELY SMALL GRAPH (1.4x1.2 - TINY PERFECT)
            fig, ax = plt.subplots(figsize=(1.4, 1.2), facecolor='white')
            
            node_colors = []
            for node in G.nodes():
                color = step.get(node, "lightgray")
                node_colors.append(color.lower() if color != "lightgray" else "#f8fafc")
            
            pos = nx.spring_layout(G, k=0.7, iterations=50)
            nx.draw(G, pos, ax=ax, with_labels=True, node_color=node_colors,
                   node_size=400, font_size=7.5, font_weight="bold",
                   font_color="white", edge_color="#cbd5e1", width=1.2)
            ax.set_title("Map", fontsize=8.5, fontweight="bold", pad=3)
            plt.tight_layout(pad=0.3)
            st.pyplot(fig)

        with explanation_col:
            current_node = list(step.keys())[-1] if step else list(G.nodes())[0]
            current_color = step.get(current_node, "None")
            progress.progress((i + 1) / len(steps))
            
            st.markdown(f"""
            <div class="step-explanation">
                <h4 style='margin: 0 0 0.8rem 0; color: #1e293b; font-size: 1.1rem;'>
                    Step {i+1}: {step_explanations[min(i, len(step_explanations)-1)].split('<strong>')[1].split('</strong>')[0]}
                </h4>
                <div style='font-size: 13.5px;'>
                    {step_explanations[min(i, len(step_explanations)-1)]}
                </div>
                <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem; margin-top: 1rem; font-size: 13px; padding-top: 0.8rem; border-top: 1px solid #e2e8f0;'>
                    <div>
                        <strong>Region:</strong> <span style='color: #ec4899; font-weight: 600;'>{current_node}</span><br>
                        <strong>Color:</strong> <span style='color: #10b981; font-weight: 600;'>{current_color}</span>
                    </div>
                    <div style='text-align: right;'>
                        <strong>Progress:</strong> {len([v for v in step.values() if v != 'lightgray'])}/{len(G)}<br>
                        <strong>Step:</strong> {i+1}/{len(steps)}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            colored = {k: v for k, v in step.items() if v != "lightgray"}
            if colored:
                st.markdown("**📋 Colors:**")
                st.dataframe(colored, use_container_width=True, height=60, hide_index=True)

        time.sleep(1.2)

    st.markdown('</div>', unsafe_allow_html=True)

# ================= SUMMARY =================
st.markdown('<div class="edu-container">', unsafe_allow_html=True)
st.markdown("## 📖 Final Summary")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 🔍 Backtracking Process
    <div class='summary-card'>
    1. **Choose** uncolored region<br>
    2. **Try colors** in order (R→G→B→Y)<br>
    3. **Validate** with neighbors<br>
    4. **Success → continue**<br>
    5. **Fail → backtrack**
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    ### ✅ Why 4 Colors Work
    <div class='summary-card'>
    - <strong>Map Theorem:</strong> 4 colors always enough<br>
    - <strong>Efficient:</strong> Prunes wrong paths early<br>
    - <strong>Complete:</strong> Finds solution if exists<br>
    - <strong>Scalable:</strong> Works for any map
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style='background: linear-gradient(135deg, #fefce8 0%, #fef3c7 100%); border-radius: 20px; padding: 2.5rem; text-align: center; border-left: 6px solid #eab308; margin-top: 2rem;'>
    <h3 style='color: #92400e; margin-bottom: 1.5rem;'>📋 Final Summary</h3>
    <p style='font-size: 1.15rem; font-weight: 500; color: #a16207; max-width: 900px; margin: 0 auto; line-height: 1.7;'>
    CSP Backtracking systematically explores color combinations while <strong>eliminating invalid choices early</strong>. 
    This guarantees finding the <strong>perfect map coloring</strong> using just 4 colors efficiently!
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)