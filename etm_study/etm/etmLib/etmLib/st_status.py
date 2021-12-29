from .s3_func import return_s3_list


def st_build_year_chore_list(out, start_year, end_year, product):
    years_hash = {}
    chore_list=[]
    print(out)
    years = range(start_year, end_year+1)
    for year in years:
        path= out + str(year)
        print(path)
        s3_list = return_s3_list('dev-et-data', path)
        prod_list=[]
        for (key,sz) in s3_list:
            if product in key:
                prod_list.append(key)
        if len(prod_list) >= 377:
            print("377 or greater")
        else:
            chore_year = year
            chore_list.append(chore_year)
    return chore_list

def st_build_year_counts(out, start_year, end_year, product):
    years_hash = {}
    chore_list=[]
    print(out)
    years = range(start_year, end_year+1)
    for year in years:
        path= out + str(year)
        print(path)
        s3_list = return_s3_list('dev-et-data', path)
        prod_list=[]
        for (key,sz) in s3_list:
            if product in key:
                prod_list.append(key)
            len_count = len(prod_list) 
            years_hash[year] = len_count
    return years_hash
