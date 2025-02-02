# Venn Diagram Visualization with Python
### Overview
This project was developed for my CSC 230 course to visualize relationships between three sets using Venn diagrams. The sets represent different groups, and the script dynamically labels the diagram based on their intersections.

### Features
- **Generates a Venn diagram** with three sets (`A`, `B`, and `C`).
- **Automatically labels** each region with the corresponding elements.
- **Uses Python's `matplotlib_venn`** for visualization.

### Technologies Used
- Python
- Matplotlib (for plotting)
- matplotlib_venn (for creating Venn diagrams)
  
### How to Run
1. Install the required libraries:
   ```bash
   pip install matplotlib matplotlib_venn
2. Run the script:
   ```bash
   python venn_diagram.py
3. A Venn diagram will be displayed, showing the elements in each set and their intersections.

### Example Sets
- A = {'a', 'b', 'c', 'k', 'm', 'n', 'p', 'q', 'r', 'v', 'w', 'x'}
- B = {'d', 'e', 'f', 'k', 'm', 'n', 's', 't', 'u', 'v', 'w', 'x'}
- C = {'g', 'h', 'j', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'}

### Future Improvements
- Expand to support more than three sets.
- Allow user input for dynamic set creation.
- Add additional analysis tools for set relationships.
