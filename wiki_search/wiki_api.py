import wikipediaapi
    
def wiki_search(text):
    try:
        wiki_wiki = wikipediaapi.Wikipedia(
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )

        p_wiki = wiki_wiki.page(text)
        url = p_wiki.fullurl
    except:
        url = '請輸入正確的格式且以英文搜尋'
    
    
    return url
