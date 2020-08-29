from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

# pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

# 이건 내가 몽고 디비를 사용하기 위함이지.
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.Meatogether  # 'Meatogether'라는 이름의 db를 만듭니다.



















#################11111111111111111111111111111111111111111111111######################
##############이제 api연결해서 내가 쓴 댓글이 몽고디비에 저장 또는 불러오기 만들기#################


# 주문하기(POST) API
@app.route('/reservations', methods=['POST'])
def save_reservation():  # 여길 채워나가세요!
    # 예약자 이름 가져오기
    receiver_name = request.form['name_give']
    # 고객이 쓴 번호 가져오기
    receiver_phone = request.form['phoneNumb_give']
    # 고객이 쓴 추가적인 댓글
    receiver_chat = request.form['chat_give']

    # DB에 넣을 정보 하나 하나를 orderdata_one으로 지정하기
    reservation_one = {'Name': receiver_name,
                       'Phone': receiver_phone,
                       'chats': receiver_chat,
                       }

    # 몽고DB에 ByOthersReservation라는 이름으로  저장하라는 명령 쓰기
    db.ByOthersReservation.insert_one(reservation_one)

    # 저장되었는지 확인하기 그리고 성공했으면 성공되었다고 말하기
    # 'result'랑 석세스 msg는 원래 저장되어잇는 함수인가????
    return jsonify({'result': 'success', 'msg': '주문이 몽고디비에 저장되었다'})


# 주문 목록보기(Read) API
@app.route('/reservations', methods=['GET'])
def view_reservations():
    # 1. DB에서 리뷰 정보 모두 가져오기
    reserveorders = list(db.ByOthersReservation.find({}, {'_id': 0}))
    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'DBreservations': reserveorders})
    # 여기서 DBorders는 내가 임의로 정해도 되는 말인가???응응


# 여길 채워나가세요!


#############_111111111111111111111111111111111111111111111111111111111111111111111111111_###############################


























###########2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222######################
#####업로드 페이지랑 연결해서 고객이 쓴 글을 업로드 버튼 누르면 내 db에 저장되도록 만들기##############


##############이제 api연결해서 내가 쓴 댓글이 몽고디비에 저장 또는 불러오기 만들기#################


# 주문하기(POST) API
@app.route('/upload', methods=['POST'])
def save_uopload():  # 여길 채워나가세요!
    # 업로드 페이지 타이틀 가져오기
    upload_Title = request.form['Title_give']
    # 인원수 가져오기
    upload_Howmany  = request.form['Howmany_give']
    # 시간 가져오기
    upload_Time = request.form['Time_give']
    #가격 가져오기
    upload_Price = request.form['Price_give']
    # 메뉴 가져오기
    upload_Menu = request.form['Menu_give']
    # 사진 가져오기
    upload_Img = request.form['Img_give']

    # DB에 넣을 정보 하나 하나를 orderdata_one으로 지정하기
    Whattheywrote_one = {'Title': upload_Title,
                       'Howmany': upload_Howmany,
                       'Time': upload_Time,
                       'Price': upload_Price,
                       'Menu': upload_Menu,
                       'Img': upload_Img,

                       }

    # 몽고DB에 uploadePage라는 이름으로  저장하라는 명령 쓰기
    db.uploadePage.insert_one(Whattheywrote_one)

    # 저장되었는지 확인하기 그리고 성공했으면 성공되었다고 말하기
    # 'result'랑 석세스 msg는 원래 저장되어잇는 함수인가????
    return jsonify({'result': 'success', 'msg': '성공적으로 업로드 했다'})
####일단 요기까지  1차로 저장만 완성 불러오는 것도 이따가 연결해야함##

# /showUpload는 나중에 /bo /afterchoosegu 등과 연동시켜야 한다
@app.route('/showUpload', methods=['GET'])
def loading_uploadData():
    # 1. DB에서 리뷰 정보 모두 가져오기
    uploadThing = list(db.uploadePage.find({}, {'_id': 0}))
    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'DBupload': uploadThing})
    # 여기서 DBorders는 내가 임의로 정해도 되는 말인가???응응


# 여길 채워나가세요!


#############_____________________________________________________________________###############################


###############22222222222222222222222222222222222222222222222222#########################




























@app.route('/')
def home():  # 함수명 수정 - 이름만 보고 접속되는 페이지를 확인할 수 있게!
    return render_template('mainpage.html')


@app.route('/gu')
def choosegu():
    return render_template('AfterChooseGu.html')


@app.route('/bo')
def byothers():
    return render_template('WritingByOthers.html')


@app.route('/write')
def up():
    return render_template('uploadpage.html')


#  이 아래 부분 if__name어쩌고가 항상 마지막에 나와야 해
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
