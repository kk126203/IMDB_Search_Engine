
The priority of this search engine : 

First priority is that if words in the input string show up in name of the movies, then it will be selected.

Second priority is that if the input string matches any sentence in the wiki of the movies, then it will be selected.

Third priority is that we split the input string by space into words, and count how many times these words appear in the wiki of the movies, then select it and sort by that numbers



Reference : 

Thanks for Mr.Aakash Japi who provides an efficient data structure to manipulate the search. I refered to his index table that is used to store the position of the words in each file, and implement the algorithm myself to acheive the searching and result ranking of this IMDB movie search engine.

source : http://aakashjapi.com/fuckin-search-engines-how-do-they-work/
