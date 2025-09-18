dataset = [
    {
        "region":"North","sales":1200,"profit":10.2
    },
    {
         "region":"South","sales":1800,"profit":10.2
    },
    {
         "region":"West","sales":1100,"profit":17.2
    }
]




def load_data(data):
    return data


def calculate_total_sales(data):
    return sum(item["sales"] for item in data)

def average_profit(data):
    return sum(item["profit"] for item in data)/len(data)

def sales_by_region(data):
    region_sales = {}
    for item in data:
        region_sales[item["region"]]=region_sales.get(item["region"],0)+item["sales"]
        return region_sales
        


print(calculate_total_sales(dataset))







# 


