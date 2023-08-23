from constants import domo_bq_map
import json

def reformat_metadata(response):
    # identify and parse the useful metadata from the response
    looker_metadata = {}
    dynamic_fields=[]
    looker_metadata['chartType']=  response['metadata']['chartType']
    looker_metadata['domoId']= response['subscriptions'][0]['cardId']
    try:
        looker_metadata['view'] = domo_bq_map.get(response['subscriptions'][0]['dataSourceName'])
    except:
        print(f"No view found for the given datasource{response['subscriptions'][0]['dataSourceName']}")
        return None
    for subscription in response['subscriptions']:
        #there are two subscriptions sometimes one for summary and one for main chart
        if subscription['subscription']['name']=='main':
            looker_metadata['fields'] = columns_to_fields(subscription['subscription']['columns'],looker_metadata['view'])
            looker_metadata['calculated']=[item["formulaId"] for item in subscription['subscription']['columns'] if item.get("formulaId")]
            card_filter,dynamic_field_f = filter_to_dict(subscription['subscription']['filters'], looker_metadata['view'],"operand")
            dynamic_fields = dynamic_fields + dynamic_field_f
            looker_metadata['pivots'] = groupby_to_pivot(subscription['subscription']["groupBy"],looker_metadata['view'])
    looker_metadata['title'] = response['title']
    card_slicer,dynamic_fields_s = filter_to_dict(response['slicers'], looker_metadata['view'],"operator")
    dynamic_fields = dynamic_fields + dynamic_fields_s
    unique_dynamic_as_tuples = set(tuple(sorted(d.items())) for d in dynamic_fields)
    # Convert tuples back to dictionaries
    unique_dynamic_fields = [dict(t) for t in unique_dynamic_as_tuples]
    if unique_dynamic_fields:
                looker_metadata["dynamic_fields"]=json.dumps(unique_dynamic_fields)  
    looker_metadata['filters'] = {**{k:v for k, v in card_filter.items() if k not in card_slicer},**card_slicer}
    return looker_metadata


def columns_to_fields(columns,view):
    fields = []
    for item in columns:
        if item.get("column"):
            #check for date columns
            if 'time' in item.get("column").lower() or "_at" in item.get("column").lower():
                fields.append(view+"."+item['column'].replace(" ","_").lower()+"_date")
            elif item.get("aggregation"):
                fields.append(view+"."+item.get("aggregation").lower()+"_"+item['column'].replace(" ","_").lower())
            else:
                fields.append(view+"."+item['column'].replace(" ","_").lower())
        else:
            print(item)
    return fields

def filter_to_dict(filter,view,comparison:str='operand',dynamic_fields=[]):
    filters ={}
    for item in filter:
        print("item",item.get('column'))
        if item['values'] != []:
            if item[comparison]=="GREAT_THAN_EQUALS_TO":
                if item.get("dataType") or item.get("type")=="numeric":
                    filters[view+"."+item['column'].replace(" ","_").lower()]= ">="+item['values'][0]
                else:
                    #this is a date
                    # convert date in yy-mm-dd format to yy/mm/dd
                    date = item["values"][0].replace("-","/")
                    filters[view+"."+item['column'].replace(" ","_").lower()+"_date"]= "after "+date
            
            elif item[comparison]=="LESS_THAN_EQUALS_TO":
                if item.get("dataType") or item.get("type")=="numeric":
                    filters[view+"."+item['column'].replace(" ","_").lower()]= "<="+item['values'][0]
                else:
                    #this is a date
                    # convert date in yy-mm-dd format to yy/mm/dd
                    date = item["values"][0].replace("-","/")
                    filters[view+"."+item['column'].replace(" ","_").lower()+"_date"]= "before "+date

            elif item[comparison]=="EQUALS_TO":
                if item.get("dataType") or item.get("type")=="numeric":
                    filters[view+"."+item['column'].replace(" ","_").lower()]= "="+item['values'][0]
                else:
                    #this is a date
                    # convert date in yy-mm-dd format to yy/mm/dd
                    date = item["values"][0].replace("-","/")
                    filters[view+"."+item['column'].replace(" ","_").lower()+"_date"]= "on "+date
            
            elif item[comparison]=="BETWEEN":
                if item.get("dataType") or item.get("type")=="numeric":
                    filters[view+"."+item['column'].replace(" ","_").lower()]= ">="+item['values'][0]+",<="+item['values'][1]
                else:
                    startdate = item.values[0].replace("-","/")
                    enddate = item.values[1].replace("-","/")
                    filters[view+"."+item['column'].replace(" ","_").lower()+"_date"]= startdate+" to "+enddate
            
            elif item[comparison]=="CONTAINS":
#                value = [item['values'][0].replace('\"',"%")]
                value = f"%{item['values'][0]}%"
                filters[view+"."+item['column'].replace(" ","_").lower()]=value
            
            elif item[comparison] == "NOT_IN":
                # check if comparison with space or two spaces then replace with empty
                updated_values = [item if len(item) > 2 else "EMPTY" for item in item['values']]
                #check if this is a comparison with a lot of values and do it only for filters
                if len(updated_values)>3:
                    # we would create a dynamic field
                    field_to_mod = view+"."+item['column'].replace(" ","_").lower()
                    dynamic_field ={"category":"dimension","expression":"upper(${"+field_to_mod+"})","label":item['column'].replace(" ","_").lower()+"_upper","dimension":item['column'].replace(" ","_").lower()+"_upper"}
                    dynamic_fields.append(dynamic_field)
                    #dynamic_fields="""[{"category":"dimension","expression":"upper(${u2_users_performance_part5_final_results_vw.card_title})","label":"card_title_upper","value_format":null,"value_format_name":"","dimension":"card_title_upper"}]"""
                    filters[view+"."+item['column'].replace(" ","_").lower()+"_upper"]= "-"+",-".join(updated_values).upper()
                else: 
                    filters[view+"."+item['column'].replace(" ","_").lower()]= "-"+",-".join(updated_values)

            elif item[comparison] == "IN":
                updated_values = [item if len(item) > 2 else "EMPTY" for item in item['values']]
                #check if this is a comparison with a lot of values
                if len(updated_values)>3:
                    field_to_mod = view+"."+item['column'].replace(" ","_").lower()
                    dynamic_field ={"category":"dimension","expression":"upper(${"+field_to_mod+"})","label":item['column'].replace(" ","_").lower()+"_upper","dimension":item['column'].replace(" ","_").lower()+"_upper"}
                    dynamic_fields.append(dynamic_field)
                    #dynamic_fields="""[{"category":"dimension","expression":"upper(${u2_users_performance_part5_final_results_vw.card_title})","label":"card_title_upper","value_format":null,"value_format_name":"","dimension":"card_title_upper"}]"""
                    filters[item['column'].replace(" ","_").lower()+"_upper"]= ",".join(item['values']).upper()
                else: 
                    filters[view+"."+item['column'].replace(" ","_").lower()]= ",".join(item['values'])
                print("this is the function ", dynamic_fields)
            else:
                print(item)
        pass
    #removing duplicates in dynamic fields
    return filters,dynamic_fields

def groupby_to_pivot(groupby,view):
    pivots=[]
    for item in groupby:
        if item.get("column"):
            pivots.append(view+"."+item['column'].replace(" ","_").lower())
        else:
            print(item)
    return pivots

