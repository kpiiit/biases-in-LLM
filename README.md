# Directory structure
```bash
├── task1
│   ├── caste_file.py
│   ├── caste_final.py
│   ├── gender_disco.py
│   ├── last2.txt
│   ├── output.txt
│   ├── regionleast10.py
│   ├── regionmostoccurring.py
│   ├── regiontop10.py
│   └── religion_final.py
└── task2
    ├── alpha
    │   ├── alpha.jsonl
    │   ├── caste_data.txt
    │   ├── caste_write.py
    │   ├── code1.py
    │   ├── extracted_data.txt
    │   ├── graph_caste.py
    │   ├── graph.py
    │   ├── metric.py
    │   ├── output_file_caste.txt
    │   ├── output_file_religion.txt
    │   ├── output_file.txt
    │   ├── religion_data.txt
    │   ├── religion_graph.py
    │   ├── religion_write.py
    │   ├── sections.py
    │   └── write.py
    ├── beta
    │   ├── beta.jsonl
    │   ├── caste_data.txt
    │   ├── caste_write.py
    │   ├── code1.py
    │   ├── extracted_data.txt
    │   ├── graph_caste.py
    │   ├── graph.py
    │   ├── metric.py
    │   ├── output_caste.py
    │   ├── output_file_caste.txt
    │   ├── output_file_religion.txt
    │   ├── output_file.txt
    │   ├── religion_data.txt
    │   ├── religion_graph.py
    │   ├── religion_write.py
    │   ├── sections.py
    │   └── write.py
    ├── delta
    │   ├── caste_data.txt
    │   ├── caste_write.py
    │   ├── code1.py
    │   ├── delta.jsonl
    │   ├── extracted_data.txt
    │   ├── graph_caste.py
    │   ├── graph.py
    │   ├── metric.py
    │   ├── output_caste.py
    │   ├── output_file_caste.txt
    │   ├── output_file_religion.txt
    │   ├── religion_data.txt
    │   ├── religion_graph.py
    │   ├── religion_write.py
    │   ├── sections.py
    │   └── write.py
    ├── epsilon
    │   ├── caste_data.txt
    │   ├── caste_write.py
    │   ├── code1.py
    │   ├── epsilon.jsonl
    │   ├── extracted_data.txt
    │   ├── graph_caste.py
    │   ├── graph.py
    │   ├── metric.py
    │   ├── output_caste.py
    │   ├── output_file_caste.txt
    │   ├── output_file_religion.txt
    │   ├── output_file.txt
    │   ├── religion_data.txt
    │   ├── religion_graph.py
    │   ├── religion_write.py
    │   ├── sections.py
    │   └── write.py
    ├── eta
    │   ├── caste_data.txt
    │   ├── caste_write.py
    │   ├── code1.py
    │   ├── eta.jsonl
    │   ├── extracted_data.txt
    │   ├── graph_caste.py
    │   ├── graph.py
    │   ├── metric.py
    │   ├── output_caste.py
    │   ├── output_file_caste.txt
    │   ├── output_file_religion.txt
    │   ├── output_file.txt
    │   ├── religion_data.txt
    │   ├── religion_graph.py
    │   ├── religion_write.py
    │   ├── sections.py
    │   └── write.py
    ├── gamma
    │   ├── caste_data.txt
    │   ├── caste_write.py
    │   ├── code1.py
    │   ├── extracted_data.txt
    │   ├── gamma.jsonl
    │   ├── graph_caste.py
    │   ├── graph.py
    │   ├── metric.py
    │   ├── output_caste.py
    │   ├── output_file_caste.txt
    │   ├── output_file_religion.txt
    │   ├── output_file.txt
    │   ├── religion_data.txt
    │   ├── religion_graph.py
    │   ├── religion_write.py
    │   ├── sections.py
    │   └── write.py
    ├── iota
    │   ├── caste_data.txt
    │   ├── caste_write.py
    │   ├── code1.py
    │   ├── extracted_data.txt
    │   ├── graph_caste.py
    │   ├── graph.py
    │   ├── iota.jsonl
    │   ├── metric.py
    │   ├── output_file_caste.txt
    │   ├── output_file_religion.txt
    │   ├── output_file.txt
    │   ├── religion_data.txt
    │   ├── religion_graph.py
    │   ├── religion_write.py
    │   ├── sections.py
    │   └── write.py
    ├── theta
    │   ├── caste_data.txt
    │   ├── caste_write.py
    │   ├── code1.py
    │   ├── extracted_data.txt
    │   ├── graph_caste.py
    │   ├── graph.py
    │   ├── metric.py
    │   ├── output_caste.py
    │   ├── output_file_caste.txt
    │   ├── output_file_religion.txt
    │   ├── output_file.txt
    │   ├── religion_data.txt
    │   ├── religion_graph.py
    │   ├── religion_write.py
    │   ├── sections.py
    │   ├── theta.jsonl
    │   └── write.py
    └── zeta
        ├── caste_data.txt
        ├── caste_write.py
        ├── code1.py
        ├── extracted_data.txt
        ├── graph_caste.py
        ├── graph.py
        ├── metric.py
        ├── output_file_caste.txt
        ├── output_file_religion.txt
        ├── output_file.txt
        ├── religion_data.txt
        ├── religion_graph.py
        ├── religion_write.py
        ├── sections.py
        ├── write.py
        └── zeta.jsonl
```
# RUN CODE
- FOR TASK 1 YOU NEED TO RUN ALL FILES IN DIRECTORY OF TASK1
- FOR TASK 2 YOU NEED TO RUN FILE IN EACH SUBDIRECTORY OF TASK2
- FILES TO BE EXECUTED IN TASK2 ARE FOR TASK 2
```
python religion_graph.py
```
```
python graph.py
```
- graph.py was for region graphs
```
python graph_caste.py
```
- The first graph on running would depict negative bias while second one will depict positive bias
