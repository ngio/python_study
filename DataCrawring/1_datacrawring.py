
    #movie_df = pd.DataFrame(dataset, index=view_seq)  # DataFrame에 적재
    movie_df = pd.DataFrame(dataset)  # DataFrame에 적재
    #movie_df = movie_df.set_index('title') # 인덱스 설정
    movie_df = movie_df.set_index('viewSeq') # 인덱스 설정
    movie_df2 = movie_df.drop_duplicates("synopsis", keep='first')  # 중복제거
    print(movie_df2.shape)  # .shape를 통해 dataframe의 row와 column 수를 알 수 있다
    print(len(movie_df2.index)) 
    print(list(movie_df2.columns))
