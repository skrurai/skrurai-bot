def clean(api_object, clean_statuses, clean_likes):
    while True:
        
        if(clean_statuses):
            for status in api_object.user_timeline():
                json = status._json
                id = json['id']
                
                if('\U0001F6AB' not in json['text']):
                    api_object.destroy_status(id)

        if(clean_likes):
            for status in api_object.favorites():
                api_object.destroy_favorite(id=status._json['id'])
