FTC - CYK Implementation (Lange, Leiss)
Implementation of the conversion of a GLC to Chomsky's Normal Form and Binary Normal Form. Along with the implementation of the CYK algorithm and Modified CYK proposed in the (Lange, Leiss) paper.

Danniel Henrique, João Amorim

## Instructions:
Grammar files are read from the grammar folder. If wanting to input sentences by file, use the folder sentence.
Output folder shows the result from using the algorithm.

## Ready to Use:

```
python main.py CYK grammar_3 "" grammar_3_input.txt True     # Default config

python main.py CYK_Mod grammar_3 "" grammar_3_input.txt True # CYK by Lange & Leiss


# run with sentence input from terminal:
python main.py CYK_Mod grammar_5_large 000011111 "" False
                                       # Sentence
```

How to use:
- Run main.py with or without parameters. 
- If with parameters, the following is the order:

- python main.py [CYK, CYK_Mod] [filename] [single sentence] [filename of sentences] [True, False depending on Testing time]

