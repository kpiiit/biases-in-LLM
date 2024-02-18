# Directory structure
```bash
├── task1
│   ├── caste_file.py - code on caste to extarct data from file
│   ├── caste_final.py - code on caste to extract data from list provided in code
│   ├── gender_disco.py - gender code
│   ├── last2.txt - consist of template for religion and caste
│   ├── output.txt - names of male and female for gender code
│   ├── regionleast10.py - region code for least 10 stereotyped entries in dataset
│   ├── regionmostoccurring.py - region code for top 10 most occurring entries in dataset
│   ├── regiontop10.py - region code for top 10 most stereotyped entries in dataset
│   └── religion_final.py - religion code
└── task2
    ├── alpha
    │   ├── alpha.jsonl - json file with prompt
    │   ├── caste_data.txt - seperated caste data
    │   ├── caste_write.py - code to separate caste data having bias
    │   ├── code1.py - intial code to separate based on region ,caste and religion
    │   ├── extracted_data.txt - extracted region data
    │   ├── graph_caste.py - graph plotted for caste
    │   ├── graph.py - graph plotted for region
    │   ├── metric.py - f1 score metrics used in code
    │   ├── output_file_caste.txt - filtered biased entries of caste
    │   ├── output_file_religion.txt - filtered biased entries of religion
    │   ├── output_file.txt - filtered biased entries of region
    │   ├── religion_data.txt - initial data of religion without filteration
    │   ├── religion_graph.py - religion graph
    │   ├── religion_write.py - code to separate religion data having bias
    │   ├── sections.py - code to check how many law sections have been used in jsonl file
    │   └── write.py - code to separate region data having bias
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
- FOR TASK 1 YOU NEED TO RUN ALL PYTHON FILES IN DIRECTORY OF TASK1
- FOR TASK 2 YOU NEED TO RUN 3 FILES IN EACH SUBDIRECTORY OF TASK2
- FILES TO BE EXECUTED IN TASK 2
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
- In codes, file paths need to be changed in order to run it properly
