import json

while True:
    emr=input('Yeni Istifadeci elave etmek isteyirsiniz mi (Y/N) :')
    if emr=='Y':
        ad=input('Ad daxil edin :')
        soyad=input('Soyad daxil edin :')
        yas=int(input('Yas daxil edin :'))
        # user=[f'Istifadecinin adi:{ad}\n Istifadecinin soyadi :{soyad}\n Istifadecinin yasi :{yas}\n']
        dictionary= {
                'Istifadecinin adi' : ad,
                'Istifadecinin soyadi' : soyad,
                'Istifadecinin yasi' : yas
        }
        list = [dictionary]
        print(list)
        data=json.dumps(list)

        conn=open('classwork/users.json','w')
        conn.write(data)
        conn=open('classwork/users.json','r')
        getDataFromJson=conn.read();
        convertToDict=json.loads(getDataFromJson)

        for list in convertToDict:
                print(f'Telebe adi : {list["Istifadecinin adi"]},Telebe soyadi : {list["Istifadecinin soyadi"]},Telebe Yasi : {list["Istifadecinin yasi"]} ')

        # for list in convertToDict:
        #  print(f'Telebe adi : {dictionary["ad"]},Telebe soyadi : {dictionary["soyad"]} ')
        
        

        # print(dictionary)

        

        # data=json.dumps(list)
        # conn=open('users.json','w')
        # conn.write(data)
        
       
        

        
    else:
        break

# def Convert(user):
#         res_dct = {ad, soyad, yas}
#         return res_dct

# user = ['ad', 'soyad', 'yas']       
# print(Convert(user))

# dict = (ad, soyad, yas)
# print(type(dict))

# list = [dict]
# print(type(list))


