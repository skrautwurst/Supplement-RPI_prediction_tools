#### RNA-protein interaction predictions without high-throughput data: an overview and benchmark of *in silico* tools

This repository contains supplementary files and information for the publication Krautwurst and Lamkiewicz (2024, doi: ).

`tool_collection.md`  
    Collection of all RPI prediction tools gathered during initial literature research. Contains basic information on each tool and their availability status.

`HTS_RPI_tools.md`  
    RPI prediction tools which are focused on the availability or usage of HTS datasets. These were not evaluated in our study, except otherwise noted.

`tool_evaluation.xlsx`  
    Evaluation information and results of the evaluated RPI prediction tools in our study.

`tool_evaluation-score.md`  
    Reasoning and information on the distribution of evaluation score points for all evaluated tools.  

`evaluation_table.csv`  
    Evaluation result values from `tool_evaluation.xlsx`, as `csv` for further processing/plotting of the data (does not include post-processing potential).

`evaluation_table_withppp.csv`  
    Evaluation result values from `tool_evaluation.xlsx`, as `csv` for further processing/plotting of the data (includes post-processing potential).

`guidetree_tools.pdf/png`  
    Guide tree figure in high resolution.

`examples_figure.pdf`  
    Figure of the four investigated biological RPI examples, with the interactions visualized based on the available literature.

`evaluation_heatmap.pdf`  
    Evaluation heatmap in high resolution.

`plot_heatmap.py`  
    In-house python script for plotting the `evaluation_heatmap` based on the `evaluation_table.csv`.
