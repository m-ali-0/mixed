Imported libraries: sys, xxhash

Overflow method: we have key of the files, and overflow with index to know which file is after another. 
whenever the size of the file is full, the program creates new overflow file named "{key}_{index}.txt", and adds the string to that new file.

one extra not: for the cases like running the file twice, the code deletes the text files from previous run. it looks for text files whose name start with an integer, 
so if you put an INPUT FILE IN THE FOLDER FOR CHECKING, PLEASE AVOID NAMING IT WITH AN INTEGER AT THE BEGINNING

