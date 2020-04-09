<h1> Cycles Detection in an Undirected Graph</h1>
<p>In this code, you can create an undirected graph and add its edges; then,
the code finds all cycles also cycles of the cycle in the graph and print its members.
The main idea is finding one cycle at the time and destroy it, then repeat this process until no cycle will be found
in the graph. in the final, your graph will not have any cycle in it. For example, consider the following undirected graph:</p>
<img src = "https://github.com/amoazeni75/detect_cycles_undirected_graph/blob/master/graph.png" >
<p>When run the code, you see this out put</p>
<div>
  <code>
  members [2, 3, 4, 1, 0]
</code>
</div>
<div>
<code>
  members [9, 8, 7]
</code>
  </div>
  <div>
<code>
  members [5, 10, 9, 8, 7, 2, 3]
</code>
  </div>
  <div>
<code>
  members [6, 5, 10, 9, 8, 7, 2, 3, 4]
</code>
</div>
