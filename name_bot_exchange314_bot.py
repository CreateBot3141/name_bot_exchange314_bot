
def print_message_menu (namebot,user_id,id_sql,list_sql,start_sql,step_sql,message_id,operation):

    print ('[+] operation:',operation)


    import iz_func
    import iz_telegram
    db,cursor = iz_func.connect ()
    parameter01 = "name"
    parameter02 = ""
    parameter03 = ""
    parameter04 = ""
    parameter05 = ""
    name_table  = "bot_product" 
    step_sql    = step_sql 
    start_sql   = start_sql

    message_out = ''
    if operation == 'Купить': 
        message_out,menu = iz_telegram.get_message (user_id,'🛍 Купить',namebot)
    if operation == 'Продать':    
        message_out,menu = iz_telegram.get_message (user_id,'💲Продать',namebot)
    if message_out == '':    
        message_out,menu = iz_telegram.get_message (user_id,'🛍 Купить',namebot)


    

    sign        = ['status',['start',iz_telegram.get_namekey (user_id,namebot,'Хорошо')],['stop',iz_telegram.get_namekey (user_id,namebot,'Плохо')]]
    pattern,menu = iz_telegram.get_message (user_id,'Шаблон кнопки список продуктов',namebot)

    if list_sql == 0:
        name_sql = "select id,status"
        if parameter01 != "":
            name_sql =  name_sql + ",`"+str(parameter01)+"`"
        if parameter02 != "":
            name_sql =  name_sql + ",`"+str(parameter02)+"`"
        if parameter03 != "":
            name_sql =  name_sql + ",`"+str(parameter03)+"`"
        name_sql =  name_sql + "from "+str(name_table)+" "
        name_sql =  name_sql + ' where parents = "%%parents%%" and '
        name_sql =  name_sql + ' namebot = "'+str(namebot)+'" limit %%start_list%%,%%step_list%%'
        list_sql = iz_telegram.new_list(name_sql,start_sql,step_sql)
        message_id = 0

    if operation == 'Купить':
        sql = iz_telegram.get_list (list_sql,'new','Купить')

    if operation == 'Продать':
        sql = iz_telegram.get_list (list_sql,'new','Продать')    

    if operation == 'Объявление':
        sql = iz_telegram.get_list (list_sql,'new','Объявление')    

    if  operation == 'reset':
        sql = iz_telegram.get_list (list_sql,'reset','')
    if  operation == 'next':
        sql = iz_telegram.get_list (list_sql,'next','')
    if  operation == 'last':
        sql = iz_telegram.get_list (list_sql,'last','')
    if  operation == 'catalog':
        sql = iz_telegram.get_list (list_sql,'catalog',str(id_sql))

    cursor.execute(sql)
    data = cursor.fetchall()
    markup = iz_telegram.button_body_design_01 (data,pattern,parameter01,parameter02,parameter03,parameter04,parameter05,sign,list_sql)
    
    iz_telegram.button_end_design_01 (user_id,namebot,markup,list_sql)

    body = iz_telegram.get_body_product (user_id,namebot,id_sql)

    if body != '':
        message_out = body

    answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)

def save_picture_file (url_picture,name_file_save):
    #name_file_save = 'Vadim.jpg'
    from  urllib.request import urlopen 
    #try:
    urlt = urlopen(url_picture)
    f = urlt.read()
    open(name_file_save,"wb").write(f)
    #except Exception as e:
    #    color_start,color_end = color (2)
    #    print (color_start,'[+] Ошибка скачивания файла:',e,color_end)
    #    print (color_start,'[+] Название файла:',url_picture,color_end)
    #    name_file_save = ''
    return name_file_save

def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome,refer,user_id_refer,FIO_id):
    import iz_func
    import iz_game
    import iz_main
    import time
    import iz_telegram


    if message_in == 'Добавить объявление':
        print_message_menu (namebot,user_id,0,0,0,10,message_id,'Объявление')


    if message_in.find ('cript_') != -1:
        word = message_in.replace('cript_','')
        iz_telegram.save_variable (user_id,namebot,"Криптовалюта",str(word))
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Готово','S',0)
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'🔧 Настройки','S',0)

    if message_in.find ('valut_') != -1:
        word = message_in.replace('valut_','')
        iz_telegram.save_variable (user_id,namebot,"Валюта",str(word))
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'Готово','S',0)
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,'🔧 Настройки','S',0)

    if message_in == 'Кошелек':
        message_out,menu = iz_telegram.get_message (user_id,'💼 Кошелек',namebot)
        summ1 = iz_telegram.get_register (namebot,user_id,'Баланс BTC')
        summ2 = iz_telegram.get_register (namebot,user_id,'Заблокировано BTC')
        summ3 = iz_telegram.get_register (namebot,user_id,'Успешных сделок')
        summ4 = iz_telegram.get_register (namebot,user_id,'Общую сумма BTC')
        summ5 = iz_telegram.get_register (namebot,user_id,'Приглашено пользователей')
        summ6 = iz_telegram.get_register (namebot,user_id,'Заработано BTC')
        summ7 = iz_telegram.get_register (namebot,user_id,'Рейтинг 👶')
        summ8 = iz_telegram.get_register (namebot,user_id,'Отзывы 👍')
        summ9 = iz_telegram.get_register (namebot,user_id,'Отзывы 👎')
        message_out = message_out.replace('%%Баланс BTC%%',str(summ1))
        message_out = message_out.replace('%%Заблокировано BTC%%',str(summ2))
        message_out = message_out.replace('%%Успешных сделок%%',str(summ3))
        message_out = message_out.replace('%%Общую сумма BTC%%',str(summ4))
        message_out = message_out.replace('%%Приглашено пользователей%%',str(summ5))
        message_out = message_out.replace('%%Заработано BTC%%',str(summ6))
        message_out = message_out.replace('%%Рейтинг 👶%%',str(summ7))
        message_out = message_out.replace('%%Отзывы 👍%%',str(summ8))
        message_out = message_out.replace('%%Отзывы 👎%%',str(summ9))
        message_out = message_out.replace('%%Примерно%%',str(10))
        message_out = message_out.replace('%%Количество дней%%',str(100))
        markup = iz_telegram.get_menu (user_id,menu,namebot)
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0) 

    if message_in == 'Купить':
        #message_out,menu = iz_telegram.get_message (user_id,'🛍 Купить',namebot)
        #markup = ''
        #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)
        print_message_menu (namebot,user_id,0,0,0,10,message_id,'Купить')


    if message_in == 'Продать':
        #message_out,menu = iz_telegram.get_message (user_id,'💲Продать',namebot)
        #markup = ''
        #answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)
        print_message_menu (namebot,user_id,0,0,0,10,message_id,'Продать')    

    if message_in == '📩 Внести':
        amount_s      =  0.00005;
        currency_s    = 'BTC'
        #user_id       = '399838806'
        namebot       = '@exchange314_bot'
        lastid,checkout_url,address,amount,qrcode_url = iz_func.cheque (amount_s,currency_s,user_id,namebot)
        print ('[+] lastid:',lastid)
        print ('[+] checkout_url:',checkout_url)
        print ('[+] address:',address)
        print ('[+] amount:',amount)
        print ('[+] qrcode_url:',qrcode_url)
        message_out,menu = iz_telegram.get_message (user_id,'Адрес кошелька',namebot)
        message_out = str(address)
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)  
        name_file_save = 'qrcode.jpg'
        save_picture_file (qrcode_url,name_file_save)
        iz_telegram.send_photo (user_id,namebot,name_file_save)

    if message_in.find ('setting_') != -1: 
        list = [["BTC/USDT","001"],["ETH/USDT","002"]]
        iz_telegram.change_setting_user (user_id,namebot,list,message_in)
        markup = iz_telegram.get_setting_user (user_id,namebot,list)
        message_out = "Привет"
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)  

    if message_in == '/setting': 
        list = [["BTC/USDT","001"],["ETH/USDT","002"]]
        markup = iz_telegram.get_setting_user (user_id,namebot,list)
        message_out = "Привет"
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)  
    
    if message_in == '/start': 
        status = '' 
        iz_telegram.save_variable (user_id,namebot,'status','')
    
    if message_in == 'Ознакомлен': 
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"После регистрации на бирже",'S',0)         
        pass

    if message_in == 'Подписаться на сигналы': 
        message_out,menu = iz_telegram.get_message (user_id,'Вы сделали подписку на сигналы крипты',namebot)
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,0)  
        
    if message_in == 'Передать ключи API': 
        iz_telegram.save_variable (user_id,namebot,'status','Введите ID Binance')
        markup  = ''
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Введите ID Binance",'S',0) 

    if status == 'Введите ID Binance': 
        iz_telegram.save_variable (user_id,namebot,'ID Binance',message_in)
        iz_telegram.save_variable (user_id,namebot,'status','Ввести API key')
        markup  = ''
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Ввести API key",'S',0) 

    if status == 'Ввести API key': 
        iz_telegram.save_variable (user_id,namebot,'API KEY',message_in)
        iz_telegram.save_variable (user_id,namebot,'status','Ввести SECRET KEY')
        markup  = ''
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Введите secret key",'S',0)
        
    if status == 'Ввести SECRET KEY':     
        iz_telegram.save_variable (user_id,namebot,'SECRET KEY',message_in)
        iz_telegram.save_variable (user_id,namebot,'status','')
        markup  = ''
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Спасибо за регистрацию",'S',0)
        API_KEY      = iz_telegram.load_variable (user_id,namebot,'API KEY')
        SECRET_KEY   = iz_telegram.load_variable (user_id,namebot,'SECRET KEY')
        ID_Binance   = iz_telegram.load_variable (user_id,namebot,'ID Binance')
        db,cursor = iz_func.connect ()
        login     = ''  
        project   = ''  
        summ      = ''  
        system    = ''  
        wallet    = ''  
        komment   = ID_Binance  
        adress    = API_KEY
        telefon   = SECRET_KEY
        sql = "INSERT INTO bot_active_user (language,namebot,user_id,login,project,summ,`system`,wallet,komment,adress,telefon) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format ('ru',namebot,user_id,login,project,summ,system,wallet,komment,adress,telefon)
        cursor.execute(sql)
        db.commit() 

    if message_in.find ('info') != -1:
        import json
        json_string  = iz_func.change_back(message_in.replace('info_',''))
        data_json = json.loads(json_string)
        operation = data_json['o']

        if operation == 'key':
            id_sql   = data_json['id']
            list_sql = data_json['sql']
            #iz_telegram.replacement ('bot_product','status',id_sql,['start','stop'])
            print_message_menu (namebot,user_id,id_sql,list_sql,0,10,message_id,'catalog')

