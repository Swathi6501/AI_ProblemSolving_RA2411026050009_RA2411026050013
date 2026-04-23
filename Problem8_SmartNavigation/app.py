import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

from bfs_dfs import bfs, dfs

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart Navigation", layout="wide")

# ---------------- INITIAL VARIABLES ----------------
bfs_path = None
dfs_path = None

# ---------------- UI STYLE ----------------
st.markdown("""
<style>

/* 🔥 GOOGLE FONTS */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg,
        #f8bbd0,
        #bbdefb,
        #c8e6c9,
        #e1bee7,
        #b2dfdb
    );
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;

    font-family: 'Poppins', 'Inter', sans-serif;
    font-size: 16.5px;
    color: #1f2d3d;
}

/* ANIMATION */
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* TITLE */
h1 {
    text-align: center;
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
    font-size: 40px;
    color: #1c2b36;
    letter-spacing: 1px;
}

/* SUBTITLE */
h3 {
    text-align: center;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    font-size: 22px;
    color: #37474f;
}

/* INPUT */
textarea, input {
    border-radius: 10px !important;
    padding: 10px !important;
    border: 1px solid #ccc !important;
    font-family: 'Inter', sans-serif;
}

/* BUTTON */
.stButton>button {
    background: linear-gradient(135deg, #f48fb1, #90caf9, #a5d6a7);
    color: black;
    font-weight: 600;
    border-radius: 12px;
    padding: 10px 20px;
    border: none;
    transition: all 0.3s ease-in-out;
    font-family: 'Poppins', sans-serif;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0px 6px 18px rgba(0,0,0,0.25);
}

.stButton>button:focus {
    outline: none !important;
    box-shadow: none !important;
}

/* GLASS CARDS */
.card {
    background: rgba(255, 255, 255, 0.75);
    backdrop-filter: blur(12px);
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.12);
    border: 1px solid rgba(255,255,255,0.3);
}

/* SPACING */
.block-container {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("# 🚀 Smart Navigation System")
st.markdown("### BFS & DFS Path Visualizer")

st.markdown("---")

# ---------------- INPUT ----------------
st.markdown("## 🧩 Enter Graph")

graph_input = st.text_area("Graph Input", height=120)

col1, col2 = st.columns(2)
with col1:
    start = st.text_input("Start Node")
with col2:
    goal = st.text_input("Goal Node")

# ---------------- GRAPH PARSER ----------------
def parse_graph(text):
    graph = {}
    for line in text.strip().split("\n"):
        if ":" in line:
            node, neighbors = line.split(":")
            graph[node.strip()] = [n.strip() for n in neighbors.split(",") if n.strip()]
    return graph

# ---------------- DRAW GRAPH ----------------
def draw_graph(graph, path=None):
    G = nx.DiGraph()

    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G, seed=42)

    fig, ax = plt.subplots(figsize=(5, 4))

    nx.draw(G, pos,
            with_labels=True,
            node_color="#bbdefb",
            node_size=1500,
            font_weight='bold',
            ax=ax)

    if path:
        nx.draw_networkx_nodes(G, pos,
                               nodelist=path,
                               node_color="#66bb6a",
                               node_size=1700,
                               ax=ax)

        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos,
                               edgelist=edges,
                               edge_color="#2e7d32",
                               width=2.5,
                               ax=ax)

    return fig

# ---------------- MAIN ----------------
if st.button("✨ Find Path"):

    if not graph_input or not start or not goal:
        st.warning("Please fill all inputs")

    else:
        graph = parse_graph(graph_input)

        bfs_path = bfs(graph, start, goal)
        dfs_path = dfs(graph, start, goal)

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("🔵 BFS Result")

            if bfs_path:
                st.success(" → ".join(bfs_path))
                st.pyplot(draw_graph(graph, bfs_path))
            else:
                st.error("No path found")

            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("🟢 DFS Result")

            if dfs_path:
                st.success(" → ".join(dfs_path))
                st.pyplot(draw_graph(graph, dfs_path))
            else:
                st.error("No path found")

            st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FINAL SUMMARY (EDUCATIONAL + ENGAGING VERSION) ----------------
st.markdown("## 🧾 Final Summary")

if bfs_path is not None and dfs_path is not None:

    st.markdown("""
<div style="
    background: linear-gradient(135deg, #ffffff, #f3e5f5, #e3f2fd, #e8f5e9);
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.12);
    font-family: 'Poppins', 'Inter', sans-serif;
    font-size: 17px;
    line-height: 1.75;
">

### 🌟 1.This Project Demonstrates

This system shows how **graph search algorithms** explore the same network in completely different ways.

Even though BFS and DFS work on the same graph:
- They **do not think the same way**
- They **do not explore the same nodes in the same order**
- They can produce **different paths to the same destination**

---

### 🧠 2. BFS(Breadth First Search) – Intelligent Layer-by-Layer Search

<div style="background:#e3f2fd;padding:12px;border-radius:10px;margin:8px 0;">
✔ BFS explores the graph **level by level**
</div>

✔ It first checks all nearby nodes before going deeper  
✔ Always guarantees the **shortest path (in unweighted graphs)**  
✔ Works like a **ripple expanding in water**

💡 Real-world analogy:  
Think of Google Maps finding the **fastest route**

---

### 🔍 3. DFS (Depth First Search) – Deep Exploration Strategy

<div style="background:#e8f5e9;padding:12px;border-radius:10px;margin:8px 0;">
✔ DFS explores one path **as deep as possible first**
</div>

✔ It may go far away from the goal before coming back  
✔ Does NOT guarantee the shortest path  
✔ Works like **exploring a maze blindly until a dead end**

💡 Real-world analogy:  
Trying every possible road in a maze until one works

---

### ⚖️ 4. Key Difference (Important Insight)

✔ BFS = Structured + Optimal + Shortest Path  
✔ DFS = Deep + Exploratory + Flexible  

👉 Same graph, but completely different thinking strategies

---

### 🚀 5. Final Learning Conclusion

This project clearly demonstrates that:

✔ Algorithms are not just code — they represent **different ways of thinking**  
✔ BFS is ideal when **efficiency matters**  
✔ DFS is ideal when **exploration matters**  
✔ Choosing the right algorithm is critical in AI problem solving

---

### 🎯 6. Real AI Relevance

This Concept is used in:
- 🗺️ Google Maps (routing systems)
- 🤖 AI search problems
- 🎮 Game decision trees
- 🧩 Puzzle solving systems

</div>
""", unsafe_allow_html=True)