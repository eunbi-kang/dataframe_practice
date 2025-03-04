##
## 🌝 SELECT, UPDATE, Column 추가 (projection), MERGE
##
import random

import pandas as pd
from pandas import pivot

from map_practice20250304 import multiple

## ✅ 사용자 더미 데이터 (딕셔너리 리스트 형태)
user_data = [{'user_id': 1, 'name': 'User_1', 'email': 'user1@example.com', 'age': 59},
             {'user_id': 2, 'name': 'User_2', 'email': 'user2@example.com', 'age': 42},
             {'user_id': 3, 'name': 'User_3', 'email': 'user3@example.com', 'age': 46},
             {'user_id': 4, 'name': 'User_4', 'email': 'user4@example.com', 'age': 26},
             {'user_id': 5, 'name': 'User_5', 'email': 'user5@example.com', 'age': 21},
             {'user_id': 6, 'name': 'User_6', 'email': 'user6@example.com', 'age': 36},
             {'user_id': 7, 'name': 'User_7', 'email': 'user7@example.com', 'age': 30},
             {'user_id': 8, 'name': 'User_8', 'email': 'user8@example.com', 'age': 55},
             {'user_id': 9, 'name': 'User_9', 'email': 'user9@example.com', 'age': 27},
             {'user_id': 10, 'name': 'User_10', 'email': 'user10@example.com', 'age': 60}]

## ✅ 주문 더미 데이터 (딕셔너리 리스트 형태)
order_data = [{'id': 1, 'user_id': 3, 'book_id': 3},
              {'id': 2, 'user_id': 7, 'book_id': 9},
              {'id': 3, 'user_id': 10, 'book_id': 8},
              {'id': 4, 'user_id': 8, 'book_id': 8},
              {'id': 5, 'user_id': 10, 'book_id': 3},
              {'id': 6, 'user_id': 9, 'book_id': 8},
              {'id': 7, 'user_id': 3, 'book_id': 8},
              {'id': 8, 'user_id': 5, 'book_id': 9},
              {'id': 9, 'user_id': 8, 'book_id': 9},
              {'id': 10, 'user_id': 2, 'book_id': 3}]

## ✅ 도서 더미 데이터 (딕셔너리 리스트 형태)
book_data = [
    {"book_id": 1, "title": "Book A", "author": "Author A", "publisher": "Publisher A", "price": random.randint(10000, 50000)},
    {"book_id": 2, "title": "Book B", "author": "Author B", "publisher": "Publisher B", "price": random.randint(10000, 50000)},
    {"book_id": 3, "title": "Book C", "author": "Author C", "publisher": "Publisher C", "price": random.randint(10000, 50000)},
    {"book_id": 4, "title": "Book D", "author": "Author D", "publisher": "Publisher D", "price": random.randint(10000, 50000)},
    {"book_id": 5, "title": "Book E", "author": "Author E", "publisher": "Publisher E", "price": random.randint(10000, 50000)},
    {"book_id": 6, "title": "Book F", "author": "Author F", "publisher": "Publisher F", "price": random.randint(10000, 50000)},
    {"book_id": 7, "title": "Book G", "author": "Author G", "publisher": "Publisher G", "price": random.randint(10000, 50000)}
]


if __name__ == "__main__":
    user_df = pd.DataFrame(user_data, columns=['user_id', 'name', 'email', 'age'])  # columns 자동 설정됨
    order_df = pd.DataFrame(order_data, columns=['id', 'user_id', 'book_id'])
    book_df = pd.DataFrame(book_data, columns=['book_id', 'title', 'author','publisher','price'])

    ## ✅ SELECT
    # print(user_df)
    # print('order_df', order_df)
    # print('book_df', book_df)
    # print(user_df.loc[4, 'email'])

    ## ✅ UPDATE
    # user_df.loc[4, 'email'] = "john@example.com"
    # print(user_df.loc[4, 'email']) #user5@example.com 출력

    ## ✅ Column 추가 (projection)
    # inplace 키워드 추가시 원본이 바뀜
    print('----------------------------------------------')
    # user_df['test'] = 0
    # user_df['test2'] = 1
    # user_df.drop(['test', 'test2'], axis=1, inplace=True)

    ## ✅ MERGE
    # user_order_merge = pd.merge(user_df, order_df, left_on="id", right_on="user_id", how="inner")

    # user_order_merge = pd.merge(user_df, order_df, on="user_id", how='inner')

    # user_order_book_merge = pd.merge(
    #     pd.merge(user_df, order_df, on="user_id", how="inner"),
    #     book_df, on="book_id", how="inner")
    # print(user_df)

    ## ✅ apply()
    # user_df['test1']=2
    # results = user_df[['age','test1']].apply(lambda x: multiple(x['age'], x['test1']), axis=1)
    # print(results)


    ## ✅ groupby 사용
    # group_df = book_df.groupby('author')
    # for key, value in group_df:
    #     print("key", key)
    #     print("value", value)

    ## ✅ groupby 사용하여 평균 구하기 - mean() 사용
    # group_df = book_df.groupby('author')['price'].mean()
    # print(group_df)

    ## ✅ pivot_table()
    pivot_df = order_df.pivot_table(index='user_id',
                                    columns='book_id',
                                    values='id',
                                    aggfunc='count',
                                    fill_value=0 )

    print(pivot_df)

    ## ✅ pivot table + price Merge 해보기 예제
    pivot_price = (pd.merge(user_df, order_df, on="user_id", how="inner"))

    print(pivot_price)
