from web_scrapping_function import get_urls,extract_text_from_div,extract_date_from_url
import pandas as pd
from transformers import pipeline
from web_scrapping_function import make_mapping,replace_company_with_symbol
from data_base_function import create_db_connection,execute_list_query
from chat_gpt_api import get_stock_symbol


def make_summarizer():

    summarizer=pipeline("summarization")
    return summarizer

def make_ner_tagger():
    ner_model='dslim/distilbert-NER'
    ner_tagger=pipeline("ner",model=ner_model)
    return ner_tagger

def make_classifier():
    classifier=pipeline("summarization")
    return classifier

def shorten_text(text, max_length=1024):
   
    if len(text) > max_length:
        return text[:max_length]
    return text
 


def sentiment_with_date_and_org(url,summarizer,ner_tagger,classifier):

    
    #extraction of data
    text_long=extract_text_from_div(url)
    date=extract_date_from_url(url)
    text=shorten_text(text_long)
    
    #sumarize
    
    outputs=summarizer(text,max_length=100,clean_up_tokenization_spaces=True,)
    summarized_text_str = str(outputs[0]['summary_text'])
    
    #entity detection
    ner_tagger=pipeline("ner",aggregation_strategy="simple")
    outputs_ner=ner_tagger(summarized_text_str)
    org_entities = [entity['word'] for entity in outputs_ner if entity['entity_group']== 'ORG']
    org_entity = org_entities[0] if org_entities else "no_data"
    stock_symbol=""
    if org_entities=="no_data":
        stock_symbol="no_data"
    else:
        stock_symbol=get_stock_symbol(org_entity)
        

    #sentiment 
    classifier=pipeline("text-classification")
    label=classifier(summarized_text_str)[0]['label']
    print(label)
    outputs_sentiment=classifier(summarized_text_str)[0]['score']
    
    if label=="NEGATIVE":
        outputs_sentiment*=-1
    elif label=="NEUTRAL":
        outputs_sentiment=0
    
  

    return date,stock_symbol,outputs_sentiment

def get_results(urls):

    summarizer = make_summarizer()
    ner_tagger = make_ner_tagger()
    classifier = make_classifier()

    results = []
    
    for url in urls:
        result = sentiment_with_date_and_org(url, summarizer, ner_tagger, classifier)
        results.append(result)
        print(result)
    
    return results


def main(url, db_params):
    

    urls = get_urls(url)
    results = get_results(urls)

    mapping_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    mapping = make_mapping(mapping_url)

    processed_results = []
    for date, company, score in results:
        if company:
            processed_results.append([date, company, score])

    query = '''
    INSERT INTO news_data (news_date, company_name, sentiment_score)
    VALUES (%s, %s, %s)
    '''
    connection = create_db_connection(*db_params)
    for results in processed_results:
        execute_list_query(connection, query, results)
    
    connection.commit()

    for result in processed_results:
        print(result)


     

