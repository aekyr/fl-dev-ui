from datetime import datetime, timedelta


# SUPPORT MODULES
now = datetime.now() 
future = datetime.now() + timedelta(days=14, hours=3, seconds=34)

taskgroups = {  1:'FL-Core', 
                2:'FLP Pytorch',
                3:'FLP TensorFlow',
                4:'FL-Data Services',
                }


tasks = [
        {
            'id':1,
            'assignees':['ron', 'lucas', 'kenneth', 'ryan heng'],
            'time':{
                'datetime_start':now,
                'datetime_end':future
            },
            'info' : {
                'title': 'Pytorch Pipelining',
                'subtitle': 'hello',
                'description': 'pipeline pytorch to automate with mlflow by this date SKAN likes CKAN',
            },
            'data' : {
                'section':1,
                'status':1,
                'group':'FLP Pytorch'
            }
        },
        {
            'id':1,
            'assignees':['ron', 'lucas', 'kenneth'],
            'time':{
                'datetime_start':now,
                'datetime_end':future
            },
            'info' : {
                'title': 'Pytorch Pipelining',
                'subtitle': 'hello',
                'description': 'pipeline pytorch to automate with mlflow by this date SKAN likes CKAN',
            },
            'data' : {
                'section':3,
                'status':1,
                'group':'FLP Tensorflow'
            }
        },
        {
            'id':1,
            'assignees':['ron', 'lucas'],
            'time':{
                'datetime_start':now,
                'datetime_end':future
            },
            'info' : {
                'title': 'Pytorch Pipelining',
                'subtitle': 'hello',
                'description': 'pipeline pytorch to automate with mlflow by this date SKAN likes CKAN',
            },
            'data' : {
                'section':2,
                'status':1,
                'group':'FL Data Services'
            }
        },
        {
            'id':1,
            'assignees':['ron', 'lucas'],
            'time':{
                'datetime_start':now,
                'datetime_end':future
            },
            'info' : {
                'title': 'Pytorch3 Pipelining',
                'subtitle': 'hello',
                'description': 'pipeline pytorch to automate with mlflow by this date SKAN likes CKAN',
            },
            'data' : {
                'section':0,
                'status': 'complete', 
                'group':'FL Core'
            }
        },
        {
            'id':1,
            'assignees':['mmmmmm', 'lucas' 'kenneth'],
            'time':{
                'datetime_start':now,
                'datetime_end':future
            },
            'info' : {
                'title': 'Pytorch Pipelining',
                'subtitle': 'hello',
                'description': 'pipeline pytorch to automate with mlflow by this date SKAN likes CKAN',
            },
            'data' : {
                'section':1,
                'status':1,
                'group':'FL Data Services'
            }
        },
        {
            'id':1,
            'assignees':['ron'],
            'time':{
                'datetime_start':now,
                'datetime_end':now - timedelta(days=14, hours=3, seconds=34)
            },
            'info' : {
                'title': 'Pytorch Pipelining late',
                'subtitle': 'hello',
                'description': 'pipeline pytorch to automate with mlflow by this date SKAN likes CKAN',
            },
            'data' : {
                'section':3,
                'status':1,
                'group':'FL Core'
            }
        },
        {
            'id':1,
            'assignees':['ron'],
            'time':{
                'datetime_start':now,
                'datetime_end':now + timedelta(days=14, hours=3, seconds=34)
            },
            'info' : {
                'title': 'Pytorch Pipelining early',
                'subtitle': 'hello',
                'description': 'pipeline pytorch to automate with mlflow by this date SKAN likes CKAN',
            },
            'data' : {
                'section':1,
                'status':1,
                'group':'FL Core'
            }
        },
        {
            'id':1,
            'assignees':['ron'],
            'time':{
                'datetime_start':now,
                'datetime_end':now + timedelta(days=14, hours=3, seconds=34)
            },
            'info' : {
                'title': 'Pytorch Pipelining early',
                'subtitle': 'hello',
                'description': 'pipeline pytorch to automate with mlflow by this date SKAN likes CKAN',
            },
            'data' : {
                'section':3,
                'status':1,
                'group':'FL Core'
            }
        },
        {
            'id':1,
            'assignees':['ron'],
            'time':{
                'datetime_start':now,
                'datetime_end':None
            },
            'info' : {
                'title': 'Pytorch Pipelining long term',
                'subtitle': 'hello',
                'description': 'pipeline pytorch to automate with mlflow by this date SKAN likes CKAN',
            },
            'data' : {
                'section':1,
                'status':1,
                'group':'FL Core'
            }
        },
        {
            'id':1,
            'assignees':['kenrythethird'],
            'time':{
                'datetime_start':now,
                'datetime_end':future
            },
            'info' : {
                'title': 'Pytorch Pipelining',
                'subtitle': 'hello',
                'description': 'pipeline pytorch to automate with mlflow by this date SKAN likes CKAN',
            },
            'data' : {
                'section':1,
                'status':1,
                'group':'FL Data Services'
            }
        },
        {
            'id':1,
            'assignees':['ron', 'lucas'],
            'time':{
                'datetime_start':now,
                'datetime_end':future
            },
            'info' : {
                'title': 'Pytorch Pipelining',
                'subtitle': 'hello',
                'description': 'pipeline pytorch to automate with mlflow by this date SKAN likes CKAN',
            },
            'data' : {
                'section':2,
                'status':1,
                'group':'FLP Pytorch'
            }
        }




    ]

