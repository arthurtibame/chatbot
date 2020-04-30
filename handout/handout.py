from linebot.models import TemplateSendMessage, CarouselTemplate, CarouselColumn, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction

handout_icon1 = "https://image.flaticon.com/icons/svg/1061/1061447.svg"
handout_icon2 = 'https://upload.wikimedia.org/wikipedia/commons/f/f1/Books_Flat_Icon_Vector.svg'
handout_icon3 = 'https://banner2.cleanpng.com/20180407/jpq/kisspng-book-flat-design-books-5ac984c5e9ef33.3004996215231561659582.jpg'
book_icon = "https://i.pinimg.com/236x/2c/fc/93/2cfc93d7665f5d7728782700e50596e3--icons.jpg"
timetable_url = "https://docs.google.com/spreadsheets/d/1qTkccFsNRy8IJLFEDK2ty-GB24Np1cu7avLoB0uZZUs/edit#gid=1865763997"
html_url = "https://drive.google.com/open?id=1bXnZtE9LyhTV80IPttCYJ0Ro5jOmIaaJ"
python_basic_url = 'https://drive.google.com/open?id=1tcBxB6_5h5nLIu40cKuBvtzviGKjOw0M'
linux_url = 'https://drive.google.com/open?id=1N1GmA9-tYUSTK8AWCERfplyBQoKCe0BD'
pyetl_url = 'https://drive.google.com/open?id=1HyBsyshzSuBQtKZYrH09vuloWmlLv-v0'
pyai_url = 'https://drive.google.com/open?id=1Xp-i_7ltQBo2r-luiF4Rp-4vfnLgck52'
data_mining_url = 'https://drive.google.com/open?id=1r45ik4uD2TYr7xrNp5c9VfrkXEAVMSLX'
nosql_url = 'https://drive.google.com/open?id=1VeDkM1g3MYNaFUDQ8O_m4lF43HT-w_1R'
text_mining_nlu_url = 'https://drive.google.com/open?id=1puNXOTh1DoArz_20eV748D1OpvmdXvNR'
hadoop_url = 'https://drive.google.com/open?id=10mZ5iis0aCI7S4AzbFOAlEXW4FOdr5dW'
kafka_url = 'https://drive.google.com/open?id=1ZfRDO713xLXHSVrMXUWOYXlep4kYXRW1'

def handout():

    handout_carouse = CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url=handout_icon1,
                        title='課程講義 page 1',
                        text='請選擇您要的講義',
                        actions=[
                        URITemplateAction(
                            label='網頁概論',
                            uri=html_url
                        ),
                        URITemplateAction(
                            label='Python 基礎',
                            uri=python_basic_url
                        ),
                        URITemplateAction(
                            label='Linux',
                            uri=linux_url
                        ),
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=handout_icon2,
                        title='課程講義 page 2',
                        text=' ',
                        actions=[
                        URITemplateAction(
                            label='PyETL',
                            uri=pyetl_url
                        ),
                        URITemplateAction(
                            label='PyAI',
                            uri=pyai_url
                        ),
                        URITemplateAction(
                            label='Data Mining(含R語言)',
                            uri=data_mining_url
                        ),


                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=handout_icon3,
                        title='課程講義 page 3',
                        text=' ',
                        actions=[
                        
                        URITemplateAction(
                            label='NoSQL',
                            uri=nosql_url
                        ),
                        
                        URITemplateAction(
                            label='Text Mining + NLU',
                            uri=text_mining_nlu_url
                        ),
                        
                        URITemplateAction(
                                label='Kafka',
                                uri=kafka_url
                        ),


                        ]
                    )
                    
                    ]
                )
    
    return handout_carouse