import pandas as pd

# from practice1 import user_data
def multiple(param1, param2):
    return param1 * param2

if __name__ == "__main__":
    data = {
        "국어": [90, 85, 80],
        "영어": [88, 76, 92],
        "수학": [95, 89, 85]
    }
    exam_df = pd.DataFrame(data, columns=['국어', '영어', '수학'])
    exam_df['평균'] = (exam_df['국어'] + exam_df['수학'] + exam_df['영어'])/3
    # exam_df.apply(lambda table: average(table['국어']+table['수학']+table['영어']))
    print(exam_df)

    # print('hello world!!')
    # = range(1,10,1) = range(start:end:step)
    # number1 = list(range(1,11))
    # number2 = list(range(11,21))
    # results = map(multiple, number1, number2)

    # for result in results:
    #     print(list(results))