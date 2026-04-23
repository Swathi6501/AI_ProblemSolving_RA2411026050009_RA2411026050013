🚀 AI PROBLEM SOLVING ASSIGNMENT
📌 Repository Name

AI_ProblemSolving_RA2411026050009_RA2411026050013

👥 Team Members
Swathi (Reg No: RA2411026050009)
Teammate (Reg No: RA2411026050013)
🧠 OVERVIEW

This project demonstrates Artificial Intelligence problem-solving using graph-based algorithms and constraint satisfaction techniques. It focuses on two major areas:

Graph Traversal (BFS & DFS)
Constraint Satisfaction Problem (Map Coloring)

These are fundamental AI concepts used in:

Navigation systems (like GPS)
Scheduling systems
Optimization problems
Network routing systems
🚀 SMART NAVIGATION SYSTEM (BFS & DFS)
📌 Problem Statement

The Smart Navigation System finds a path between a start node and a goal node using graph traversal techniques. It compares Breadth First Search (BFS) and Depth First Search (DFS) to show how different strategies explore a graph.

🧠 Concept Explanation

A graph is used to represent connected locations:

Nodes → Locations
Edges → Paths between locations

The system determines how to reach a destination using two different AI search strategies.

⚙️ Algorithms Used
✔ Breadth First Search (BFS)
Explores level by level
Guarantees shortest path in unweighted graphs
Uses queue data structure
✔ Depth First Search (DFS)
Explores deeper paths first
Uses recursion/stack
Does not guarantee shortest path
🔄 Working Process
Graph is created from user input
Start and goal nodes are defined
BFS finds shortest possible path
DFS explores deep alternative paths
Both results are visualized and compared
🎯 Features
Interactive graph input system
BFS shortest path visualization
DFS traversal visualization
Clear comparison between algorithms
Clean UI using Streamlit
📥 Input Format
A:B,C
B:D,E
C:D
D:F
E:F
F:

Start Node: A
Goal Node: F

📊 Output Explanation
BFS Path: Finds shortest route
DFS Path: Finds one valid traversal route
Graph visualization highlights both paths
⏱ Complexity
BFS: O(V + E)
DFS: O(V + E)

Where:

V = number of vertices
E = number of edges
📸 Screenshots (Smart Navigation)
Input Interface

BFS Execution

DFS Execution

🎨 MAP COLORING PROBLEM (CSP)
📌 Problem Statement

The Map Coloring Problem is a Constraint Satisfaction Problem where regions of a graph must be colored such that no two adjacent regions share the same color.

This is used in:

Scheduling problems
Frequency allocation
Resource distribution systems
🧠 Concept Explanation

Each region is treated as a variable, and each color is a possible value.
The constraint ensures that no two adjacent nodes share the same color.

The system tries different combinations and uses backtracking when conflicts occur.

⚙️ Algorithm Used
✔ Backtracking Algorithm
Assigns colors step-by-step
Checks constraints at every step
Backtracks when conflict is found
✔ Constraint Satisfaction Problem (CSP)
Ensures all constraints are satisfied
Eliminates invalid assignments efficiently
🔄 Working Process
Graph is created from input
Nodes represent regions
Edges represent adjacency constraints
Colors are assigned one by one
If conflict occurs → backtracking is applied
Final valid solution is generated
🎨 Features
Interactive Streamlit UI
Step-by-step visualization
Color assignment tracking
Graph coloring display
Clean and modern UI design
📥 Input Format
A:B,C
B:C,D
C:D
D:
📊 Output Explanation
Each node gets a valid color
No adjacent nodes share same color
Step-by-step solving process is displayed
⏱ Complexity

Time Complexity: O(C^V)

Where:

V = number of nodes
C = number of colors
📸 Screenshots (Map Coloring CSP)
Input Interface

Step-by-step Execution

Final Output

🏁 FINAL CONCLUSION (BOTH PROJECTS)

This project successfully demonstrates two fundamental Artificial Intelligence techniques:

✔ Graph Search Algorithms (BFS & DFS)
Used for pathfinding and navigation
Helps find optimal or alternative routes
Widely used in real-world systems like GPS navigation
✔ Constraint Satisfaction Problem (Map Coloring)
Solves optimization under constraints
Ensures valid assignment of resources
Used in scheduling, allocation, and planning systems
🚀 Overall Learning Outcome

Through this project, we learned:

How AI solves real-world problems using graphs
How search algorithms explore decision spaces
How constraints are used to eliminate invalid solutions
How backtracking improves problem-solving efficiency
How visualization helps understand AI behavior
🧠 Final Insight

Both projects together show how AI systems:

Search for solutions (BFS/DFS)
Validate constraints (CSP)
Make intelligent decisions step-by-step
Represent real-world computational thinking models