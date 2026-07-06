import json

def get_rating(reviews):
    rating=5
    if reviews:
        rating = sum(reviews)//len(reviews)
    return "⭐"*rating
with open('./menu.json', 'r') as f:
    data = json.load(f)
# print('data', data)
items = data.get('items',[])
   # print(items)
while True:
    print('-'*30)
    print('Super Famous Restaruant')
    print('-'*30)
    print('1. Show Menu')
    print('2. Order Items')
    print('3. Update Menu')
    print('4. Add Review')
    print('5. Exit')
    print('-'*30)

    choice = int(input('enter your choice:'))
    print('-'*30)

    if choice == 1:
        print('Id\tItem_name\tPrice\tRatings')
        print('-'*30)
        for item in items:
            print(f'{item.get('id')}\t{item.get('item_name')}\t{item.get('price')}\t{get_rating(item.get("reviews",[]))}')
        print('-'*30)

    elif choice == 2:
        order_items =list(map(int,input('Which item you want to order').split(',')))
        print('-'*30)
        print('ID\tITEM_NAME\tPRICE')
        print('-'*30)
        total_bill=0
        for order_item in order_items:
            for item in items:
                if item['id'] == order_item:
                    print(f'{item.get('id')}\t{item.get('item_name')}\t{item.get('price')}')
                    total_bill += int(item.get('price',10))
                    break
        print('-'*30)
        print(f'Total Amount: {total_bill}')
        print('-'*30)

    elif choice == 3:
        item_name = input('enter the item name:')
        item_price = int(input('enter the item price:'))
        item_type = input('enter the veg or no-veg:')

        items.append({
            'id':len(items)+1,
            'item_name':item_name,
            'price':item_price,
            'veg': True if item_type == 'veg' else False,
            'reviews':[]
        })

        data['items'] = items
        with open('project/menu.json','w') as f:
            json.dump(data, f)
        print('Item is added')  

    elif choice == 4:
        item_id = int(input('Enter the item id:'))
        rating = int(input('give your rating 1-5:'))
        for i, item in enumerate(items):
            if item['id'] == item_id:
                items[i]['reviews'].append(rating)
                break
        print('Thank you.. for your rating have a nice day...!!')
    else:
        data['items'] = items
        with open('project/menu.json','w') as f:
            json.dump(data, f)
        print('Thank you')  
        break
