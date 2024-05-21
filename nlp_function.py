from web_scrapping_function import get_urls,extract_text_from_div,extract_date_from_url
import pandas as pd
from transformers import pipeline

url_list=get_urls("https://finance.yahoo.com/")
url=url_list[0]


def sentiment_with_date_and_org(url):
    
    #extraction of data
    text=extract_text_from_div(url)
    date=extract_date_from_url(url)
    #sumarize
    summarizer=pipeline("summarization")
    outputs=summarizer(text,max_length=57,clean_up_tokenization_spaces=True)
    summarized_text_str = str(outputs[0]['summary_text'])
    
    #entity detection
    ner_tagger=pipeline("ner",aggregation_strategy="simple")
    outputs_ner=ner_tagger(summarized_text_str)
    org_entities = [entity['word'] for entity in outputs_ner if entity['entity_group']== 'ORG']
    org_entities=org_entities[0]
    #sentiment 
    classifier=pipeline("text-classification")
    outputs_sentiment=classifier(summarized_text_str)[0]['score']
  

    return date,org_entities,outputs_sentiment

     

