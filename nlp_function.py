from web_scrapping_function import get_urls,extract_text_from_div,extract_date_from_url
import pandas as pd
from transformers import pipeline




def sentiment_with_date_and_org(url):

    model='mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis'
    
    #extraction of data
    text=extract_text_from_div(url)
    date=extract_date_from_url(url)
    #sumarize
    summarizer=pipeline("summarization")
    outputs=summarizer(text,max_length=100,clean_up_tokenization_spaces=True)
    summarized_text_str = str(outputs[0]['summary_text'])
    
    #entity detection
    ner_tagger=pipeline("ner",aggregation_strategy="simple")
    outputs_ner=ner_tagger(summarized_text_str)
    org_entities = [entity['word'] for entity in outputs_ner if entity['entity_group']== 'ORG']
    org_entities=org_entities[0]
    #sentiment 
    classifier=pipeline("text-classification",model=model)
    label=classifier(summarized_text_str)[0]['label']
    outputs_sentiment=classifier(summarized_text_str)[0]['score']
    
    if label=="negative": outputs_sentiment*(-1)
    
  

    return date,org_entities,outputs_sentiment

     

