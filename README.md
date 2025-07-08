# CosmereMindMap (in progress)


An ongoing exploratory project where I’m building mind maps of character relationships and POV dynamics using Python. My end goal is creating a full mindmap of character relationships for Brandon Sanderson’s Stormlight Archive books. 

This is my first time developing a narrative mind map, so I’ve also built test projects using the Coppermind Wiki chapter summaries as well as the full Pride and Prejudice (via Project Gutenberg) book to prototype parsing, co-mention logic, and network graph visualizations.

Tools include pandas, networkx, matplotlib, and other Python libraries for text processing and data visualization.



# What is a MindMap?
The mind map is a graph-based visualization where:

Nodes represent characters.

Edges represent co-mentions within the same chapter or scene.

Edge weight increases based on the frequency of co-mentions, highlighting stronger character relationships or repeated narrative intersections.




# Files 
```
├── README.md      # Project overview
├── PaP.ipynb      # Test mindmap using Pride and Prejudice text
├── TWoK_Coppermind.ipynb      # Jupyter notebook on mindmap for coppermind summaries
├── TWoK_Coppermind.py      # Python file on mindmap for coppermind summaries
├── data/
│   ├── TWoK_chapter_summaries.csv      # raw data for coppermind summaries, made personally
│   └── Pride_and_Prejudice.txt      # raw Pride and Prejudice text gotten from Project Gutenberg
├── src/
│   └── text_cleaner.py      # text cleaning pipeline for using throughout project
```
