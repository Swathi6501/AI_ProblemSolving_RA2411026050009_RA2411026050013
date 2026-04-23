import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

from bfs_dfs import bfs, dfs

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart Navigation", layout="centered")

# ---------------- UI STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fce4ec, #e3f2fd, #e8f5e9);
    font-family: 'Segoe UI';
}

/* Title */
h1 {
    text-align: center;
    color: #37474f;
}

/* Button */
.stButton>button {
    background: linear-gradient(135deg, #f8bbd0, #90caf9, #a5d6a7);
    color: black;
    border-radius: 10px;
    padding: 10px 16px;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.05);
}

/* Inputs */
textarea, input {
    background-color: white !important;
    border-radius: 6px;
}

/* Card */
.card {
    background: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("# 🚀 Smart Navigation System")
st.markdown("### BFS & DFS Path Visualizer")

st.markdown("---")

# ---------------- INPUT ----------------
st.markdown("### 🧩 Enter Graph")

graph_input = st.text_area("Graph Input", height=150)

col1, col2 = st.columns(2)
with col1:
    start = st.text_input("Start Node")
with col2:
    goal = st.text_input("Goal Node")

# ---------------- PARSE ----------------
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

    fig, ax = plt.subplots()

    # default nodes
    nx.draw(G, pos, with_labels=True,
            node_color="#bbdefb",
            node_size=2000,
            font_weight='bold',
            ax=ax)

    # highlight path
    if path:
        nx.draw_networkx_nodes(G, pos,
                               nodelist=path,
                               node_color="#81c784",
                               node_size=2200,
                               ax=ax)

        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos,
                               edgelist=edges,
                               edge_color="#4caf50",
                               width=3,
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

        # BFS
        with col1:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("🔵 BFS Result")

            if bfs_path:
                st.success(" → ".join(bfs_path))
                fig = draw_graph(graph, bfs_path)
                st.pyplot(fig)
            else:
                st.error("No path found")

            st.markdown('</div>', unsafe_allow_html=True)

        # DFS
        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("🟢 DFS Result")

            if dfs_path:
                st.success(" → ".join(dfs_path))
                fig = draw_graph(graph, dfs_path)
                st.pyplot(fig)
            else:
                st.error("No path found")

            st.markdown('</div>', unsafe_allow_html=True)

        # ---------------- LEGEND ----------------
        st.markdown("## 🎨 Legend")
        st.info("""
🔵 Default Nodes  
🟢 Path Nodes  
🟩 Highlighted Edges show the path  
""")

        # ---------------- COMPARISON ----------------
        st.markdown("## ⚖️ Algorithm Comparison")

        if bfs_path and dfs_path:
            if len(bfs_path) < len(dfs_path):
                st.success("✅ BFS gives the shortest path")
            elif len(bfs_path) > len(dfs_path):
                st.warning("⚠️ DFS may not give shortest path")
            else:
                st.info("ℹ️ Both paths are equal")

        # ---------------- NOTES ----------------
        st.markdown("## 📘 Notes")

        st.write("""
- **BFS (Breadth First Search)** explores level by level and guarantees the shortest path in unweighted graphs.

- **DFS (Depth First Search)** explores deeply into one branch before backtracking.

- BFS is best for navigation problems (shortest route).

- DFS is useful in backtracking, maze solving, and recursive problems.

- Time Complexity:
  - BFS: O(V + E)
  - DFS: O(V + E)
""")