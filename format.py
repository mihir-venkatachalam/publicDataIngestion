
class Data:
    def  __init__(self,name,frequency,metric,date,value,source):
        self.name = name
        self.frequency = frequency
        self.metric = metric
        self.date = date
        self.value = value
        self.source = source

    def row(self):
        return {
                'company_name': self.name,
                'metric_name': self.metric,
                'value': self.value,
                'modified_at': "",
                'start_date': self.date,
                'time_period': self.calculate_period(),
                'frequency': self.frequency,
                'primary_segment':'ALL',
                'secondary_segment':'ALL',
                'tertiary_segment':'ALL',
                'source': self.source,
                'id':"",
                'custom_segment_name':'BENCHMARK',
                'custom_filter':'ALL',
                'json_value':""
                }

    def calculate_period(self):
        if self.frequency == 'A':
            return self.date[:4]


        if self.frequency == 'Q':
            month = self.date[5:7]
            map={"01":"Q1-","02":"Q1-","03":"Q1-","04":"Q2-","05":"Q2-","06":"Q2-","07":"Q3-","08":"Q3-","09":"Q3-","10":"Q4-","11":"Q4-","12":"Q4-"}
            if month in map:
                return map[month]+self.date[:4]
            if month not in map:
                raise Exception("Invalid month or no month given")


