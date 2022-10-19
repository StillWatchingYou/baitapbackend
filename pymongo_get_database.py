import sys

from pymongo import MongoClient

myclient = MongoClient('localhost', 27017)

db = myclient.Bai_tap_so_1

col = db.bai1

print('chon phuong thuc sua ban muon')
print('1 de sua chua du lieu')
print('2 de them du lieu')
print('3 de xoa du lieu')
cachsua = int (input())


#chinh sua du lieu
if cachsua == 1 : print("Phan ban muon sua")

phanmuonsua = int (input())

#case1 (noi dung bai hoc)
if phanmuonsua == 1:
    filter = {'id': 1}

    print('Thay doi tieu de nhan 1, Thay doi noi dung nhan 2')
    x =  int (input())

    #chinh sua tieu de cua bai hoc so 1
    if x ==  1:

      print("Nhap ten tieu de moi")
      tieudemoi = input()
      # update
      tieudethaydoi = {"$set": {'title' :   tieudemoi}}
      col.update_one(filter, tieudethaydoi)

    #chinh sua noi dung cua bai hoc so 1
    if x == 2:

      print('Ban muon sua dong nao')
      dongcansua = int(input())
      if  dongcansua > 4:
          print('Da co loi xay ra, vui long thu lai')
          sys.exit(0)
      print("Nhap noi dung moi")
      noidungmoi = input()
      #update
      if dongcansua == 1:
          noidungthaydoi = {"$set": {'contents.0': noidungmoi}}
      if dongcansua == 2:
          noidungthaydoi = {"$set": {'contents.1': noidungmoi}}
      if dongcansua == 3:
          noidungthaydoi = {"$set": {'contents.2': noidungmoi}}
      if dongcansua == 4:
          noidungthaydoi = {"$set": {'contents.3': noidungmoi}}
      col.update_one(filter, noidungthaydoi)


    if x != 1 and x != 2:
        print('Da co loi xay ra, vui long thu lai')
        sys.exit(0)



#case 2 (module bai hoc)
if phanmuonsua == 2:
    filter = {'id': 2}
    print('Thay doi tieu de nhan 1, Thay doi noi dung nhan 2')
    y =  int (input())

#chinh sua tieu de cua bai hoc so 2
    if y ==  1:
        print("Nhap ten tieu de moi")
        tieudemoi = input()
  #updatedulieu
        tieudethaydoi = {"$set": {'title': tieudemoi}}
        col.update_one(filter, tieudethaydoi)
    if y == 2:
        print("Chon 1 de sua anh, Chon 2 de chinh sua phan noi dung duoi anh")
        z = int (input())
        if z == 2:
            print('chon anh ban can sua')
            anhcansua = int (input())
            print('vi tri cua anh moi')
            anhmoi = input()
            if anhcansua == 1:
                anhthaydoi = {"$set": {'contentWithimg.0.img': anhmoi}}
            if anhcansua == 2:
                anhthaydoi = {"$set": {'contentWithimg.1.img': anhmoi}}
        if z == 1:
            print('chon noi dung anh ban can sua')
            dongcansua = int(input())
            print('noi dung cua anh moi')
            noidungmoi = input()
            if dongcansua == 1:
                anhthaydoi = {"$set": {'contentWithimg.0.contents': noidungmoi}}
            if dongcansua == 2:
                anhthaydoi = {"$set": {'contentWithimg.1.contents': noidungmoi}}









# checkdatabase
cursor = col.find()
for record in cursor:
 print(record)