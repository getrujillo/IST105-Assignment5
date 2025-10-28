from django.shortcuts import render
from pymongo import MongoClient
from datetime import datetime


MONGO_IP = '172.31.24.37'

client = MongoClient(f'mongodb://{MONGO_IP}:27017/')
db = client['assignment6_db']
collection = db['calculations']

def index(request):
    result = None
    error = None
    
    if request.method == 'POST':
        try:
            a = request.POST.get('a', '')
            b = request.POST.get('b', '')
            c = request.POST.get('c', '')
            d = request.POST.get('d', '')
            e = request.POST.get('e', '')
            
            values = []
            for val in [a, b, c, d, e]:
                if not val or not val.replace('-', '').replace('.', '').isdigit():
                    error = "All inputs must be numeric values"
                    return render(request, 'bitwise/index.html', {'error': error})
                values.append(float(val))
            
            warnings = []
            if any(v < 0 for v in values):
                warnings.append("Warning: Some values are negative")
            
            average = sum(values) / len(values)
            avg_check = "greater than 50" if average > 50 else "less than or equal to 50"
            
            positive_count = sum(1 for v in values if v > 0)
            is_even = (positive_count & 1) == 0
            parity = "even" if is_even else "odd"
            
            filtered_values = sorted([v for v in values if v > 10])
            
            result = {
                'original_values': values,
                'sorted_values': filtered_values,
                'average': round(average, 2),
                'avg_check': avg_check,
                'positive_count': positive_count,
                'parity': parity,
                'warnings': warnings
            }
            
            document = {
                'input': {'a': values[0], 'b': values[1], 'c': values[2], 'd': values[3], 'e': values[4]},
                'output': result,
                'timestamp': datetime.now()
            }
            collection.insert_one(document)
            
        except Exception as ex:
            error = f"Error: {str(ex)}"
    
    return render(request, 'bitwise/index.html', {'result': result, 'error': error})

def view_all(request):
    entries = list(collection.find().sort('timestamp', -1))
    return render(request, 'bitwise/view_all.html', {'entries': entries})