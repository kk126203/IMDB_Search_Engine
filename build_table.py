import re, os, operator


##Hhelper function for checking if an input string is Integer type
def Irrelevant_Integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False



## In this function, we process the words in the input file, remove some irrelavant words like 'and', 'of', 'in', and 'for', as well as the exclamation marks that is not needed. Then output the file as a list with remaining words splitted by space
## The removed words are referenced in Top 50 English stop words
def Clean_File(filename):
    stopwords = open('./stop_words.txt').read()
    p = re.compile('[\W_]+')
    cur_file = open(filename, 'r').read().lower()
    cur_file = p.sub(' ',cur_file)
    re.sub(r'[\W_]+','', cur_file)
    cur_file = cur_file.split()
    cur_file = [w for w in cur_file if w not in stopwords]
    irr_int = []
    for w in cur_file :
        if Irrelevant_Integer(w) and len(w)<4:              
            irr_int.append(w)
    cur_file = [w for w in cur_file if w not in irr_int]
    return cur_file    



## In this function, we caculate the index position of each word in the input list, so as to do the sentence matching for futher processing
def Word_Position(input_list):
    pos = {}
    for i, word in enumerate(input_list):
        if word in pos.keys():
            pos[word].append(i)
        else:
            pos[word] = [i]
            
    return pos



## In this function, we build a first table that contains a filename as a key, and a list of its words' position in the file as the table value. 
def Build_Table():
    table = {}
    arr = os.listdir('./back-end')
    for filename in arr:
        dest = './back-end/'+filename
        cur_file = Clean_File(dest)
        cur_file = Word_Position(cur_file)
        table[filename] = cur_file
    return table



## In this func, we transformed the table above to a final table that lets the words become the key of the final table, and the value is another inner table that contains a filename as its key, and a list that shows the position of the word in such file as the value of inner table.
def Final_Table(input_table):
    final_table = {}
    for filename in input_table.keys():
        for word in input_table[filename].keys():
            if word in final_table.keys():
                final_table[word][filename] = input_table[filename][word] 
            else:
                final_table[word] = {filename : input_table[filename][word]}
    return final_table


## This func implements the searching algorithm. First in each file, we extract the corresponding position list of each words of the input query, then we do the position match by subtracting its index position in the input query, then if the input query is completely in the file, there would be an integer shows up at every list, and this file will thus become the file we want.
## First priority is that if words in the input string show up in name of the movies, then it will be selected.
## Second priority is that if the input string matches any sentence in the wiki of the movies, then it will be selected.
## Third priority is that we split the input string by space into words, and count how many times these words appear in the wiki of the movies, then select it and sort by that numbers. 
def Sentence_Match(input_table, query, table1):
    stopwords = open('./stop_words.txt').read()
    p = re.compile('[\W_]+')
    query = p.sub(' ', query).lower()
    l1, output, priority1, priority2 = [], [], [], []
    arr = os.listdir('./back-end')

    query_arr = [w for w in query.split() if w not in stopwords]
    irr_int = []
    for w in query_arr :
        if Irrelevant_Integer(w) and len(w)<4:              
            irr_int.append(w)
    query_arr = [w for w in query_arr if w not in irr_int]

    for word in query_arr:
        for file in arr:
            ff = str(file.lower())[:-4]
            if word in ff and word not in output:
                priority1.append(file)
                
    
    for word in query_arr:
        if word in input_table.keys():
            l1.append(input_table[word].keys())
    if len(l1)==0:
        return []
    
    s1 = set(l1[0]).intersection(*l1)
    u1 = set(l1[0]).union(*l1)
    print(u1)
    
    for filename in s1:
        tmp = []
        for word in query_arr:
            if word in input_table.keys():
                tmp.append(input_table[word][filename])
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] -= i
        if set(tmp[0]).intersection(*tmp):
            priority2.append(filename)


    for filename in priority1:
        output.append(filename)

    print output
    
    if len(query_arr)>1:
        for filename in priority2:
            if filename not in output:
                output.append(filename)

    print output
    
    u1 = [f for f in u1 if f not in output]
    record = {}
    for file in u1:
        total = 0
        for word in query_arr :
            if word in table1[file].keys():
                cur_size = len(table1[file][word])
                total+=cur_size
        record[file] = total
        
    record = sorted(record.items(), key=operator.itemgetter(1))
    record = list(reversed(record))
    

    print record
    for file in record:
        if file not in output:
            output.append(file[0])
            
    return output

	
