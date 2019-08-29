city = ['New York City (NYC)','Mexico City','Delhi','Paris','Bangkok'] #10,000 per category
lang_list = ['en','es','hi','fr','th']
topics   ={
            'Environment':['outbreak','contamination','pollution','wildlife-conservation','endangered-species','climate-change','global-warming','landslide','scarcity','ocean-dump','oil-spill','consumerism','GMO','deforestation','natural-disaster','overpopulation','soil-contamination','marine-life','calamity','drought','famine','flood','smog','acid-rain','storm'],
            'Crime' : ['trafficing','murder','suspect','cops','police','arrest','sentenced','abduction','drug abuse','fraud','violence','homicide','genocide','theft','illegal','crime','detention','criminal'],
            'Politics' : ['political','economy','assembly','senate','election','lok-sabha','rajya-sabha','PM','MP','parliament','MLA','minister','president','committee','Congress','republican','BJP','white-house','UN','National-People’s-Congress','National-Assembly','REM-(La-République-En-Marche)','LR','Socialist-party'],
            'Social Unrest' : ['riot','social-unrest','anarchy','rebellion','contraversy','protest','strike','bandh','agitation','up-roar','political-movement','social-revolution'],
            'Infrastructure' : ['infrastructure','roadways','railways','waterlines','electical-grid','sanitation','gasline','bridge','tunnel','telecom','airport']
          }
count = 0

search_dict = {}

for c in city:
    for topic,query in topics.items():
        for l in lang_list:
            Key = c +'_'+ topic +'_'+ l #Key
            Value = ' OR '.join(query) + ' -RT ' + c + ' lang:' + l #Value
            search_dict[Key]=Value
            count+=1

#print(count)
#print(list(search_dict.keys())[0])    
#print(list(search_dict.values())[0])
#print(list(search_dict.keys())[0].split(','))
return search_dict
