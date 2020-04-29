from datetime import date 
import pandas as pd

from linebot.models import TemplateSendMessage, ButtonsTemplate, DatetimePickerTemplateAction



def timetable(month_g, day_g):
    #輸入月份
    month = '0'+str(month_g)
    print(month)
    if month == '04' or month == '05' or month == '06' or month == '07' or month == '08' or month == '09':
        df = pd.read_excel(open('timetable.xlsx', 'rb'),
                    sheet_name='109.{}'.format(month))  

        date_row_list = [0,4,8,12,16]           
        result = []
        #搜尋日期
        day = day_g
        for i in date_row_list:
            for j in range(len(df.iloc[0,:])):
                if df.iloc[i, j] == day:
                    df1 = df.iloc[i:i+4,j]
                    df1 = df1.fillna(0)
                    my_class1 = df1.iloc[2]
                    if my_class1 !=0:
                        result.append(my_class1)
                    #print(df1)
                    #檢查要不要夜輔
                    if df1.iloc[3] != 0 :
                        night_class = '{} 月 {} 日 晚上有課程 !'.format(int(month), int(day))
                        my_class2 = df1.iloc[3]
                        result.append(night_class)
                        result.append(my_class2)
                    elif df1.iloc[2] == 0 :
                        dayoff = '{} 月 {} 日 這天似乎放假喔,來學校練習吧 !'.format(int(month), int(day))
                        result.append(dayoff)                

                    else:
                        night_class = '{} 月 {} 日 晚上可以加油留下來夜輔'.format(int(month), int(day))
                        result.append(night_class)
        #print(result)
    else:
        error = '請輸入正確的月份或是日期'
        result.append(error)
    
    #final_result
    #=pd.DataFrame([result])
    #final_result = final_result.to_json()#.strip('[').strip(',"').strip(']')orient='values'



    print(result)
    
    return result        




