# README
Implementation of  "On-Accelerating-Multi-Layered-Heterogeneous-Network-Embedding-Learning"

## Requirements

- numpy
- scipy

(may have to be independently installed) or pip install -r requirements.txt to install all dependencies

## Installation

1. cd deepwalk
2. pip install -r requirements.txt
3. python setup.py install

## Usage

- **Example Usage**

  `$deepwalk --input example_graphs/karate.adjlist --number-walks 10 --representation-size 128 --walk-length 3 --window-size 2 --output karate.embeddings`

**--input**: *input_filename*

> 1. `--format adjlist` for an adjacency list, e.g:
>
>    ```
>    1 2 3 4 5 6 7 8 9 11 12 13 14 18 20 22 32
>    2 1 3 4 8 14 18 20 22 31
>    3 1 2 4 8 9 10 14 28 29 33
>    ...
>    ```
>
> 2. `--format edgelist` for an edge list, e.g:
>
>    ```
>    1 2
>    1 3
>    1 4
>    ...
>    ```
>
> 3. - `--format mat` for a Matlab .mat file containing an adjacency matrix
>
>      (note, you must also specify the variable name of the adjacency matrix `--matfile-variable-name`)

**--output**: *output_filename*

> The output representations in skipgram format - first line is header, all other lines are node-id and *d* dimensional representation:
>
> ```
> 34 64
> 1 0.016579 -0.033659 0.342167 -0.046998 ...
> 2 -0.007003 0.265891 -0.351422 0.043923 ...
> ...
> ```

## Commands

**For Politics data**:

```deepwalk --format edgelist --input Politics-UK/lists-to-community.txt --number-walks 10 --representation-size 128 --walk-length 3 --window-size 2 --output Politics-UK/lists-to-community.embeddings```

**For Olympics data**:

```deepwalk --format edgelist --input Olympics/lists-to-community.txt --number-walks 10 --representation-size 128 --walk-length 3 --window-size 2 --output Olympics/lists-to-community.embeddings```

