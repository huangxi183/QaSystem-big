##### input data source
  1.freebase, link: http://storage.googleapis.com/freebase-public/deleted_freebase.tar.gz? 

##### code description
  1.Using MapReduce to profile the freebase, get the three fileds out : object, predicate, subject. Some of them
   are in MID. 
  2.Then for every record get two key-value pairs <object, subject+predicate> and <subject, object+predicate>

##### screenshot description
  1.Screen Shot showed the count of lines when I put the cleaned freebase into spark
