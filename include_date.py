from datetime import datetime
the_date = datetime.now()
date = '\n\nThis is an automated tweet coming from somewhere! ({})'.format(str(the_date.strftime("%d/%m/%Y %H:%M:%S")))