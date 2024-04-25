# CMPS 2200 Recitation 08

## Answers

**Name:** Nicolas Labarca
**Name:**_________________________


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**


The work and span complexity is O(N), where N represents the number of visited edges in the graph.


- **2b)**

path = []

while destination is not None and parents.get(destination) is not None:
    path.append(destination)
    destination = parents[destination]

return ''.join(reversed(path))
